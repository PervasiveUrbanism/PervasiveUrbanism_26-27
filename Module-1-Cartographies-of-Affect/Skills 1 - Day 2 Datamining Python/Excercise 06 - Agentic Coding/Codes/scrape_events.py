"""Collect seven inclusive calendar days from Umweltkalender Berlin."""
import argparse
import csv
import json
import logging
import re
import time
from datetime import date, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

BASE = "https://www.umweltkalender-berlin.de"
FIELDS = ["event", "date", "time", "venue", "address", "price", "source_url", "description"]
MONTHS = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]


def clean(value):
    return " ".join(value.split())


class Client:
    def __init__(self, delay=1.0):
        self.delay = delay
        self.last_request = 0.0

    def fetch(self, url):
        for attempt in range(3):
            time.sleep(max(0, self.delay - (time.monotonic() - self.last_request)))
            self.last_request = time.monotonic()
            try:
                request = Request(url, headers={"User-Agent": "RC15-Teaching-EventScraper/1.0"})
                with urlopen(request, timeout=30) as response:
                    html = response.read().decode(response.headers.get_content_charset() or "utf-8")
                return BeautifulSoup(html, "html.parser")
            except (HTTPError, URLError, TimeoutError) as exc:
                if isinstance(exc, HTTPError) and exc.code < 500 and exc.code != 429:
                    raise
                if attempt == 2:
                    raise
                logging.warning("Retrying %s: %s", url, exc)
                time.sleep(2 ** (attempt + 1))


def listing_url(day):
    filters = {"zeitraum": "1t", "ab_tag": str(day.day), "ab_monat": str(day.month), "ab_jahr": str(day.year)}
    return BASE + "/angebote/filter?" + urlencode({"filterJson": json.dumps(filters)})


def discover(soup, day):
    if not soup.select_one("#js-filter-form"):
        raise ValueError("Expected listing form missing; response may not be an event listing")
    urls = {}
    # Hidden cards are included: the site's 'Alle anzeigen' control reveals them.
    for anchor in soup.select('.js-grid-item a[href*="/angebote/details/"]'):
        url = urljoin(BASE, anchor["href"])
        parts = urlsplit(url)
        match = re.fullmatch(r"/angebote/details/(\d+)", parts.path)
        occurrence = parse_qs(parts.query).get("dat", [""])[0]
        if match and occurrence == day.isoformat():
            urls[BASE + parts.path + "?" + urlencode({"dat": occurrence})] = clean(anchor.get_text(" ", strip=True))
    return urls


def labelled(soup, label):
    for strong in soup.find_all("strong"):
        if clean(strong.get_text(" ", strip=True)) == label:
            node = strong.find_next_sibling("div")
            return clean(node.get_text(" ", strip=True)) if node else ""
    return ""


def parse_event(soup, url, listing_text=""):
    title = soup.select_one("h1")
    header = soup.select_one(".date_detail")
    description = soup.select_one(".read-more-content")
    if title is None or description is None:
        raise ValueError("Required detail selectors missing")
    occurrence = date.fromisoformat(parse_qs(urlsplit(url).query)["dat"][0])
    if header is not None:
        for extra in header.select('.zusatzinfo'):
            extra.decompose()
    header_text = clean(header.get_text(" ", strip=True)) if header else ""
    expected = rf"\b0?{occurrence.day}\.\s+{MONTHS[occurrence.month - 1]}\s+{occurrence.year}\b"
    if header_text and not re.search(expected, header_text):
        raise ValueError(f"Detail date does not match URL: {header_text}")
    if not header_text and not listing_text:
        raise ValueError("No occurrence date available in detail or listing")
    time_match = re.search(r"\b\d{1,2}:\d{2}(?:\s*[-–]\s*\d{1,2}:\d{2})?\s*Uhr", header_text or listing_text)
    location = labelled(soup, "Ort/Treffpunkt:")
    # Preserve the full source location; do not invent a venue from the organiser.
    venue = ""
    address = location
    postal = re.search(r"\b\d{5}\s+Berlin\b", location)
    if postal:
        venue = location[postal.end():].strip(" ,;")
    elif location and not re.search(r"\d|Das Angebot ist möglich", location):
        venue = location
        address = ""
    return dict(zip(FIELDS, [
        clean(title.get_text(" ", strip=True)), occurrence.isoformat(),
        clean(time_match.group()).removesuffix(" Uhr") if time_match else "",
        venue, address, labelled(soup, "Kosten:"), url,
        clean(description.get_text(" ", strip=True)),
    ]))


def run(start, output, delay=1.0, limit=None):
    client = Client(delay)
    urls = {}
    failures = []
    for offset in range(7):
        day = start + timedelta(days=offset)
        url = listing_url(day)
        try:
            found = discover(client.fetch(url), day)
            logging.info("%s: %d dated occurrences", day, len(found))
            urls.update(found)
        except Exception as exc:
            failures.append({"source_url": url, "error": str(exc)})
            logging.error("Listing failed: %s", exc)
    selected = sorted(urls, key=lambda u: (parse_qs(urlsplit(u).query)["dat"][0], u))
    if limit is not None:
        selected = selected[:limit]
    rows = []
    for index, url in enumerate(selected, 1):
        try:
            rows.append(parse_event(client.fetch(url), url, urls[url]))
            logging.info("Detail %d/%d: %s", index, len(selected), rows[-1]["event"])
        except Exception as exc:
            failures.append({"source_url": url, "error": str(exc)})
            logging.error("Detail failed %s: %s", url, exc)
    rows.sort(key=lambda r: (r["date"], r["time"], r["event"]))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    report = {"start": start.isoformat(), "end": (start + timedelta(days=6)).isoformat(),
              "discovered": len(urls), "attempted": len(selected), "written": len(rows),
              "sample_limit": limit, "failures": failures}
    output.with_suffix(".report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    logging.info("Wrote %d rows to %s; %d failures", len(rows), output, len(failures))
    return 1 if failures else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", required=True, type=date.fromisoformat, help="First date, YYYY-MM-DD; seven days inclusive")
    parser.add_argument("--output", type=Path, help="CSV path (default: output/events_START.csv)")
    parser.add_argument("--delay", type=float, default=1.0, help="Minimum seconds between requests (at least 1)")
    parser.add_argument("--limit", type=int, help="Limit detail requests for a smoke test; produces a partial CSV")
    args = parser.parse_args()
    if args.delay < 1 or (args.limit is not None and args.limit < 1):
        parser.error("--delay must be at least 1 and --limit must be positive")
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    return run(args.start, args.output or Path(f"output/events_{args.start}.csv"), args.delay, args.limit)


if __name__ == "__main__":
    raise SystemExit(main())

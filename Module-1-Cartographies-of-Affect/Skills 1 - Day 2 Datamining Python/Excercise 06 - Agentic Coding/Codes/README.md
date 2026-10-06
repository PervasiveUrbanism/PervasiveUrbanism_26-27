# RC15: Umweltkalender Berlin scraper

Collect one row per dated event occurrence over seven inclusive calendar days.

## Windows setup and usage

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scrape_events.py --start 2026-10-12
```

This example collects 12–18 October 2026. Any start date is accepted; it need not be a Monday. Choose your own date and optionally pass `--output output/my_week.csv`.

The UTF-8 CSV has these columns:

`event,date,time,venue,address,price,source_url,description`

A neighbouring `.report.json` records discovery counts and failures. Exit code 1 means the output is incomplete because requests or parsing failed. `--limit 3` creates a partial smoke-test output; its limit is recorded in the report.

## Teaching and data decisions

- Fetch a filtered listing for each of the seven dates using the site's GET `filterJson` format. Read all cards, including cards hidden by the interface's “Alle anzeigen” button.
- Keep only links with a matching `dat` date, deduplicate dated URLs, and fetch each occurrence's detail page. Permanent undated offers are excluded. Multi-day offers can appear on several days.
- Verify the displayed detail date against the requested occurrence. For past occurrences whose detail header is removed, use the matching dated listing card for date and time. Extract title, full description, cost, and meeting location from the detail. Missing optional fields remain blank.
- Keep price as source text, including additional admission and concessions.
- Address preserves the full “Ort/Treffpunkt” text. Venue uses trailing meeting instructions after a Berlin postcode when present, or a location without digits. It may remain blank. This is a conservative heuristic, not a guaranteed separation of venue and address; the organiser is never substituted for venue.
- Request sequentially with a minimum one-second interval, a 30-second timeout, and up to three attempts for transient network errors. No organiser/ticket pages are requested.

The selectors and filter parameters depend on the site's current markup. An empty day is logged but cannot by itself prove the site's response is complete. Check unusual zero counts and the failure report. Sold-out/cancelled events remain in the dataset when listed; there is no separate status column in the requested schema.

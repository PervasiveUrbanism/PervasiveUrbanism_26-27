import unittest
from datetime import date
from bs4 import BeautifulSoup
from scrape_events import discover, parse_event


class ExtractionTests(unittest.TestCase):
    def test_hidden_cards_and_dated_deduplication(self):
        html = '<form id="js-filter-form"></form>'
        for day in ['2026-10-05', '2026-10-05', '2026-10-06', '']:
            html += f'<div class="js-grid-item" style="display:none"><a href="/angebote/details/12?dat={day}">Example</a></div>'
        self.assertEqual(len(discover(BeautifulSoup(html, 'html.parser'), date(2026, 10, 5))), 1)

    def test_past_occurrence_uses_listing_time_and_keeps_full_price(self):
        soup = BeautifulSoup('<h1>Workshop</h1><div class="read-more-content">Full description</div><strong>Kosten:</strong><br><div>15 € zzgl. Eintritt</div><strong>Ort/Treffpunkt:</strong><br><div>Mitte, Teststraße 1, 10115 Berlin, Werkstatt</div>', 'html.parser')
        row = parse_event(soup, 'https://www.umweltkalender-berlin.de/angebote/details/12?dat=2026-10-05', 'Mo., 05.10.2026 | 15:00 - 17:00 Uhr')
        self.assertEqual(row['time'], '15:00 - 17:00')
        self.assertEqual(row['price'], '15 € zzgl. Eintritt')
        self.assertEqual(row['venue'], 'Werkstatt')

    def test_wrong_detail_date_is_rejected(self):
        soup = BeautifulSoup('<h1>Example</h1><div class="date_detail">Dienstag, 06. Oktober 2026</div><div class="read-more-content">Description</div>', 'html.parser')
        with self.assertRaises(ValueError):
            parse_event(soup, 'https://www.umweltkalender-berlin.de/angebote/details/12?dat=2026-10-05')


if __name__ == '__main__':
    unittest.main()

# 📘 BookScraper

A web scraper for [books.toscrape.com](https://books.toscrape.com) that extracts book titles, prices, stock status, and images. Supports filtering and export to JSON/CSV.

## 🚀 Features

- ✅ Multi-page scraping (up to 50 pages)
- 🔍 Filter by keyword or price
- 💾 Export to JSON or CSV
- 🧪 Modular and testable codebase

## 📦 Structure

books_scraper/
├── main.py
├── scraper/
│ ├── fetcher.py
│ ├── parser.py
│ └── exporter.py
├── utils/
│ └── logger.py
├── output/
├── tests/
├── requirements.txt
└── README.md


## ⚙️ Usage

```bash
# Basic scrape and export to JSON
python main.py

# Filter by keyword
python main.py --keyword "travel"

# Filter by price range
python main.py --min-price 10 --max-price 30

# Export to CSV
python main.py --output-format csv --output-file output/books


---

## 🧪 (Bonus) `tests/test_parser.py`

# ```python
# from scraper.parser import parse_products

# def test_parse_products():
#     with open("tests/sample_page.html", encoding="utf-8") as f:
#         html = f.read()
#     products = parse_products(html)
#     assert len(products) > 0
#     assert "title" in products[0]
#     assert "price" in products[0]
# 📘 BookScraper

A web scraper for [books.toscrape.com](https://books.toscrape.com) that extracts book titles, prices, stock status, and images. Supports filtering and export to JSON/CSV.

## 🚀 Features

- ✅ Multi-page scraping (up to 50 pages)
- 🔍 Filter by keyword or price
- 💾 Export to JSON or CSV
- 🧪 Modular and testable codebase

## 📦 Structure

<pre> ``` books_scraper/ ├── README.md ├── requirements.txt ├── main.py ├── config.py ├── scraper/ │ ├── __init__.py │ ├── fetcher.py │ ├── parser.py │ └── exporter.py ├── utils/ │ ├── __init__.py │ └── logger.py ├── tests/ │ ├── test_parser.py │ ├── test_filters.py │ ├── test_exporter.py │ └── sample_page.html ├── output/ │ └── products.json ``` </pre>


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

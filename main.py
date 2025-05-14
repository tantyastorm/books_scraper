import argparse
from scraper.fetcher import fetch_page
from scraper.parser import parse_products
from scraper.exporter import export_to_json, export_to_csv
from utils.logger import get_logger

logger = get_logger()

def scrape_all_pages(base_url):
    products = []
    for page_num in range(1, 51):  # 50 pages on books.toscrape.com
        url = f"{base_url}/catalogue/page-{page_num}.html"
        logger.info(f"Fetching: {url}")
        html = fetch_page(url)
        if not html:
            break
        products_on_page = parse_products(html)
        if not products_on_page:
            break
        products.extend(products_on_page)
    return products

def main():
    parser = argparse.ArgumentParser(description="Scrape books from books.toscrape.com")
    parser.add_argument("--keyword", help="Filter by keyword in title")
    parser.add_argument("--min-price", type=float, help="Minimum price filter")
    parser.add_argument("--max-price", type=float, help="Maximum price filter")
    parser.add_argument("--output-format", choices=["json", "csv"], default="json")
    parser.add_argument("--output-file", default="output/products")
    args = parser.parse_args()

    base_url = "https://books.toscrape.com"
    products = scrape_all_pages(base_url)

    if args.keyword:
        products = [p for p in products if args.keyword.lower() in p["title"].lower()]
    if args.min_price:
        products = [p for p in products if p["price"] >= args.min_price]
    if args.max_price:
        products = [p for p in products if p["price"] <= args.max_price]

    logger.info(f"Found {len(products)} products after filtering.")

    if args.output_format == "json":
        export_to_json(products, f"{args.output_file}.json")
    else:
        export_to_csv(products, f"{args.output_file}.csv")

    logger.info("Done!")

if __name__ == "__main__":
    main()

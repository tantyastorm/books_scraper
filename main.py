from scraper.fetcher import fetch_page
from scraper.parser import parse_products
from scraper.exporter import export_to_json, export_to_csv
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(description="Scrape product info from books.toscrape.com")

    parser.add_argument("--keyword", help="Filter by keyword in title")
    parser.add_argument("--min-price", type=float, help="Minimum price")
    parser.add_argument("--max-price", type=float, help="Maximum price")
    parser.add_argument("--output", default="output/products.json", help="Output JSON file path")

    return parser.parse_args()

def main():
   
    args = get_args()

    url = "https://books.toscrape.com/catalogue/page-1.html"
    print("Fetching page...")
    html = fetch_page(url)
    
    print("Parsing products...")
    products = parse_products(html)
    print(f"[DEBUG] Found {len(products)} products before filtering.")

    if args.keyword:
        print(f"[DEBUG] Filtering by keyword: {args.keyword}")
        products = [p for p in products if args.keyword.lower() in p["title"].lower()]

    if args.min_price is not None:
        print(f"[DEBUG] Filtering by min_price: {args.min_price}")
        products = [p for p in products if p["price"] >= args.min_price]

    if args.max_price is not None:
        print(f"[DEBUG] Filtering by max_price: {args.max_price}")
        products = [p for p in products if p["price"] <= args.max_price]

    print(f"Found {len(products)} products after filtering. Exporting...")
    export_to_json(products, args.output)
    print("Done!")


if __name__ == "__main__":
    main()

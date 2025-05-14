from bs4 import BeautifulSoup
import re

def parse_products(html):
    soup = BeautifulSoup(html, "lxml")
    product_list = []

    products = soup.select("article.product_pod")
    print(f"[DEBUG] Found {len(products)} product cards.")

    for article in products:
        title_tag = article.h3.a
        title = title_tag["title"] if title_tag else "N/A"

        price_tag = article.select_one("p.price_color")
        if price_tag:
            price_text = price_tag.text.strip()
            price_match = re.search(r"[\d.]+", price_text)
            price = float(price_match.group()) if price_match else 0.0
        else:
            price = 0.0

        product_list.append({
            "title": title,
            "price": price
        })

    return product_list


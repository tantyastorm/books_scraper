from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "lxml")
    items = soup.select(".product_pod")
    products = []

    for item in items:
        title = item.h3.a["title"]
        price_str = item.select_one(".price_color").text.strip()
        price = float(price_str.replace("£", "").strip())
        stock = item.select_one(".instock.availability").text.strip()
        img_url = "https://books.toscrape.com/" + item.img["src"].replace("../", "")

        products.append({
            "title": title,
            "price": price,
            "stock": stock,
            "image_url": img_url
        })
    return products

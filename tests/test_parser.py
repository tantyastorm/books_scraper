import os
from scraper.parser import parse_products

def test_parse_products():
    # Путь к sample_page.html
    test_file_path = os.path.join(os.path.dirname(__file__), "sample_page.html")

    with open(test_file_path, encoding="utf-8") as f:
        html = f.read()

    products = parse_products(html)

    assert isinstance(products, list), "Should return a list"
    assert len(products) > 0, "Should extract at least one product"
    
    product = products[0]
    assert "title" in product, "Product should have a title"
    assert "price" in product, "Product should have a price"
    assert isinstance(product["price"], float), "Price should be a float"
    assert "stock" in product, "Product should have stock info"
    assert "image_url" in product, "Product should have image URL"

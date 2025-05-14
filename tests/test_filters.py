from scraper.parser import parse_products

# Sample mock product list
products = [
    {"title": "Alpha Book", "price": 15.99, "stock": "In stock", "image_url": "http://example.com/1.jpg"},
    {"title": "Beta Book", "price": 35.0, "stock": "In stock", "image_url": "http://example.com/2.jpg"},
    {"title": "Gamma Book", "price": 5.0, "stock": "In stock", "image_url": "http://example.com/3.jpg"},
]

def test_keyword_filter():
    filtered = [p for p in products if "beta" in p["title"].lower()]
    assert len(filtered) == 1
    assert filtered[0]["title"] == "Beta Book"

def test_price_range_filter():
    filtered = [p for p in products if 10 <= p["price"] <= 20]
    assert len(filtered) == 1
    assert filtered[0]["title"] == "Alpha Book"

def test_max_price_filter():
    filtered = [p for p in products if p["price"] <= 10]
    assert len(filtered) == 1
    assert filtered[0]["title"] == "Gamma Book"

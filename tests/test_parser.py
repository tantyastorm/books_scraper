import unittest
from scraper.parser import parse_products
from bs4 import BeautifulSoup

class TestParser(unittest.TestCase):
    def test_parse_sample_html(self):
        html = '''<html>...mocked HTML snippet of a product...</html>'''
        soup = BeautifulSoup(html, "lxml")
        result = parse_products(soup)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("title", result[0])
        self.assertIn("price", result[0])

if __name__ == "__main__":
    unittest.main()

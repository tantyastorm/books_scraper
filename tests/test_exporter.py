import os
import json
from scraper.exporter import export_to_json

def test_export_to_json(tmp_path):
    test_data = [
        {"title": "Test Book", "price": 12.34, "stock": "In stock", "image_url": "http://example.com/img.jpg"}
    ]
    output_file = tmp_path / "test_output.json"
    export_to_json(test_data, output_file)

    assert output_file.exists()

    with open(output_file, encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert data[0]["title"] == "Test Book"

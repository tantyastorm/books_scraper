import requests

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        return response.text
    return None

import requests
from utils.logger import log


def fetch_page(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        log(f"Error fetching URL: {e}")
        return ""

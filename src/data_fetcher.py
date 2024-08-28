import requests
from bs4 import BeautifulSoup


def fetch_data(site):
    response = requests.get(site['url'])
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    data = parse_html(soup)
    return data

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {site['name']}: {e}")
    return None

def parse_html(soup):
    data = []

    return data




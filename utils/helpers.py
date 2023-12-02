import requests
from bs4 import BeautifulSoup as bs


def get_url(i):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    print(url)
    return url


def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")
    return soup

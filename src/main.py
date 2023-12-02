import pandas as pd
from utils.helpers import get_url, get_soup


titles = []
prices = []
cover_links = []
book_links = []

url_base = "https://books.toscrape.com"
for i in range(1, 51):
    url = get_url(i)
    soup = get_soup(url)

    books = soup.find_all("article")

    titles = titles + [book.find("img")["alt"] for book in books]
    prices = prices + [book.find("p", class_="price_color").text[2:] for book in books]
    cover_links = cover_links + [
        url_base + book.find("img")["src"][2:] for book in books
    ]
    book_links = book_links + [
        url_base + "/" + book.find("a")["href"] for book in books
    ]


df = pd.DataFrame(
    {
        "titles": titles,
        "prices": prices,
        "cover_urls": cover_links,
        "book_links": book_links,
    }
)

df.to_csv("data/results.csv", index=False)

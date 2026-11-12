
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/"

books = []

for page in range(1, 51):

    if page == 1:
        url = base_url
    else:
        url = f"{base_url}catalogue/page-{page}.html"

    print(f"Scraping page {page}...")

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.product_pod"):

        title = book.h3.a["title"]

        price = book.select_one(".price_color").text

        availability = book.select_one(
            ".availability"
        ).text.strip()

        rating = book.select_one(
            ".star-rating"
        )["class"][1]

        books.append({
            "Title": title,
            "Price": float(
                price.replace("£", "").replace("Â", "")
            ),
            "Rating": rating,
            "Availability": availability
        })

    time.sleep(0.3)

df = pd.DataFrame(books)

df.to_csv("books.csv", index=False)

print("\nScraping completed!")
print("Total books collected:", len(df))

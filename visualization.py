
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books.csv")

# 1. Rating Distribution
rating_counts = df["Rating"].value_counts()

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()


# 2. Book Price Distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=8)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

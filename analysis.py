import pandas as pd

df = pd.read_csv("books.csv")

# Explore dataset
print(df.head())

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Average book price
print("Average Price:", df["Price"].mean())

# Most expensive book
print("Highest Price:", df["Price"].max())

# Cheapest book
print("Lowest Price:", df["Price"].min())

# Rating distribution
print(df["Rating"].value_counts())

# Availability
print(df["Availability"].value_counts())
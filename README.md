# 📚 E-commerce Book Data Analyzer

A Python-based web scraping and data analysis project that collects book information from an online bookstore and analyzes the collected dataset using Pandas.

## 🎯 Project Overview

This project demonstrates how to collect data from a website using web scraping techniques, store it in CSV format, and perform exploratory data analysis (EDA) to discover useful insights.

The project uses the practice website [Books to Scrape](https://books.toscrape.com/).

## 🛠️ Technologies Used

- Python
- Requests – Fetch website content
- BeautifulSoup – Extract information from HTML
- Pandas – Data manipulation and analysis
- Matplotlib – Data visualization

## 📁 Project Structure

```text
book_analysis/
│
├── scraper.py
├── analysis.py
├── books.csv
└── README.md
```

## 📊 Data Collected

The scraper extracts the following information:

- Book Title
- Book Price
- Book Rating
- Availability Status

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd book_analysis
```

Install dependencies:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

## 🚀 How to Run

**Step 1: Collect Data**

```bash
python scraper.py
```

**Step 2: Analyze Data**

```bash
python analysis.py
```

## 🔍 Analysis Performed

- Average book price
- Highest and lowest book prices
- Rating distribution
- Availability analysis
- Basic statistical summary

## 💡 Project Goals

- Understand web scraping using Python.
- Learn how to extract structured data from HTML.
- Practice working with CSV datasets.
- Perform exploratory data analysis using Pandas.
- Develop practical data analytics skills.

## 👨‍💻 Author

MK

Aspiring Data Analyst | Python Developer

## 📌 Disclaimer

This project uses a practice website specifically designed for web scraping and educational purposes.

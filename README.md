# Extract, Transform and Load Articles from News Websites

**How to use it:**

1️⃣ Download repository.

2️⃣ Install required libraries:

```python
pip install -r requirements.txt
```

3️⃣ To start scraping and the ETL process, just type on the terminal:

```python
python pipeline.py
```

✅ It's done!

The script will:

- Extract: Scrap articles from the front page of the websites:
  1. [El Universal](http://www.eluniversal.com.mx/)
  2. [CNN en Español](https://cnnespanol.cnn.com/) 
- Transform: Clean the data from empty values and enrich them with tokenization, i.e. separate the words within the title and the body for a posterior analysis.
- Load: Load the data to a local SQLite database.

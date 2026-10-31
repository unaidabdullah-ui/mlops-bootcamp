# Stage 3: Working With Data

⏱️ Suggested time: 3–4 weeks · 🎓 Learned from: CampusX, CodeWithHarry

## 🎯 Goals

By the end of this stage you can:
- Load CSV, JSON and SQL data into pandas
- Clean data and engineer features with SQL
- Collect data from the web with scraping
- Explore data visually with Matplotlib and Seaborn

## 📂 What's Inside

| Folder | Topic |
|--------|-------|
| [`pandas-data-loading`](pandas-data-loading) | `read_csv` options (chunks, dtypes, encodings) and `read_json` / SQL |
| [`sql-feature-engineering`](sql-feature-engineering) | SQLite pipeline: create → load → clean → features → analytics → views → indexes |
| [`web-scraping`](web-scraping) | Scrape quotes, authors and tags into a CSV with Requests + BeautifulSoup |
| [`matplotlib-basics`](matplotlib-basics) | Clean data, scatter plot, fit a linear regression |
| [`seaborn-eda`](seaborn-eda) | Exploratory analysis of an employee salary dataset |

## ▶️ Run It

```bash
pip install pandas numpy matplotlib seaborn scikit-learn requests beautifulsoup4 jupyter

# SQL pipeline (SQLite)
cd sql-feature-engineering
for f in sql/*.sql; do sqlite3 customers.db < "$f"; done

# Plots + regression
cd ../matplotlib-basics && python app.py
```

Notebooks: run `jupyter notebook` and open any `.ipynb`. Some large datasets aren't committed; see `DATA.md` in the folder.

## 🏋️ Practice

1. In `pandas-data-loading`, load `aug_train.csv` in chunks and count the rows per city without loading the whole file.
2. Add a SQL query that ranks customers by `purchase_amount` within each `city` using a window function.
3. Change the scraper to also follow each author's page and save their birth date.

## 📚 Free Resources

- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas) · [Data Visualization](https://www.kaggle.com/learn/data-visualization)
- [SQLBolt](https://sqlbolt.com/): interactive SQL lessons
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

## ✅ Checklist

- [ ] I can load messy data from CSV, JSON and SQL
- [ ] I can write SQL with joins, GROUP BY and window functions
- [ ] I can tell a story about a dataset with 3–4 plots

**← Previous** [Stage 2: Linux & Shell](../02-linux-shell) · **Next →** [Stage 4: Machine Learning](../04-machine-learning)

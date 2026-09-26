# Zomato Restaurants: EDA Mini Project

**Notebook:** `Zomato_EDA.ipynb` | **Dataset:** `datasets/zomato_eda_mini_project.csv`

## Dataset
103 restaurant listings across 7 Indian cities (Mumbai, Delhi, Pune, Kolkata, Chennai, Bangalore, Hyderabad).

| Column | Description |
|---|---|
| Restaurant Name | Name of the outlet |
| City | City of the outlet |
| Cuisines | Comma-separated cuisines served |
| Average Cost for two | Cost in ₹ |
| Price range | 1 (cheap) to 4 (expensive) |
| Aggregate rating | Rating out of 5 |
| Votes | Number of user votes |

**Data quality:** a few missing values in City (2), Cuisines (3), Cost (2), Rating (2) and Votes (1), plus 3 duplicate rows.
The data is deliberately messy for cleaning practice. The same cleaning techniques (fillna, drop_duplicates, str.strip/title) are shown in `02_Pandas/Pandas_for_Data_Science.ipynb`.

## Analysis performed
- `head()` and `info()` inspection
- Countplot of cuisines (which cuisines are most popular)
- Histogram of ratings by cuisine and of votes (with KDE)
- Boxplot and barplot of **average cost for two by city**
- Barplot of **average rating by city**

## Key findings
- The most common cuisine combinations are **North Indian + Chinese**, **Street Food + North Indian** and **South Indian + Seafood**.
- **Chennai and Kolkata** have the highest average cost for two (about ₹1,100). **Bangalore** is the cheapest (about ₹550) but has the **highest average rating (3.85)**.
- **Mumbai** has the lowest average rating (3.53).
- Cost has almost **no correlation with rating** (r ≈ 0.05), so expensive does not mean better. Cost is moderately correlated with **votes** (r ≈ 0.5).

## What I learned
Using Seaborn's count, hist, box and bar plots to compare categories. I also learned that a countplot on a
high-cardinality text column (Cuisines) crowds the axis, so splitting the cuisines or rotating the labels would improve it.

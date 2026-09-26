# DSML: Data Science & Machine Learning Progress

|                         |                 |
| ----------------------- | --------------- |
| **Name**                | Gagan Gautam    |
| **Registration Number** | RA2411026030067 |
| **Subject**             | DSML            |

This repository holds all my work for the **Data Science & Machine Learning (DSML)** course: the lab notebooks,
practice notebooks and mini projects. The folders are ordered in the sequence I learned the topics, from NumPy and
Pandas through statistics, EDA and visualisation to regression models, followed by complete projects.

Every folder that loads data has its own **`datasets/`** subfolder, so each topic is self-contained and every notebook
runs from top to bottom with no path changes.

---

## Repository Structure

```
DSML-Progress/
│
├── README.md                                        ← you are here
│
├── 01_NumPy/
│   ├── NumPy_for_Data_Science.ipynb                 ← complete NumPy reference for data science
│   └── datasets/
│       └── iris_data.csv                            ← loaded with np.genfromtxt
│
├── 02_Pandas/
│   ├── Pandas_for_Data_Science.ipynb                ← complete Pandas reference (student data)
│   ├── DataFrame_Basics.ipynb                       ← creating DataFrames, selecting columns, loc
│   ├── Pandas_Day2_Indexing_Slicing.ipynb           ← indexing/slicing, add/modify, missing values, sort/filter
│   ├── DSML_Pandas_Basics_and_Visualization.ipynb   ← class notebook: Iris, Superstore, salary plots, correlation
│   └── datasets/
│       ├── students_performance.csv                 ← used by Pandas_for_Data_Science
│       ├── departments.csv                          ← merge example
│       ├── data.csv                                 ← used by Pandas_Day2
│       ├── iris_data.csv                            ┐
│       ├── superstore.csv                           │ used by the DSML class notebook
│       ├── salary_data_cleaned.csv                  │
│       └── salary_dataset.csv                       ┘
│
├── 03_Statistics/
│   ├── Descriptive_Statistics.ipynb                 ← central tendency, spread, normal distribution, z-scores
│   └── datasets/
│       └── Titanic-Dataset.csv
│
├── 04_EDA_and_Visualization/
│   ├── EDA_Salary_Visualization.ipynb               ← univariate & bivariate EDA with Seaborn
│   └── datasets/
│       └── salary_dataset.csv
│
├── 05_Linear_Regression/                            ← (data created inside each notebook)
│   ├── Linear_Regression_Experience_Salary_NumPy.ipynb
│   ├── Linear_Regression_Study_Hours_v1.ipynb
│   ├── Linear_Regression_Study_Hours_v2.ipynb
│   ├── Linear_Regression_Slope_Intercept.ipynb
│   └── Linear_Regression_AI_Power_Forecast.ipynb
│
├── 06_Logistic_Regression/                          ← (data created inside each notebook)
│   ├── Logistic_Regression_Roll_Number.ipynb
│   └── Logistic_Regression_Study_Hours.ipynb
│
└── Projects/
    ├── Zomato_EDA/
    │   ├── README.md
    │   ├── Zomato_EDA.ipynb
    │   └── datasets/zomato_eda_mini_project.csv
    ├── Titanic_EDA/
    │   ├── README.md
    │   ├── Titanic_EDA.ipynb
    │   └── datasets/Titanic-Dataset.csv
    └── Salary_EDA/
        ├── README.md
        ├── Salary_EDA.ipynb
        └── datasets/salary_dataset.csv
```

---

## Datasets

| File                          | Location(s)                                               | Rows × Cols | Source                                                                                                                           |
| ----------------------------- | --------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `iris_data.csv`               | `01_NumPy/datasets`, `02_Pandas/datasets`                 | 150 × 6     | **Real** Iris dataset (UCI/Kaggle layout)                                                                                        |
| `students_performance.csv`    | `02_Pandas/datasets`                                      | 63 × 11     | **Practice data** made for learning Pandas, with deliberate missing values, 3 duplicate rows and inconsistent city spellings     |
| `departments.csv`             | `02_Pandas/datasets`                                      | 4 × 4       | Lookup table for the merge examples                                                                                              |
| `data.csv`                    | `02_Pandas/datasets`                                      | 8,000 × 8   | **Synthetic** version in the UCI Online-Retail format. The first and last rows match the original; the original has 541,909 rows |
| `superstore.csv`              | `02_Pandas/datasets`                                      | 51,290 × 27 | **Synthetic** Global-Superstore-style orders with the same 27 columns                                                            |
| `salary_data_cleaned.csv`     | `02_Pandas/datasets`                                      | 742 × 28    | **Synthetic** Glassdoor-style job postings with the same 28 columns. The first 5 rows match the original                         |
| `salary_dataset.csv`          | `02_Pandas`, `04_EDA…`, `Projects/Salary_EDA`             | 71 × 6      | **Synthetic**, recreated from the saved outputs. The visible original rows are kept                                              |
| `Titanic-Dataset.csv`         | `03_Statistics/datasets`, `Projects/Titanic_EDA/datasets` | 891 × 12    | **Real** (original course file)                                                                                                  |
| `zomato_eda_mini_project.csv` | `Projects/Zomato_EDA/datasets`                            | 103 × 7     | **Real** (original course file)                                                                                                  |

> The synthetic files have the same column names, data types and value ranges as the class originals, so every notebook runs.
> The saved outputs of the class notebooks were produced with the original data, so re-running them gives slightly different numbers and charts.

---

## Directory Details

### 📁 01_NumPy

**Contents:** `NumPy_for_Data_Science.ipynb` walks through NumPy in 12 sections:

1. Creating arrays (`array`, `zeros`, `ones`, `arange`, `linspace`, `eye`)
2. Attributes and dtypes
3. Indexing and slicing
4. Vectorised arithmetic, broadcasting and ufuncs
5. Aggregations along axes
6. Reshaping, stacking and splitting
7. Boolean masking and `np.where`
8. Random number generation
9. Linear algebra (`@`, `inv`, `det`, and linear regression solved by hand with the Normal Equation)
10. `NaN` handling
11. Loading the real Iris dataset with `np.genfromtxt`: per-species means with masks, a correlation matrix, and standardisation and min-max scaling
12. A speed test against Python lists

**What I learned**

- NumPy arrays are the data structure underneath Pandas and scikit-learn.
- Vectorised operations replace loops and run roughly 10–50× faster than loops over Python lists.
- `axis=0` works down columns and `axis=1` works across rows.
- Masks over one array can filter a related array (for example, measurements by species).
- scikit-learn needs a 2-D feature matrix, which is why we write `X = df[['Hours']]` or `reshape(-1, 1)`.
- Feature scaling (z-score or min-max) is simple array arithmetic.

### 📁 02_Pandas

**Contents**

- `Pandas_for_Data_Science.ipynb` is a complete reference built on the student-performance dataset. It covers Series/DataFrame creation, `read_csv`,
  `info`/`describe`/`value_counts`, `[]` vs `loc` vs `iloc` vs `at`/`iat`, `set_index`, adding/inserting/renaming/dropping columns,
  missing-value imputation (median, mean, mode and group-wise `transform`), duplicates, text cleaning with `.str`, sorting and
  filtering (`isin`, `between`, `query`, `nlargest`), `groupby().agg()`, `apply`/`map`/`pd.cut`, `merge`/`concat`, pivot tables and crosstabs.
- `DataFrame_Basics.ipynb` covers building a DataFrame from a dictionary, `info()`, and column selection with `head`/`tail`.
- `Pandas_Day2_Indexing_Slicing.ipynb` reads the Online-Retail invoice data and completes the four Day 2 topics:
  **indexing and slicing** (`[]`, `iloc`, `loc`, `at`/`iat`, `set_index`), **adding and modifying data** (computed columns, `to_datetime`,
  conditional updates, adding and deleting rows and columns), **missing values** (`isnull`, `fillna`, `dropna(subset=…)`) and
  **sorting and filtering** (multi-column sort, cancelled orders, `isin`, `str.contains`, `query`, revenue by country).
- `DSML_Pandas_Basics_and_Visualization.ipynb` is the main class notebook. It covers NumPy arithmetic, Iris exploration
  (`loc`/`iloc`, adding, modifying, filling, sorting and filtering, and `groupby`), the Superstore dataset (51k rows), and salary
  histograms, bar, scatter and regression plots. It ends with a **correlation heatmap** and a **Location vs Job Role countplot**.

**What I learned**

- Every analysis starts with `head()`, `info()`, `describe()` and `isnull().sum()`.
- `loc` includes the end label, while `iloc` excludes the end position.
- Missing values should be imputed column by column, and a group-wise median is fairer when groups differ.
- Text must be cleaned (`str.strip().str.title()`) before grouping, or "Chennai" and "chennai " count as two cities.
- `groupby` + `agg` answers most business questions in a single line.

### 📁 03_Statistics

**Contents:** `Descriptive_Statistics.ipynb` generates a synthetic customer dataset of 120 rows with NumPy random distributions
(`randint`, `normal`, `poisson`, `uniform`) and calculates the **mean, median, mode, frequency counts, range, variance and
standard deviation**. It then covers the **normal distribution**: a histogram with a fitted bell curve and ±1σ/2σ lines, a check of the
68-95-99.7 empirical rule, skewness, **z-scores** for spotting unusual customers, and box and histogram plots of skewed data.

**What I learned**

- The difference between measures of central tendency (mean, median, mode) and measures of spread (range, variance, std).
- The median is robust to outliers and the mean is not.
- Income is roughly normal, while counts such as purchases follow a right-skewed Poisson distribution.
- A z-score says how many standard deviations a value lies from the mean, which is a simple way to find outliers.

### 📁 04_EDA_and_Visualization

**Contents:** `EDA_Salary_Visualization.ipynb` performs EDA on a salary dataset (Experience, Education, JobRole, Location, Salary).
It covers data inspection, null checks, **univariate** plots (salary and experience histograms with KDE, job-role countplot) and
**bivariate** plots (salary by job role, salary by education, experience vs salary regplot).

**What I learned**

- Univariate analysis looks at one variable's distribution. Bivariate analysis looks at the relationship between two variables.
- When to use each plot: histogram/KDE for distributions, countplot for categories, barplot for mean by category,
  boxplot for spread and outliers, scatter/regplot for numeric relationships, and heatmap for correlation.
- Plots need titles, axis labels and rotated tick labels to be readable.

### 📁 05_Linear_Regression

**Contents**

- `Linear_Regression_Experience_Salary_NumPy.ipynb` is my first model. It predicts salary from years of experience using NumPy arrays and prints slope and intercept.
- `Linear_Regression_Study_Hours_v1.ipynb` predicts marks from study hours, plots the fitted line, and caps predictions at 100.
- `Linear_Regression_Study_Hours_v2.ipynb` is the same problem done again in class, with a bug fixed (`plt.tittle` changed to `plt.title`).
- `Linear_Regression_Slope_Intercept.ipynb` trains the model and prints formatted `coef_` and `intercept_`.
- `Linear_Regression_AI_Power_Forecast.ipynb` fits a trend over years and forecasts 2030.

**What I learned**

- Linear regression fits `y = mx + c` by minimising squared error. The slope is the change in y per unit of x.
- The standard scikit-learn workflow: `model = LinearRegression()` → `fit(X, y)` → `predict(new_X)`.
- Predictions can go outside realistic limits (marks above 100), so the output needs domain rules.
- Extrapolating far beyond the training range (the 2030 forecast) is unreliable, especially when the real trend is not linear.

### 📁 06_Logistic_Regression

**Contents**

- `Logistic_Regression_Roll_Number.ipynb` is my first classifier. It covers `train_test_split` and predicting pass/fail.
- `Logistic_Regression_Study_Hours.ipynb` predicts pass/fail from study hours. It uses `predict_proba` for probabilities, a scatter plot, and `accuracy_score`.

**What I learned**

- Logistic regression is used for **classification**. It outputs a probability through the sigmoid function and applies a 0.5 threshold.
- Why data is split into training and testing sets, and what `random_state` does for reproducibility.
- `predict_proba` gives more information than `predict`: a prediction of "pass" at 0.79 is less certain than one at 0.99.
- 100% accuracy on a 2-sample test set does not mean much. Evaluation needs enough data and a confusion matrix.
- The feature must make sense. Roll number has no causal link to passing, so that model learned a coincidence.

### 📁 Projects

| Project         | Dataset                                                   | Summary                                                                                                                                              |
| --------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zomato_EDA**  | `zomato_eda_mini_project.csv` (103 restaurants, 7 cities) | Cuisine popularity, rating and vote distributions, cost and rating by city                                                                           |
| **Titanic_EDA** | `Titanic-Dataset.csv` (891 passengers)                    | Full EDA: cleaning, feature engineering, survival analysis, correlation, and a baseline logistic regression model (82.7% accuracy vs 61.5% baseline) |
| **Salary_EDA**  | `salary_dataset.csv` (71 employees)                       | Salary by job role, education and location; experience vs salary; box plots                                                                          |

Each project folder has its own `README.md` with details and findings.

**What I learned from the projects**

- A full EDA workflow: load → inspect → clean → engineer features → univariate → bivariate → correlation → conclusions.
- Real datasets contain missing values, duplicates and inconsistent entries that must be handled first.
- Domain knowledge helps with cleaning. On the Titanic data, filling Age by passenger _title_ (Mr/Mrs/Miss/Master)
  was more accurate than using one global median.
- EDA is useful when it leads to conclusions, such as "sex and class were the strongest survival factors".

---

## Challenges I Faced

1. **`loc` vs `iloc` confusion.** Slices returned an unexpected number of rows until I learned that `loc` includes the end label and `iloc` excludes the end position.
2. **The 2-D input requirement.** `model.fit(df['Hours'], y)` failed, and the fix was `df[['Hours']]` or `reshape(-1, 1)`. The related
   _"X does not have valid feature names"_ warning appeared when I predicted with a plain list after training on a DataFrame.
3. **Hard-coded Colab paths.** Notebooks that used `/content/...` paths broke outside Google Colab.
4. **Typos that crash cells.** `plt.tittle(...)` raised an `AttributeError`, and `data.describe` without `()` printed a method object instead of statistics.
5. **Running cells out of order.** A class cell only worked because a later cell had already been run, so the notebook failed when run from the top.
6. **Missing data decisions.** I found it hard to choose between dropping and filling values, and to pick a fill value (mean, median, mode or group-wise).
7. **Messy text data.** The same city with different spacing or capitalisation was counted as separate groups.
8. **Choosing the right plot.** Early on I used countplots on high-cardinality columns such as Cuisines, which made the charts unreadable.
9. **Reading model results.** At first I did not question a 100% accuracy on 2 test samples, or a model that predicts from roll numbers.
10. **Managing files.** My notebooks were spread across Downloads, two zip files and Colab, with generic names like `Untitled0.ipynb`, and some topics were only headings in a notebook.

---

## How to Run

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
jupyter notebook
```

Open any notebook and run it from inside its own folder. Each notebook loads its data from the `datasets/` folder next to it.

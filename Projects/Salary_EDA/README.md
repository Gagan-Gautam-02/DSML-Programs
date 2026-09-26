# Salary Dataset: EDA Project

**Notebook:** `Salary_EDA.ipynb` | **Dataset:** `datasets/salary_dataset.csv` (71 rows). This is a synthetic copy recreated from the saved outputs. The saved outputs in the notebook come from the original class data.

## Dataset columns
Experience, Education (Bachelor/Master/PhD), JobRole, Location, Skills, Salary

## Analysis performed
- **Inspection:** `info()`, `shape`, `describe()`, missing-value check
- **Univariate:** salary distribution, experience distribution, number of employees by job role
- **Bivariate:** average salary by job role, education and location; experience vs salary (scatter and regression line); salary spread by education (boxplot)

## What I learned
- The difference between univariate analysis (one variable) and bivariate analysis (two variables).
- A regression line on a scatter plot shows the trend between experience and salary.
- Boxplots show the median, spread and outliers, which a barplot of means hides.

# Titanic Survival: EDA Project

**Notebook:** `Titanic_EDA.ipynb` | **Dataset:** `datasets/Titanic-Dataset.csv` (891 rows × 12 columns)

## Workflow
1. **Inspect:** shape, dtypes, `describe()`
2. **Missing values:** Age (177), Cabin (687), Embarked (2), shown as a heatmap
3. **Cleaning:** Age filled with the median per title (Mr/Mrs/Miss/Master/Rare), Embarked filled with the mode, Cabin replaced by a `HasCabin` flag
4. **Feature engineering:** `Title`, `FamilySize`, `IsAlone`, `AgeGroup`, `FareBand`
5. **Univariate analysis:** survival, class and sex counts; age and fare distributions; fare outliers (IQR)
6. **Bivariate analysis:** survival rate by sex, class, port, age group, family size and title; class × sex interaction
7. **Correlation heatmap**
8. **Model-ready dataset:** one-hot encoding and a baseline Logistic Regression

## Key findings
| Factor | Survival rate |
|---|---|
| Overall | 38.4% |
| Female / Male | 74.2% / 18.9% |
| 1st / 2nd / 3rd class | ~63% / ~47% / ~24% |
| 1st-class women | 96.8% |
| 3rd-class men | 13.5% |
| Family size 2–4 | 55–72% |
| Travelling alone | 30% |

- **Sex** (r = 0.54) and **class** (r = −0.34) were the strongest predictors, followed by **HasCabin** (0.32) and **Fare** (0.26).
- A Logistic Regression on the engineered features reached **82.7% accuracy** against a **61.5%** "everyone died" baseline.

import nbformat as nbf

nb = nbf.v4.new_notebook()

text = """\
# XGBoost Detailed Implementation
In this notebook, we will:
1. Create a detailed dataset
2. Implement XGBoost Classifier
3. Evaluate the model with all parameters
4. Visualize the results
"""

code1 = """\
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, classification_report, roc_curve, auc)
import xgboost as xgb

# Set random seed for reproducibility
np.random.seed(42)
import warnings
warnings.filterwarnings('ignore')
"""

text2 = "## 1. Create a Detailed Dataset"
code2 = """\
# We will create a synthetic dataset for binary classification
X, y = make_classification(n_samples=2000, n_features=20, n_informative=15, 
                           n_redundant=5, random_state=42, weights=[0.7, 0.3])

# Create a DataFrame for better visualization
feature_names = [f'Feature_{i}' for i in range(1, 21)]
df = pd.DataFrame(X, columns=feature_names)
df['Target'] = y

print("Dataset Shape:", df.shape)
df.head()
"""

text3 = "## 2. Exploratory Data Analysis"
code3 = """\
# Class distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Target', data=df, palette='viridis')
plt.title('Target Variable Distribution')
plt.show()
"""

code3_2 = """\
# Correlation heatmap of the first 10 features
plt.figure(figsize=(10, 8))
sns.heatmap(df.iloc[:, :10].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (First 10 Features)')
plt.show()
"""

text4 = "## 3. Data Splitting"
code4 = """\
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")
"""

text5 = "## 4. Implement XGBoost"
code5 = """\
# Initialize XGBoost Classifier
# We can tune parameters like max_depth, learning_rate, n_estimators, etc.
xgb_clf = xgb.XGBClassifier(
    objective='binary:logistic',
    max_depth=5,
    learning_rate=0.1,
    n_estimators=100,
    eval_metric='logloss',
    random_state=42
)

# Train the model
xgb_clf.fit(X_train, y_train)
"""

text6 = "## 5. Model Evaluation & Visualizations"
code6 = """\
# Make predictions
y_pred = xgb_clf.predict(X_test)
y_pred_proba = xgb_clf.predict_proba(X_test)[:, 1]

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("\\nClassification Report:\\n")
print(classification_report(y_test, y_pred))
"""

code7 = """\
# Confusion Matrix Visualization
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
"""

code8 = """\
# ROC Curve Visualization
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc='lower right')
plt.show()
"""

text9 = "## 6. Feature Importance"
code9 = """\
# Plot feature importance using XGBoost's built-in function
plt.figure(figsize=(10, 8))
xgb.plot_importance(xgb_clf, max_num_features=10, importance_type='weight', title='Feature Importance (Weight)')
plt.show()
"""

code9_2 = """\
# Alternative visualization with Seaborn
feature_importances = xgb_clf.feature_importances_
indices = np.argsort(feature_importances)[::-1]

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances[indices][:10], y=np.array(feature_names)[indices][:10], palette='viridis')
plt.title('Top 10 Feature Importances')
plt.xlabel('Relative Importance')
plt.ylabel('Feature')
plt.show()
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text),
    nbf.v4.new_code_cell(code1),
    nbf.v4.new_markdown_cell(text2),
    nbf.v4.new_code_cell(code2),
    nbf.v4.new_markdown_cell(text3),
    nbf.v4.new_code_cell(code3),
    nbf.v4.new_code_cell(code3_2),
    nbf.v4.new_markdown_cell(text4),
    nbf.v4.new_code_cell(code4),
    nbf.v4.new_markdown_cell(text5),
    nbf.v4.new_code_cell(code5),
    nbf.v4.new_markdown_cell(text6),
    nbf.v4.new_code_cell(code6),
    nbf.v4.new_code_cell(code7),
    nbf.v4.new_code_cell(code8),
    nbf.v4.new_markdown_cell(text9),
    nbf.v4.new_code_cell(code9),
    nbf.v4.new_code_cell(code9_2)
]

with open('c:/Users/Acer/Downloads/DSML-Progress-main/xgboost/xgboost_implementation.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

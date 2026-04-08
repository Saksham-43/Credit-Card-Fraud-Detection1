## Credit-Card-Fraud-Detection1

This project aims to detect fraudulent credit card transactions using Machine Learning techniques. The dataset is highly imbalanced, so different oversampling techniques were applied to improve fraud detection.

## Dataset

The dataset contains 284,807 transactions, including 492 fraud cases. Features V1–V28 are anonymized using PCA transformation, along with Time and Amount.

## Models Used
* Logistic Regression
* KNN
* Decision Tree
* Random Forest
* XGBoost

## Imbalance Handling Techniques
* Random Oversampling
* SMOTE
* ADASYN

## Best Model

XGBoost with SMOTE achieved the best performance based on Accuracy and ROC-AUC score.

## Streamlit App

A Streamlit web interface is created to allow users to test transactions and predict whether they are Fraudulent or Legitimate.

# Loan Defaulter Prediction

## Overview

In banking and financial services, the ability to predict whether a potential customer may default on a loan is crucial for minimizing risks. This project focuses on predicting the likelihood of loan defaults based on various customer attributes, such as income, credit amount, family status, and more. The objective is to help financial institutions make more informed, data-driven decisions when granting credit, reducing the risk associated with defaults, and optimizing credit allocation.

## Problem Statement

Financial institutions face substantial risks in extending credit, as defaults can lead to significant losses and instability in the financial ecosystem. This project aims to build a machine learning model to predict the likelihood of a loan default. By analyzing customer behavior, this model assists in improving operational efficiency, ensuring quicker and more accurate credit approvals, and ultimately supporting better risk management strategies.

## Dataset Overview

The **Loan Defaulter** dataset consists of various customer attributes, which are critical in predicting whether an individual is likely to default on a loan. Below are the key variables used in this analysis:

- **TARGET**: Indicates if the loan was paid on time (0 for no default, 1 for default)
- **NAME_CONTRACT_TYPE**: Type of loan contract
- **CODE_GENDER**: Gender of the customer
- **FLAG_OWN_CAR**: Indicates if the customer owns a car
- **FLAG_OWN_REALTY**: Indicates if the customer owns real estate
- **CNT_CHILDREN**: Number of children the customer has
- **AMT_INCOME_TOTAL**: Total income of the customer
- **AMT_CREDIT**: Credit amount requested
- **AMT_ANNUITY**: Annuity amount (monthly payment)
- **AMT_GOODS_PRICE**: Price of goods purchased
- **NAME_INCOME_TYPE**: Type of income the customer receives (e.g., working, pensioner)
- **NAME_EDUCATION_TYPE**: Customer's education level
- **NAME_FAMILY_STATUS**: Marital status
- **NAME_HOUSING_TYPE**: Type of housing the customer resides in
- **DAYS_BIRTH**: Age of the customer in days
- **DAYS_EMPLOYED**: Number of days employed before applying for the loan
- **ORGANIZATION_TYPE**: Type of organization the customer is employed by

### Data Quality Insights

#### Data Cleaning
- **Missing Values**: Some columns, such as `AMT_ANNUITY` and `AMT_GOODS_PRICE`, contained missing values, which were handled by removing rows with missing data.
- **Outliers**: Extreme values, such as unusually high credit amounts and employment days, were identified and analyzed. Some of these outliers were found to be valid, reflecting specific customer characteristics (e.g., unemployed or self-employed individuals).
  
#### Exogenous Data
External economic factors, such as interest rates, unemployment rates, and inflation, were incorporated into the analysis to provide broader economic context to the predictions. These factors can have a significant impact on repayment behavior.

## Data Visualization

Key visualizations provide insight into the dataset's characteristics:

- **Class Imbalance**: The dataset is heavily imbalanced, with 91.9% of clients having no payment difficulties (TARGET = 0) and only 8.1% facing defaults (TARGET = 1).
- **Gender Distribution**: The dataset shows a slight imbalance in gender, with more male data points.
- **Car Ownership and Real Estate Ownership**: These features show a correlation between asset ownership and default risk.
- **Children Distribution**: Having more children increases the likelihood of payment difficulties.
- **Credit Amount and Loan Annuity**: These are crucial features influencing the default prediction.

## Machine Learning Model

### Model Selection and Training

A **Logistic Regression** model was chosen due to its interpretability and effectiveness in binary classification tasks. The model was trained on the processed dataset and evaluated using cross-validation. We applied **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the classes and improve the model's ability to detect defaults.

### Model Evaluation

The model's performance was evaluated using metrics such as accuracy, precision, recall, and F1-score. The use of class balancing through SMOTE significantly improved the prediction of the minority class (defaults), resulting in a better overall performance.

### Confusion Matrix:
The confusion matrix before and after applying class balancing techniques shows a marked improvement in the model's ability to predict defaults.

## External Resources

To enrich the analysis and modeling process, the following resources were consulted:

1. **[Project website](https://darwincharris.github.io/ProjectSelection-DM202430/index.html)**: A detailed overview of the project selection process, which provided valuable context for defining the scope of the analysis.
   
2. **[Data Visualizations on Looker Studio](https://lookerstudio.google.com/reporting/3a5fadf5-0bf8-4370-a2a1-0b9add124378)**: Interactive visualizations that helped in the analysis and interpretation of key metrics, including loan default predictions and customer demographics.

3. **[Loan Defaulter Dataset on Kaggle](https://www.kaggle.com/datasets/gauravduttakiit/loan-defaulter?select=columns_description.csv)**: The source dataset used for this project. It contains detailed information about customers' financial attributes and loan performance.

These resources contributed significantly to the data exploration and model development phases of the project, offering deeper insights into the challenges faced by financial institutions when managing loan risks.

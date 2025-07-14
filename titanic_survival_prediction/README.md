# Titanic Survival Prediction

A beginner machine learning project to explore survival prediction on the Titanic dataset using logistic regression and random forest models.

# Overview

This project walks through the full supervised learning pipeline:

    - Data loading and exploration
    - Data cleaning and preprocessing
    - Feature encoding and transformation
    - Model training (Logistic Regression and Random Forest)
    - Model evaluation and comparison

# Models and Results

## Logistic Regression (Baseline)
    - Accuracy: ~81%
    - Stregnths: Performed well despite dataset simplicity and linear separability

## Random Foreest Classifier (Default)
    - Accuracy: ~79%
    - Initial hypothesis was that the random forest model, being non-linear, would outperform logistic regression.
      However, it underperformed slightly.
    - Possible reasons include:
        - Small dataset size limiting tree diversity
        - Model overfitting or default hyperparameters

## Random Forest (Tuned via GridSearchCV)
    - Best Parameters:
        {max_depth: 5,
        mas_features: sqrt,
        min_samples_leaf: 2,
        min_samples_split: 5,
        n_estimators: 200
        }
    - Cross-Validation Accuracy: ~83%
    - Test Set Accuracy: ~82.7%
    - F1 Score for Survivors: ~0.78
    - Clear performance improvement after hyperparameter tuning, especially in balancing precision and recall
    - Strong generalization with reduced overfitting, thanks to parameter constraints (max_depth, min_sample_leaf, etc)

## Data Source and Preproccessing

Dataset: [Titanic - Machine Learning from Disaster (Kaggle)] (https://www.kaggle.com/competitions/titanic/data)

Key preprocessing steps:
    - Removed columns with high missingness ('Cabin')
    - Imputed missing values in 'Age' and 'Embarked'
    - Encoded categorical variables:
        - 'Sex' mapped to binary
        - 'Embarked' one-hot encoded
    - Dropped identifiers ('Name', 'Ticket', 'PassengerId')

## Project Structure

    titanic_survival_prediction
    |--data
        |--train.csv
    |--notebooks
        |--Titanic_Survival_Prediction.ipynb
    |--requirements.txt
    |--README.md

## Tech Stack

    - Python 3.8+
    - pandas, numpy
    - seaborn, matplotlib
    - scikit-learn
    - Jypyter Notebook / VS Code

## Author

Antonio Scalfaro
GitHub: [https://github.com/tscalfaro]

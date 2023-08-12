# Importing all the necessary modules 
import os, sys 
from dataclasses import dataclass #type:ignore
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomeException
from src.utils import model_evaluation, save_pkl
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeRegressor

# Creating config class for model training
class ModelTrainerConfig:
    model_file_path = os.path.join("E:/Python_Models/Diamond_Price_Prediction/artifacts", "best_model.pkl")

# Creating class for Model Training
class ModelTrainer:
    def __init__(self):
        self.configDetails = ModelTrainerConfig()
    
    def model_trainer(self, train_data, test_data):
        try:
            logging.info('Initiating training ...')
            # Segregating the test and train data into input (X) and target (y)
            X_train = train_data.iloc[:,:-1]
            X_test = test_data.iloc[:, :-1]
            y_train = train_data.iloc[:,-1]
            y_test = test_data.iloc[:, -1]

            # Creating a dictionary having all the models
            models = {
                "Linear Regression": LinearRegression(),
                "Lasso Regression": Lasso(),
                "Ridge Regression": Ridge(),
                "Elastic Net": ElasticNet(),
                "Decision Tree Regressor": DecisionTreeRegressor()
            }

            report = model_evaluation(X_train, y_train, X_test, y_test, models)
            logging.info(f'The model report with r2 scores is \n{report}')
            logging.info('='*35)

            # Sorting the report dictionary as per their values 
            sorted_report = dict(sorted(report.items(), key = lambda item: item[1]))
            best_model_name = list(sorted_report.keys())[-1]
            best_score = list(sorted_report.values())[-1]
            best_model = models[best_model_name]
            logging.info(f'Our best model is: {best_model_name}: {best_score} (r2_score)')

            save_pkl(self.configDetails.model_file_path, best_model)
            logging.info('Pickle file of the best model is save successfully in artifacts')

        
        except Exception as e:
            logging.info('Error in model training')
            raise CustomeException(e, sys) # type: ignore
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import sys, os # type: ignore
from src.logger import logging
from src.exception import CustomeException
from dataclasses import dataclass #type: ignore
from utils import save_pkl

# Data Transformataion Configuration class 
@dataclass
class DataTransformConfig:
    pkl_path = os.path.join('E:/Python_Models/Diamond_Price_Prediction/artifacts', 'preprocessor.pkl')

# Data Transformation Class
class DataTransformation:
    def __init__(self):
        self.configDetails = DataTransformConfig() 
    
    def get_transformation_object(self):
        try:
            logging.info('Data Transformation Object is being created ...')

            # Segregating between numerical and categorical colums
            num_columns = ['carat', 'depth','table', 'x', 'y', 'z']
            cat_columns = ['cut', 'color', 'clarity']

            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info('Pipeline is being created ...')

            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,num_columns),
                ('cat_pipeline',cat_pipeline,cat_columns)
            ])

            logging.info('Pipeline is successfully created')

            return preprocessor
    
        except Exception as e:
            logging.info('Error Occured in Pipeline creation')
            raise CustomeException(e,sys) # type: ignore
    
    def data_transform(self, train_data_path, test_data_path):
        try:
            logging.info("Data_Transformation has initiated!")

            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)
        
            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_data.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_data.head().to_string()}')

            # Segregating into input (X) and target (y) variables
            X_train = train_data.drop(labels = ['id', 'price'], axis = 1) # type: ignore
            X_test = test_data.drop(labels = ['id', 'price'], axis = 1) # type: ignore
            y_train = train_data[['price']]  # type: ignore
            y_test = test_data[['price']]  # type: ignore

            # Getting the transformation object 
            preprocessor = self.get_transformation_object()
            X_train = pd.DataFrame(preprocessor.fit_transform(X_train), columns=preprocessor.get_feature_names_out()) # type: ignore
            X_test = pd.DataFrame(preprocessor.transform(X_test), columns=preprocessor.get_feature_names_out()) # type: ignore

            # Concating input and target variable together
            train_dataset = pd.concat([X_train, y_train], axis = 1)
            test_dataset = pd.concat([X_test, y_test], axis = 1)
        
            logging.info('Transformation Done succesfully')

            save_pkl(pkl_file_path = self.configDetails.pkl_path, pkl_obj = preprocessor)
            logging.info('Pickle File Extracted and saved in artifacts.')

            return (train_dataset, test_dataset, self.configDetails.pkl_path)
        
        except Exception as e:
            logging.info('Error while transformation !!')
            raise CustomeException(e, sys) # type: ignore
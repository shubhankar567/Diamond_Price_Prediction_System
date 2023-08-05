# Importing necessary libraries
import os
import sys # type: ignore
#sys.path.append(r'E:\Python_Models\Diamond_Price_Prediction\src') 
#Interpreter was unable to locate src.logger and src.exception
#So I written the above command in the venv\Lib\site-packages\sitecustomize.py

from src.logger import logging 
from src.exception import CustomeException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # type: ignore


# Data Ingestion Initialization
@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train_data.csv')
    test_data_path = os.path.join('artifacts', 'test_data.csv')
    raw_data_path = os.path.join('artifacts', 'raw_data.csv')

# Creating Data Ingestion class
class DataIngestion:
    def __init__(self):
        self.file_paths = DataIngestionConfig()
    
    def initiateIngestion(self):
        logging.info("Ingestion Started")
        try:
            df = pd.read_csv('E:/Python_Models/Diamond_Price_Prediction/notebooks/data/gemstone.csv')
            logging.info('Dataset is read')

            os.makedirs(os.path.dirname(self.file_paths.raw_data_path), exist_ok=True)
            df.to_csv(self.file_paths.raw_data_path, index = False)
            logging.info('Raw data is stored in artifacts')

            # Train test split
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            train_set.to_csv(self.file_paths.train_data_path, index = False, header = True)
            test_set.to_csv(self.file_paths.test_data_path, index = False, header = True)
            logging.info('Data Ingestion is done successfully!')
            
            return (
                self.file_paths.train_data_path, self.file_paths.train_data_path
            )

        except Exception as e:
            logging.info("Error during Data Ingestion")


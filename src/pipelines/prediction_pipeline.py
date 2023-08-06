import os, sys
from exception import CustomeException
from logger import logging
from utils import load_pkl
import pandas as pd

class PredictPipeine:
    def __init__(self):
        pass

    def prediction(self, input_data):
        try:
            # Creating the path for locating all the pickle files
            preprocess_pkl_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_pkl_path = os.path.join('artifacts', 'best_model.pkl')

            # Loading the pickle files
            preprocessor = load_pkl(preprocess_pkl_path)
            model = load_pkl(model_pkl_path)

            # Preprocessing
            input_processed = preprocessor.transform(input_data)

            # Predicting
            prediction = model.predict(input_processed)

            return prediction
        except Exception as e:
            logging.info('Error occured in Prediction Pipeline')
            raise CustomeException(e, sys) #type:ignore

# Creating a class for transforming the input data into a dataframe
class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def data_to_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomeException(e,sys) # type: ignore

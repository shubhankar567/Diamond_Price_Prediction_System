import os, sys
import pickle # type: ignore
from src.exception import CustomeException 
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeRegressor

# Dumping the pickle file
def save_pkl(pkl_file_path, pkl_obj):
    try:
        os.makedirs(os.path.dirname(pkl_file_path), exist_ok=True)
        with open(pkl_file_path, 'wb') as file_obj:
            pickle.dump(pkl_obj, file_obj)
    except Exception as e:
        raise CustomeException(e, sys) # type:ignore

# loading the pickle file
def load_pkl(pkl_file_path):
    try:
        with open(pkl_file_path, 'rb') as file_obj:
            pkl = pickle.load(file_obj)
        return pkl
    except Exception as e:
        logging.info('Error while Loading the pickle file')
        raise CustomeException(e, sys) # type: ignore
    
# Model Evaluation
def model_evaluation(X_train, y_train, X_test, y_test, models):
    try:
        logging.info('Evaluation started')
        report = {}
        for model_name in models:
            model = models[model_name]
            model.fit(X_train, y_train)

            # Making predictions
            y_predict = model.predict(X_test)

            # Getting all the metrics
            r2 = r2_score(y_test, y_predict)

            report[model_name] = r2

        logging.info(f'The report of all the models is \n{report}')
        return report
    except Exception as e:
        logging.info('Error occured while evaluating the model')
        raise CustomeException(e, sys) #type:ignore
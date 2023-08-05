import os, sys
import pickle
from src.exception import CustomeException 

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
        raise CustomeException(e, sys) # type: ignore
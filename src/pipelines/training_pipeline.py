import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

def run_pipeline():
    # Initialization of data ingestion
    ingest_obj = DataIngestion()
    train_path, test_path = ingest_obj.initiateIngestion() # type: ignore
    print(train_path, test_path)

    # Initialization for transformation
    transform_obj = DataTransformation()
    train_dataset, test_dataset, pkl_file_path = transform_obj.data_transform(train_path, test_path)

    # Initialization for Training
    trainer_obj = ModelTrainer()
    trainer_obj.model_trainer(train_dataset, test_dataset)
    print("training pipeline")

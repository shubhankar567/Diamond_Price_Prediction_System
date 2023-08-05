import pandas as pd
from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation

if __name__ == "__main__":
    # Initialization of data ingestion
    ingest_obj = DataIngestion()
    train_path, test_path = ingest_obj.initiateIngestion() # type: ignore
    print(train_path, test_path)

    # Initialization for transformation
    transform_obj = DataTransformation()
    train_dataset, test_dataset, _ = transform_obj.data_transform(train_path, test_path)

    # Initialization for Training
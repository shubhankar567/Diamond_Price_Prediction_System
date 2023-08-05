import pandas as pd
from components.data_ingestion import DataIngestion


if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiateIngestion()
    print(train_path, test_path)


# Diamond Price Prediction System

The Diamond Price Prediction System is a project that predicts the price of a diamond based on various input features such as cut, color, clarity, depth, table, x, y, z, and carat. The system utilizes several machine learning models, including Linear Regression, Lasso, Ridge, Elastic Net, and Decision Tree Regressor. After thorough evaluation, the Decision Tree Regressor has been selected as the best model for predicting diamond prices.

## Project Structure

The project is organized into the following main components:

### 1. src Folder

This folder contains the core source code for the Diamond Price Prediction System.

- **exception.py:** This module handles custom exceptions for the project.
- **logger.py:** It provides a logging utility to log events during the execution of the system.
- **utils.py:** Contains utility functions used across the project.
- **components Folder:**

  - **data_ingestion.py:** Handles the loading of input data from the "gemstone.csv" file.
  - **data_transformation.py:** Performs data preprocessing and transformation tasks.
  - **model_trainer.py:** Implements the training of the Decision Tree Regressor model.

- **pipelines Folder:**

  - **training_pipeline.py:** Initiates the entire training process, including data ingestion, transformation, and model training. The trained model is then saved in the artifacts folder.
  - **prediction_pipeline.py:** Loads the trained model and makes predictions based on new inputs.

### 2. setup.py

The `setup.py` file contains configuration details about the Diamond Price Prediction System.

### 3. requirements.txt

The `requirements.txt` file lists all the required libraries and dependencies for running the project. Make sure to install these dependencies before running the system.

### 4. artifacts Folder

The `artifacts` folder is used to store pickle files and datasets, including the trained Decision Tree Regressor model.

### 5. notebooks Folder

The `notebooks` folder contains Jupyter notebooks used for exploratory data analysis and experimentation during the development of the project.

### 6. application.py

The `application.py` file acts as a Flask web application that provides a user-friendly interface for users to input diamond characteristics and receive price predictions based on the trained model.

### Dependencies

The Diamond Price Prediction System relies on the following libraries:

- scikit-learn (sklearn)
- Python
- NumPy
- Seaborn
- Flask

## Getting Started

To run the Diamond Price Prediction System, follow these steps:

1. Install the required dependencies listed in `requirements.txt`.

2. Run the `training_pipeline.py` file to train the model and generate the required artifacts.

3. After successful training, run the `application.py` file to launch the Flask web application.

4. Access the application in your web browser and provide the diamond characteristics as input to get the predicted price.

## Contribution

Contributions to the Diamond Price Prediction System are welcome. If you find any issues or have suggestions for improvement, feel free to submit a pull request or open an issue.

Happy predicting!
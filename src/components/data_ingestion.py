## Loads raw data from files (CSV, JSON, etc.) or external sources (APIs, databases)...

import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exceptions import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer



@dataclass  ## used to create simple classes for storing data without writing boilerplate code like __init__() manually...
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() ##This line creates an instance of the DataIngestionConfig class and stores it in the ingestion_config attribute.

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")

        try:
            df = pd.read_csv('notebook\data\stud.csv') 
            logging.info("Completed reading the dataset as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)  ## This one line ensures the common directory 'artifacts' exists.
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_array,test_array = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    modeltrainer = ModelTrainer()
    modeltrainer.initiate_model_trainer(train_array,test_array)
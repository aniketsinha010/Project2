import sys
from dataclasses import dataclass
import os

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()    

    def get_data_transformer_object(self):
        try:
            numerical_columns = ['math_score', 'reading_score', 'writing_score']
            categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            numerical_pipeline = Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy="median")),
                    ("Standard Scaler",StandardScaler())
                ]
            )
            logging.info(f"Numerical Features : {numerical_columns}")

            categorical_pipeline = Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy="most_frequent")),
                    ("One Hot Encoder",OneHotEncoder())
                ]
            )
            logging.info(f"Categorical Features : {categorical_columns}")

            ##now combining the categorical_pipeline & numerical_pipeline using column Transformer...
            preprocessor = ColumnTransformer(
                [
                    ("Numerical Pipeline",numerical_pipeline,numerical_columns),
                    ("Categorical Pipeline",categorical_pipeline,categorical_columns),
                ]
            )

            return preprocessor            

        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Completed reading train and test data")

            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            target_column = "average"
            input_feature_train_df = train_df.drop(target_column,axis=1)
            target_feature_train_df = train_df[target_column]
            input_feature_test_df = test_df.drop(target_column,axis=1)
            target_feature_test_df = test_df[target_column]

            logging.info("Applying preprocessing object on training and test DataFrame")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            ## horizontally concatenating the input and output features...
            ## model training will be done in seperate file, for the convinience of storage we are combining back the input and output features
            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            logging.info("Completed Data Transformation")

            ## saving the preprocessor object to a pickle file...
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
            )

        except Exception as e:
            raise CustomException(e,sys)

""" 
In a typical ML project, the predict_pipeline.py file handles the inference logic—taking user input (or test data), transforming 
it using the saved preprocessor (e.g., scaler, encoder), and making predictions using the saved trained model.
"""

import sys
import pandas as pd

from src.exceptions import CustomException
from src.utils import save_object,load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(slef,features):
        try:
            model_path = "artifacts\model.pkl"
            preprocessor_path = "artifacts\preprocessor.pkl"

            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            ## transforming the input data...
            data_transformed = preprocessor.transform(features)
            ## predicting...
            data_predicted = model.predict(data_transformed)

            return data_predicted
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:  ## this class will be responsible for mapping (all the inputs we give to the html) to (the backend)...
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
            
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score


    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
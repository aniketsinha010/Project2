
## In utils.py file  put reusable helper functions — things that are not specific to any one stage  but are used across the project.

import os
import sys
import dill

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

from src.exceptions import CustomException


def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)



def evaluate_model(X_train,X_test,Y_train,Y_test,models):
    try:
        report = []
        for model_name,model in models.items():
            ## training the model...
            model.fit(X_train,Y_train)
            ## predicting...
            Y_predicted = model.predict(X_test)

            ## R2 Score...
            test_model_score = r2_score(Y_test,Y_predicted)

            report.append({
                "Model": model_name,
                "R2 Score": test_model_score
            })

        return report

    except Exception as e:
        raise CustomException(e,sys)
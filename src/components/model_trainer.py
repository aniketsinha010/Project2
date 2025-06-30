import sys
from dataclasses import dataclass
import os

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from catboost import CatBoostRegressor
from xgboost import XGBRegressor


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train,Y_train,X_test,Y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1],
            )
            models = {
                "Linear Regression" : LinearRegression(),
                "Lasso Regression" : Lasso(random_state=42),
                "Ridge Regression" : Ridge(random_state=42),
                "KNN Regressor": KNeighborsRegressor(),
                "Support Vector Regression" : SVR(),
                "Decision Tree": DecisionTreeRegressor(random_state=42),
                "Random Forest Regression": RandomForestRegressor(random_state=42),
                "XGB Regression": XGBRegressor(), 
                "CatBoost Regression": CatBoostRegressor(verbose=False,random_state=42),
                "AdaBoost Regression": AdaBoostRegressor(random_state=42)
            }

            model_report: list = evaluate_model(X_train,X_test,Y_train,Y_test,models)  ## importd from utils...

            # Find the best model based on highest R2 score
            best_model_dict = max(model_report, key=lambda x: x["R2 Score"])
            best_model_name = best_model_dict["Model"]
            best_model_score = best_model_dict["R2 Score"]
            best_model = models[best_model_name] ## this is the actual model...

            if best_model_score < 0.6:
                raise CustomException("No Best Models found",sys)
            logging.info("Best Model Found")

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            ## this is just for checking whether the code is correct...
            predicted = best_model.predict(X_test)
            r2 = r2_score(Y_test,predicted)
            logging.info(f"R2 Score of best model {best_model_name} is {best_model_score}")
            return r2

        except Exception as e:
            raise CustomException(e,sys)
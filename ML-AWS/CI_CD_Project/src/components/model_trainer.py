import numpy as np
import pandas as pd
import os, sys
from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import save_obj
from src.utils import evaluate_models



@dataclass
class modelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = modelTrainerConfig()

    def initiateModelTrainer(self, train, test):
        try:
            logging.info("Split Training and Testing Started")
            X_train, y_train, X_test, y_test = (
                train[:, :-1],
                train[:, -1],
                test[:,:-1],
                test[:, -1]
            )

            logging.info("Models being defined")
            models = {
                "Random Forest": RandomForestRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "KNearest Neighbour": KNeighborsRegressor(),
                #"XGBoost": XGBRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                #"CatBoost": CatBoostRegressor()
            }

            models_report:dict=evaluate_models(X_train=X_train, y_train=y_train, X_test = X_test, y_test = y_test, models=models)
            logging.info("Model Dictionary Set")
            

            best_model_score = max(models_report.values())
            

            best_model_name = list(models_report.keys())[
                list(models_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]


            #print(best_model_name)
            logging.info("Best Model Selected")

            if best_model_score<0.6:
                raise CustomException("No threshold model found")
            
            logging.info(f"Best Model Found")

            save_obj(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            predicted = best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square


        except Exception as e:
            CustomException(e, sys)

import pandas as pd
import numpy as np
import sys, os
from dataclasses import dataclass

from data_ingestion import DataIngestion
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transform_object(self):
        try:
            num_features = ['reading_score', 'writing_score']
            cat_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                    
                ]
            )

            logging.info("Numerical Pipeline Defined")
            logging.info("Categorical Pipeline Defined")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, num_features),
                    ("cat_pipeline", cat_pipeline, cat_features)
                ]
            )

            logging.info("Entire Pipeline Created")

            return preprocessor
        except Exception as e:
           raise CustomException(e, sys)

    def initiate_data_transform(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read Train-Test data")

            preprocessing_obj = self.get_data_transform_object()
            logging.info("Obtained Preprocessing Object")

            target_column = "math_score"
            numerical_column = ["writing_score", "reading_score"]

            X_train_df = train_df.drop(columns=[target_column], axis=1)
            y_train_df = train_df[target_column]

            X_test_df = test_df.drop(columns=[target_column], axis=1)
            y_test_df = test_df[target_column]

            X_train_preprocess = preprocessing_obj.fit_transform(X_train_df)
            X_test_preprocess = preprocessing_obj.transform(X_test_df)
            logging.info("Completed Transforms")

            train_arr = np.c_[X_train_preprocess, np.array(y_train_df)]
            test_arr = np.c_[X_test_preprocess, np.array(y_test_df)]
            logging.info("Saving Data")

            save_obj(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return(train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)

            


        except Exception as e:
           raise CustomException(e, sys)

    
if __name__ == "__main__":
    obj = DataIngestion()
    train, test = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transform(train, test)





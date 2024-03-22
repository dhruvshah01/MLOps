import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:            
            model_pth = "/Users/dhruvshah/Desktop/MLOps/ML-AWS/CI_CD_Project/src/components/artifacts/model.pkl"
            preprocessor_pth = "/Users/dhruvshah/Desktop/MLOps/ML-AWS/CI_CD_Project/src/components/artifacts/preprocessor.pkl"
            model = load_object(file_pth = model_pth)
            preprocessor = load_object(file_pth = preprocessor_pth)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(sys, e)


class CustomData:
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

    def get_data_as_frame(self):
        try:
            data_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            df = pd.DataFrame(data_dict)
            return df
        except Exception as e:
            raise CustomException(sys, e)


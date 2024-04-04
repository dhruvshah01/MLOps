import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from pathlib import Path
from TextSummarizer.entity import DataIngestionConfig  
import os  

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading data from {self.config.source_url}")
            filename, headers = request.urlretrieve(
                url = self.config.source_url, 
                filename = self.config.local_data_file)
            logger.info(f"{filename} downloaded with information: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists")

    def extract_data(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_obj:
            print(zip_obj)
            zip_obj.extractall(unzip_path)

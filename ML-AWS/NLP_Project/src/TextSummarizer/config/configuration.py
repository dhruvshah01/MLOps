from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml, create_directory
from TextSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path: str = CONFIG_FILE_PATH,
                 params_file_path: str = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        lst = [self.config.artifacts_root]
        create_directory(lst)
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

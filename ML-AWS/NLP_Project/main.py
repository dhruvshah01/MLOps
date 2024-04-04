from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Pipeline"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(f"Error in {STAGE_NAME}: {e}")
    raise e
import os
import sys
import logging

logging_str = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
log_dir = "Logs"
log_filePath = os.path.join(log_dir, "log.txt")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filePath),
        logging.StreamHandler(sys.stdout)
    ]
    )

logger = logging.getLogger("textSummarizerLogger")
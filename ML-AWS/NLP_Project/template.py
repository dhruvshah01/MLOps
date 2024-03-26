import os
import logging
from pathlib import Path

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

project_name = "TextSummarizer"

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "experiments/trials.ipynb",
    "README.md",
]

for filepath in list_files:
    filepath = Path(filepath)
    fileDir, fileName = os.path.split(filepath)
    if fileDir!= "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"{fileDir} created")

    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Empty file {filepath} created!")
            
    else:
        logging.info(f"File {filepath} already exists!")
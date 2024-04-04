import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file {yaml_file.name} read successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file is empty: {path}")
    except Exception as e:
         raise e


def create_directory(path_to_directories: list, verbose = True) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created")
    return None

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"


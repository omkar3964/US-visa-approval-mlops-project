import os
import sys
import yaml
import dill
import numpy as np
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import get_logger

logging = get_logger('')

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns the content as a dictionary.
    """
    logging.info(f"Reading YAML file: {file_path}")
    try:
        with open(file_path, "rb") as yaml_file:
            content = yaml.safe_load(yaml_file)
        logging.info(f"YAML file loaded successfully: {file_path}")
        return content

    except Exception as e:
        raise USvisaException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes data to a YAML file.
    If replace=True, removes any existing file before writing.
    """
    logging.info(f"Writing YAML file: {file_path}")
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            yaml.dump(content, file, allow_unicode=True)

        logging.info(f"YAML file written successfully: {file_path}")

    except Exception as e:
        raise USvisaException(e, sys) from e


def save_numpy_array_data(file_path: str, array: np.ndarray) -> None:
    """
    Save a numpy array to a file.
    """
    logging.info(f"Saving numpy array to: {file_path}")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
        logging.info("Numpy array saved successfully.")
    except Exception as e:
        raise USvisaException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    Load a numpy array from a file.
    """
    logging.info(f"Loading numpy array from: {file_path}")
    try:
        with open(file_path, "rb") as file_obj:
            array = np.load(file_obj)
        logging.info("Numpy array loaded successfully.")
        return array
    except Exception as e:
        raise USvisaException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    """
    Serialize and save a Python object using dill.
    """
    logging.info(f"Saving object to: {file_path}")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Object saved successfully.")
    except Exception as e:
        raise USvisaException(e, sys) from e


def load_object(file_path: str) -> object:
    """
    Load a serialized Python object using dill.
    """
    logging.info(f"Loading object from: {file_path}")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Object loaded successfully.")
        return obj
    except Exception as e:
        raise USvisaException(e, sys) from e


def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    Drops specified columns from a pandas DataFrame.
    """
    logging.info(f"Dropping columns: {cols}")
    try:
        df = df.drop(columns=cols, axis=1)
        logging.info("Columns dropped successfully.")
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e

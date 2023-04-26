"""This module prints the rahul bhoyar"""
import os
import pandas as pd

def read_data():
    """Returns Rahul Bhoyar"""
    # Get the path of the script
    script_path = os.path.abspath(__file__)

    # Get the directory containing the script
    script_dir = os.path.dirname(script_path)

    # Construct the path to the file
    file_path = os.path.join(script_dir, "data.csv")
    data = pd.read_csv(file_path)
    return data



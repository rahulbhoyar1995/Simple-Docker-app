"test case file"
import sys
import os
import pandas as pd
import pytest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from project import read_data
# Get the absolute path of the "project.py" file

def test_read_data():
    """Test if read_data() returns a pandas dataframe"""
    data = read_data()
    assert isinstance(data, pd.DataFrame)
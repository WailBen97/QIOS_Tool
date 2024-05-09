import os
import pandas as pd
import numpy as np


def load_data(data_dir, data_file):
    """
    Load data from a file in the data directory.
    """
    data_path = os.path.join(data_dir, data_file)

    return pd.read_csv(data_path)

def preprocess_data_from_interface(df):
    """
    Preprocess the data.
    """
    # Drop rows with missing values
    df = df.dropna()

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Convert categorical columns to numeric
    df = pd.get_dummies(df)

    return df
def obtenir_zone_climatique(code_postal):
    zone_climatique = {
        'H1': [1, 2, 3, 5, 8, 10, 14, 15, 19, 21, 23, 25, 27, 28, 38, 39, 42, 43, 45, 51, 52, 54, 55, 57, 58, 59, 60, 61, 62, 63, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 80, 87, 88, 89, 90, 91, 92, 93, 94, 95],
        'H2': [4, 7, 9, 12, 16, 17, 18, 22, 24, 26, 29, 31, 32, 33, 35, 36, 37, 40, 41, 44, 46, 47, 48, 49, 50, 53, 56, 64, 65, 72, 79, 81, 82, 84, 85, 86],
        'H3': [6, 11, 13, 20, 30, 34, 66, 83]
    }

    for zone, codes in zone_climatique.items():
        if code_postal in codes:
            return zone

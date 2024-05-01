import numpy as np
import pandas as pd

def remove_na(df):
    """Function to remove NA values if they exist"""
    # Check if there are any NA values in the DataFrame
    if df.isna().any().any():
        print("NA values found. Removing them...")
        # Remove all rows with NA values
        df = df.dropna()
    else:
        print("No NA values found.")
    return df

def remove_duplicates(df):
    """Function to remove duplicates if they exist"""
    # Check if there are any duplicate rows in the DataFrame
    if df.duplicated().any():
        print("Duplicate rows found. Removing them...")
        # Remove duplicate rows, keeping the first occurrence
        df = df.drop_duplicates(keep='last') # keep=False to remove all occurrences of duplicates.
    else:
        print("No duplicate rows found.")
    return df
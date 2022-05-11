import pandas as pd
import numpy as np
import os


class data_cleaner:
    
    def __init__(self):
        pass
    
    def percent_missing(df):
    
        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)
    
        # Count number of missing values per column
        missingCount = df.isnull().sum()
    
        # Calculate total number of missing values
        totalMissing = missingCount.sum()
    
        # Calculate percentage of missing values
        print("This dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")
    
    
    def fix_missing_ffill(df, col):
        df[col] = df[col].fillna(method='ffill')
        return df[col]
    
    
    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
           
            df.drop_duplicates(inplace=True)
    
            return df
        
    def convert_to_datetime(df, columns):
        for col in columns:
            df[col] = pd.to_datetime(df[col])
    
    
    def convert_to_int(df, columns):
        for col in columns:
            df[col] = df[col].astype("int64")
            
            return df
        

import pandas as pd
import numpy as np
import os


class Cleaner:
    
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
        
    # drop columns with more than 30% missing values
    def drop_missing_value(df, col):
        perc = 30.0 # in percent %
        min_count =  int(((100-perc)/100)*df.shape[0] + 1)
        mod_df = df.dropna( axis=1, thresh=min_count)
        
        return mod_df
    
    
    # fill the forward value 
    def fix_missing_ffill(df, col):
        df[col] = df[col].fillna(method='ffill')
        return df[col]

    
    # fill the backward value 
    def fix_missing_bfill(df, col):
        df[col] = df[col].fillna(method='bfill')
        return df[col]
    
    

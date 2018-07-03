import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import Imputer #deals with missing values
import os.path
from pprint import pprint

""" 
Helpers for reading the data file
"""

fname = 'data/UCI_Credit_Card.csv'
index_column = 'ID'
n = 10

def read_file(nan_strategy = None):

    if not(nan_strategy == 'drop_nan' or nan_strategy == 'fill_na' or nan_strategy == None):
        raise ValueError("Chose the value drop_nan, fill_na or none!")

    df = pd.read_csv(fname, index_col = index_column)
    if not os.path.isfile(fname):
         raise FileNotFoundError

    print(df.head(n))          #print n rows from the data
    print('Your are working with a file with shape: {}'.format(df.shape), 'with data type: {}', '\n',df.dtypes.value_counts())   

    print('The column names ===> ', '\n'
            ,df.columns)
    
    #print'The NaN values: ===>',df.isnull().sum(), '\n'# returns True if any of the values in the column is missing, otherwise it is a false 
    
    (df == 0).astype(int).sum(axis=1)                       #counts the zeros for each row
    
    miss_val = df.isnull().sum()                            #total missing values
    miss_val_fraction = 100 * df.isnull().sum() / len(df)   #percentage of missing values
    miss_val_table = pd.concat([miss_val, miss_val_fraction], axis=1) #create a new table for storing the info about missing values
    miss_val_table = miss_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'}) #rename missing values
    miss_val_sorted = miss_val_table[miss_val_table.iloc[:,1] != 0].sort_values(       
            '% of Total Values', ascending=False).round(1)  
    
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n" 
            "There are " + str(miss_val_sorted.shape[0]) +
            " columns that have missing values.")
    #(df == 'NaN').astype(int).sum(axis=1)

    if nan_strategy == 'drop_nan':
        return df.dropna()
    
    if nan_strategy == 'fill_na':
        return df.fillna(df.mean())
    
    if nan_strategy == None:
        return df

#read_file()

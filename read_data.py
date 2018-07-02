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
    print('Your are working with a file with shape: {}'.format(df.shape), '\n')    
    
    #list_col = df.columns.values #creates a list with the column names  
    print('The column names ===> ' ,df.columns)
    
    #print'The NaN values: ===>',df.isnull().sum(), '\n'# returns True if any of the values in the column is missing, otherwise it is a false 
    
    (df == 0).astype(int).sum(axis=1) # counts the zeros for each row
    (df == 'NaN').astype(int).sum(axis=1)

    #df_noNan = df.dropna() 
    if nan_strategy == 'drop_nan':
        return df.dropna()
    
    df_replacedNan = df.fillna(df.mean())
    #df_replacedNan = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) # or median, most_frequent, depending on the case
    
    if nan_strategy == 'fill_na':
        return df.fillna(df.mean())
    
    if nan_strategy == None:
        return df

    #return df

#read_file()

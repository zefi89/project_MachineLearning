import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import Imputer #deals with missing values
import os.path

""" 
Helpers for reading the data file
"""

fname = 'data/UCI_Credit_Card.csv'
index_column = 'ID'

def read_file():
    df = pd.read_csv(fname, index_col = index_column)
    if not os.path.isfile(fname):
         raise FileNotFoundError

    print(df.head(10))          #print 10 rows from the data
    print'Your are working with a file with shape: ', df.shape
    
    list_col = df.columns.values #creates a list with the column names  
    print'The column names ===> ' ,list_col
    #print'The NaN values: ===>',df.isnull().sum(), '\n'# returns True if any of the values in the column is missing, otherwise it is a false 
    
    (df == 0).astype(int).sum(axis=1) # counts the zeros for each row
    (df == 'NaN').astype(int).sum(axis=1)


    #deal with NaN values: drop or fill Nan values based on the problem
    
    #get some statistics about the missing values

    df_noNan = df.dropna() 
    
    #fill missing values with the mean
    df_replacedNan = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) # or median, most_frequent, depending on the case

read_file()

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from read_data import read_file
plt.style.use('fivethirtyeight')
"""
Making some plots to check for anomalies & understand the data
"""

#check variable distributions
df = read_file()
my_path = 'plots'

file=open("output.txt", 'w')  #store into a file the descriptions for each column
for column in df:
    out = df[column].describe()
    s = str(out)
    file.write(s + '\n')
file.close()



for column in df:
    name = list(df[column])
    plt.hist(df[column], alpha = 0.3)
    plt.title('Hist '+ column);
    plt.xlabel(column); 
    plt.ylabel('Count' + column);
    plt.savefig(os.path.join(my_path, "hist_{}.png".format(column)))

"""
For checking single / specific plot
"""
#fig = plt.figure()
#plt.hist(df['AGE'], alpha=0.3)
#plt.hist(df['default.payment.next.month'], alpha=0.3)
#plt.title('Age of Client'); plt.xlabel('Age (years)'); plt.ylabel('Count');
#fig.savefig('plots/payment_hist.png')
#plt.show()


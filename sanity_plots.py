import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from read_data import read_file
plt.style.use('fivethirtyeight')
"""
Making some plots to check for anomalies & understand the data
"""

#check variable distributions
df = read_file()

#store into a file the descriptions for each column 

file=open("output.txt", 'w')  
for column in df:
    out = df[column].describe()
    s = str(out)
    file.write(s + '\n')
file.close()


#df['PAY_0'].plot()

fig = plt.figure()
plt.hist(df['AGE'], alpha=0.3)
plt.title('Age of Client'); plt.xlabel('Age (years)'); plt.ylabel('Count');
fig.savefig('plots/age_hist.png')
#plt.show()


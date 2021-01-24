"""
Filename        : read_csv.py
Created On      : 2021-01-24
Latest Modified : 2021-01-24 
Author          : Yutaro Nakayama
Description     : sample of reading csv file.  
"""

import sys
import pandas as pd

args = sys.argv
file_name = args[1]
row = args[2]

def read_csv(file_name, row):
  col_names = ['c{0:02d}'.format(i) for i in range(14)]
  df = pd.read_csv(file_name, names=col_names)
  print(df.iloc[:,1:13])
read_csv(file_name, row)

import pandas as pd
import numpy as np

df = pd.read_csv('data_full.csv', sep = ';')

print(df.to_string())
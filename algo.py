import pandas as pd
from scipy import spatial

df = pd.read_csv('data_full_full.csv', sep = ';')

print(df.to_string())



#als imput misschien nieuwe lijst
#en dan top 10 dichts bij de cosine similarity recommenden?
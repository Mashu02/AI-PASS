import pandas as pd
from math import sqrt

df = pd.read_csv('data_full_full.csv', sep=';')

# print(df.to_string())

df_list = df.values.tolist()
# print(df_list)


list_user = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, ]

# https://en.wikipedia.org/wiki/Cosine_similarity
def cosine_sim(lijst):
    for x in df_list:
        sum = 0
        sumA = 0
        sumB = 0
        for i, j in zip(x, lijst):
            sum += i * j
            sumA += i * i
            sumB += j * j

        cossim = sum / ((sqrt(sumA)) * (sqrt(sumB)))
        print(cossim)
        print(x)

cosine_sim(list_user)


# verschillende returns en stuk gui

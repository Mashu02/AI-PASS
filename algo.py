import pandas as pd
from math import sqrt
from collections import Counter

df = pd.read_csv('data_full_full.csv', sep=';')
df_list = df.values.tolist()



#wil ik doen bij de top 5 combinaties hoevaak die voor komt
def most_picks():
    c = Counter()
    for combination in df_list:
        c[str(combination)] += 1


    #print 13 komt 13 keer voor
    print(c['[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'])
    #print(c)





list_user = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

# https://en.wikipedia.org/wiki/Cosine_similarity
def cosine_sim(lijst):
    top = []
    combination_with_cosim = {}
    for x in df_list:
        sum = 0
        sumA = 0
        sumB = 0
        for i, j in zip(x, lijst):
            sum += i * j
            sumA += i * i
            sumB += j * j
        cossim = sum / ((sqrt(sumA)) * (sqrt(sumB)))
        combination_with_cosim[str(x)] = cossim
    print(combination_with_cosim)

#cosine_sim(list_user)


#kan nu gewoon de hoogste waarde doen en dan combination in lijst






# verschillende returns en stuk gui

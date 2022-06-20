import pandas as pd
from math import sqrt

df = pd.read_csv('data_full_full.csv', sep = ';')

print(df.to_string())

df_list = df.values.tolist()
#print(df_list)


list_user = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#https://en.wikipedia.org/wiki/Cosine_similarity
def cosine_sim(lijst):
    sum = 0
    sumA = 0
    sumB = 0

    for x in (df_list):
        for i,j in zip(x, lijst):
            sum += i*j
            sumA += i*i
            sumB += j*j

        cossim = sum / ((sqrt(sumA)) * (sqrt(sumB)))
        print(cossim)
        print(x)

#cosine_sim(list_user)


# def jaccard():
#     for x in (df_list):
#         intersec = len(list(set(x).intersection(list_user)))
#         union = (len(x) + len(list_user)) - intersec
#         y = float(intersec) / union
#         print(y)
#
# jaccard()
#kijk hoeveel 1 en er in de lijst zitten
#moet dubble for loop en dan kijken of ze allbei gelijk zijn aan 1 dan counter +=1
#dan counter / len



#als imput misschien nieuwe lijst
#en dan top 10 dichts bij de cosine similarity recommenden?
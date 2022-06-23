import pandas as pd
from math import sqrt
from collections import Counter
import numpy as np
from PIL import Image




df = pd.read_csv('data_full_full.csv', sep=';')
df_list = df.values.tolist()

list_user = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

def color_random_image(list_color_rgb):
    how_many_colors = len(list_color_rgb)

    # Make a Numpy array 500x500 of random integers 0, 1 or 2
    na = np.random.randint(0, how_many_colors, (500,500), np.uint8)

    # Convert to PIL Image
    im = Image.fromarray(na)

    # Push in 3-entry palette with red, blue and yellow:
    im.putpalette(list_color_rgb)

    # Save
    im.save('result.png')


#wil ik doen bij de top 5 combinaties hoevaak die voor komt
def most_picks(combination_nummer):
    c = Counter()
    for combination in df_list:
        c[str(combination)] += 1
    #print 13 komt 13 keer voor
    print(c[combination_nummer])

#most_picks('[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]')



# https://en.wikipedia.org/wiki/Cosine_similarity
def cosine_sim(lijst, top_hoeveel):
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

    #remove de input
    del combination_with_cosim[str(list_user)]

    #de top waardes in een dictionary
    top_dic = dict(Counter(combination_with_cosim).most_common(top_hoeveel))
    top_dic_keys = list(top_dic.keys())
    print(top_dic)
    #return list met top 5 als string
    return top_dic_keys


print(cosine_sim(list_user,5))



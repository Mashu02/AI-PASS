import pandas as pd
from math import sqrt
from collections import Counter
import random
from PIL import Image
import pygame

df = pd.read_csv('data_full_full.csv', sep=';')
df_list = df.values.tolist()
list_user = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

def create_image(colors):
    image = Image.new('RGB', (500, 500))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), random.choice(colors))
    image.save('image.png')

def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

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


#print(cosine_sim(list_user,5))



import pandas as pd
from math import sqrt
from collections import Counter
import random
from PIL import Image
import pygame
import colors as c
import pyperclip

#kleuren van algoritme naar rgb codes
colors = [(0, 0, 0), (128, 128, 128), (192, 192, 192), (255, 255, 255), (139, 69, 19), (255, 0, 0)
          , (255, 150, 0), (255, 215, 0), (245, 245, 220), (255, 255, 0), (0, 128, 0), (64, 224, 208), (0, 128, 128)
          , (0, 0, 255), (238, 130, 238), (128, 0, 128), (255, 105, 180)]

df = pd.read_csv('data_full_full.csv', sep=';')
df_list = df.values.tolist()

# voor rbg value naar text
def get_key(val):
    for key, value in c.color_with_rbg.items():
        if val == value:
            return key


#om een size x size image te genereren met gegeven kleuren maar random plek
def create_image(colors, size):

    image = Image.new('RGB', (size, size))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), random.choice(colors))
    image.save('image.png')

def create_image2(colors, size):
    image = Image.new('RGB', (size, size))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), random.choice(colors))
    image.save('image2.png')

# om van de keys uit dictionary naar rgb code
def list_to_color(tuple):
    return [color for keep, color in zip(tuple, colors) if keep]

#voor PIL image naar pygame
def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

#copy de gelikte combinations in clip board
def list_to_clipboard(output_list):
    if len(output_list) > 0:
        pyperclip.copy('\n'.join(output_list))

# wil ik doen bij de top 5 combinaties hoevaak die voor komt
#telt hoevaak kleur combinatie is voorgekomen
def most_picks(combination_nummer):
    c = Counter()
    for combination in df_list:
        c[str(combination)] += 1
    return (c[combination_nummer])


# https://en.wikipedia.org/wiki/Cosine_similarity
#algoritme cosine similarity
def cosine_sim(lijst, top_hoeveel, input_user):
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
        combination_with_cosim[tuple(x)] = cossim

    # remove de input
    if input_user not in combination_with_cosim:
        pass
    else:
        del combination_with_cosim[input_user]

    # de top waardes in een dictionary
    top_dic = dict(Counter(combination_with_cosim).most_common(top_hoeveel))
    top_dic_keys = list(top_dic.keys())
    # return list met top 5 als string
    return top_dic_keys


def cosine_sim_score(lijst, top_hoeveel, input_user):
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
        combination_with_cosim[tuple(x)] = cossim

    # remove de input
    if input_user not in combination_with_cosim:
        pass
    else:
        del combination_with_cosim[input_user]

    # de top waardes in een dictionary
    top_dic = dict(Counter(combination_with_cosim).most_common(top_hoeveel))
    top_dic_values = list(top_dic.values())
    # return list met top 5 als string
    return top_dic_values



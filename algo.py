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


def get_key(val):
    """voor rbg value naar text uit dictionary colors.py

    Args:
        val (tuple): value in rbg value waarde

    Returns:
        key (str): de key van de gegeven value
    """
    for key, value in c.color_with_rbg.items():
        if val == value:
            return key

def create_image(colors, size):
    """om een size x size image te genereren met gegeven kleuren maar random plek

    Args:
        colors (list): list van value in rbg value waarde
        size (int): width en heigt in pixel van de generated kleuren

    Returns:
        image (image): een image die gesaved word
    """
    image = Image.new('RGB', (size, size))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), random.choice(colors))
    image.save('image.png')

def create_image2(colors, size):
    """om een size x size image te genereren met gegeven kleuren maar random plek

    Args:
        colors (list): list van value in rbg value waarde
        size (int): width en heigt in pixel van de generated kleuren

    Returns:
        image (image): een image die gesaved word
    """
    image = Image.new('RGB', (size, size))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), random.choice(colors))
    image.save('image2.png')

def list_to_color(tuple):
    """om van de keys uit dictionary naar rgb code in list

    Args:
        tuple (tuple): combinatie van 0 en 1 in een tuple

    Returns:
        list (list): een lijst met waardes van rgb value
    """
    return [color for keep, color in zip(tuple, colors) if keep]

def pilImageToSurface(pilImage):
    """voor PIL image naar pygame

    Args:
        pilImage (png file): PIL image

    Returns:
        image (pygame.image.fromstring): image om te kunnen gebruiken in pygame
    """
    return pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

def data_check():
    """kijkt of de dataset wel echt werkt

    Args:
        None

    Returns:
        True (bool): als er geen [0,0,...] in zit en als die niet leeg is
        False (bool): als er wel [0,0,...] en of leeg is
    """
    if [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] not in df_list and len(df_list) >= 1:
        return True
    else:
        return False

def list_to_clipboard(output_list):
    """copy de gelikte combinations in clip board

    Args:
        output_list (list): lijst die je wilt kopiëren

    Returns:
        None
    """
    if len(output_list) > 0:
        pyperclip.copy('\n'.join(output_list))

def most_picks(combination_nummer):
    """telt hoevaak kleur combinatie is voorgekomen

    Args:
        combination_nummer (str): de combinatie met 0 en 1 in een tuple als string

    Returns:
        c[combination_nummer] (int): hoevaak het voorkomt
    """
    c = Counter()
    for combination in df_list:
        c[str(combination)] += 1
    return (c[combination_nummer])


# https://en.wikipedia.org/wiki/Cosine_similarity

def cosine_sim(lijst, top_hoeveel, input_user, whole_data_in_list):
    """algoritme cosine similarity met de combinatie van kleuren

    Args:
        lijst (list): input van de gebruiker in lijst van 1 en 0
        top_hoeveel (int): de top hoeveel je wilt in combinatie
        input_user (tuple): de gebruiker input in een tuple om te verwijderen

    Returns:
        top_dic_keys (list): return de top combinaties van kleuren[0 en 1]en in een list
    """
    combination_with_cosim = {}
    #elke combinatie in de hele dataset
    for x in whole_data_in_list:
        sum = 0
        sumA = 0
        sumB = 0
        for i, j in zip(x, lijst):

            #dot product, doet alle elementen in de gegeven lijst * alle andere elementen in de dataframe
            sum += i * j

            #magnitude, doet elk van de elementen in kwadraat en telt alles op dan pak je de wortel ervan
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
    return top_dic_keys

def cosine_sim_score(lijst, top_hoeveel, input_user, whole_data_in_list):
    """algoritme cosine similarity met de percentage van kleuren

    Args:
        lijst (list): input van de gebruiker in lijst van 1 en 0
        top_hoeveel (int): de top hoeveel je wilt in combinatie
        input_user (tuple): de gebruiker input in een tuple om te verwijderen

    Returns:
        top_dic_values (list): return de top combinaties met percentage van kleuren
    """
    combination_with_cosim = {}
    for x in whole_data_in_list:
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



import sys
import pygame
import colors as c
import buttons as b

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()


#screen
screen = pygame.display.set_mode((1700, 900))
pygame.display.set_caption('color matcher')
font = pygame.font.SysFont(None, 20)
click = False


clicked_button = {"Black" : 0,  "Grey" : 0,  "Silver" : 0,  "White" : 0,  "Brown" : 0,
                  "Red" : 0,  "Orange" : 0,  "Gold" : 0,  "Beige" : 0,  "Yellow" : 0,
                  "Green" : 0,  "Turqoise" : 0,  "Teal" : 0,  "Blue" : 0,  "Violet" : 0,
                  "Purple" : 0,  "Pink" : 0}
clicked_button_list = []
clicked_button_list_codes = []

def place_button(button, button_color):
    return pygame.draw.rect(screen, button, button_color)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:

        screen.fill((240,255,255))
        draw_text('pick colors', font, c.black, screen, 20, 20)
        draw_text('selected colors', font, c.black, screen, 650, 80)
        y_pos = 100
        mouse = pygame.mouse.get_pos()


        button_feedback = pygame.Rect(1445, 800, 200, 50)
        if button_feedback.collidepoint((mouse)):
            if click:
                feedback()
        elif b.button_black.collidepoint((mouse)):
            if click:
                if clicked_button["Black"] == 1 or (0, 0, 0) in clicked_button_list_codes or "Black" in clicked_button_list:
                    clicked_button["Black"] = 0
                    clicked_button_list_codes.remove((0, 0, 0))
                    clicked_button_list.remove("Black")
                else:
                    clicked_button["Black"] = 1
                    clicked_button_list_codes.append((0, 0, 0))
                    clicked_button_list.append("Black")
        elif b.button_grey.collidepoint((mouse)):
            if click:
                if clicked_button["Grey"] == 1 or (128,128,128) in clicked_button_list_codes or "Grey" in clicked_button_list:
                    clicked_button["Grey"] = 0
                    clicked_button_list_codes.remove((128,128,128))
                    clicked_button_list.remove("Grey")
                else:
                    clicked_button["Grey"] = 1
                    clicked_button_list_codes.append((128,128,128))
                    clicked_button_list.append("Grey")
        elif b.button_silver.collidepoint((mouse)):
            if click:
                if clicked_button["Silver"] == 1 or (192,192,192) in clicked_button_list_codes or "Silver" in clicked_button_list:
                    clicked_button["Silver"] = 0
                    clicked_button_list_codes.remove((192,192,192))
                    clicked_button_list.remove("Silver")
                else:
                    clicked_button["Silver"] = 1
                    clicked_button_list_codes.append((192,192,192))
                    clicked_button_list.append("Silver")
        elif b.button_white.collidepoint((mouse)):
            if click:
                if clicked_button["White"] == 1 or (255,255,255) in clicked_button_list_codes or "White" in clicked_button_list:
                    clicked_button["White"] = 0
                    clicked_button_list_codes.remove((255,255,255))
                    clicked_button_list.remove("White")
                else:
                    clicked_button["White"] = 1
                    clicked_button_list_codes.append((255,255,255))
                    clicked_button_list.append("White")
        elif b.button_brown.collidepoint((mouse)):
            if click:
                if clicked_button["Brown"] == 1 or (139,69,19) in clicked_button_list_codes or "Brown" in clicked_button_list:
                    clicked_button["Brown"] = 0
                    clicked_button_list_codes.remove((139,69,19))
                    clicked_button_list.remove("Brown")
                else:
                    clicked_button["Brown"] = 1
                    clicked_button_list_codes.append((139,69,19))
                    clicked_button_list.append("Brown")
        elif b.button_red.collidepoint((mouse)):
            if click:
                if clicked_button["Red"] == 1 or (255,0,0) in clicked_button_list_codes or "Red" in clicked_button_list:
                    clicked_button["Red"] = 0
                    clicked_button_list_codes.remove((255,0,0))
                    clicked_button_list.remove("Red")
                else:
                    clicked_button["Red"] = 1
                    clicked_button_list_codes.append((255,0,0))
                    clicked_button_list.append("Red")
        elif b.button_orange.collidepoint((mouse)):
            if click:
                if clicked_button["Orange"] == 1 or (255,150,0) in clicked_button_list_codes or "Orange" in clicked_button_list:
                    clicked_button["Orange"] = 0
                    clicked_button_list_codes.remove((255,150,0))
                    clicked_button_list.remove("Orange")
                else:
                    clicked_button["Orange"] = 1
                    clicked_button_list_codes.append((255,150,0))
                    clicked_button_list.append("Orange")
        elif b.button_gold.collidepoint((mouse)):
            if click:
                if clicked_button["Gold"] == 1 or (255,215,0) in clicked_button_list_codes or "Gold" in clicked_button_list:
                    clicked_button["Gold"] = 0
                    clicked_button_list_codes.remove((255,215,0))
                    clicked_button_list.remove("Gold")
                else:
                    clicked_button["Gold"] = 1
                    clicked_button_list_codes.append((255,215,0))
                    clicked_button_list.append("Gold")
        elif b.button_beige.collidepoint((mouse)):
            if click:
                if clicked_button["Beige"] == 1 or (245,245,220) in clicked_button_list_codes or "Beige" in clicked_button_list:
                    clicked_button["Beige"] = 0
                    clicked_button_list_codes.remove((245,245,220))
                    clicked_button_list.remove("Beige")
                else:
                    clicked_button["Beige"] = 1
                    clicked_button_list_codes.append((245,245,220))
                    clicked_button_list.append("Beige")
        elif b.button_yellow.collidepoint((mouse)):
            if click:
                if clicked_button["Yellow"] == 1 or (0, 0, 0) in clicked_button_list_codes or "Yellow" in clicked_button_list:
                    clicked_button["Yellow"] = 0
                    clicked_button_list_codes.remove((0, 0, 0))
                    clicked_button_list.remove("Yellow")
                else:
                    clicked_button["Yellow"] = 1
                    clicked_button_list_codes.append((0, 0, 0))
                    clicked_button_list.append("Yellow")
        elif b.button_green.collidepoint((mouse)):
            if click:
                if clicked_button["Green"] == 1 or (0,128,0) in clicked_button_list:
                    clicked_button["Green"] = 0
                    clicked_button_list.remove((0,128,0))
                else:
                    clicked_button["Green"] = 1
                    clicked_button_list.append((0,128,0))
        elif b.button_turqoise.collidepoint((mouse)):
            if click:
                if clicked_button["Turqoise"] == 1 or (64,224,208) in clicked_button_list:
                    clicked_button["Turqoise"] = 0
                    clicked_button_list.remove((64,224,208))
                else:
                    clicked_button["Turqoise"] = 1
                    clicked_button_list.append((64,224,208))
        elif b.button_teal.collidepoint((mouse)):
            if click:
                if clicked_button["Teal"] == 1 or (0,128,128) in clicked_button_list:
                    clicked_button["Teal"] = 0
                    clicked_button_list.remove((0,128,128))
                else:
                    clicked_button["Teal"] = 1
                    clicked_button_list.append((0,128,128))
        elif b.button_blue.collidepoint((mouse)):
            if click:
                if clicked_button["Blue"] == 1 or (0,0,255) in clicked_button_list:
                    clicked_button["Blue"] = 0
                    clicked_button_list.remove((0,0,255))
                else:
                    clicked_button["Blue"] = 1
                    clicked_button_list.append((0,0,255))
        elif b.button_violet.collidepoint((mouse)):
            if click:
                if clicked_button["Violet"] == 1 or (238,130,238) in clicked_button_list:
                    clicked_button["Violet"] = 0
                    clicked_button_list.remove((238,130,238))
                else:
                    clicked_button["Violet"] = 1
                    clicked_button_list.append((238,130,238))
        elif b.button_purple.collidepoint((mouse)):
            if click:
                if clicked_button["Purple"] == 1 or (128,0,128) in clicked_button_list:
                    clicked_button["Purple"] = 0
                    clicked_button_list.remove((128,0,128))
                else:
                    clicked_button["Purple"] = 1
                    clicked_button_list.append((128,0,128))
        elif b.button_pink.collidepoint((mouse)):
            if click:
                if clicked_button["Pink"] == 1 or (255,105,180) in clicked_button_list:
                    clicked_button["Pink"] = 0
                    clicked_button_list.remove((255,105,180))
                else:
                    clicked_button["Pink"] = 1
                    clicked_button_list.append((255,105,180))


        pygame.draw.rect(screen, (211, 211, 211), button_feedback)
        click = False

        place_button(c.black, b.button_black)
        place_button(c.grey, b.button_grey)
        place_button(c.silver, b.button_silver)
        place_button(c.white, b.button_white)
        place_button(c.brown, b.button_brown)
        place_button(c.red, b.button_red)
        place_button(c.orange, b.button_orange)
        place_button(c.gold, b.button_gold)
        place_button(c.beige, b.button_beige)
        place_button(c.yellow, b.button_yellow)
        place_button(c.green, b.button_green)
        place_button(c.turqoise, b.button_turqoise)
        place_button(c.teal, b.button_teal)
        place_button(c.blue, b.button_blue)
        place_button(c.violet, b.button_violet)
        place_button(c.purple, b.button_purple)
        place_button(c.pink, b.button_pink)


        print(clicked_button_list)

        for single_color in clicked_button_list:
            draw_text(single_color, font, c.black, screen, 650, y_pos)
            y_pos += 18

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


#MOET NOG DE INPUT IN EEN LIJST KRIJGEN


def feedback():
    running = True
    while running:
        screen.fill((240,255,255))

        draw_text('feedback', font, c.black, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()
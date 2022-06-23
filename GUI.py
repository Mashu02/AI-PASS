import sys
import pygame
import buttons
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
clicked_button = []

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

        mouse = pygame.mouse.get_pos()


        button_feedback = pygame.Rect(1445, 800, 200, 50)
        if button_feedback.collidepoint((mouse)):
            if click:
                feedback()
        elif b.button_black.collidepoint((mouse)):
            if click:
                if "Black" in clicked_button:
                    clicked_button.remove("Black")
                else:
                    clicked_button.append("Black")

        elif b.button_grey.collidepoint((mouse)):
            if click:
                if "Grey" in clicked_button:
                    clicked_button.remove("Grey")
                else:
                    clicked_button.append("Grey")

        elif b.button_silver.collidepoint((mouse)):
            if click:
                if "Silver" in clicked_button:
                    clicked_button.remove("Silver")
                else:
                    clicked_button.append("Silver")

        elif b.button_white.collidepoint((mouse)):
            if click:
                if "White" in clicked_button:
                    clicked_button.remove("White")
                else:
                    clicked_button.append("White")

        elif b.button_brown.collidepoint((mouse)):
            if click:
                if "Brown" in clicked_button:
                    clicked_button.remove("Brown")
                else:
                    clicked_button.append("Brown")

        elif b.button_red.collidepoint((mouse)):
            if click:
                if "Red" in clicked_button:
                    clicked_button.remove("Red")
                else:
                    clicked_button.append("Red")

        elif b.button_orange.collidepoint((mouse)):
            if click:
                if "Orange" in clicked_button:
                    clicked_button.remove("Orange")
                else:
                    clicked_button.append("Orange")

        elif b.button_gold.collidepoint((mouse)):
            if click:
                if "Gold" in clicked_button:
                    clicked_button.remove("Gold")
                else:
                    clicked_button.append("Gold")

        elif b.button_beige.collidepoint((mouse)):
            if click:
                if "Beige" in clicked_button:
                    clicked_button.remove("Beige")
                else:
                    clicked_button.append("Beige")

        elif b.button_yellow.collidepoint((mouse)):
            if click:
                if "Yellow" in clicked_button:
                    clicked_button.remove("Yellow")
                else:
                    clicked_button.append("Yellow")

        elif b.button_green.collidepoint((mouse)):
            if click:
                if "Green" in clicked_button:
                    clicked_button.remove("Green")
                else:
                    clicked_button.append("Green")

        elif b.button_turqoise.collidepoint((mouse)):
            if click:
                if "Turqoise" in clicked_button:
                    clicked_button.remove("Turqoise")
                else:
                    clicked_button.append("Turqoise")

        elif b.button_teal.collidepoint((mouse)):
            if click:
                if "Teal" in clicked_button:
                    clicked_button.remove("Teal")
                else:
                    clicked_button.append("Teal")

        elif b.button_blue.collidepoint((mouse)):
            if click:
                if "Blue" in clicked_button:
                    clicked_button.remove("Blue")
                else:
                    clicked_button.append("Blue")

        elif b.button_violet.collidepoint((mouse)):
            if click:
                if "Violet" in clicked_button:
                    clicked_button.remove("Violet")
                else:
                    clicked_button.append("Violet")

        elif b.button_purple.collidepoint((mouse)):
            if click:
                if "Purple" in clicked_button:
                    clicked_button.remove("Purple")
                else:
                    clicked_button.append("Purple")

        elif b.button_pink.collidepoint((mouse)):
            if click:
                if "Pink" in clicked_button:
                    clicked_button.remove("Pink")
                else:
                    clicked_button.append("Pink")


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



        print(clicked_button)

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
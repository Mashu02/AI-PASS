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

def place_button(button, button_color):
    return pygame.draw.rect(screen, button, button_color)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        clicked_button = []
        screen.fill((255, 255, 247))
        draw_text('pick colors', font, c.black, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(1445, 800, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                feedback()
        pygame.draw.rect(screen, (211, 211, 211), button_1)
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


def feedback():
    running = True
    while running:
        screen.fill((255, 255, 247))

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
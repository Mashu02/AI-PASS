import sys
import pygame
import colors as c
import buttons as b
import algo
from pygame.locals import *
from PIL import Image

mainClock = pygame.time.Clock()
pygame.init()


#screen
screen = pygame.display.set_mode((1536, 870))
pygame.display.set_caption('color matcher')
font = pygame.font.SysFont(None, 20)
click = False
mouse = pygame.mouse.get_pos()
clicked_button = {"Black" : 0,  "Grey" : 0,  "Silver" : 0,  "White" : 0,  "Brown" : 0,
                  "Red" : 0,  "Orange" : 0,  "Gold" : 0,  "Beige" : 0,  "Yellow" : 0,
                  "Green" : 0,  "Turqoise" : 0,  "Teal" : 0,  "Blue" : 0,  "Violet" : 0,
                  "Purple" : 0,  "Pink" : 0}
clicked_button_list = []
clicked_button_list_codes = []
liked_color_combinations = []
color_name_liked_combo = []


def place_button(button, button_color):
    """Om de buttons op het scherm te plaatsen

    Args:
        button (tuple): een rbg value van kleur
        button_color (pygame.Rect): een pygame rect met x,y waarde en width height waarde

    Returns:
        pygame.draw.rect: tekent de button op het scherm met de kleur en button
    """
    return pygame.draw.rect(screen, button, button_color)


def place_liked_buttons(button_x, button_y,size):
    """voor de green button in feedback

    Args:
        button_x (int): x waarde van button
        button_y (int): y waarde van button
        size (int): width height waarde van button

    Returns:
        None
    """
    green_button = pygame.Rect(button_x, button_y, size, size)
    green_button_black_border = pygame.Rect(button_x - 3, button_y - 3, size + 6, size + 6)
    pygame.draw.rect(screen, c.black, green_button_black_border)
    pygame.draw.rect(screen, (102, 255, 0), green_button)

def draw_text(text, font, color, surface, x, y):
    """Om de text te plaatsen op het scherm

    Args:
        text (str): text op scherm
        font (pygame.font.SysFont): font en size
        color (tuple): een rbg value van kleur
        surface (pygame.display.set_mode): x en y voor resolutie scherm
        x (int): x waarde van text
        y (int): x waarde van text

    Returns:
        None
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    """main menu scherm loop
    Args:
        None
    Returns:
        None
    """
    while True:
        #scherm kleur
        screen.fill((240,255,255))
        draw_text('Pick color(s)', pygame.font.SysFont(None, 50), c.black, screen, 275, 35)
        draw_text('Selected colors', pygame.font.SysFont(None, 50), c.black, screen, 695, 35)
        draw_text('Your liked combinations:', pygame.font.SysFont(None, 50), c.black, screen, 1065, 35)
        y_pos = 92
        y_pos_color_code = 92

        #muis positie
        mouse = pygame.mouse.get_pos()

        #button maken
        button_generate = pygame.Rect(696, 700, 301, 100)
        button_generate_outline = pygame.Rect(693, 697, 307, 106)

        button_feedback = pygame.Rect(230, 700, 401, 100)
        button_feedback_outline = pygame.Rect(227,697,407,106)

        button_clear = pygame.Rect(1065, 700, 280, 100)
        button_clear_outline = pygame.Rect(1062, 697, 286, 106)

        button_save = pygame.Rect(1380, 700, 130, 100)
        button_save_outline = pygame.Rect(1377, 697, 136, 106)


        #is voor de buttons wanneer de muis tussen de x en y waardes zit
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
                if clicked_button["Yellow"] == 1 or (255,255,0) in clicked_button_list_codes or "Yellow" in clicked_button_list:
                    clicked_button["Yellow"] = 0
                    clicked_button_list_codes.remove((255,255,0))
                    clicked_button_list.remove("Yellow")
                else:
                    clicked_button["Yellow"] = 1
                    clicked_button_list_codes.append((255,255,0))
                    clicked_button_list.append("Yellow")
        elif b.button_green.collidepoint((mouse)):
            if click:
                if clicked_button["Green"] == 1 or (0,128,0) in clicked_button_list_codes or "Green" in clicked_button_list:
                    clicked_button["Green"] = 0
                    clicked_button_list_codes.remove((0,128,0))
                    clicked_button_list.remove("Green")
                else:
                    clicked_button["Green"] = 1
                    clicked_button_list_codes.append((0,128,0))
                    clicked_button_list.append("Green")
        elif b.button_turqoise.collidepoint((mouse)):
            if click:
                if clicked_button["Turqoise"] == 1 or (64,224,208) in clicked_button_list_codes or "Turqoise" in clicked_button_list:
                    clicked_button["Turqoise"] = 0
                    clicked_button_list_codes.remove((64,224,208))
                    clicked_button_list.remove("Turqoise")
                else:
                    clicked_button["Turqoise"] = 1
                    clicked_button_list_codes.append((64,224,208))
                    clicked_button_list.append("Turqoise")
        elif b.button_teal.collidepoint((mouse)):
            if click:
                if clicked_button["Teal"] == 1 or (0,128,128) in clicked_button_list_codes or "Teal" in clicked_button_list:
                    clicked_button["Teal"] = 0
                    clicked_button_list_codes.remove((0,128,128))
                    clicked_button_list.remove("Teal")
                else:
                    clicked_button["Teal"] = 1
                    clicked_button_list_codes.append((0,128,128))
                    clicked_button_list.append("Teal")
        elif b.button_blue.collidepoint((mouse)):
            if click:
                if clicked_button["Blue"] == 1 or (0,0,255) in clicked_button_list_codes or "Blue" in clicked_button_list:
                    clicked_button["Blue"] = 0
                    clicked_button_list_codes.remove((0,0,255))
                    clicked_button_list.remove("Blue")
                else:
                    clicked_button["Blue"] = 1
                    clicked_button_list_codes.append((0,0,255))
                    clicked_button_list.append("Blue")
        elif b.button_violet.collidepoint((mouse)):
            if click:
                if clicked_button["Violet"] == 1 or (238,130,238) in clicked_button_list_codes or "Violet" in clicked_button_list:
                    clicked_button["Violet"] = 0
                    clicked_button_list_codes.remove((238,130,238))
                    clicked_button_list.remove("Violet")
                else:
                    clicked_button["Violet"] = 1
                    clicked_button_list_codes.append((238,130,238))
                    clicked_button_list.append("Violet")
        elif b.button_purple.collidepoint((mouse)):
            if click:
                if clicked_button["Purple"] == 1 or (128,0,128) in clicked_button_list_codes or "Purple" in clicked_button_list:
                    clicked_button["Purple"] = 0
                    clicked_button_list_codes.remove((128,0,128))
                    clicked_button_list.remove("Purple")
                else:
                    clicked_button["Purple"] = 1
                    clicked_button_list_codes.append((128,0,128))
                    clicked_button_list.append("Purple")
        elif b.button_pink.collidepoint((mouse)):
            if click:
                if clicked_button["Pink"] == 1 or (255,105,180) in clicked_button_list_codes or "Pink" in clicked_button_list:
                    clicked_button["Pink"] = 0
                    clicked_button_list_codes.remove((255,105,180))
                    clicked_button_list.remove("Pink")
                else:
                    clicked_button["Pink"] = 1
                    clicked_button_list_codes.append((255,105,180))
                    clicked_button_list.append("Pink")
        if button_generate.collidepoint((mouse)):
            if click:
                generate()
        if button_clear.collidepoint((mouse)):
            if click:
                liked_color_combinations.clear()
        if button_save.collidepoint((mouse)):
            if click:
                algo.list_to_clipboard(str(liked_color_combinations))
                draw_text('copied to clipboard!', pygame.font.SysFont(None, 35), c.black, screen, 1250, 630)

        #button placen
        pygame.draw.rect(screen, c.black, button_feedback_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_feedback)

        pygame.draw.rect(screen, c.black, button_generate_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_generate)

        pygame.draw.rect(screen, c.black, button_clear_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_clear)

        pygame.draw.rect(screen, c.black, button_save_outline)
        pygame.draw.rect(screen, (211, 211, 211), button_save)

        #text plaatsen
        draw_text('show result', pygame.font.SysFont(None, 60), c.black, screen, 310, 730)
        draw_text('generate input', pygame.font.SysFont(None, 40), c.black, screen, 746, 735)
        draw_text('clear combinations', pygame.font.SysFont(None, 40), c.black, screen, 1070, 735)
        draw_text('copy', pygame.font.SysFont(None, 40), c.black, screen, 1410, 735)
        click = False

        #kleur buttons plaatsen
        place_button(c.black, b.out_button_black)
        place_button(c.black, b.button_black)
        place_button(c.black, b.out_button_grey)
        place_button(c.grey, b.button_grey)
        place_button(c.black, b.out_button_silver)
        place_button(c.silver, b.button_silver)
        place_button(c.black, b.out_button_white)
        place_button(c.white, b.button_white)
        place_button(c.black, b.out_button_brown)
        place_button(c.brown, b.button_brown)
        place_button(c.black, b.out_button_red)
        place_button(c.red, b.button_red)
        place_button(c.black, b.out_button_orange)
        place_button(c.orange, b.button_orange)
        place_button(c.black, b.out_button_gold)
        place_button(c.gold, b.button_gold)
        place_button(c.black, b.out_button_beige)
        place_button(c.beige, b.button_beige)
        place_button(c.black, b.out_button_yellow)
        place_button(c.yellow, b.button_yellow)
        place_button(c.black, b.out_button_green)
        place_button(c.green, b.button_green)
        place_button(c.black, b.out_button_turqoise)
        place_button(c.turqoise, b.button_turqoise)
        place_button(c.black, b.out_button_teal)
        place_button(c.teal, b.button_teal)
        place_button(c.black, b.out_button_blue)
        place_button(c.blue, b.button_blue)
        place_button(c.black, b.out_button_violet)
        place_button(c.violet, b.button_violet)
        place_button(c.black, b.out_button_purple)
        place_button(c.purple, b.button_purple)
        place_button(c.black, b.out_button_pink)
        place_button(c.pink, b.button_pink)


        #color list in selected
        for single_color in clicked_button_list:
            draw_text("-"+single_color, pygame.font.SysFont(None, 25), c.black, screen, 685, y_pos)
            y_pos += 20

        for liked_color_combo in liked_color_combinations:
            draw_text(str(liked_color_combo), pygame.font.SysFont(None, 25), c.black, screen, 1100, y_pos_color_code)
            y_pos_color_code += 25

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
        mainClock.tick(25)

def generate():
    """generate menu scherm loop
    Args:
        None
    Returns:
        None
    """
    running = True
    while running:
        y_pos = 135
        screen.fill((240,255,255))
        draw_text('generated', pygame.font.SysFont(None, 35), c.black, screen, 500, 50)
        algo.create_image(clicked_button_list_codes, 500)
        randomly_generated_image1 = pygame.image.load('image.png')
        screen.blit(randomly_generated_image1, (320, 100))


        input_list_user = (list(clicked_button.values()))
        top_count = algo.most_picks(str(input_list_user))
        draw_text(str(top_count) + " votes", pygame.font.SysFont(None, 30), c.black, screen, 75, 100)

        for single_color in clicked_button_list:
            draw_text("-" + single_color, pygame.font.SysFont(None, 30), c.black, screen, 75, y_pos)
            y_pos += 25

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(25)

def feedback():
    """feedback menu scherm loop
    Args:
        None
    Returns:
        None
    """
    running = True
    while running:
        #y posities voor de result blokken
        y_pos = 379
        y_pos2 = 379
        y_pos3 = 379
        y_pos4 = 379
        y_pos5 = 379
        y_pos6 = 795
        y_pos7 = 795
        y_pos8 = 795
        y_pos9 = 795
        y_pos10 = 795
        color_code_feedback = []
        color_score_list = []
        mouse = pygame.mouse.get_pos()
        screen.fill((240,255,255))
        draw_text('feedback', font, c.black, screen, 20, 20)

        input = clicked_button.values()
        input_tuple = tuple(input)

        #gebruikt algoritme
        algoritme_uitkomst = algo.cosine_sim(input, 10, input_tuple)
        algoritme_score = algo.cosine_sim_score(input, 10, input_tuple)

        #klikken komt dan in de lijst
        for color_zero_one in algoritme_uitkomst:
            x = (algo.list_to_color(color_zero_one))
            color_code_feedback.append(x)

        #% berekenen van algoritme score
        for single_score in algoritme_score:
            score_percent = single_score * 100
            score_percent2 = round(score_percent, 2)
            color_score_list.append(score_percent2)


        #elk van de resultaten plaatsen met de info erbij
        score_color_percent = str(color_score_list[0])
        color_names = color_code_feedback[0]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 20, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 20, y_pos)
            y_pos += 19
        top_1_count = list(algoritme_uitkomst[0])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 20, 335)
        algo.create_image(color_code_feedback[0], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        screen.blit(pygame_surface_top1, (20, 40))
        place_liked_buttons(135,350,40)
        if 135 + 40 > mouse[0] > 135 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,143,355)

        score_color_percent = str(color_score_list[1])
        color_names = color_code_feedback[1]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 315, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 315, y_pos2)
            y_pos2 += 19
        top_1_count = list(algoritme_uitkomst[1])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 315, 335)
        algo.create_image(color_code_feedback[1], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        screen.blit(pygame_surface_top1, (315, 40))
        place_liked_buttons(430, 350, 40)
        if 430 + 40 > mouse[0] > 430 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,438,355)

        score_color_percent = str(color_score_list[2])
        color_names = color_code_feedback[2]
        draw_text(score_color_percent + "%" + " similar", font, c.black, screen, 610, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 610, y_pos3)
            y_pos3 += 19
        top_1_count = list(algoritme_uitkomst[2])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 610, 335)
        algo.create_image(color_code_feedback[2], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        screen.blit(pygame_surface_top1, (610, 40))
        place_liked_buttons(725, 350, 40)
        if 725 + 40 > mouse[0] > 725 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,733,355)

        score_color_percent = str(color_score_list[3])
        color_names = color_code_feedback[3]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 905, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 905, y_pos4)
            y_pos4 += 19
        top_1_count = list(algoritme_uitkomst[3])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 905, 335)
        algo.create_image(color_code_feedback[3], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        screen.blit(pygame_surface_top1, (905, 40))
        place_liked_buttons(1010, 350, 40)
        if 1010 + 40 > mouse[0] > 1010 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,1018,355)

        score_color_percent = str(color_score_list[4])
        color_names = color_code_feedback[4]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 1200, 357)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 1200, y_pos5)
            y_pos5 += 19
        top_1_count = list(algoritme_uitkomst[4])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 1200, 335)
        algo.create_image(color_code_feedback[4], 270)
        randomly_generated_image1 = Image.open(r'image.png')
        pygame_surface_top1 = algo.pilImageToSurface(randomly_generated_image1)
        pygame_surface_top1 = pygame.transform.smoothscale(pygame_surface_top1, (275, 275))
        screen.blit(pygame_surface_top1, (1200, 40))
        place_liked_buttons(1315, 350, 40)
        if 1315 + 40 > mouse[0] > 1315 and 350 + 40 > mouse[1] > 350:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,1323,355)

        score_color_percent = str(color_score_list[5])
        color_names = color_code_feedback[5]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 20, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 20, y_pos6)
            y_pos6 += 19
        top_1_count = list(algoritme_uitkomst[5])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 20, 751)
        algo.create_image2(color_code_feedback[5], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        screen.blit(pygame_surface_top2, (20, 465))
        place_liked_buttons(135, 764, 40)
        if 135 + 40 > mouse[0] > 135 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,143,769)

        score_color_percent = str(color_score_list[6])
        color_names = color_code_feedback[6]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 315, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 315, y_pos7)
            y_pos7 += 19
        top_1_count = list(algoritme_uitkomst[6])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 315, 751)
        algo.create_image2(color_code_feedback[6], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        screen.blit(pygame_surface_top2, (315, 465))
        place_liked_buttons(430, 764, 40)
        if 430 + 40 > mouse[0] > 430 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,438,769)

        score_color_percent = str(color_score_list[7])
        color_names = color_code_feedback[7]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 610, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 610, y_pos8)
            y_pos8 += 19
        top_1_count = list(algoritme_uitkomst[7])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 610, 751)
        algo.create_image2(color_code_feedback[7], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        screen.blit(pygame_surface_top2, (610, 465))
        place_liked_buttons(725, 764, 40)
        if 725 + 40 > mouse[0] > 725 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,733,769)

        score_color_percent = str(color_score_list[8])
        color_names = color_code_feedback[8]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 905, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 905, y_pos9)
            y_pos9 += 19
        top_1_count = list(algoritme_uitkomst[8])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 905, 751)
        algo.create_image2(color_code_feedback[8], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        screen.blit(pygame_surface_top2, (905, 465))
        place_liked_buttons(1010, 764, 40)
        if 1010 + 40 > mouse[0] > 1010 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,1018,769)

        score_color_percent = str(color_score_list[9])
        color_names = color_code_feedback[9]
        draw_text(score_color_percent + "%" + " similar",font, c.black, screen, 1200, 771)
        for single_color in color_names:
            color_name_single = algo.get_key(single_color)
            draw_text("-" + color_name_single, font, c.black, screen, 1200, y_pos10)
            y_pos10 += 19
        top_1_count = list(algoritme_uitkomst[9])
        most_picks_1 = algo.most_picks(str(top_1_count))
        draw_text(str(most_picks_1) + " votes", font, c.black, screen, 1200, 751)
        algo.create_image2(color_code_feedback[9], 270)
        randomly_generated_image2 = Image.open(r'image2.png')
        pygame_surface_top2 = algo.pilImageToSurface(randomly_generated_image2)
        pygame_surface_top2 = pygame.transform.smoothscale(pygame_surface_top2, (275, 275))
        screen.blit(pygame_surface_top2, (1200, 465))
        place_liked_buttons(1315, 764, 40)
        if 1315 + 40 > mouse[0] > 1315 and 764 + 40 > mouse[1] > 764:
            if click and color_names not in liked_color_combinations:
                liked_color_combinations.append(color_names)
                draw_text("X",pygame.font.SysFont(None, 55),c.black, screen,1323,769)
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(20)

main_menu()
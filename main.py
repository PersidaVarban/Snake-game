import pygame
import sys
from button import Button
from nivele import level_game, sound_func

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(" > SNAKE GAME <  Ver. 1.0 Beta")
bg = pygame.image.load("photo/Background.jpg")
bg = pygame.transform.scale(bg, (1280, 720))
selected_skin = None
sound_enabled = True
level_numbers = {
    " > Level 1 < ": 1,
    " > Level 2 < ": 2,
    " > Level 3 < ": 3,
    "> Level 4 <": 4
}

def get_font(size):
    return pygame.font.Font("photo/font.ttf", size)

def play():
    pygame.display.set_caption("Play")
    levels = [" > Level 1 < ", " > Level 2 < ", " > Level 3 < ", "> Level 4 <"]
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(bg, (0, 0))
        PLAY_TEXT = get_font(45).render("Choose the level", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 140))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        level_buttons = []
        for i, level in enumerate(levels):
            level_button = Button(image=None, pos=(640, 260 + i * 80),
                                  text_input=level, font=get_font(30), base_color="White", hovering_color="Green")
            level_button.changeColor(PLAY_MOUSE_POS)
            level_button.update(screen)
            level_buttons.append(level_button)
        PLAY_BACK = Button(image=None, pos=(640, 640),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, level_button in enumerate(level_buttons):
                    if level_button.checkForInput(PLAY_MOUSE_POS):
                        if selected_skin == 1:
                            level_game(i+1, 1)
                            pygame.display.set_mode((1280, 720))
                            main_menu()
                        else:
                            level_game(i+1, None)
                            pygame.display.set_mode((1280, 720))
                            main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()


def skins_menu():
    global selected_skin
    while True:
        screen.blit(bg, (0, 0))
        SKINS_MOUSE_POS = pygame.mouse.get_pos()
        SKINS_TEXT = get_font(45).render(" >> Select your skin << ", True, "White")
        SKINS_RECT = SKINS_TEXT.get_rect(center=(640, 150))
        screen.blit(SKINS_TEXT, SKINS_RECT)
        default_skin_image = pygame.image.load("photo/default_skin/head_left.png")
        skin_1_image = pygame.image.load("photo/skin_1/Frame_10.png")
        new_width = 200
        default_skin_image = pygame.transform.scale(default_skin_image, (new_width, new_width))
        skin_1_image = pygame.transform.scale(skin_1_image, (new_width, new_width))
        screen.blit(default_skin_image, (290, 250))
        screen.blit(skin_1_image, (770, 250))
        DEFAULT_SKIN_TEXT = Button(image=None, pos=(400, 500),
                                   text_input="Default Skin", font=get_font(30), base_color="#d7fcd4",
                                   hovering_color="GREEN")
        SKIN_1_TEXT = Button(image=None, pos=(880, 500),
                             text_input="Red Corn Snake", font=get_font(30), base_color="#d7fcd4", hovering_color="GREEN")
        BACK_TEXT = Button(image=None, pos=(640, 640),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        DEFAULT_SKIN_TEXT.changeColor(SKINS_MOUSE_POS)
        DEFAULT_SKIN_TEXT.update(screen)
        SKIN_1_TEXT.changeColor(SKINS_MOUSE_POS)
        SKIN_1_TEXT.update(screen)
        BACK_TEXT.changeColor(SKINS_MOUSE_POS)
        BACK_TEXT.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_TEXT.checkForInput(SKINS_MOUSE_POS):
                    options()
                elif DEFAULT_SKIN_TEXT.checkForInput(SKINS_MOUSE_POS):
                    selected_skin = None
                    print(f"OUTPUT >> Skin-ul selectat este: {selected_skin}")
                elif SKIN_1_TEXT.checkForInput(SKINS_MOUSE_POS):
                    selected_skin = 1
                    print(f"OUTPUT >> Skin-ul selectat este: {selected_skin}")
        pygame.display.update()

def options():
    pygame.display.set_caption("Options")
    global sound_enabled
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(bg, (0, 0))
        OPTIONS_TEXT = get_font(45).render("Choose your option", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 110))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_BACK = Button(image=None, pos=(640, 640),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)
        SOUND_BUTTON = Button(image=None, pos=(640, 260),
                              text_input=" > Sound: ON < " if sound_enabled else " > Sound: OFF < ",
                              font=get_font(45), base_color="White", hovering_color="Green" if sound_enabled else "Red")
        SOUND_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SOUND_BUTTON.update(screen)
        SKINS_BUTTON = Button(image=None, pos=(640, 360),
                              text_input=" > Skins <", font=get_font(45), base_color="White", hovering_color="Green")
        SKINS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SKINS_BUTTON.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                elif SOUND_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    sound_enabled = not sound_enabled
                    if sound_enabled:
                        pygame.mixer.Sound('sunete/crunch.wav').play()
                    sound_func(sound_enabled)
                elif SKINS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    skins_menu()
        pygame.display.update()

def normalize_name(name):
    if name.strip() == "":
        return "???"
    return name.upper()

def show_scores():
    with open("database/scores.txt", "r") as file:
        lines = file.readlines()
    player_scores = {}
    for line in lines:
        name, score = line.strip().split(":")
        normalized_name = normalize_name(name)
        if normalized_name not in player_scores:
            player_scores[normalized_name] = []
        player_scores[normalized_name].append(int(score))
    sorted_players = sorted(player_scores.keys())
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.Font('photo/font.ttf', 20)
        scoreboard_text = font.render("SCOREBOARD", True, (255, 255, 255))
        scoreboard_rect = scoreboard_text.get_rect(center=(screen.get_width() // 2, 40))
        screen.blit(scoreboard_text, scoreboard_rect)
        name_title = font.render("NAME", True, (255, 255, 255))
        score_title = font.render("HI SCORE", True, (255, 255, 255))
        name_title_rect = name_title.get_rect(topleft=(50, 80))
        score_title_rect = score_title.get_rect(topright=(screen.get_width() - 50, 80))
        screen.blit(name_title, name_title_rect)
        screen.blit(score_title, score_title_rect)
        y = 145
        for player in sorted_players:
            max_score = max(player_scores[player])
            name_text = font.render(player, True, (255, 255, 255))
            score_text = font.render(str(max_score), True, (255, 255, 255))
            name_rect = name_text.get_rect(topleft=(50, y))
            score_rect = score_text.get_rect(topright=(screen.get_width() - 50, y))
            screen.blit(name_text, name_rect)
            screen.blit(score_text, score_rect)
            y += 30
        BACK_BUTTON = Button(image=None, pos=(1140, 670),
                             text_input="BACK", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON.changeColor(pygame.mouse.get_pos())
        BACK_BUTTON.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    return
        pygame.display.update()

def main_menu():
    while True:
        screen.blit(bg, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("SNAKE GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("photo/PLay Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("photo/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4",
                                hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("photo/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCORES_BUTTON = Button(image=None, pos=(155, 665),
                               text_input="SCORES", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SCORES_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if SCORES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    show_scores()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()
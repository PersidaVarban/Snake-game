import pygame, sys, random, os
from pygame.math import Vector2

enabled_sound = True
def sound_func(s):
    global enabled_sound
    enabled_sound  = s

def create_database_folder():
    if not os.path.exists('database'):
        os.makedirs('database')

def save_score(name, score):
    with open(os.path.join('database', 'scores.txt'), 'a') as file:
        file.write(f'{name}: {score}\n')

def level_game(gamemode, skin):
    global cell_number
    global speed
    if gamemode == 1:
        cell_number = 10
        body = [Vector2(5, 4), Vector2(4, 4), Vector2(3, 4)]
        bonus = False
        speed = 170
    elif gamemode == 2:
        cell_number = 15
        body = [Vector2(7, 7), Vector2(6, 7), Vector2(5, 7)]
        bonus = True
        speed = 150
    elif gamemode == 3:
        cell_number = 20
        body = [Vector2(9, 8), Vector2(8, 8), Vector2(7, 8)]
        bonus = True
        speed = 130
    elif gamemode == 4:
        cell_number = 20
        body = [Vector2(9, 8), Vector2(8, 8), Vector2(7, 8)]
        bonus = True
        speed = 100


    class SNAKE:
        def __init__(self):
            self.body = body
            self.direction = Vector2(0, 0)
            self.new_block = False
            if skin == 1:
                self.head_up = pygame.image.load('photo/default_skin/head_up.png').convert_alpha()
                self.head_down = pygame.image.load('photo/default_skin/head_down.png').convert_alpha()
                self.head_right = pygame.image.load('photo/default_skin/head_right.png').convert_alpha()
                self.head_left = pygame.image.load('photo/skin_1/Frame_10.png').convert_alpha()
                self.tail_up = pygame.image.load('photo/default_skin/tail_up.png').convert_alpha()
                self.tail_down = pygame.image.load('photo/default_skin/tail_down.png').convert_alpha()
                self.tail_right = pygame.image.load('photo/default_skin/tail_right.png').convert_alpha()
                self.tail_left = pygame.image.load('photo/default_skin/tail_left.png').convert_alpha()
                self.body_vertical = pygame.image.load('photo/default_skin/body_vertical.png').convert_alpha()
                self.body_horizontal = pygame.image.load('photo/default_skin/body_horizontal.png').convert_alpha()
                self.body_tr = pygame.image.load('photo/default_skin/body_tr.png').convert_alpha()
                self.body_tl = pygame.image.load('photo/default_skin/body_tl.png').convert_alpha()
                self.body_br = pygame.image.load('photo/default_skin/body_br.png').convert_alpha()
                self.body_bl = pygame.image.load('photo/default_skin/body_bl.png').convert_alpha()
            else:
                self.head_up = pygame.image.load('photo/default_skin/head_up.png').convert_alpha()
                self.head_down = pygame.image.load('photo/default_skin/head_down.png').convert_alpha()
                self.head_right = pygame.image.load('photo/default_skin/head_right.png').convert_alpha()
                self.head_left = pygame.image.load('photo/default_skin/head_left.png').convert_alpha()
                self.tail_up = pygame.image.load('photo/default_skin/tail_up.png').convert_alpha()
                self.tail_down = pygame.image.load('photo/default_skin/tail_down.png').convert_alpha()
                self.tail_right = pygame.image.load('photo/default_skin/tail_right.png').convert_alpha()
                self.tail_left = pygame.image.load('photo/default_skin/tail_left.png').convert_alpha()
                self.body_vertical = pygame.image.load('photo/default_skin/body_vertical.png').convert_alpha()
                self.body_horizontal = pygame.image.load('photo/default_skin/body_horizontal.png').convert_alpha()
                self.body_tr = pygame.image.load('photo/default_skin/body_tr.png').convert_alpha()
                self.body_tl = pygame.image.load('photo/default_skin/body_tl.png').convert_alpha()
                self.body_br = pygame.image.load('photo/default_skin/body_br.png').convert_alpha()
                self.body_bl = pygame.image.load('photo/default_skin/body_bl.png').convert_alpha()
            global enabled_sound, speed
            self.crunch_sound =  pygame.mixer.Sound('sunete/crunch.wav')
            if enabled_sound:    
                self.crunch_sound.set_volume(1.0)
            else:
                self.crunch_sound.set_volume(0.0)
        def new_speed(self, new_speed):
            self.speed = new_speed
        def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()
            for index, block in enumerate(self.body):
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
                if index == 0:
                    screen.blit(self.head, block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail, block_rect)
                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.x == next_block.x:
                        screen.blit(self.body_vertical, block_rect)
                    elif previous_block.y == next_block.y:
                        screen.blit(self.body_horizontal, block_rect)
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            screen.blit(self.body_tl, block_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.body_bl, block_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.body_tr, block_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.body_br, block_rect)
        def update_head_graphics(self):
            head_relation = self.body[1] - self.body[0]
            if head_relation == Vector2(1, 0):
                self.head = self.head_left
            elif head_relation == Vector2(-1, 0):
                self.head = self.head_right
            elif head_relation == Vector2(0, 1):
                self.head = self.head_up
            elif head_relation == Vector2(0, -1):
                self.head = self.head_down
        def update_tail_graphics(self):
            tail_relation = self.body[-2] - self.body[-1]
            if tail_relation == Vector2(1, 0):
                self.tail = self.tail_left
            elif tail_relation == Vector2(-1, 0):
                self.tail = self.tail_right
            elif tail_relation == Vector2(0, 1):
                self.tail = self.tail_up
            elif tail_relation == Vector2(0, -1):
                self.tail = self.tail_down
        def move_snake(self):
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
        def add_block(self):
            self.body.append(Vector2(-1, -1))
        def play_crunch_sound(self):
            self.crunch_sound.play()
        def reset(self):
            self.body = body
            self.direction = Vector2(0, 0)

    class BLOCKS:
        def __init__(self):
            self.blocks = []
            self.randomizee()

        def draw_blocks(self):
            for block_pos in self.blocks:
                blocks_rect = pygame.Rect(int(block_pos.x * cell_size), int(block_pos.y * cell_size), cell_size,
                                          cell_size)
                screen.blit(block_image, blocks_rect)

        def randomizee(self):
            if gamemode == 2 or gamemode == 3 or gamemode == 4:
                for _ in range(gamemode):
                    x = random.randint(0, cell_number - 1)
                    y = random.randint(0, cell_number - 2)
                    block_pos = Vector2(x, y)
                    self.blocks.append(block_pos)

        def get_block_positions(self):
            return self.blocks

    class FRUIT:
        def __init__(self, blocks_instance):
            self.blocks_instance = blocks_instance
            self.blocks = self.blocks_instance.get_block_positions()
            self.randomize()
            self.is_special_fruit = False

        def draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
            if bonus:
                if self.is_special_fruit:
                    screen.blit(special_apple, fruit_rect)
                else:
                    screen.blit(apple, fruit_rect)
            else:
                screen.blit(apple, fruit_rect)

        def randomize(self):
            while True:
                self.x = random.randint(0, cell_number - 1)
                self.y = random.randint(0, cell_number - 1)
                self.pos = Vector2(self.x, self.y)
                overlap = False
                for block_pos in self.blocks:
                    if block_pos == self.pos:
                        overlap = True
                        break

                if not overlap:
                    break

            if bonus:
                random_number = random.randint(1, 100)
                self.is_special_fruit = random_number <= 5

    class MAIN:
        def __init__(self):
            self.blocks_instance = BLOCKS()
            self.snake = SNAKE()
            self.fruit = FRUIT(self.blocks_instance)
            self.blocks = self.blocks_instance
            self.score = 0

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
        def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.blocks.draw_blocks()
            self.snake.draw_snake()
            self.draw_score()
        def check_collision(self):
            victory_scores = {1: 96, 2: 219, 3: 393, 4: 392}
            for block_pos in self.blocks.blocks:
                if block_pos == self.snake.body[0]:
                    self.save_score_menu(win=False)
                    self.snake.reset()
                    self.fruit.randomize()
                    self.score = 0
                    return
            if self.fruit.pos == self.snake.body[0]:
                if self.fruit.is_special_fruit:
                    self.score += 5
                    for _ in range(5):
                        self.snake.add_block()
                    if gamemode in victory_scores and self.score == victory_scores[gamemode]:
                        self.save_score_menu(win=True)
                        pygame.quit()
                        sys.exit()
                else:
                    self.score += 1
                    self.snake.add_block()
                    if gamemode in victory_scores and self.score == victory_scores[gamemode]:
                        self.save_score_menu(win=True)
                        pygame.quit()
                        sys.exit()
                self.fruit.randomize()
                self.snake.play_crunch_sound()
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

        def save_score_menu(self, win=True):
            initial_resolution = pygame.display.get_surface().get_size()
            font = pygame.font.Font('photo/font.ttf', 36)

            if win:
                text = font.render('You win!', True, (255, 255, 255))
            else:
                text = font.render('You lose!', True, (255, 0, 0))

            text_rect = text.get_rect(center=(initial_resolution[0] // 2, initial_resolution[1] // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(3000)

            name = ''
            pygame.display.set_mode((1280, 720))
            should_save_score = False
            menu_active = True
            while menu_active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            menu_active = False
                            should_save_score = True
                        elif event.key == pygame.K_n:
                            menu_active = False
                            pygame.display.set_mode(initial_resolution)
                            return

                screen.fill((0, 0, 0))
                font = pygame.font.Font('photo/font.ttf', 20)
                menu_text = font.render('Do you want to save your score? (Y/N) - N: Restart', True, (255, 255, 255))
                menu_text_rect = menu_text.get_rect(center=(1280 // 2, 720 // 2))
                screen.blit(menu_text, menu_text_rect)
                pygame.display.flip()

            if not should_save_score:
                self.snake.reset()
                self.fruit.randomize()
                self.score = 0
                return

            input_active = True
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            save_score(name, self.score)
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            if len(name) < 10 and input_active:
                                name += event.unicode

                screen.fill((0, 0, 0))
                font = pygame.font.Font('photo/font.ttf', 36)
                score_text = font.render(f'Your score: {self.score}', True, (255, 255, 255))
                score_text_rect = score_text.get_rect(center=(1280 // 2, 720 // 2 - 100))
                screen.blit(score_text, score_text_rect)
                name_text = font.render('Your Name:', True, (255, 255, 255))
                name_text_rect = name_text.get_rect(midleft=(210, 425))
                screen.blit(name_text, name_text_rect)
                name_surface = font.render(name, True, (255, 255, 255))
                name_rect = name_surface.get_rect(midleft=(710, 425))
                screen.blit(name_surface, name_rect)
                pygame.display.flip()

        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                self.save_score_menu(win=False)
                self.snake.reset()
                self.fruit.randomize()
                self.score = 0
                return

            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()

        def game_over(self):
            self.snake.reset()
            self.score = 0

        def draw_grass(self):
            grass_color = (167, 209, 61)
            for row in range(cell_number):
                if row % 2 == 0:
                    for col in range(cell_number):
                        if col % 2 == 0:
                            grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                            pygame.draw.rect(screen, grass_color, grass_rect)
                else:
                    for col in range(cell_number):
                        if col % 2 != 0:
                            grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                            pygame.draw.rect(screen, grass_color, grass_rect)

        def draw_score(self):
            small_font = pygame.font.Font('photo/font.ttf', 12)
            smallest_font = pygame.font.Font('photo/font.ttf', 10)
            level_text = f"Level {gamemode}"
            score_text = f"Score: {self.score}"
            button_text = "ESC - Pause, R - Restart"
            level_surface = small_font.render(level_text, True, (56, 74, 12))
            score_surface = small_font.render(score_text, True, (56, 74, 12))
            button_surface = smallest_font.render(button_text, True, (56, 74, 12))
            level_rect = level_surface.get_rect(topleft=(20, 20))
            score_rect = score_surface.get_rect(topright=(cell_number * cell_size - 20, 20))
            button_rect = button_surface.get_rect(bottomleft=(20, screen.get_height() - 20))
            bg_rect = pygame.Rect(score_rect.left - 5, score_rect.top - 5, score_rect.width + 10,
                                  score_rect.height + 10)
            pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)
            screen.blit(level_surface, level_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(button_surface, button_rect)

    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    cell_size = 40
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    clock = pygame.time.Clock()
    apple = pygame.image.load('photo/mar.png').convert_alpha()
    special_apple = pygame.image.load('photo/mar_bonus.png').convert_alpha()
    block_image = pygame.image.load('photo/block.png').convert_alpha()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, speed)
    main_game = MAIN()
    pause = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE and not pause:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not pause:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT and not pause:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN and not pause:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT and not pause:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_ESCAPE:
                    font = pygame.font.Font('photo/font.ttf', cell_number)
                    text_line1 = font.render('Press C to continue, R to', True, (255, 255, 255))
                    text_line2 = font.render('start over or B to go in menu', True, (255, 255, 255))
                    text_rect1 = text_line1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 20))
                    text_rect2 = text_line2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 20))
                    screen.fill((0, 0, 0)) 
                    screen.blit(text_line1, text_rect1)
                    screen.blit(text_line2, text_rect2)
                    pygame.display.flip()
                    if not pause:
                        pause = True  
                else:
                    if event.key == pygame.K_c:
                        pause = False
                    elif event.key == pygame.K_r:
                        main_game.game_over()
                        pause = False
                    elif event.key == pygame.K_b:
                        return
        if not pause:
            screen.fill((175, 215, 70))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)
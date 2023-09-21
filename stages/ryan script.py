# imports
import pygame as py
from sys import exit
import os
import array
from array import *
import threading
import random 
# this could easily surpass 10k lines of code if I have different enemy patterns for each difficulty

# notes

py.init()

# this makes sure the window is scaled correctly when it is displayed.
if os.name == "nt":
    try:
        import ctypes
        
        awareness  = ctypes.c_int()
        error_Code = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        error_Code = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        success    = ctypes.windll.user32.SetProcessDPIAware()
    except:pass 

# death animation stuff
deaths = False
death_x = array('i',[])
death_y = array('i',[])
death_animation_num = array('i',[])
death_frame1 = py.image.load("assets/enemies/death frame 1.png")
death_frame2 = py.image.load("assets/enemies/death frame 2.png")
death_frame3 = py.image.load("assets/enemies/death frame 3.png")
death_frame4 = py.image.load("assets/enemies/death frame 4.png")
death_frame5 = py.image.load("assets/enemies/death frame 5.png")
death_frame6 = py.image.load("assets/enemies/death frame 6.png")
death_frame7 = py.image.load("assets/enemies/death frame 7.png")
death_frame8 = py.image.load("assets/enemies/death frame 8.png")

play_game      = True
difficulty_num = 1
keys           = py.key.get_pressed()

# menu stuff
menu_number = 1
home_page = True

# GUI dimensions
WIDTH  = 576
HEIGHT = 1024

# player starting location
y = 512
x = 512

# player sprites
player_animation_num = 1
character1    = py.image.load("assets/ships/ship 1.png")
character2    = py.image.load("assets/ships/ship 2.png")
character3    = py.image.load("assets/ships/ship 3.png")
character4    = py.image.load("assets/ships/ship 4.png")
character1l   = py.image.load("assets/ships/ship 1 l.png")
character2l   = py.image.load("assets/ships/ship 2 l.png")
character3l   = py.image.load("assets/ships/ship 3 l.png")
character1r   = py.image.load("assets/ships/ship 1 r.png")
character2r   = py.image.load("assets/ships/ship 2 r.png")
character3r   = py.image.load("assets/ships/ship 3 r.png")

player_bullet_1 = py.image.load("assets/bullets/bullet 1.png")
player_bullet_2 = py.image.load("assets/bullets/bullet 2.png")
player_bullet_3 = py.image.load("assets/bullets/bullet 3.png")
player_bullet_4 = py.image.load("assets/bullets/bullet 4.png")

enemy1_bullet_1 = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 1.png")
enemy1_bullet_2 = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 2.png")
enemy1_bullet_3 = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 3.png")
enemy1_bullet_4 = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 4.png")

in_game_background = py.image.load("assets/backgrounds/backgrounds/Background 0.png")
in_game_background_rect = in_game_background.get_rect(center=(288, 512))


enemy1_1 = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 1.png")
enemy1_2 = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 2.png")
enemy1_3 = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 3.png")
enemy1_4 = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 4.png")

# set up window
game_window = py.display.set_mode((WIDTH, HEIGHT))
game_window.fill((0, 0, 0))



background = py.image.load("assets/HUD/Pixel Nebula Title HUD.png")
buttons = py.image.load("assets/HUD/Pixel Nebula Menu Buttons.png")
button_highlight = py.image.load("assets/HUD/Pixel Nebula Menu Choice.png")

# difficulty text
easy_diff     = py.image.load("assets/HUD/easy difficulty.png")
normal_diff   = py.image.load("assets/HUD/normal difficulty.png")
hard_diff     = py.image.load("assets/HUD/hard difficulty.png")
insane_diff   = py.image.load("assets/HUD/insane difficulty.png")

in_battle = False 

def create_enemies(path: str):

    enemies_dict = {}

    with open(path, "r") as reader:

        for n, line in enumerate(reader):
            
            line = line.strip()

            if not line or line == "EOF":
                break 

            values = [int(k.strip()) for k in line.split(",")]

            for i in range(len(values)):

                if i not in enemies_dict:
                    enemies_dict[i] = {
                        'bullets' : []
                    }

                # x pos
                if n == 0:
                    enemies_dict[i]['x'] = values[i]
                
                # y pos
                elif n == 1:
                    enemies_dict[i]['y'] = values[i]
                
                # x speed
                elif n == 2:
                    enemies_dict[i]['x_speed'] = values[i]

                # y speed
                elif n == 3:
                    enemies_dict[i]['y_speed'] = values[i]

    print("Loaded enemies:", enemies_dict)
    return enemies_dict



def game_loop(path: str):

    enemies_dict = create_enemies(path)

    in_battle = True 

    animation_frame = 0

    player_y = 512
    player_x = 512
    player_move_speed = 25
    player_bullets = []

    while in_battle:

        events = py.event.get()
        keys   = py.key.get_pressed()

        game_window.blit(in_game_background, in_game_background_rect)

        if animation_frame == 0: 
            enemy1_sprite = enemy1_1
            enemy1_bullet_sprite = enemy1_bullet_1
            player_bullet_sprite = player_bullet_1
            player_sprite = character1

        if animation_frame == 1:
            enemy1_sprite = enemy1_2
            enemy1_bullet_sprite = enemy1_bullet_2
            player_bullet_sprite = player_bullet_2
            player_sprite = character2

        if animation_frame == 2:
            enemy1_sprite = enemy1_3
            enemy1_bullet_sprite = enemy1_bullet_3
            player_bullet_sprite = player_bullet_3
            player_sprite = character3

        if animation_frame == 3:
            enemy1_sprite = enemy1_4
            enemy1_bullet_sprite = enemy1_bullet_4
            player_bullet_sprite = player_bullet_4
            player_sprite = character4

        animation_frame = (animation_frame + 1) % 4

        player_sprite_rect = player_sprite.get_rect(center=(player_x, player_y))
        game_window.blit(player_sprite, player_sprite_rect)

        for key, enemy in enemies_dict.items():

            enemy1_rect = enemy1_sprite.get_rect(center=(enemy['x'], enemy['y']))
    
            game_window.blit(enemy1_sprite, enemy1_rect)


            enemy['x'] += enemy['x_speed']
            enemy['y'] += enemy['y_speed']

            _deleted = 0
            for i, bullet in enumerate(list(enemy['bullets'])):

                bullet['x'] = enemy['x']
                bullet['y'] += 64

                if bullet['y'] > HEIGHT + 100:

                    del enemy['bullets'][i - _deleted]
                    _deleted += 1
                    continue

                enemy1_bullet_sprite_rect = enemy1_bullet_sprite.get_rect(center=(enemy['x'], bullet['y']))
                game_window.blit(enemy1_bullet_sprite, enemy1_bullet_sprite_rect)

            if True:
                enemy['bullets'].append({'x': enemy['x'], 'y': enemy['y'] + 64 })

    
        _deleted = 0
        for i, bullet in enumerate(list(player_bullets)):

            bullet['y'] -= 64

            if bullet['y'] < -100:

                del player_bullets[i - _deleted]
                _deleted += 1
                continue

            player_bullet_sprite_rect = player_bullet_sprite.get_rect(center=(bullet['x'], bullet['y']))
            game_window.blit(player_bullet_sprite, player_bullet_sprite_rect)
 

        
        if keys[py.K_SPACE]:

            player_bullets.append({'x': player_x, 'y': player_y})

        if keys[py.K_a]:
            player_x -= player_move_speed
        elif keys[py.K_d]: 
            player_x += player_move_speed
        
        if keys[py.K_w]:
            player_y -= player_move_speed
        elif keys[py.K_s]: 
            player_y += player_move_speed

        if player_x < 0:
            player_x = 0

        if player_x > WIDTH:
            player_x = WIDTH

        if player_y > HEIGHT:
            player_y = HEIGHT

        if player_y < 0:
            player_y = 0

        for event in events:
            if event.type == py.QUIT: 
                in_battle = False; 

        py.time.delay(100)
        py.display.update()


# game loop
while play_game:

    events = py.event.get()

    keys   = py.key.get_pressed()

    if not in_battle: 

        # background and buttons for menu

        background_rect = background.get_rect(center=(288, 512))

        game_window.blit(background, background_rect)

        buttons_rect = buttons.get_rect(center=(288, 700))
        
        game_window.blit(buttons, buttons_rect)

        # place menu button highlighter
        if   menu_number == 1 and home_page: highlight_rect = button_highlight.get_rect(center=(288, 572)); game_window.blit(button_highlight, highlight_rect)
        elif menu_number == 2 and home_page: highlight_rect = button_highlight.get_rect(center=(288, 700)); game_window.blit(button_highlight, highlight_rect)
        elif menu_number == 3 and home_page: highlight_rect = button_highlight.get_rect(center=(288, 828)); game_window.blit(button_highlight, highlight_rect)
        
        # place difficulty setting text
        if   difficulty_num == 1 and home_page: easy_rect   = easy_diff.  get_rect(center=(288, 700)); game_window.blit(easy_diff,   easy_rect)
        elif difficulty_num == 2 and home_page: normal_rect = normal_diff.get_rect(center=(288, 700)); game_window.blit(normal_diff, normal_rect)
        elif difficulty_num == 3 and home_page: hard_rect   = hard_diff.  get_rect(center=(288, 700)); game_window.blit(hard_diff,   hard_rect)
        elif difficulty_num == 4 and home_page: insane_rect = insane_diff.get_rect(center=(288, 700)); game_window.blit(insane_diff, insane_rect)


    # keybindings
    if keys[py.K_a] or keys[py.K_LEFT]:

        # change difficulty
        if home_page:
            if menu_number == 2 and difficulty_num >= 2: 
                difficulty_num -= 1; 
                py.time.delay(250)
                
        else:
            # move left
            if keys[py.K_LSHIFT]: 
                if x > 20: x -= 2
            else:
                if x > 20: x -= 4

    if keys[py.K_d] or keys[py.K_RIGHT]:

        if home_page:
            if menu_number == 2 and difficulty_num <= 4: 
                difficulty_num += 1; 
                py.time.delay(250)
        
        else:
            # move right
            if keys[py.K_LSHIFT]: 
                if x < 556: x += 2
            else:
                if x < 556: x += 4

    if keys[py.K_s] or keys[py.K_DOWN]:

        if home_page:
            if menu_number <= 2: 
                menu_number += 1; 
                py.time.delay(250)
                
        else:
            # move down
            if keys[py.K_LSHIFT]: 
                if y < 1004: y += 2
            else:
                if y < 1004: y += 4

    if keys[py.K_w] or keys[py.K_UP]:

        # move up menu button
        if home_page:
            if menu_number >= 2: 
                menu_number -= 1
                py.time.delay(250)

        else:
            # move up
            if keys[py.K_LSHIFT]: 
                if y > 20: y -= 2
            else:
                if y > 20: y -= 4

    if keys[py.K_RETURN]:
        # choose menu option
        if home_page and menu_number == 1: 
            in_battle = True
            if   difficulty_num == 1: 
                file_path = "easy1.txt"

            elif difficulty_num == 2: 
                file_path = "normal.txt"

            elif difficulty_num == 3: 
                file_path = "hard.txt"

            elif difficulty_num == 4: 
                file_path = "insane.txt"
            
            game_loop(file_path)
            # put stuff here that chooses which file is read depending on the difficulty chosen

        if home_page and menu_number == 3: 
            play_game = False

    for event in events:
        # close program
        if event.type == py.QUIT: 
            play_game = False; 

    py.display.update()

    py.time.delay(10)
# imports
import pygame as py
from sys import exit
import os
import threading
py.init()
# this could easily surpass 10k lines of code if I have different enemy patterns for each difficulty

# notes
# set up collisions
# set up what happens when enough enemies are killed
# set up energy orbs
# set up bosses

# this makes sure the window is scaled correctly when it is displayed.
if os.name == "nt":
    try:
        import ctypes
        
        awareness  = ctypes.c_int()
        error_Code = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        error_Code = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        success    = ctypes.windll.user32.SetProcessDPIAware()
    except:pass 



# bullet stuff
orbs_collected = 0
bullet_delay = 500
bullet_damage = 1
player_bullet_index_num = 0
bullet_animation_num = 1
bullets_present = False
player_bullet_x       = []
player_bullet_y       = []


# level information arrays
def reset_arrays():
    global enemy0_animation_num, enemy1_animation_num, enemy2_animation_num, enemy3_animation_num, enemy4_animation_num
    global array1_filled, array2_filled, array3_filled, array4_filled, array5_filled
    global enemy0_x, enemy1_x, enemy2_x, enemy3_x, enemy4_x 
    global enemy0_y, enemy1_y, enemy2_y, enemy3_y, enemy4_y
    global enemy0_x_speed, enemy1_x_speed, enemy2_x_speed, enemy3_x_speed, enemy4_x_speed
    global enemy0_y_speed, enemy1_y_speed, enemy2_y_speed, enemy3_y_speed, enemy4_y_speed
    global enemy0_rects, enemy1_rects, enemy2_rects, enemy3_rects, enemy4_rects
    global enemy0_bullets_present, enemy1_bullets_present, enemy2_bullets_present, enemy3_bullets_present, enemy4_bullets_present
    global enemy0_bullet_index_num, enemy1_bullet_index_num, enemy2_bullet_index_num, enemy3_bullet_index_num, enemy4_bullet_index_num
    global enemy0_bullet_animation_num, enemy1_bullet_animation_num, enemy2_bullet_animation_num, enemy3_bullet_animation_num, enemy4_bullet_animation_num
    global enemy0_bullet_x, enemy1_bullet_x, enemy2_bullet_x, enemy3_bullet_x, enemy4_bullet_x
    global enemy0_bullet_y, enemy1_bullet_y, enemy2_bullet_y, enemy3_bullet_y, enemy4_bullet_y
    global enemy0_bullet_x_speed, enemy1_bullet_x_speed, enemy2_bullet_x_speed, enemy3_bullet_x_speed, enemy4_bullet_x_speed
    global enemy0_bullet_y_speed, enemy1_bullet_y_speed, enemy2_bullet_y_speed, enemy3_bullet_y_speed, enemy4_bullet_y_speed
    global deaths, death_x, death_y, death_animation_num
    global items, item_x, item_y, item_animation_num

    # death animation stuff
    deaths = False
    death_x = []
    death_y = []
    death_animation_num = []

    # item stuff
    items  = False
    item_x = []
    item_y = []
    item_animation_num = []

    # enemy animation stuff
    enemy0_animation_num, enemy1_animation_num, enemy2_animation_num, enemy3_animation_num, enemy4_animation_num = 1, 1, 1, 1, 1
    array1_filled, array2_filled, array3_filled, array4_filled, array5_filled                                    = False, False, False, False, False
    enemy0_x, enemy1_x, enemy2_x, enemy3_x, enemy4_x                                                             = [], [], [], [], []
    enemy0_y, enemy1_y, enemy2_y, enemy3_y, enemy4_y                                                             = [], [], [], [], []
    enemy0_x_speed, enemy1_x_speed, enemy2_x_speed, enemy3_x_speed, enemy4_x_speed                               = [], [], [], [], []
    enemy0_y_speed, enemy1_y_speed, enemy2_y_speed, enemy3_y_speed, enemy4_y_speed                               = [], [], [], [], []
    enemy0_rects, enemy1_rects, enemy2_rects, enemy3_rects, enemy4_rects                                         = [], [], [], [], []

    # enemy bullet animation stuff
    enemy0_bullets_present, enemy1_bullets_present, enemy2_bullets_present, enemy3_bullets_present, enemy4_bullets_present                          = True, True, False, False, False
    enemy0_bullet_index_num, enemy1_bullet_index_num, enemy2_bullet_index_num, enemy3_bullet_index_num, enemy4_bullet_index_num                     = 0, 0, 0, 0, 0
    enemy0_bullet_animation_num, enemy1_bullet_animation_num, enemy2_bullet_animation_num, enemy3_bullet_animation_num, enemy4_bullet_animation_num = 1, 1, 1, 1, 1
    enemy0_bullet_x, enemy1_bullet_x, enemy2_bullet_x, enemy3_bullet_x, enemy4_bullet_x                                                             = [], [], [], [], []
    enemy0_bullet_y, enemy1_bullet_y, enemy2_bullet_y, enemy3_bullet_y, enemy4_bullet_y                                                             = [], [], [], [], []
    enemy0_bullet_x_speed, enemy1_bullet_x_speed, enemy2_bullet_x_speed, enemy3_bullet_x_speed, enemy4_bullet_x_speed                               = [], [], [], [], []
    enemy0_bullet_y_speed, enemy1_bullet_y_speed, enemy2_bullet_y_speed, enemy3_bullet_y_speed, enemy4_bullet_y_speed                               = [], [], [], [], []
# the function is run once to make sure that the variables exist
reset_arrays()


# important stuff
animation_num = 1
in_battle      = False
play_game      = True
live_num       = 3
difficulty_num = 1
stage_num      = 0
enemies_killed = 0
events         = py.event.get()
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

# set up window
game_window = py.display.set_mode((WIDTH, HEIGHT))

# sprites

# backgrounds
menu_background  = py.image.load("assets/HUD/Pixel Nebula Title HUD.png")
background0      = py.image.load("assets/backgrounds/backgrounds/Background 0.png")
background1      = py.image.load("assets/backgrounds/backgrounds/Background 1.png")
background2      = py.image.load("assets/backgrounds/backgrounds/Background 2.png")
background3      = py.image.load("assets/backgrounds/backgrounds/Background 3.png")
background4      = py.image.load("assets/backgrounds/backgrounds/Background 4.png")
background5      = py.image.load("assets/backgrounds/backgrounds/Background 5.png")
background6      = py.image.load("assets/backgrounds/backgrounds/Background 6.png")
background7      = py.image.load("assets/backgrounds/backgrounds/Background 7.png")
backgrounds      = [background0, background1, background2, background3, background4, background5, background6, background7]

# lives
lives0           = py.image.load("assets/HUD/lives 0.png")
lives1           = py.image.load("assets/HUD/lives 1.png")
lives2           = py.image.load("assets/HUD/lives 2.png")
lives3           = py.image.load("assets/HUD/lives 3.png")
lives            = [lives0, lives1, lives2, lives3]

# characters
character0       = py.image.load("assets/ships/ship 1.png")
character1       = py.image.load("assets/ships/ship 2.png")
character2       = py.image.load("assets/ships/ship 3.png")
character3       = py.image.load("assets/ships/ship 4.png")
characters       = [character0, character1, character2, character3]

# character moves left
character0_left  = py.image.load("assets/ships/ship 1 l.png")
character1_left  = py.image.load("assets/ships/ship 2 l.png")
character2_left  = py.image.load("assets/ships/ship 3 l.png")
character3_left  = py.image.load("assets/ships/ship 4 l.png")
characters_left  = [character0_left, character1_left, character2_left, character3_left]

# character moves right
character0_right = py.image.load("assets/ships/ship 1 r.png")
character1_right = py.image.load("assets/ships/ship 2 r.png")
character2_right = py.image.load("assets/ships/ship 3 r.png")
character3_right = py.image.load("assets/ships/ship 4 r.png")
characters_right = [character0_right, character1_right, character2_right, character3_right]

# level win animations
stage_clear0     = py.image.load("assets/ships/level clear 1.png")
stage_clear1     = py.image.load("assets/ships/level clear 2.png")
stage_clear2     = py.image.load("assets/ships/level clear 3.png")
stage_clear3     = py.image.load("assets/ships/level clear 4.png")
stage_clear4     = py.image.load("assets/ships/level clear 5.png")
stage_clear5     = py.image.load("assets/ships/level clear 6.png")
stage_clear6     = py.image.load("assets/ships/level clear 7.png")
stage_clear7     = py.image.load("assets/ships/level clear 8.png")
stage_clear8     = py.image.load("assets/ships/level clear 9.png")
stage_clear9     = py.image.load("assets/ships/level clear 10.png")
stage_clear10    = py.image.load("assets/ships/level clear 11.png")
stage_clear11    = py.image.load("assets/ships/level clear 12.png")
stage_clear      = [stage_clear0, stage_clear1, stage_clear2, stage_clear3,  stage_clear4,  stage_clear5, 
                    stage_clear6, stage_clear7, stage_clear8, stage_clear9, stage_clear10, stage_clear11]

# player bullets
character_bullet0 = py.image.load("assets/bullets/bullet 1.png")
character_bullet1 = py.image.load("assets/bullets/bullet 2.png")
character_bullet2 = py.image.load("assets/bullets/bullet 3.png")
character_bullet3 = py.image.load("assets/bullets/bullet 4.png")
character_bullets = [character_bullet0, character_bullet1, character_bullet2, character_bullet3]

# enemy 1 bullets
enemy0_bullet0   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 1.png")
enemy0_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 2.png")
enemy0_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 3.png")
enemy0_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 4.png")
enemy0_bullets   = [enemy0_bullet0, enemy0_bullet1, enemy0_bullet2, enemy0_bullet3]

# enemy 1 sprites
enemy0_frame0    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 1.png")
enemy0_frame1    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 2.png")
enemy0_frame2    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 3.png")
enemy0_frame3    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 4.png")
enemy0_frames    = [enemy0_frame0, enemy0_frame1, enemy0_frame2, enemy0_frame3]

# enemy 2 bullets
enemy1_bullet0   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 1.png")
enemy1_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 2.png")
enemy1_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 3.png")
enemy1_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 4.png")
enemy1_bullets   = [enemy1_bullet0, enemy1_bullet1, enemy1_bullet2, enemy1_bullet3]

# enemy 2 sprites
enemy1_frame0    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 1.png")
enemy1_frame1    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 2.png")
enemy1_frame2    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 3.png")
enemy1_frame3    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 4.png")
enemy1_frames    = [enemy1_frame0, enemy1_frame1, enemy1_frame2, enemy1_frame3]

# enemy 3 bullets
enemy2_bullet0   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 1.png")
enemy2_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 2.png")
enemy2_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 3.png")
enemy2_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 4.png")
enemy2_bullets   = [enemy2_bullet0, enemy2_bullet1, enemy2_bullet2, enemy2_bullet3]

# enemy 3 sprites
enemy2_frame0    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 1.png")
enemy2_frame1    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 2.png")
enemy2_frame2    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 3.png")
enemy2_frame3    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 4.png")
enemy2_frames    = [enemy2_frame0, enemy2_frame1, enemy2_frame2, enemy2_frame3]

# enemy 4 bullets
enemy3_bullet0   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 1.png")
enemy3_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 2.png")
enemy3_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 3.png")
enemy3_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 4.png")
enemy3_bullets   = [enemy3_bullet0, enemy3_bullet1, enemy3_bullet2, enemy3_bullet3]

# enemy 4 sprites
enemy3_frame0    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 1.png")
enemy3_frame1    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 2.png")
enemy3_frame2    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 3.png")
enemy3_frame3    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 4.png")
enemy3_frames    = [enemy3_frame0, enemy3_frame1, enemy3_frame2, enemy3_frame3]

# enemy 5 bullets
enemy4_bullet0   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 1.png")
enemy4_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 2.png")
enemy4_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 3.png")
enemy4_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 4.png")
enemy4_bullets   = [enemy4_bullet0, enemy4_bullet1, enemy4_bullet2, enemy4_bullet3]
enemy_bullets    = [enemy0_bullets, enemy1_bullets, enemy2_bullets, enemy3_bullets, enemy4_bullets]

# enemy 5 sprites
enemy4_frame0    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 1.png")
enemy4_frame1    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 2.png")
enemy4_frame2    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 3.png")
enemy4_frame3    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 4.png")
enemy4_frames    = [enemy4_frame0, enemy4_frame1, enemy4_frame2, enemy4_frame3]
enemy_frames     = [enemy0_frames, enemy1_frames, enemy2_frames, enemy3_frames, enemy4_frames]


easy_diff        = py.image.load("assets/HUD/easy difficulty.png")
normal_diff      = py.image.load("assets/HUD/normal difficulty.png")
hard_diff        = py.image.load("assets/HUD/hard difficulty.png")
insane_diff      = py.image.load("assets/HUD/insane difficulty.png")
button_highlight = py.image.load("assets/HUD/Pixel Nebula Menu Choice.png")
buttons          = py.image.load("assets/HUD/Pixel Nebula Menu Buttons.png")

# death animation frames
death_frame0     = py.image.load("assets/enemies/death frame 1.png")
death_frame1     = py.image.load("assets/enemies/death frame 2.png")
death_frame2     = py.image.load("assets/enemies/death frame 3.png")
death_frame3     = py.image.load("assets/enemies/death frame 4.png")
death_frame4     = py.image.load("assets/enemies/death frame 5.png")
death_frame5     = py.image.load("assets/enemies/death frame 6.png")
death_frame6     = py.image.load("assets/enemies/death frame 7.png")
death_frame7     = py.image.load("assets/enemies/death frame 8.png")
death_frames     = [death_frame0, death_frame1, death_frame2, death_frame3, death_frame4, death_frame5, death_frame6, death_frame7]

# power orb sprites
energy0          = py.image.load("assets/items/energy/energy 1.png")
energy1          = py.image.load("assets/items/energy/energy 2.png")
energy2          = py.image.load("assets/items/energy/energy 3.png")
energy3          = py.image.load("assets/items/energy/energy 4.png")
energy4          = py.image.load("assets/items/energy/energy 5.png")
energy5          = py.image.load("assets/items/energy/energy 6.png")
energys          = [energy0, energy1, energy2, energy3, energy4, energy5]

# map levels
map_level0       = py.image.load("assets/HUD/map level/map level 0.png")
map_level1       = py.image.load("assets/HUD/map level/map level 1.png")
map_level2       = py.image.load("assets/HUD/map level/map level 2.png")
map_level3       = py.image.load("assets/HUD/map level/map level 3.png")
map_level4       = py.image.load("assets/HUD/map level/map level 4.png")
map_level5       = py.image.load("assets/HUD/map level/map level 5.png")
map_level6       = py.image.load("assets/HUD/map level/map level 6.png")
map_level7       = py.image.load("assets/HUD/map level/map level 7.png")
map_level8       = py.image.load("assets/HUD/map level/map level 8.png")
map_level9       = py.image.load("assets/HUD/map level/map level 9.png")
map_level10      = py.image.load("assets/HUD/map level/map level 10.png")
map_level11      = py.image.load("assets/HUD/map level/map level 11.png")
map_level12      = py.image.load("assets/HUD/map level/map level 12.png")
map_level13      = py.image.load("assets/HUD/map level/map level 13.png")
map_level14      = py.image.load("assets/HUD/map level/map level 14.png")
map_level15      = py.image.load("assets/HUD/map level/map level 15.png")
map_level16      = py.image.load("assets/HUD/map level/map level 16.png")
map_level17      = py.image.load("assets/HUD/map level/map level 17.png")
map_level18      = py.image.load("assets/HUD/map level/map level 18.png")
map_level19      = py.image.load("assets/HUD/map level/map level 19.png")
map_level20      = py.image.load("assets/HUD/map level/map level 20.png")
map_level21      = py.image.load("assets/HUD/map level/map level 21.png")
map_level22      = py.image.load("assets/HUD/map level/map level 22.png")
map_level23      = py.image.load("assets/HUD/map level/map level 23.png")
map_level24      = py.image.load("assets/HUD/map level/map level 24.png")
map_level25      = py.image.load("assets/HUD/map level/map level 25.png")
map_level26      = py.image.load("assets/HUD/map level/map level 26.png")
map_level27      = py.image.load("assets/HUD/map level/map level 27.png")
map_level28      = py.image.load("assets/HUD/map level/map level 28.png")
map_level29      = py.image.load("assets/HUD/map level/map level 29.png")
map_level30      = py.image.load("assets/HUD/map level/map level 30.png")
map_level31      = py.image.load("assets/HUD/map level/map level 31.png")
map_level32      = py.image.load("assets/HUD/map level/map level 32.png")
map_level33      = py.image.load("assets/HUD/map level/map level 33.png")
map_level34      = py.image.load("assets/HUD/map level/map level 34.png")
map_background   = py.image.load("assets/HUD/map background.png")
map_buttons      = py.image.load("assets/HUD/Pixel Nebula Map Buttons.png")
map_levels       = [map_level0,  map_level1,  map_level2,  map_level3,  map_level4,  map_level5,  map_level6,  map_level7,  map_level8,  map_level9, 
                    map_level10, map_level11, map_level12, map_level13, map_level14, map_level15, map_level16, map_level17, map_level18, map_level19,
                    map_level20, map_level21, map_level22, map_level23, map_level24, map_level25, map_level26, map_level27, map_level28, map_level29,
                    map_level30, map_level31, map_level32, map_level33, map_level34]





def create_bullet(controller: dict):
    global player_bullets

    last_shot_time = 0

    while True:
        while in_battle:

            keys = py.key.get_pressed()

            if keys[py.K_SPACE]:
                # create a bullet

                if last_shot_time + bullet_delay < py.time.get_ticks():

                    player_bullets.append({'x': player_x, 'y': player_y})  

                    last_shot_time = py.time.get_ticks()

            if controller.get('shutdown', False): break
        py.time.delay(10)
        if controller.get('shutdown', False): print("Thread is stopping..."); break


e = { "shutdown" : False }
thread = threading.Thread(target=create_bullet, args=(e,))
thread.start()



def create_enemies(path: str):

    enemies_dict = {}

    path = path[stage_num].strip()

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

                # bullet speed
                elif n == 4:
                    enemies_dict[i]['bullet_speed'] = values[i]

                # bullet fire rate
                elif n == 5:
                    enemies_dict[i]['bullet_delay'] = values[i]

                # enemy type
                elif n == 6:
                    enemies_dict[i]['enemy_type'] = values[i]

    print("Loaded enemies:", enemies_dict)
    return enemies_dict



def game_loop(path: str):
    global player_bullets, player_x, player_y, play_game, home_page, play_game, live_num, in_battle

    enemies_dict = create_enemies(path)

    animation_num = 0

    player_y = 800
    player_x = 288
    player_bullets = []
    last_frame_time = 0

    while in_battle:

        events = py.event.get()
        keys   = py.key.get_pressed()

        if   stage_num <   5: background = backgrounds[0]
        elif stage_num <  11: background = backgrounds[1]
        elif stage_num <  15: background = backgrounds[2]
        elif stage_num <  19: background = backgrounds[3]
        elif stage_num <  24: background = backgrounds[4]
        elif stage_num <  29: background = backgrounds[5]
        elif stage_num <  34: background = backgrounds[6]
        elif stage_num == 34: background = backgrounds[7]

        background_rect = background.get_rect(center=(288, 512))

        game_window.blit(background, background_rect)

        if   keys[py.K_a]: character_frame = characters_left[animation_num]
        elif keys[py.K_d]: character_frame = characters_right[animation_num]
        else             : character_frame = characters[animation_num]

        character_frame_rect = character_frame.get_rect(center=(player_x, player_y))
        game_window.blit(character_frame, character_frame_rect)

        character_bullet    = character_bullets[animation_num]

        player_rect = py.Rect(player_x - 25, player_y - 30, 50, 50)

        py.draw.rect(game_window, (255, 0, 0), (player_rect), 2)

        if last_frame_time + 100 < py.time.get_ticks():
            
            animation_num     = (animation_num + 1) % 4

            last_frame_time = py.time.get_ticks()

        for key, enemy in enemies_dict.items():

            enemy_frame_type    = enemy_frames[enemy['enemy_type']]

            enemy_bullet_type   = enemy_bullets[enemy['enemy_type']]

            enemy_frame         = enemy_frame_type[animation_num]
            
            enemy_bullet_frame  = enemy_bullet_type[animation_num]

            enemy_frame_rect = enemy_frame.get_rect(center=(enemy['x'], enemy['y']))
            game_window.blit(enemy_frame, enemy_frame_rect)

            enemy_rect = py.Rect(enemy['x'] - 25, enemy['y'] - 30,  50, 50)            

            enemy['x'] += enemy['x_speed']
            enemy['y'] += enemy['y_speed']

            if enemy_rect.colliderect(player_rect):
                in_battle = False
                live_num -= 1
                home_page = True
                if live_num == -1:
                    play_game = False; in_battle = False; e["shutdown"] = True

            _deleted = 0
            for i, bullet in enumerate(list(enemy['bullets'])):

                bullet['x'] = enemy['x']

                bullet['y'] += enemy['bullet_speed']

                if bullet['y'] > HEIGHT + 100:

                    del enemy['bullets'][i - _deleted]
                    _deleted += 1
                    continue

                enemy['bullet_rect'] = py.Rect(bullet['x'] - 6, bullet['y'] - 6, 12, 12)

                py.draw.rect(game_window, (255, 0, 0), (enemy['bullet_rect']), 2)

                enemy_bullet_rect = enemy_bullet_frame.get_rect(center=(enemy['x'], bullet['y']))
                game_window.blit(enemy_bullet_frame, enemy_bullet_rect)

                if enemy['bullet_rect'].colliderect(player_rect):
                    in_battle = False
                    live_num -= 1
                    home_page = True
                    if live_num == -1:
                        play_game = False; in_battle = False; e["shutdown"] = True

            enemy['enemy_rect'] = py.Rect(enemy['x'] - 25, enemy['y'] - 30,  50, 50)

            py.draw.rect(game_window, (255, 0, 0), (enemy['enemy_rect']), 2)



            if 'last_shot_time' not in enemy:
                enemy['last_shot_time'] = 0

            if enemy['last_shot_time'] + enemy['bullet_delay'] < py.time.get_ticks():
                enemy['bullets'].append({'x': enemy['x'], 'y': enemy['y']})

                enemy['last_shot_time'] = py.time.get_ticks()



        _deleted = 0
        for i, bullet in enumerate(list(player_bullets)):

            bullet['y'] -= 32

            if bullet['y'] < -100:

                del player_bullets[i - _deleted]
                _deleted += 1
                continue

            bullet['bullet_rect'] = py.Rect(bullet['x'] - 32, bullet['y'] - 20, 64, 40)

            py.draw.rect(game_window, (255, 0, 0), (bullet['bullet_rect']), 2)

            character_bullet_rect = character_bullet.get_rect(center=(bullet['x'], bullet['y']))
            game_window.blit(character_bullet, character_bullet_rect)


            if enemy['enemy_rect'].colliderect(bullet['bullet_rect']):
                print('you shot enemy')






        
        

        

        # keybindings
        if keys[py.K_a]:
            # move left
            if keys[py.K_LSHIFT]: 
                player_x -= 8
            else: 
                player_x -= 16

        elif keys[py.K_d]:
            # move right
            if keys[py.K_LSHIFT]: 
                player_x += 8
            else: 
                player_x += 16

        if keys[py.K_w]:
            # move up
            if keys[py.K_LSHIFT]: 
                player_y -= 8
            else:
                player_y -= 16

        elif keys[py.K_s]:
            # move down
            if keys[py.K_LSHIFT]: 
                player_y += 8
            else: 
                player_y += 16

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
                in_battle = False; play_game = False; e["shutdown"] = True

        py.time.delay(10)
        py.display.update()
        


# game loop
while play_game:

    events = py.event.get()

    keys   = py.key.get_pressed()

    if not in_battle: 
        
        background_rect = menu_background.get_rect(center=(288, 512))

        game_window.blit(menu_background, background_rect)

        buttons_rect = buttons.get_rect(center=(288, 700))
        
        game_window.blit(buttons, buttons_rect)

        # placing life count
        lives_rect = lives[live_num].get_rect(center=(288, 985)); game_window.blit(lives[live_num], lives_rect)

        # place menu button highlighter
        if   menu_number == 1 and home_page: highlight_rect = button_highlight.get_rect(center=(288, 572)); game_window.blit(button_highlight, highlight_rect)
        elif menu_number == 2 and home_page: highlight_rect = button_highlight.get_rect(center=(288, 700)); game_window.blit(button_highlight, highlight_rect)
        elif menu_number == 3 and home_page: highlight_rect = button_highlight.get_rect(center=(288, 828)); game_window.blit(button_highlight, highlight_rect)
        
        # place difficulty setting text
        if   difficulty_num == 1 and home_page: easy_rect   = easy_diff.  get_rect(center=(288, 700)); game_window.blit(easy_diff,   easy_rect)
        elif difficulty_num == 2 and home_page: normal_rect = normal_diff.get_rect(center=(288, 700)); game_window.blit(normal_diff, normal_rect)
        elif difficulty_num == 3 and home_page: hard_rect   = hard_diff.  get_rect(center=(288, 700)); game_window.blit(hard_diff,   hard_rect)
        elif difficulty_num == 4 and home_page: insane_rect = insane_diff.get_rect(center=(288, 700)); game_window.blit(insane_diff, insane_rect)

        # placing the map
        if not home_page:

            map_overlay = map_levels[stage_num]

            background_rect = map_background.get_rect(center=(288, 512))

            map_rect = map_overlay.get_rect(center=(288, 512))

            buttons_rect = map_buttons.get_rect(center=(148, 106))

            game_window.blit(map_background, background_rect)

            game_window.blit(map_overlay, map_rect)

            game_window.blit(map_buttons, buttons_rect)

            if   menu_number == 1: highlight_rect = button_highlight.get_rect(center=(148, 62));  game_window.blit(button_highlight, highlight_rect)
            elif menu_number == 2: highlight_rect = button_highlight.get_rect(center=(148, 150)); game_window.blit(button_highlight, highlight_rect)

            

    




    # keybindings
    if keys[py.K_a]:
        # move left
        if keys[py.K_LSHIFT]: 
            x -= 4
        else: 
            x -= 8

    elif keys[py.K_d]:
        # move right
        if keys[py.K_LSHIFT]: 
            x += 4
        else: 
            x += 8

    if keys[py.K_w]:
        # move up
        if keys[py.K_LSHIFT]: 
            y -= 4
        else:
            y -= 8

    elif keys[py.K_s]:
        # move down
        if keys[py.K_LSHIFT]: 
            y += 4
        else: 
            y += 8

    # set player boundaries
    if x < 0:
        x = 0

    if x > WIDTH:
        x = WIDTH

    if y > HEIGHT:
        y = HEIGHT

    if y < 0:
        y = 0

    for event in events:
    # close program
        if event.type == py.QUIT: 
                in_battle = False; play_game = False; e["shutdown"] = True

    if keys[py.K_UP]:
        # move up menu button
        if home_page:
            if menu_number >= 2: menu_number -= 1; py.time.delay(250)
        else: 
            if menu_number == 2: menu_number = 1

    if keys[py.K_DOWN]:
        # move down menu button
        if home_page:
            if menu_number <= 2: menu_number += 1; py.time.delay(250)
        else:
            if menu_number == 1: menu_number = 2

    if keys[py.K_LEFT]:
        # change difficulty
        if home_page:
            if menu_number == 2:
                if difficulty_num >= 2: difficulty_num -= 1; py.time.delay(250)

    if keys[py.K_RIGHT]:
        # change difficulty
        if home_page:
            if menu_number == 2:
                if difficulty_num <= 4: difficulty_num += 1; py.time.delay(250)

    if keys[py.K_RETURN]:
        # choose menu option
        if home_page and menu_number == 1:
            home_page = False

        elif not home_page and menu_number == 1: 
            
            in_battle = True
            if   difficulty_num == 1: file_path = open("easy.txt"); file_path = file_path.readlines()
            elif difficulty_num == 2: file_path = 'normal.txt'
            elif difficulty_num == 3: file_path = 'hard.txt'
            elif difficulty_num == 4: file_path = 'insane.txt'

            game_loop(file_path)

        elif not home_page and menu_number == 2: home_page = True; menu_number = 1

        elif home_page and menu_number == 3: play_game = False; in_battle = False 

        py.time.delay(250)

    py.display.update()

    py.time.delay(10)
# imports
import pygame as py
from sys import exit
import os
import array
from array import *
import threading
py.init()
# this could easily surpass 10k lines of code if I have different enemy patterns for each difficulty

# notes




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
    global enemy1_animation_num, enemy2_animation_num, enemy3_animation_num, enemy4_animation_num, enemy5_animation_num
    global array1_filled, array2_filled, array3_filled, array4_filled, array5_filled
    global enemy1_x, enemy2_x, enemy3_x, enemy4_x, enemy5_x 
    global enemy1_y, enemy2_y, enemy3_y, enemy4_y, enemy5_y
    global enemy1_x_speed, enemy2_x_speed, enemy3_x_speed, enemy4_x_speed, enemy5_x_speed
    global enemy1_y_speed, enemy2_y_speed, enemy3_y_speed, enemy4_y_speed, enemy5_y_speed
    global enemy1_rects, enemy2_rects, enemy3_rects, enemy4_rects, enemy5_rects
    global enemy1_bullets_present, enemy2_bullets_present, enemy3_bullets_present, enemy4_bullets_present, enemy5_bullets_present
    global enemy1_bullet_index_num, enemy2_bullet_index_num, enemy3_bullet_index_num, enemy4_bullet_index_num, enemy5_bullet_index_num
    global enemy1_bullet_animation_num, enemy2_bullet_animation_num, enemy3_bullet_animation_num, enemy4_bullet_animation_num, enemy5_bullet_animation_num
    global enemy1_bullet_x, enemy2_bullet_x, enemy3_bullet_x, enemy4_bullet_x, enemy5_bullet_x
    global enemy1_bullet_y, enemy2_bullet_y, enemy3_bullet_y, enemy4_bullet_y, enemy5_bullet_y
    global enemy1_bullet_x_speed, enemy2_bullet_x_speed, enemy3_bullet_x_speed, enemy4_bullet_x_speed, enemy5_bullet_x_speed
    global enemy1_bullet_y_speed, enemy2_bullet_y_speed, enemy3_bullet_y_speed, enemy4_bullet_y_speed, enemy5_bullet_y_speed
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
    enemy1_animation_num, enemy2_animation_num, enemy3_animation_num, enemy4_animation_num, enemy5_animation_num = 1, 1, 1, 1, 1
    array1_filled, array2_filled, array3_filled, array4_filled, array5_filled                                    = False, False, False, False, False
    enemy1_x, enemy2_x, enemy3_x, enemy4_x, enemy5_x                                                             = [], [], [], [], []
    enemy1_y, enemy2_y, enemy3_y, enemy4_y, enemy5_y                                                             = [], [], [], [], []
    enemy1_x_speed, enemy2_x_speed, enemy3_x_speed, enemy4_x_speed, enemy5_x_speed                               = [], [], [], [], []
    enemy1_y_speed, enemy2_y_speed, enemy3_y_speed, enemy4_y_speed, enemy5_y_speed                               = [], [], [], [], []
    enemy1_rects, enemy2_rects, enemy3_rects, enemy4_rects, enemy5_rects                                         = [], [], [], [], []

    # enemy bullet animation stuff
    enemy1_bullets_present, enemy2_bullets_present, enemy3_bullets_present, enemy4_bullets_present, enemy5_bullets_present                          = True, True, False, False, False
    enemy1_bullet_index_num, enemy2_bullet_index_num, enemy3_bullet_index_num, enemy4_bullet_index_num, enemy5_bullet_index_num                     = 0, 0, 0, 0, 0
    enemy1_bullet_animation_num, enemy2_bullet_animation_num, enemy3_bullet_animation_num, enemy4_bullet_animation_num, enemy5_bullet_animation_num = 1, 1, 1, 1, 1
    enemy1_bullet_x, enemy2_bullet_x, enemy3_bullet_x, enemy4_bullet_x, enemy5_bullet_x                                                             = [], [], [], [], []
    enemy1_bullet_y, enemy2_bullet_y, enemy3_bullet_y, enemy4_bullet_y, enemy5_bullet_y                                                             = [], [], [], [], []
    enemy1_bullet_x_speed, enemy2_bullet_x_speed, enemy3_bullet_x_speed, enemy4_bullet_x_speed, enemy5_bullet_x_speed                               = [], [], [], [], []
    enemy1_bullet_y_speed, enemy2_bullet_y_speed, enemy3_bullet_y_speed, enemy4_bullet_y_speed, enemy5_bullet_y_speed                               = [], [], [], [], []
# the function is run once to make sure that the variables exist
reset_arrays()


# important stuff
in_battle      = False
play_game      = True
lives          = 3
difficulty_num = 1
stage_num      = 0
enemies_killed = 0
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

# sprites
player_animation_num = 1
background0      = py.image.load("assets/backgrounds/backgrounds/Background 0.png")
background1      = py.image.load("assets/backgrounds/backgrounds/Background 1.png")
background2      = py.image.load("assets/backgrounds/backgrounds/Background 2.png")
background3      = py.image.load("assets/backgrounds/backgrounds/Background 3.png")
background4      = py.image.load("assets/backgrounds/backgrounds/Background 4.png")
background5      = py.image.load("assets/backgrounds/backgrounds/Background 5.png")
background6      = py.image.load("assets/backgrounds/backgrounds/Background 6.png")
background7      = py.image.load("assets/backgrounds/backgrounds/Background 7.png")
backgrounds      = [background0, background1, background2, background3, background4, background5, background6, background7]
menu_background  = py.image.load("assets/HUD/Pixel Nebula Title HUD.png")
lives3           = py.image.load("assets/HUD/lives 3.png")
lives2           = py.image.load("assets/HUD/lives 2.png")
lives1           = py.image.load("assets/HUD/lives 1.png")
lives0           = py.image.load("assets/HUD/lives 0.png")
character1       = py.image.load("assets/ships/ship 1.png")
character2       = py.image.load("assets/ships/ship 2.png")
character3       = py.image.load("assets/ships/ship 3.png")
character4       = py.image.load("assets/ships/ship 4.png")
character1l      = py.image.load("assets/ships/ship 1 l.png")
character2l      = py.image.load("assets/ships/ship 2 l.png")
character3l      = py.image.load("assets/ships/ship 3 l.png")
character1r      = py.image.load("assets/ships/ship 1 r.png")
character2r      = py.image.load("assets/ships/ship 2 r.png")
character3r      = py.image.load("assets/ships/ship 3 r.png")
stage_clear1     = py.image.load("assets/ships/level clear 1.png")
stage_clear2     = py.image.load("assets/ships/level clear 2.png")
stage_clear3     = py.image.load("assets/ships/level clear 3.png")
stage_clear4     = py.image.load("assets/ships/level clear 4.png")
stage_clear5     = py.image.load("assets/ships/level clear 5.png")
stage_clear6     = py.image.load("assets/ships/level clear 6.png")
stage_clear7     = py.image.load("assets/ships/level clear 7.png")
stage_clear8     = py.image.load("assets/ships/level clear 8.png")
stage_clear9     = py.image.load("assets/ships/level clear 9.png")
stage_clear10    = py.image.load("assets/ships/level clear 10.png")
stage_clear11    = py.image.load("assets/ships/level clear 11.png")
stage_clear12    = py.image.load("assets/ships/level clear 12.png")
stage_clear      = [stage_clear1, stage_clear2, stage_clear3, stage_clear4,  stage_clear5,  stage_clear6, 
                    stage_clear7, stage_clear8, stage_clear9, stage_clear10, stage_clear11, stage_clear12]
player_bullet1   = py.image.load("assets/bullets/bullet 1.png")
player_bullet2   = py.image.load("assets/bullets/bullet 2.png")
player_bullet3   = py.image.load("assets/bullets/bullet 3.png")
player_bullet4   = py.image.load("assets/bullets/bullet 4.png")
enemy1_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 1.png")
enemy1_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 2.png")
enemy1_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 3.png")
enemy1_bullet4   = py.image.load("assets/enemies/enemies 1/enemy 1/bullet 4.png")
enemy1_frame1    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 1.png")
enemy1_frame2    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 2.png")
enemy1_frame3    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 3.png")
enemy1_frame4    = py.image.load("assets/enemies/enemies 1/enemy 1/enemy 4.png")
enemy2_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 1.png")
enemy2_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 2.png")
enemy2_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 3.png")
enemy2_bullet4   = py.image.load("assets/enemies/enemies 1/enemy 2/bullet 4.png")
enemy2_frame1    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 1.png")
enemy2_frame2    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 2.png")
enemy2_frame3    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 3.png")
enemy2_frame4    = py.image.load("assets/enemies/enemies 1/enemy 2/enemy 4.png")
enemy3_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 1.png")
enemy3_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 2.png")
enemy3_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 3.png")
enemy3_bullet4   = py.image.load("assets/enemies/enemies 1/enemy 3/bullet 4.png")
enemy3_frame1    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 1.png")
enemy3_frame2    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 2.png")
enemy3_frame3    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 3.png")
enemy3_frame4    = py.image.load("assets/enemies/enemies 1/enemy 3/enemy 4.png")
enemy4_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 1.png")
enemy4_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 2.png")
enemy4_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 3.png")
enemy4_bullet4   = py.image.load("assets/enemies/enemies 1/enemy 4/bullet 4.png")
enemy4_frame1    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 1.png")
enemy4_frame2    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 2.png")
enemy4_frame3    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 3.png")
enemy4_frame4    = py.image.load("assets/enemies/enemies 1/enemy 4/enemy 4.png")
enemy5_bullet1   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 1.png")
enemy5_bullet2   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 2.png")
enemy5_bullet3   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 3.png")
enemy5_bullet4   = py.image.load("assets/enemies/enemies 1/enemy 5/bullet 4.png")
enemy5_frame1    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 1.png")
enemy5_frame2    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 2.png")
enemy5_frame3    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 3.png")
enemy5_frame4    = py.image.load("assets/enemies/enemies 1/enemy 5/enemy 4.png")
easy_diff        = py.image.load("assets/HUD/easy difficulty.png")
normal_diff      = py.image.load("assets/HUD/normal difficulty.png")
hard_diff        = py.image.load("assets/HUD/hard difficulty.png")
insane_diff      = py.image.load("assets/HUD/insane difficulty.png")
button_highlight = py.image.load("assets/HUD/Pixel Nebula Menu Choice.png")
buttons          = py.image.load("assets/HUD/Pixel Nebula Menu Buttons.png")
death_frame1     = py.image.load("assets/enemies/death frame 1.png")
death_frame2     = py.image.load("assets/enemies/death frame 2.png")
death_frame3     = py.image.load("assets/enemies/death frame 3.png")
death_frame4     = py.image.load("assets/enemies/death frame 4.png")
death_frame5     = py.image.load("assets/enemies/death frame 5.png")
death_frame6     = py.image.load("assets/enemies/death frame 6.png")
death_frame7     = py.image.load("assets/enemies/death frame 7.png")
death_frame8     = py.image.load("assets/enemies/death frame 8.png")
shield1          = py.image.load("assets/items/shield/shield frame 1.png")
shield2          = py.image.load("assets/items/shield/shield frame 2.png")
shield3          = py.image.load("assets/items/shield/shield frame 3.png")
shield4          = py.image.load("assets/items/shield/shield frame 4.png")
shield5          = py.image.load("assets/items/shield/shield frame 5.png")
shield6          = py.image.load("assets/items/shield/shield frame 6.png")
shield_orb1      = py.image.load("assets/items/shield/shield orbs/shield orb 1.png")
shield_orb2      = py.image.load("assets/items/shield/shield orbs/shield orb 2.png")
shield_orb3      = py.image.load("assets/items/shield/shield orbs/shield orb 3.png")
energy1          = py.image.load("assets/items/energy/energy 1.png")
energy2          = py.image.load("assets/items/energy/energy 2.png")
energy3          = py.image.load("assets/items/energy/energy 3.png")
energy4          = py.image.load("assets/items/energy/energy 4.png")
energy5          = py.image.load("assets/items/energy/energy 5.png")
energy6          = py.image.load("assets/items/energy/energy 6.png")
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





# set up window
game_window = py.display.set_mode((WIDTH, HEIGHT))
game_window.fill((0, 0, 0))

# animate player bullets
def player_bullet_animation():
    global player_bullet_index_num, bullet_animation_num, deaths, death_x, death_y, death_animation_num, items, item_animation_num, enemies_killed

    # use the correct image for the animation.
    if bullet_animation_num == 1: player_bullet = player_bullet1; bullet_animation_num += 1
    if bullet_animation_num == 2: player_bullet = player_bullet2; bullet_animation_num += 1
    if bullet_animation_num == 3: player_bullet = player_bullet3; bullet_animation_num += 1
    if bullet_animation_num == 4: player_bullet = player_bullet4; bullet_animation_num  = 1

    # go through each index in the bullet arrays and put a bullet at the coordinates.
    player_bullet_index_num = 0
    for bullet in player_bullet_x:
        player_bullet_rect = player_bullet.get_rect(center=(player_bullet_x[player_bullet_index_num], player_bullet_y[player_bullet_index_num]))
        game_window.blit(player_bullet, player_bullet_rect)

        bullet_rect = py.Rect(player_bullet_x[player_bullet_index_num] - 32, player_bullet_y[player_bullet_index_num] - 20, 64, 40)

        # this checks to see if the bullet is colliding with any enemy rectangle, and it will get rid of the bullet and enemy if they are colliding.
        enemy1_index = 0
        for rect in enemy1_rects:
            if bullet_rect.colliderect(rect): 

                # get rid of bullet
                player_bullet_x.pop(player_bullet_index_num)
                player_bullet_y.pop(player_bullet_index_num)

                # add coordinates to death animation
                death_x.append(enemy1_x[enemy1_index])
                death_y.append(enemy1_y[enemy1_index])
                death_animation_num.append(1)
                deaths = True

                # add coordinates to the item dropping function
                item_x.append(enemy1_x[enemy1_index])
                item_y.append(enemy1_y[enemy1_index])
                item_animation_num.append(1)
                items  = True

                # count the kill and get rid of the enemy.
                enemies_killed += 1
                enemy1_x.pop(enemy1_index)
                enemy1_y.pop(enemy1_index)
                enemy1_x_speed.pop(enemy1_index)
                enemy1_y_speed.pop(enemy1_index)
                enemy1_rects.pop(enemy1_index)
                break
            enemy1_index += 1
            
        enemy2_index = 0
        for rect in enemy2_rects:
            if bullet_rect.colliderect(rect): 

                player_bullet_x.pop(player_bullet_index_num)
                player_bullet_y.pop(player_bullet_index_num)

                death_x.append(enemy2_x[enemy2_index])
                death_y.append(enemy2_y[enemy2_index])
                deaths = True
                death_animation_num.append(1)

                item_x.append(enemy2_x[enemy2_index])
                item_y.append(enemy2_y[enemy2_index])
                item_animation_num.append(1)
                items  = True

                enemies_killed += 1
                enemy2_x.pop(enemy2_index)
                enemy2_y.pop(enemy2_index)
                enemy2_x_speed.pop(enemy2_index)
                enemy2_y_speed.pop(enemy2_index)
                enemy2_rects.pop(enemy2_index)
                break
            enemy2_index += 1

        player_bullet_index_num += 1

    # move the bullet.
    player_bullet_index_num = 0
    for bullet in player_bullet_x:
        player_bullet_y[player_bullet_index_num] -= 32
        player_bullet_index_num += 1

    # get rid of the bullet if it is out of the game window.
    player_bullet_index_num = 0
    for bullet in player_bullet_y:
        if bullet <= 0:
            player_bullet_x.pop(player_bullet_index_num)
            player_bullet_y.pop(player_bullet_index_num)
        player_bullet_index_num += 1


# animate enemy bullets.
def enemy1_bullet_animation():
    global enemy1_bullet_index_num, enemy1_bullet_animation_num, in_battle, lives, play_game, home_page, enemy1_bullets_present

    # use the correct image for the animation.
    if enemy1_bullet_animation_num == 1: enemy1_bullet = enemy1_bullet1; enemy1_bullet_animation_num += 1
    if enemy1_bullet_animation_num == 2: enemy1_bullet = enemy1_bullet2; enemy1_bullet_animation_num += 1
    if enemy1_bullet_animation_num == 3: enemy1_bullet = enemy1_bullet3; enemy1_bullet_animation_num += 1
    if enemy1_bullet_animation_num == 4: enemy1_bullet = enemy1_bullet4; enemy1_bullet_animation_num  = 1

    # go through each index in the bullet arrays and put a bullet at the coordinates.
    enemy1_bullet_index_num = 0
    for bullet in enemy1_bullet_x:
        enemy1_bullet_rectangle = enemy1_bullet.get_rect(center=(enemy1_bullet_x[enemy1_bullet_index_num], enemy1_bullet_y[enemy1_bullet_index_num]))
        game_window.blit(enemy1_bullet, enemy1_bullet_rectangle)

        enemy1_bullet_rect = py.Rect(enemy1_bullet_x[enemy1_bullet_index_num] - 6, enemy1_bullet_y[enemy1_bullet_index_num] - 6, 12, 12)

        # if the bullet is colliding withe the player, kill player and remove a life.
        if enemy1_bullet_rect.colliderect(character_rect):
            in_battle = False
            lives -= 1
            home_page = True
            if lives == -1:
                play_game = False; in_battle = False; e["shutdown"] = True
 
        enemy1_bullet_index_num += 1

    # move the bullet
    enemy1_bullet_index_num = 0
    for bullet in enemy1_bullet_x:
        enemy1_bullet_x[enemy1_bullet_index_num] += enemy1_bullet_x_speed[enemy1_bullet_index_num]
        enemy1_bullet_y[enemy1_bullet_index_num] += enemy1_bullet_y_speed[enemy1_bullet_index_num]
        enemy1_bullet_index_num += 1

    # get rid of the bullet if it is out of the game window.
    enemy1_bullet_index_num = 0
    for bullet in enemy1_bullet_x:

        if enemy1_bullet_index_num >= len(enemy1_bullet_x): break

        if enemy1_bullet_x[enemy1_bullet_index_num] >= WIDTH or enemy1_bullet_x[enemy1_bullet_index_num] <= 0 or enemy1_bullet_y[enemy1_bullet_index_num] >= HEIGHT or enemy1_bullet_y[enemy1_bullet_index_num] <= 0:
            print('bullet got removed')
            enemy1_bullet_x.pop(enemy1_bullet_index_num)
            enemy1_bullet_y.pop(enemy1_bullet_index_num)
            enemy1_bullet_x_speed.pop(enemy1_bullet_index_num)
            enemy1_bullet_y_speed.pop(enemy1_bullet_index_num)
        enemy1_bullet_index_num += 1
    


# make enemy 2 bullet animations
def enemy2_bullet_animation():
    global enemy2_bullet_index_num, enemy2_bullet_animation_num, in_battle, lives, play_game, home_page, enemy2_bullets_present

    if enemy2_bullet_animation_num == 1: enemy2_bullet = enemy2_bullet1; enemy2_bullet_animation_num += 1
    if enemy2_bullet_animation_num == 2: enemy2_bullet = enemy2_bullet2; enemy2_bullet_animation_num += 1
    if enemy2_bullet_animation_num == 3: enemy2_bullet = enemy2_bullet3; enemy2_bullet_animation_num += 1
    if enemy2_bullet_animation_num == 4: enemy2_bullet = enemy2_bullet4; enemy2_bullet_animation_num  = 1

    enemy2_bullet_index_num = 0
    for bullet in enemy2_bullet_x:
        enemy2_bullet_rectangle = enemy2_bullet.get_rect(center=(enemy2_bullet_x[enemy2_bullet_index_num], enemy2_bullet_y[enemy2_bullet_index_num]))
        game_window.blit(enemy2_bullet, enemy2_bullet_rectangle)

        enemy2_bullet_rect = py.Rect(enemy2_bullet_x[enemy2_bullet_index_num] - 6, enemy2_bullet_y[enemy2_bullet_index_num] - 6, 12, 12)

        if enemy2_bullet_rect.colliderect(character_rect):
            in_battle = False
            lives -= 1
            home_page = True
            if lives == -1:
                play_game = False; in_battle = False; e["shutdown"] = True

        enemy2_bullet_index_num += 1

    enemy2_bullet_index_num = 0
    for bullet in enemy2_bullet_x:
        enemy2_bullet_x[enemy2_bullet_index_num] += enemy2_bullet_x_speed[enemy2_bullet_index_num]
        enemy2_bullet_y[enemy2_bullet_index_num] += enemy2_bullet_y_speed[enemy2_bullet_index_num]
        enemy2_bullet_index_num += 1

    enemy2_bullet_index_num = 0
    for bullet in enemy2_bullet_x:

        if enemy2_bullet_index_num >= len(enemy2_bullet_x): break

        if enemy2_bullet_x[enemy2_bullet_index_num] >= WIDTH or enemy2_bullet_x[enemy2_bullet_index_num] <= 0 or enemy2_bullet_y[enemy2_bullet_index_num] >= HEIGHT or enemy2_bullet_y[enemy2_bullet_index_num] <= 0:
            print('bullet got removed')
            enemy2_bullet_x.pop(enemy2_bullet_index_num)
            enemy2_bullet_y.pop(enemy2_bullet_index_num)
            enemy2_bullet_x_speed.pop(enemy2_bullet_index_num)
            enemy2_bullet_y_speed.pop(enemy2_bullet_index_num)
        enemy2_bullet_index_num += 1


# main thread that controls the majority of the animations
def animations(controller: dict):
    global player_animation_num, character_rect, background
    # prevents the loop from being exited while allowing it to be activated when needed.
    while True:
        while in_battle:
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
            character_rect = py.Rect(x - 25, y - 30, 50, 50)
            if keys[py.K_a]:
                if   player_animation_num == 4: player_animation_num  = 1
                if   player_animation_num == 1: player_animation_num += 1; character1l.get_rect(center=(x, y)); game_window.blit(character1l, character1l.get_rect(center=(x, y)))
                elif player_animation_num == 2: player_animation_num += 1; character2l.get_rect(center=(x, y)); game_window.blit(character2l, character2l.get_rect(center=(x, y)))
                elif player_animation_num == 3: player_animation_num  = 1; character3l.get_rect(center=(x, y)); game_window.blit(character3l, character3l.get_rect(center=(x, y)))
            elif keys[py.K_d]:
                if   player_animation_num == 4: player_animation_num  = 1
                if   player_animation_num == 1: player_animation_num += 1; character1r.get_rect(center=(x, y)); game_window.blit(character1r, character1r.get_rect(center=(x, y)))
                elif player_animation_num == 2: player_animation_num += 1; character2r.get_rect(center=(x, y)); game_window.blit(character2r, character2r.get_rect(center=(x, y)))
                elif player_animation_num == 3: player_animation_num += 1; character3r.get_rect(center=(x, y)); game_window.blit(character3r, character3r.get_rect(center=(x, y)))
            elif player_animation_num == 1: player_animation_num += 1; character1.get_rect(center=(x, y)); game_window.blit(character1, character1.get_rect(center=(x, y)))
            elif player_animation_num == 2: player_animation_num += 1; character2.get_rect(center=(x, y)); game_window.blit(character2, character2.get_rect(center=(x, y)))
            elif player_animation_num == 3: player_animation_num += 1; character3.get_rect(center=(x, y)); game_window.blit(character3, character3.get_rect(center=(x, y)))
            elif player_animation_num == 4: player_animation_num  = 1; character4.get_rect(center=(x, y)); game_window.blit(character4, character4.get_rect(center=(x, y)))

            if bullets_present: player_bullet_animation()

            if enemy1_bullets_present: enemy1_bullet_animation()

            if enemy2_bullets_present: enemy2_bullet_animation()

            if array1_filled: enemy1()

            if array2_filled: enemy2()

            if deaths: death_animations()

            if items: item_animations()

            if enemies_killed >= 5:
                if enemy1_bullet_x == [] and enemy2_bullet_x == [] and enemy3_bullet_x == [] and enemy4_bullet_x == [] and enemy5_bullet_x == []:
                    stage_clear_animation()

            py.time.delay(25)

            if controller.get('shutdown', False): break
        if controller.get('shutdown', False): print("Thread 1 is stopping..."); break

e = { "shutdown" : False }
thread1 = threading.Thread(target=animations, args=(e,))
thread1.start()

# you are checking to see that the character collision detection is working properly

def stage_clear_animation():
    global in_battle, home_page, stage_num

    for frame in stage_clear:
        game_window.blit(background, background_rect)
        frame_rect = frame.get_rect(center=(x, y))
        game_window.blit(frame, frame_rect)
        py.time.delay(100)

    stage_num += 1
    in_battle = False
    home_page = False



# every time the spacebar is pressed, create a new bullet at the location of the player
def create_bullet(controller: dict):
    global bullets_present, player_bullet_x, player_bullet_y
    while True:
        bullets_present       = True
        player_bullet_x       = []
        player_bullet_y       = []
        

        while in_battle:
            while keys[py.K_SPACE]:
                bullets_present = True
                if orbs_collected < 15:
                    player_bullet_x.append(x)
                    player_bullet_y.append(y - 64)
                    
                
                elif orbs_collected >= 15 and orbs_collected < 30:
                    player_bullet_x.append(x - 36)
                    player_bullet_x.append(x + 36)
                    player_bullet_y.append(y - 64)
                    player_bullet_y.append(y - 64)
                    

                elif orbs_collected >= 30:
                    player_bullet_x.append(x)
                    player_bullet_x.append(x - 68)
                    player_bullet_x.append(x + 68)
                    player_bullet_y.append(y - 64)
                    player_bullet_y.append(y - 64)
                    player_bullet_y.append(y - 64)
                    

                py.time.delay(bullet_delay)

            if controller.get('shutdown', False): break
        if controller.get('shutdown', False): print("Thread 2 is stopping..."); break

thread2 = threading.Thread(target=create_bullet, args=(e,))
thread2.start()



def create_enemy1_bullet(controller: dict):
    global enemy1_bullets_present
    while True:
        while in_battle:
            enemy1_bullets_present = True
            enemy1_bullet_index = 0
            if enemies_killed < 100:
                for x in enemy1_x:
                    enemy1_bullet_x.append(x)
                    enemy1_bullet_y.append(enemy1_y[enemy1_bullet_index] + 64)
                    enemy1_bullet_x_speed.append(0)
                    enemy1_bullet_y_speed.append(enemy1_y_speed[enemy1_bullet_index] * 2)
                    enemy1_bullet_index += 1

                py.time.delay(2000)

            if controller.get('shutdown', False): break
        if controller.get('shutdown', False): print("Thread 3 is stopping..."); break

thread3 = threading.Thread(target=create_enemy1_bullet, args=(e,))
thread3.start()



def create_enemy2_bullet(controller: dict):
    global enemy2_bullets_present
    while True:
        while in_battle:
            enemy2_bullets_present = True
            enemy2_bullet_index = 0
            if enemies_killed < 100:
                for x in enemy2_x:
                    enemy2_bullet_x.append(x)
                    enemy2_bullet_y.append(enemy2_y[enemy2_bullet_index] + 64)
                    enemy2_bullet_x_speed.append(0)
                    enemy2_bullet_y_speed.append(enemy2_y_speed[enemy2_bullet_index] * 6)
                    enemy2_bullet_index += 1

                py.time.delay(3000)

            if controller.get('shutdown', False): break
        if controller.get('shutdown', False): print("Thread 4 is stopping..."); break

thread4 = threading.Thread(target=create_enemy2_bullet, args=(e,))
thread4.start()



def enemies():
    global enemy1_animation_num, array1_filled, enemy1_x, enemy1_y, enemy1_x_speed, enemy1_y_speed, array2_filled, enemy1_rects, enemy2_rects, stage_num

    reset_arrays()

    stage_number  = open(info[stage_num].strip())  
    stage_data    = stage_number.readlines()

    try:
        n = 0
        while True: enemy1_x.append(int(stage_data[n].strip())); enemy1_rects.append(0); n += 1
    except: print(enemy1_x)
    n += 1
    
    try:
        while True: enemy1_y.append(int(stage_data[n].strip())); n += 1
    except: print(enemy1_y)

    n += 1
    try:
        while True: enemy1_x_speed.append(int(stage_data[n].strip())); n += 1
    except: print(enemy1_x_speed)

    n += 1
    try:
        while True: enemy1_y_speed.append(int(stage_data[n].strip())); n += 1
    except: print(enemy1_y_speed)

    array1_filled = True

    n += 3
    print(stage_data[n].strip())
    try:
        while True: enemy2_x.append(int(stage_data[n].strip())); enemy2_rects.append(0); n += 1
    except: print(enemy2_x)
    n += 1
    
    try:
        while True: enemy2_y.append(int(stage_data[n].strip())); n += 1
    except: print(enemy2_y)

    n += 1
    try:
        while True: enemy2_x_speed.append(int(stage_data[n].strip())); n += 1
    except: print(enemy2_x_speed)

    n += 1
    try:
        while True: enemy2_y_speed.append(int(stage_data[n].strip())); n += 1
    except: print(enemy2_y_speed)

    array2_filled = True
    
    py.time.delay(25)
    


def enemy1():
    global enemy1_animation_num, enemy1_index_num, enemy1_rect, play_game, in_battle, lives, home_page

    if enemy1_animation_num == 1: enemy1 = enemy1_frame1; enemy1_animation_num += 1
    if enemy1_animation_num == 2: enemy1 = enemy1_frame2; enemy1_animation_num += 1
    if enemy1_animation_num == 3: enemy1 = enemy1_frame3; enemy1_animation_num += 1
    if enemy1_animation_num == 4: enemy1 = enemy1_frame4; enemy1_animation_num  = 1

    enemy1_index_num = 0
    for number in enemy1_x:
        enemy1_rect = enemy1.get_rect(center=(enemy1_x[enemy1_index_num], enemy1_y[enemy1_index_num]))
        game_window.blit(enemy1, enemy1_rect)

        enemy1_rectangle = py.Rect(enemy1_x[enemy1_index_num] - 25, enemy1_y[enemy1_index_num] - 30,  50, 50)

        enemy1_rects[enemy1_index_num] = enemy1_rectangle

        enemy1_index_num += 1
    
        if enemy1_rectangle.colliderect(character_rect):
            in_battle = False
            lives -= 1
            home_page = True
            if lives == -1:
                play_game = False; in_battle = False; e["shutdown"] = True

    enemy1_index_num = 0
    for number in enemy1_x:
        enemy1_x[enemy1_index_num] += enemy1_x_speed[enemy1_index_num]
        enemy1_y[enemy1_index_num] += enemy1_y_speed[enemy1_index_num]
        enemy1_index_num += 1

                

# make enemy 2
def enemy2():
    global enemy2_animation_num, enemy2_index_num, enemy2_rect, in_battle, play_game, lives, home_page

    if enemy2_animation_num == 1: enemy2 = enemy2_frame1; enemy2_animation_num += 1
    if enemy2_animation_num == 2: enemy2 = enemy2_frame2; enemy2_animation_num += 1
    if enemy2_animation_num == 3: enemy2 = enemy2_frame3; enemy2_animation_num += 1
    if enemy2_animation_num == 4: enemy2 = enemy2_frame4; enemy2_animation_num  = 1

    enemy2_index_num = 0
    for number in enemy2_x:
        enemy2_rect = enemy2.get_rect(center=(enemy2_x[enemy2_index_num], enemy2_y[enemy2_index_num]))
        game_window.blit(enemy2, enemy2_rect)

        enemy2_rectangle = py.Rect(enemy2_x[enemy2_index_num] - 25, enemy2_y[enemy2_index_num] - 30,  50, 50)

        enemy2_rects[enemy2_index_num] = enemy2_rectangle

        enemy2_index_num += 1

        if enemy2_rectangle.colliderect(character_rect):
            in_battle = False
            lives -= 1
            home_page = True
            if lives == -1:
                play_game = False; in_battle = False; e["shutdown"] = True

    enemy2_index_num = 0
    for number in enemy2_x:
        enemy2_x[enemy2_index_num] += enemy2_x_speed[enemy2_index_num]
        enemy2_y[enemy2_index_num] += enemy2_y_speed[enemy2_index_num]
        enemy2_index_num += 1



# make enemy 3
def enemy3():
    global enemy3_animation_num, enemy3_index_num, enemy3_rect, in_battle, play_game, lives, home_page

    if enemy3_animation_num == 1: enemy3 = enemy3_frame1; enemy3_animation_num += 1
    if enemy3_animation_num == 2: enemy3 = enemy3_frame2; enemy3_animation_num += 1
    if enemy3_animation_num == 3: enemy3 = enemy3_frame3; enemy3_animation_num += 1
    if enemy3_animation_num == 4: enemy3 = enemy3_frame4; enemy3_animation_num  = 1

    enemy3_index_num = 0
    for number in enemy3_x:
        enemy3_rect = enemy3.get_rect(center=(enemy3_x[enemy3_index_num], enemy3_y[enemy3_index_num]))
        game_window.blit(enemy3, enemy3_rect)

        enemy3_rectangle = py.Rect(enemy3_x[enemy3_index_num] - 25, enemy3_y[enemy3_index_num] - 30,  50, 50)

        enemy3_rects[enemy3_index_num] = enemy3_rectangle

        enemy3_index_num += 1

        if enemy3_rectangle.colliderect(character_rect):
            in_battle = False
            lives -= 1
            home_page = True
            if lives == -1:
                play_game = False; in_battle = False; e["shutdown"] = True

    enemy3_index_num = 0
    for number in enemy3_x:
        enemy3_x[enemy3_index_num] += enemy3_x_speed[enemy3_index_num]
        enemy3_y[enemy3_index_num] += enemy3_y_speed[enemy3_index_num]
        enemy3_index_num += 1



# make enemy 4
def enemy4():
    global enemy4_animation_num, enemy4_index_num, enemy4_rect, in_battle, play_game, lives, home_page

    if enemy4_animation_num == 1: enemy4 = enemy4_frame1; enemy4_animation_num += 1
    if enemy4_animation_num == 2: enemy4 = enemy4_frame2; enemy4_animation_num += 1
    if enemy4_animation_num == 3: enemy4 = enemy4_frame3; enemy4_animation_num += 1
    if enemy4_animation_num == 4: enemy4 = enemy4_frame4; enemy4_animation_num  = 1

    enemy4_index_num = 0
    for number in enemy4_x:
        enemy4_rect = enemy4.get_rect(center=(enemy4_x[enemy4_index_num], enemy4_y[enemy4_index_num]))
        game_window.blit(enemy4, enemy4_rect)

        enemy4_rectangle = py.Rect(enemy4_x[enemy4_index_num] - 25, enemy4_y[enemy4_index_num] - 30,  50, 50)

        enemy4_rects[enemy4_index_num] = enemy4_rectangle

        enemy4_index_num += 1

        if enemy4_rectangle.colliderect(character_rect):
            in_battle = False
            lives -= 1
            home_page = True
            if lives == -1:
                play_game = False; in_battle = False; e["shutdown"] = True

    enemy4_index_num = 0
    for number in enemy4_x:
        enemy4_x[enemy4_index_num] += enemy4_x_speed[enemy4_index_num]
        enemy4_y[enemy4_index_num] += enemy4_y_speed[enemy4_index_num]
        enemy4_index_num += 1



# make enemy 5
def enemy5():
    global enemy5_animation_num, enemy5_index_num, enemy5_rect, in_battle, play_game, lives, home_page

    if enemy5_animation_num == 1: enemy5 = enemy5_frame1; enemy5_animation_num += 1
    if enemy5_animation_num == 2: enemy5 = enemy5_frame2; enemy5_animation_num += 1
    if enemy5_animation_num == 3: enemy5 = enemy5_frame3; enemy5_animation_num += 1
    if enemy5_animation_num == 4: enemy5 = enemy5_frame4; enemy5_animation_num  = 1

    enemy5_index_num = 0
    for number in enemy5_x:
        enemy5_rect = enemy5.get_rect(center=(enemy5_x[enemy5_index_num], enemy5_y[enemy5_index_num]))
        game_window.blit(enemy5, enemy5_rect)

    

    enemy5_index_num = 0
    for number in enemy5_x:
        enemy5_x[enemy5_index_num] += enemy5_x_speed[enemy5_index_num]
        enemy5_y[enemy5_index_num] += enemy5_y_speed[enemy5_index_num]
        enemy5_index_num += 1



def death_animations():
    global deaths

    death_index_num = 0
    for x in death_x:
        if   death_animation_num[death_index_num] == 1: death_rect = death_frame1.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame1, death_rect); death_animation_num[death_index_num] += 1
        elif death_animation_num[death_index_num] == 2: death_rect = death_frame2.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame2, death_rect); death_animation_num[death_index_num] += 1
        elif death_animation_num[death_index_num] == 3: death_rect = death_frame3.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame3, death_rect); death_animation_num[death_index_num] += 1
        elif death_animation_num[death_index_num] == 4: death_rect = death_frame4.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame4, death_rect); death_animation_num[death_index_num] += 1
        elif death_animation_num[death_index_num] == 5: death_rect = death_frame5.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame5, death_rect); death_animation_num[death_index_num] += 1
        elif death_animation_num[death_index_num] == 6: death_rect = death_frame6.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame6, death_rect); death_animation_num[death_index_num] += 1
        elif death_animation_num[death_index_num] == 7: death_rect = death_frame7.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame7, death_rect); death_animation_num[death_index_num] += 1
        elif death_animation_num[death_index_num] == 8: death_rect = death_frame8.get_rect(center=(x, death_y[death_index_num])); game_window.blit(death_frame8, death_rect)

        if death_animation_num[death_index_num] == 8:
            death_x.pop(death_index_num)
            death_y.pop(death_index_num)
            death_animation_num.pop(death_index_num)

        death_index_num += 1

        if death_x == []: deaths = False



def item_animations():
    global items, orbs_collected, bullet_delay, bullet_damage

    item_index_num = 0
    for x in item_x:
        if   item_animation_num[item_index_num] == 1: item_rect = energy1.get_rect(center=(x, item_y[item_index_num])); game_window.blit(energy1, item_rect); item_animation_num[item_index_num] += 1
        elif item_animation_num[item_index_num] == 2: item_rect = energy2.get_rect(center=(x, item_y[item_index_num])); game_window.blit(energy2, item_rect); item_animation_num[item_index_num] += 1
        elif item_animation_num[item_index_num] == 3: item_rect = energy3.get_rect(center=(x, item_y[item_index_num])); game_window.blit(energy3, item_rect); item_animation_num[item_index_num] += 1
        elif item_animation_num[item_index_num] == 4: item_rect = energy4.get_rect(center=(x, item_y[item_index_num])); game_window.blit(energy4, item_rect); item_animation_num[item_index_num] += 1
        elif item_animation_num[item_index_num] == 5: item_rect = energy5.get_rect(center=(x, item_y[item_index_num])); game_window.blit(energy5, item_rect); item_animation_num[item_index_num] += 1
        elif item_animation_num[item_index_num] == 6: item_rect = energy6.get_rect(center=(x, item_y[item_index_num])); game_window.blit(energy6, item_rect)
        if x >= 1100:
            item_x.pop(item_index_num)
            item_y.pop(item_index_num)
            item_animation_num.pop(item_index_num)

        item_y[item_index_num] += 10

        if item_x == []: items = False

        if item_rect.colliderect(character_rect):
            orbs_collected += 1
            bullet_delay -= 3
            bullet_damage += 1
            item_x.pop(item_index_num)
            item_y.pop(item_index_num)
            item_animation_num.pop(item_index_num)

        item_index_num += 1



def time_counter(controller: dict):
    global time_passed
    time_passed = 0
    while True:
        while in_battle:
            py.time.delay(1000)
            time_passed += 1
            print(time_passed)

            if controller.get('shutdown', False): break
        py.time.delay(25)
        if controller.get('shutdown', False): print("Thread 5 is stopping..."); break


thread5 = threading.Thread(target=time_counter, args=(e,))
thread5.start()



# game loop
while play_game:

    events = py.event.get()

    keys   = py.key.get_pressed()

    if not in_battle: 

        # background and buttons for menu
        
        background_rect = menu_background.get_rect(center=(288, 512))

        game_window.blit(menu_background, background_rect)

        buttons_rect = buttons.get_rect(center=(288, 700))
        
        game_window.blit(buttons, buttons_rect)

        # placing life count
        if   lives == 3 and home_page: lives_rect = lives3.get_rect(center=(288, 985)); game_window.blit(lives3, lives_rect)
        elif lives == 2 and home_page: lives_rect = lives2.get_rect(center=(288, 985)); game_window.blit(lives2, lives_rect)
        elif lives == 1 and home_page: lives_rect = lives1.get_rect(center=(288, 985)); game_window.blit(lives1, lives_rect)
        elif lives == 0 and home_page: lives_rect = lives0.get_rect(center=(288, 985)); game_window.blit(lives0, lives_rect)

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
            if x > 20: x -= 4
        else:
            if x > 20: x -= 8

    if keys[py.K_d]:
        # move right
        if keys[py.K_LSHIFT]: 
            if x < 556: x += 4
        else:
            if x < 556: x += 8

    if keys[py.K_s]:
        # move down
        if keys[py.K_LSHIFT]: 
            if y < 1004: y += 4
        else:
            if y < 1004: y += 8

    if keys[py.K_w]:
        # move up
        if keys[py.K_LSHIFT]: 
            if y > 20: y -= 4
        else:
            if y > 20: y -= 8

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
            reset_arrays()
            
            in_battle = True
            if   difficulty_num == 1: file = open("easy.txt");   info = file.readlines(); enemies()
            elif difficulty_num == 2: file = open("normal.txt"); info = file.readlines(); enemies()
            elif difficulty_num == 3: file = open("hard.txt");   info = file.readlines(); enemies()
            elif difficulty_num == 4: file = open("insane.txt"); info = file.readlines(); enemies()

        elif not home_page and menu_number == 2: home_page = True; menu_number = 1

        elif home_page and menu_number == 3: play_game = False; in_battle = False; e["shutdown"] = True 

        py.time.delay(250)

    for event in events:
        # close program
        if event.type == py.QUIT: play_game = False; in_battle = False; e["shutdown"] = True 

    py.display.update()

    py.time.delay(10)
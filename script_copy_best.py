# imports
import math
import pygame as py
from sys import exit
import os
import random
py.init()
# this could easily surpass 10k lines of code if I have different enemy patterns for each difficulty

# notes
# make sure win and lose screens work properly
# add in bg animations


# this makes sure the window is scaled correctly when it is displayed.
if os.name == "nt":
    try:
        import ctypes
        
        awareness  = ctypes.c_int()
        error_Code = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        error_Code = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        success    = ctypes.windll.user32.SetProcessDPIAware()
    except:pass 


# dict stuff
dict = {}
dict['animations'] = {}
dict['bg data'] = {}
dict['bullet data'] = {}
dict['deaths'] = {}
dict['enemy data'] = {}
dict['game data'] = {}
dict['items'] = {}
dict['loops'] = {}
dict['player data'] = {}
dict['sprites'] = {}

dict['sprites']['bgs'] = {}
dict['sprites']['death'] = {}
dict['sprites']['enemies'] = {}
dict['sprites']['energy'] = {}
dict['sprites']['lives'] = {}
dict['sprites']['map'] = {}
dict['sprites']['menu'] = {}
dict['sprites']['player'] = {}
dict['sprites']['stage clear'] = {}

# important stuff
dict['loops']['in battle']      = False
dict['loops']['play game']      = True
dict['player data']['live num'] = 3
dict['game data']['difficulty num'] = 1
dict['animations']['last bg time'] = 0
dict['animations']['bg num'] = 0
events         = py.event.get()
keys           = py.key.get_pressed()

# turn off stuff
dict['game data']['disable player death'] = False
dict['game data']['draw hitboxes'] = True

# menu stuff
menu_number = 1
dict['loops']['home page'] = True

# GUI dimensions
WIDTH  = 576
HEIGHT = 1024

# player starting location
dict['player data']['x'] = 512
dict['player data']['y'] = 512

# set up window
game_window = py.display.set_mode((WIDTH, HEIGHT))
game_window.fill((0, 0, 0))



# temporary information
def reset_arrays():

    # death animation stuff
    dict['deaths']['death']  = False
    dict['deaths']['x'] = []
    dict['deaths']['y'] = []
    dict['deaths']['player death'] = False
    dict['animations']['deaths'] = []

    # item stuff
    dict['items']['item'] = False
    dict['items']['total'] = 0
    dict['items']['x'] = []
    dict['items']['y'] = []
    dict['animations']['items'] = []
    dict['animations']['item last time'] = []

    # important stuff
    dict['player data']['enemies killed'] = 0
    dict['enemy data']['total enemies']  = 0
    dict['enemy data']['enemy count'] = 5

    # bullet stuff
    dict['bullet data']['bullet delay'] = 500
    dict['bullet data']['bullet damage'] = 1
    dict['bullet data']['bullet speed'] = 16
    dict['bullet data']['bullet piercing'] = False
# the function is run once to make sure that the variables exist
reset_arrays()

# use a variable to go through the directory

dir = 'C:/Users/aob/Documents/Coding Stuff/school stuff/grade 10/python stuff/Computer Culminating/Pixel-Nebula/'
dir = os.path.dirname(os.path.realpath(__file__))
dir = dir.replace('\\', '/')

# menu sprites
dict['sprites']['menu']['bg']               = py.image.load(dir + "assets/HUD/Pixel Nebula Title HUD.png").convert_alpha()
dict['sprites']['menu']['normal diff']      = py.image.load(dir + "assets/HUD/normal difficulty.png").convert_alpha()
dict['sprites']['menu']['endless diff']     = py.image.load(dir + "assets/HUD/endless difficulty.png").convert_alpha()
dict['sprites']['menu']['button highlight'] = py.image.load(dir + "assets/HUD/Pixel Nebula Menu Choice.png").convert_alpha()
dict['sprites']['menu']['buttons']          = py.image.load(dir + "assets/HUD/Pixel Nebula Menu Buttons.png").convert_alpha()

# bg 0
bg00           = py.image.load(dir + "assets/backgrounds/backgrounds/background 0/frame 0.png").convert_alpha()
bg0            = [bg00]

# bg 1
bg10           = py.image.load(dir + "assets/backgrounds/backgrounds/background 1/frame 0.png").convert_alpha()
bg11           = py.image.load(dir + "assets/backgrounds/backgrounds/background 1/frame 1.png").convert_alpha()
bg1            = [bg10, bg11]

# bg 2
bg20           = py.image.load(dir + "assets/backgrounds/backgrounds/background 2/frame 0.png").convert_alpha()
bg21           = py.image.load(dir + "assets/backgrounds/backgrounds/background 2/frame 1.png").convert_alpha()
bg22           = py.image.load(dir + "assets/backgrounds/backgrounds/background 2/frame 2.png").convert_alpha()
bg23           = py.image.load(dir + "assets/backgrounds/backgrounds/background 2/frame 3.png").convert_alpha()
bg2            = [bg20, bg21, bg22, bg23]

# bg 3
bg30           = py.image.load(dir + "assets/backgrounds/backgrounds/background 3/frame 0.png").convert_alpha()
bg31           = py.image.load(dir + "assets/backgrounds/backgrounds/background 3/frame 1.png").convert_alpha()
bg32           = py.image.load(dir + "assets/backgrounds/backgrounds/background 3/frame 2.png").convert_alpha()
bg33           = py.image.load(dir + "assets/backgrounds/backgrounds/background 3/frame 3.png").convert_alpha()
bg34           = py.image.load(dir + "assets/backgrounds/backgrounds/background 3/frame 3.png").convert_alpha()
bg3            = [bg30, bg31, bg32, bg33, bg34]

# bg 4
bg40           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 0.png").convert_alpha()
bg41           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 1.png").convert_alpha()
bg42           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 2.png").convert_alpha()
bg43           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 3.png").convert_alpha()
bg44           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 4.png").convert_alpha()
bg45           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 5.png").convert_alpha()
bg46           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 6.png").convert_alpha()
bg47           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 7.png").convert_alpha()
bg48           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 8.png").convert_alpha()
bg49           = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/frame 9.png").convert_alpha()
bg4            = [bg40, bg41, bg42, bg43, bg44, bg45, bg46, bg47, bg48, bg49]

# bg 5
bg50           = py.image.load(dir + "assets/backgrounds/backgrounds/background 5/frame 0.png").convert_alpha()
bg5            = [bg50]

# bg 6
bg60           = py.image.load(dir + "assets/backgrounds/backgrounds/background 6/frame 0.png").convert_alpha()
bg6            = [bg60]

# # bg 7
bg70           = py.image.load(dir + "assets/backgrounds/backgrounds/background 7/frame 0.png").convert_alpha()
bg71           = py.image.load(dir + "assets/backgrounds/backgrounds/background 7/frame 1.png").convert_alpha()
bg72           = py.image.load(dir + "assets/backgrounds/backgrounds/background 7/frame 2.png").convert_alpha()
bg73           = py.image.load(dir + "assets/backgrounds/backgrounds/background 7/frame 3.png").convert_alpha()
bg7            = [bg70, bg71, bg72, bg73]


# bg backs
bg0_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 0/background.png").convert_alpha()
bg1_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 1/background.png").convert_alpha()
bg2_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 2/background.png").convert_alpha()
bg3_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 3/background.png").convert_alpha()
bg4_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 4/background.png").convert_alpha()
bg5_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 5/background.png").convert_alpha()
bg6_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 6/background.png").convert_alpha()
bg7_back       = py.image.load(dir + "assets/backgrounds/backgrounds/background 7/background.png").convert_alpha()

# lives
lives0         = py.image.load(dir + "assets/HUD/lives 0.png").convert_alpha()
lives1         = py.image.load(dir + "assets/HUD/lives 1.png").convert_alpha()
lives2         = py.image.load(dir + "assets/HUD/lives 2.png").convert_alpha()
lives3         = py.image.load(dir + "assets/HUD/lives 3.png").convert_alpha()

# player
player0        = py.image.load(dir + "assets/ships/ship 1.png").convert_alpha()
player1        = py.image.load(dir + "assets/ships/ship 2.png").convert_alpha()
player2        = py.image.load(dir + "assets/ships/ship 3.png").convert_alpha()
player3        = py.image.load(dir + "assets/ships/ship 4.png").convert_alpha()

# player moves left
player0_left   = py.image.load(dir + "assets/ships/ship 1 l.png").convert_alpha()
player1_left   = py.image.load(dir + "assets/ships/ship 2 l.png").convert_alpha()
player2_left   = py.image.load(dir + "assets/ships/ship 3 l.png").convert_alpha()
player3_left   = py.image.load(dir + "assets/ships/ship 4 l.png").convert_alpha()

# player moves right
player0_right  = py.image.load(dir + "assets/ships/ship 1 r.png").convert_alpha()
player1_right  = py.image.load(dir + "assets/ships/ship 2 r.png").convert_alpha()
player2_right  = py.image.load(dir + "assets/ships/ship 3 r.png").convert_alpha()
player3_right  = py.image.load(dir + "assets/ships/ship 4 r.png").convert_alpha()

# level win animations
stage_clear0   = py.image.load(dir + "assets/ships/level clear 1.png").convert_alpha()
stage_clear1   = py.image.load(dir + "assets/ships/level clear 2.png").convert_alpha()
stage_clear2   = py.image.load(dir + "assets/ships/level clear 3.png").convert_alpha()
stage_clear3   = py.image.load(dir + "assets/ships/level clear 4.png").convert_alpha()
stage_clear4   = py.image.load(dir + "assets/ships/level clear 5.png").convert_alpha()
stage_clear5   = py.image.load(dir + "assets/ships/level clear 6.png").convert_alpha()
stage_clear6   = py.image.load(dir + "assets/ships/level clear 7.png").convert_alpha()
stage_clear7   = py.image.load(dir + "assets/ships/level clear 8.png").convert_alpha()
stage_clear8   = py.image.load(dir + "assets/ships/level clear 9.png").convert_alpha()
stage_clear9   = py.image.load(dir + "assets/ships/level clear 10.png").convert_alpha()
stage_clear10  = py.image.load(dir + "assets/ships/level clear 11.png").convert_alpha()
stage_clear11  = py.image.load(dir + "assets/ships/level clear 12.png").convert_alpha()

# player bullets
player_bullet0 = py.image.load(dir + "assets/bullets/bullet 1.png").convert_alpha()
player_bullet1 = py.image.load(dir + "assets/bullets/bullet 2.png").convert_alpha()
player_bullet2 = py.image.load(dir + "assets/bullets/bullet 3.png").convert_alpha()
player_bullet3 = py.image.load(dir + "assets/bullets/bullet 4.png").convert_alpha()

# enemy 0 bullets
enemy0_bullet0 = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/bullet 1.png").convert_alpha()
enemy0_bullet1 = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/bullet 2.png").convert_alpha()
enemy0_bullet2 = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/bullet 3.png").convert_alpha()
enemy0_bullet3 = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/bullet 4.png").convert_alpha()
enemy0_bullets = [enemy0_bullet0, enemy0_bullet1, enemy0_bullet2, enemy0_bullet3]

# enemy 0 sprites
enemy0_frame0  = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/enemy 1.png").convert_alpha()
enemy0_frame1  = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/enemy 2.png").convert_alpha()
enemy0_frame2  = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/enemy 3.png").convert_alpha()
enemy0_frame3  = py.image.load(dir + "assets/enemies/enemies 1/enemy 1/enemy 4.png").convert_alpha()
enemy0_frames  = [enemy0_frame0, enemy0_frame1, enemy0_frame2, enemy0_frame3]

# enemy 1 bullets
enemy1_bullet0 = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/bullet 1.png").convert_alpha()
enemy1_bullet1 = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/bullet 2.png").convert_alpha()
enemy1_bullet2 = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/bullet 3.png").convert_alpha()
enemy1_bullet3 = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/bullet 4.png").convert_alpha()
enemy1_bullets = [enemy1_bullet0, enemy1_bullet1, enemy1_bullet2, enemy1_bullet3]

# enemy 1 sprites
enemy1_frame0  = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/enemy 1.png").convert_alpha()
enemy1_frame1  = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/enemy 2.png").convert_alpha()
enemy1_frame2  = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/enemy 3.png").convert_alpha()
enemy1_frame3  = py.image.load(dir + "assets/enemies/enemies 1/enemy 2/enemy 4.png").convert_alpha()
enemy1_frames  = [enemy1_frame0, enemy1_frame1, enemy1_frame2, enemy1_frame3]

# enemy 2 bullets
enemy2_bullet0 = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/bullet 1.png").convert_alpha()
enemy2_bullet1 = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/bullet 2.png").convert_alpha()
enemy2_bullet2 = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/bullet 3.png").convert_alpha()
enemy2_bullet3 = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/bullet 4.png").convert_alpha()
enemy2_bullets = [enemy2_bullet0, enemy2_bullet1, enemy2_bullet2, enemy2_bullet3]

# enemy 2 sprites
enemy2_frame0  = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/enemy 1.png").convert_alpha()
enemy2_frame1  = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/enemy 2.png").convert_alpha()
enemy2_frame2  = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/enemy 3.png").convert_alpha()
enemy2_frame3  = py.image.load(dir + "assets/enemies/enemies 1/enemy 3/enemy 4.png").convert_alpha()
enemy2_frames  = [enemy2_frame0, enemy2_frame1, enemy2_frame2, enemy2_frame3]

# enemy 3 bullets
enemy3_bullet0 = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/bullet 1.png").convert_alpha()
enemy3_bullet1 = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/bullet 2.png").convert_alpha()
enemy3_bullet2 = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/bullet 3.png").convert_alpha()
enemy3_bullet3 = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/bullet 4.png").convert_alpha()
enemy3_bullets = [enemy3_bullet0, enemy3_bullet1, enemy3_bullet2, enemy3_bullet3]

# enemy 3 sprites
enemy3_frame0  = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/enemy 1.png").convert_alpha()
enemy3_frame1  = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/enemy 2.png").convert_alpha()
enemy3_frame2  = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/enemy 3.png").convert_alpha()
enemy3_frame3  = py.image.load(dir + "assets/enemies/enemies 1/enemy 4/enemy 4.png").convert_alpha()
enemy3_frames  = [enemy3_frame0, enemy3_frame1, enemy3_frame2, enemy3_frame3]

# enemy 4 bullets
enemy4_bullet0 = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/bullet 1.png").convert_alpha()
enemy4_bullet1 = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/bullet 2.png").convert_alpha()
enemy4_bullet2 = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/bullet 3.png").convert_alpha()
enemy4_bullet3 = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/bullet 4.png").convert_alpha()
enemy4_bullets = [enemy4_bullet0, enemy4_bullet1, enemy4_bullet2, enemy4_bullet3]

# enemy 4 sprites
enemy4_frame0  = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/enemy 1.png").convert_alpha()
enemy4_frame1  = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/enemy 2.png").convert_alpha()
enemy4_frame2  = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/enemy 3.png").convert_alpha()
enemy4_frame3  = py.image.load(dir + "assets/enemies/enemies 1/enemy 5/enemy 4.png").convert_alpha()
enemy4_frames  = [enemy4_frame0, enemy4_frame1, enemy4_frame2, enemy4_frame3]

# death animation frames
death_frame0   = py.image.load(dir + "assets/enemies/death frame 1.png").convert_alpha()
death_frame1   = py.image.load(dir + "assets/enemies/death frame 2.png").convert_alpha()
death_frame2   = py.image.load(dir + "assets/enemies/death frame 3.png").convert_alpha()
death_frame3   = py.image.load(dir + "assets/enemies/death frame 4.png").convert_alpha()
death_frame4   = py.image.load(dir + "assets/enemies/death frame 5.png").convert_alpha()
death_frame5   = py.image.load(dir + "assets/enemies/death frame 6.png").convert_alpha()
death_frame6   = py.image.load(dir + "assets/enemies/death frame 7.png").convert_alpha()
death_frame7   = py.image.load(dir + "assets/enemies/death frame 8.png").convert_alpha()

# power orb sprites
energy0        = py.image.load(dir + "assets/items/energy/energy 1.png").convert_alpha()
energy1        = py.image.load(dir + "assets/items/energy/energy 2.png").convert_alpha()
energy2        = py.image.load(dir + "assets/items/energy/energy 3.png").convert_alpha()
energy3        = py.image.load(dir + "assets/items/energy/energy 4.png").convert_alpha()
energy4        = py.image.load(dir + "assets/items/energy/energy 5.png").convert_alpha()
energy5        = py.image.load(dir + "assets/items/energy/energy 6.png").convert_alpha()

# map levels
map_level0     = py.image.load(dir + "assets/HUD/map level/map level 0.png").convert_alpha()
map_level1     = py.image.load(dir + "assets/HUD/map level/map level 1.png").convert_alpha()
map_level2     = py.image.load(dir + "assets/HUD/map level/map level 2.png").convert_alpha()
map_level3     = py.image.load(dir + "assets/HUD/map level/map level 3.png").convert_alpha()
map_level4     = py.image.load(dir + "assets/HUD/map level/map level 4.png").convert_alpha()
map_level5     = py.image.load(dir + "assets/HUD/map level/map level 5.png").convert_alpha()
map_level6     = py.image.load(dir + "assets/HUD/map level/map level 6.png").convert_alpha()
map_level7     = py.image.load(dir + "assets/HUD/map level/map level 7.png").convert_alpha()
map_level8     = py.image.load(dir + "assets/HUD/map level/map level 8.png").convert_alpha()
map_level9     = py.image.load(dir + "assets/HUD/map level/map level 9.png").convert_alpha()
map_level10    = py.image.load(dir + "assets/HUD/map level/map level 10.png").convert_alpha()
map_level11    = py.image.load(dir + "assets/HUD/map level/map level 11.png").convert_alpha()
map_level12    = py.image.load(dir + "assets/HUD/map level/map level 12.png").convert_alpha()
map_level13    = py.image.load(dir + "assets/HUD/map level/map level 13.png").convert_alpha()
map_level14    = py.image.load(dir + "assets/HUD/map level/map level 14.png").convert_alpha()
map_level15    = py.image.load(dir + "assets/HUD/map level/map level 15.png").convert_alpha()
map_level16    = py.image.load(dir + "assets/HUD/map level/map level 16.png").convert_alpha()
map_level17    = py.image.load(dir + "assets/HUD/map level/map level 17.png").convert_alpha()
map_level18    = py.image.load(dir + "assets/HUD/map level/map level 18.png").convert_alpha()
map_level19    = py.image.load(dir + "assets/HUD/map level/map level 19.png").convert_alpha()
map_level20    = py.image.load(dir + "assets/HUD/map level/map level 20.png").convert_alpha()
map_level21    = py.image.load(dir + "assets/HUD/map level/map level 21.png").convert_alpha()
map_level22    = py.image.load(dir + "assets/HUD/map level/map level 22.png").convert_alpha()
map_level23    = py.image.load(dir + "assets/HUD/map level/map level 23.png").convert_alpha()
map_level24    = py.image.load(dir + "assets/HUD/map level/map level 24.png").convert_alpha()
map_level25    = py.image.load(dir + "assets/HUD/map level/map level 25.png").convert_alpha()
map_level26    = py.image.load(dir + "assets/HUD/map level/map level 26.png").convert_alpha()
map_level27    = py.image.load(dir + "assets/HUD/map level/map level 27.png").convert_alpha()
map_level28    = py.image.load(dir + "assets/HUD/map level/map level 28.png").convert_alpha()
map_level29    = py.image.load(dir + "assets/HUD/map level/map level 29.png").convert_alpha()
map_level30    = py.image.load(dir + "assets/HUD/map level/map level 30.png").convert_alpha()
map_level31    = py.image.load(dir + "assets/HUD/map level/map level 31.png").convert_alpha()
map_level32    = py.image.load(dir + "assets/HUD/map level/map level 32.png").convert_alpha()
map_level33    = py.image.load(dir + "assets/HUD/map level/map level 33.png").convert_alpha()
map_level34    = py.image.load(dir + "assets/HUD/map level/map level 34.png").convert_alpha()
map_bg         = py.image.load(dir + "assets/HUD/map background.png").convert_alpha()
map_buttons    = py.image.load(dir + "assets/HUD/Pixel Nebula Map Buttons.png").convert_alpha()



# sprite dict arrays
dict['sprites']['bgs']['front']      = [bg0, bg1, bg2, bg3, bg4, bg5, bg6, bg7]
dict['sprites']['bgs']['backs']      = [bg0_back, bg1_back, bg2_back, bg3_back, bg4_back, bg5_back, bg6_back, bg7_back]
dict['sprites']['lives']             = [lives0, lives1, lives2, lives3]
dict['sprites']['player']['f']       = [player0, player1, player2, player3]
dict['sprites']['player']['l']       = [player0_left, player1_left, player2_left, player3_left]
dict['sprites']['player']['r']       = [player0_right, player1_right, player2_right, player3_right]
dict['sprites']['stage clear']       = [stage_clear0, stage_clear1, stage_clear2, stage_clear3,  stage_clear4, stage_clear5, 
                                        stage_clear6, stage_clear7, stage_clear8, stage_clear9, stage_clear10, stage_clear11]
dict['sprites']['player']['bullets'] = [player_bullet0, player_bullet1, player_bullet2, player_bullet3]
dict['sprites']['enemies']['b']      = [enemy0_bullets, enemy1_bullets, enemy2_bullets, enemy3_bullets, enemy4_bullets]
dict['sprites']['enemies']['f']      = [enemy0_frames, enemy1_frames, enemy2_frames, enemy3_frames, enemy4_frames]
dict['sprites']['death']             = [death_frame0, death_frame1, death_frame2, death_frame3, death_frame4, death_frame5, death_frame6, death_frame7]
dict['sprites']['energy']            = [energy0, energy1, energy2, energy3, energy4, energy5]
dict['sprites']['map']               = [map_level0,  map_level5, map_level11, map_level15,map_level19, map_level24, map_level29, map_level34]



# variables for the stage and wave being displayed
dict['game data']['wave num']  = 0
dict['game data']['stage num'] = 0

# load delay between each wave for each stage
stage0_wave_lengths = [30, 30, 30, 30]
stage1_wave_lengths = [20, 20, 20, 20]
stage2_wave_lengths = [25, 25, 25, 25, 25]
stage3_wave_lengths = [20, 20, 20, 20, 20]
stage4_wave_lengths = [25, 25, 25, 25, 25, 25]
stage5_wave_lengths = [20, 20, 20, 20, 20, 20]
stage6_wave_lengths = [15, 15, 15, 20, 15, 15, 18]
stage7_wave_lengths = [15, 15, 15, 15, 15, 15, 15]
dict['game data']['stage wave lengths'] = [stage0_wave_lengths, stage1_wave_lengths, stage2_wave_lengths, stage3_wave_lengths, 
                                            stage4_wave_lengths, stage5_wave_lengths, stage6_wave_lengths, stage7_wave_lengths]

# load enemy data for each stage
stages = [
    # stage 0
    [
        {
                "x"             :[350,   100,   200,   500,   300,   150,   450,   288,   144,   432],
                "y"             :[-250,  -500,  -750,  -1000, -1250, -1500, -1750, -2000, -1500, -1500],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     4,     4,     4,     4,     4,     4,     3,     3],
                "bullet_y_speed":[16,    16,    16,    16,    16,    16,    16,    16,    24,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,  3000,  3000],
                "enemy_type"    :[0,     0,     0,     0,     0,     0,     0,     0,     1,     1],
        },
        {
                "x"             :[100,   400,   300,   200,   150,   350,   450,   300,   150,   450,   200],
                "y"             :[-250,  -250,  -750,  -750,  -1250, -1500, -1500, -2000, -1250, -2250, -2500],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     3,     4,     3,     4,     4,     3,     4,     3,     4,     4],
                "bullet_y_speed":[16,    24,    16,    24,    16,    16,    24,    16,    24,    16,    16],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[2000,  3000,  2000,  3000,  2000,  2000,  3000,  2000,  3000,  2000,  2000],
                "enemy_type"    :[0,     1,     0,     1,     0,     0,     1,     0,     1,     0,     0],
        },
        {
                "x"             :[400,   200,   300,   150,   500,   250,   400,   100,   350,   500,   200,   150],
                "y"             :[-250,  -500,  -500,  -1000, -1250, -1250, -1750, -2000, -1500, -1750, -2250, -2000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[3,     4,     3,     3,     4,     3,     4,     4,     3,     3,     4,     3],
                "bullet_y_speed":[24,    16,    24,    24,    16,    24,    16,    16,    24,    24,    16,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[3000,  2000,  3000,  3000,  2000,  3000,  2000,  2000,  3000,  3000,  2000,  3000],
                "enemy_type"    :[1,     0,     1,     1,     0,     1,     0,     0,     1,     1,     0,     1],
        },
        {
                "x"             :[200,   500,   300,   150,   400,   250,   100,   300,   150,   500,   350,   100,   200],
                "y"             :[-250,  -500,  -500,  -1000, -1250, -1250, -1750, -2000, -1500, -1750, -2250, -2000, -2250],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[3,     4,     3,     3,     4,     3,     4,     4,     3,     3,     4,     3,     3],
                "bullet_y_speed":[24,    16,    24,    24,    16,    24,    16,    16,    24,    24,    16,    24,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[3000,  2000,  3000,  3000,  2000,  3000,  2000,  2000,  3000,  3000,  2000,  3000,  3000],
                "enemy_type"    :[1,     0,     1,     1,     0,     1,     0,     0,     1,     1,     0,     1,     1],
        },
        {
                "x"             :[288,   144,   432,   360,   216,   72,    504,   216,   360,    288,   144,   432,   288,   288],
                "y"             :[-250,  -250,  -250,  -250,  -250,  -750,  -750,  -750,  -750,  -750,  -750,  -750,  -1000, -750],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     4,     3,     3,     4,     4,     4,     4,     3,     3,     3,     3,     2],
                "bullet_y_speed":[16,    16,    16,    24,    24,    16,    16,    16,    16,    24,    24,    24,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     32],
                "bullet_delay"  :[2000,  2000,  2000,  3000,  3000,  2000,  2000,  2000,  2000,  3000,  3000,  3000,  3000,  2500],
                "enemy_type"    :[0,     0,     0,     1,     1,     0,     0,     0,     0,     1,     1,     1,     1,     2],
        },
    ],

    # stage 1
    [
        {
                "x"             :[350,   100,   200,   500,   300,   150,   450,   288,   144,   432],
                "y"             :[-250,  -500,  -750,  -1000, -1250, -1500, -1750, -2000, -1500, -1500],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     5,     5,     5,     5,     5,     5,     4,     4],
                "bullet_y_speed":[24,    24,    24,    24,    24,    24,    24,    24,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[1500,  1500,  1500,  1500,  1500,  1500,  1500,  1500,  2500,  2500],
                "enemy_type"    :[0,     0,     0,     0,     0,     0,     0,     0,     1,     1],
        },
        {
                "x"             :[100,   400,   300,   200,   150,   350,   450,   300,   150,   450,   200],
                "y"             :[-250,  -250,  -750,  -750,  -1250, -1500, -1500, -2000, -1250, -2250, -2500],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     4,     5,     4,     5,     5,     4,     5,     4,     5,     5],
                "bullet_y_speed":[24,    32,    24,    32,    24,    32,    24,    24,    32,    24,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[1500,  2500,  1500,  2500,  1500,  1500,  2500,  1500,  2500,  1500,  1500],
                "enemy_type"    :[0,     1,     0,     1,     0,     0,     1,     0,     1,     0,     0],
        },
        {
                "x"             :[400,   200,   300,   150,   500,   250,   400,   100,   350,   500,   200,   150],
                "y"             :[-250,  -500,  -500,  -1000, -1250, -1250, -1750, -2000, -1500, -1750, -2250, -2000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     5,     4,     4,     5,     4,     5,     5,     4,     4,     5,     4],
                "bullet_y_speed":[32,    24,    32,    32,    24,    32,    24,    24,    32,    32,    24,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[2500,  1500,  2500,  2500,  1500,  2500,  1500,  1500,  2500,  2500,  1500,  2500],
                "enemy_type"    :[1,     0,     1,     1,     0,     1,     0,     0,     1,     1,     0,     1],
        },
        {
                "x"             :[200,   500,   300,   150,   400,   250,   100,   300,   150,   500,   350,   100,   200],
                "y"             :[-250,  -500,  -500,  -1000, -1250, -1250, -1750, -2000, -1500, -1750, -2250, -2000, -2250],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     5,     4,     4,     5,     4,     5,     5,     4,     4,     5,     4,     4],
                "bullet_y_speed":[32,    24,    32,    32,    24,    32,    24,    24,    32,    32,    24,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "bullet_delay"  :[2500,  1500,  2500,  2500,  1500,  2500,  1500,  1500,  2500,  2500,  1500,  2500,  2500],
                "enemy_type"    :[1,     0,     1,     1,     0,     1,     0,     0,     1,     1,     0,     1,     1],
        },
        {
                "x"             :[288,   144,   432,   360,   216,   72,    504,   216,   360,    288,   144,  432,   288,   288],
                "y"             :[-250,  -250,  -250,  -250,  -250,  -750,  -750,  -750,  -750,  -750,  -750,  -750,  -1000, -750],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     5,     4,     4,     5,     5,     5,     5,     4,     4,     4,     4,     3],
                "bullet_y_speed":[24,    24,    24,    32,    32,    24,    24,    24,    24,    32,    32,    32,    48,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     48],
                "bullet_delay"  :[1500,  1500,  1500,  2500,  2500,  1500,  1500,  1500,  1500,  2500,  2500,  2500,  2500,  2000],
                "enemy_type"    :[0,     0,     0,     1,     1,     0,     0,     0,     0,     1,     1,     1,     1,     2],
        },
    ],

    # stage 2
    [
        {
                "x"             :[144,   432,   288,   500,   150,   450,   300,   400,   200,   288],
                "y"             :[-250,  -250,  -250,  -500,  -750,  -1000, -1250, -1000, -750, -750],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     3,     4,     4,     4,     4,     3,     3,     2],
                "bullet_y_speed":[16,    16,    24,    16,    16,    16,    16,    24,    24,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     32],
                "bullet_delay"  :[2000,  2000,  3000,  2000,  2000,  2000,  2000,  3000,  3000,  2500],
                "enemy_type"    :[0,     0,     1,     0,     0,     0,     0,     1,     1,     2],
        },
        {
                "x"             :[72,    216,   360,   504,   150,   250,   450,   216,   360,   350,   100],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -750, -500,   -500,  -500, -1000, -750],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     4,     4,     4,     4,     3,     2,     2,     4,     3],
                "bullet_y_speed":[16,    16,    16,    16,    16,    16,    24,    32,    32,    16,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    32,    0,     0],
                "bullet_delay"  :[2000,  2000,  2000,  3000,  2000,  2000,  3000,  2500,  2500,  2000,  3000],
                "enemy_type"    :[0,     0,     0,     0,     0,     0,     1,     2,     2,     0,     1],
        },
        {
                "x"             :[72,    288,   504,   150,   500,   250,   400,   100,   350,   500,   200,   150],
                "y"             :[-250,  -250,  -250,  -500,  -750,  -750,  -1000, -750, -1000,  -1250, -1500, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[3,     3,     3,     4,     4,     3,     4,     2,     3,     3,     4,     2],
                "bullet_y_speed":[24,    24,    24,    16,    16,    24,    16,    32,    24,    24,    16,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    0,     0,     0,     32],
                "bullet_delay"  :[3000,  3000,  3000,  2000,  2000,  3000,  2000,  2500,  3000,  3000,  2000,  2500],
                "enemy_type"    :[1,     1,     1,     0,     0,     1,     0,     2,     1,     1,     0,     2],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750,  -1000, -1000, -1250],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     3,     3,     4,     3,     4,     2,     3,     2,     4,     3,     3],
                "bullet_y_speed":[16,    16,    24,    24,    16,    24,    16,    32,    24,    32,    16,    24,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    0,     32,    0,     0,     0],
                "bullet_delay"  :[2000,  2000,  3000,  3000,  2000,  3000,  2000,  2500,  3000,  2500,  2000,  3000,  3000],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200,   288],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750,  -1000, -1000, -1250, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[3,     3,     4,     4,     4,     3,     4,     2,     3,     2,     4,     3,     3,     2],
                "bullet_y_speed":[24,    24,    16,    16,    16,    24,    16,    32,    24,    32,    16,    24,    24,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    0,     32,    0,     0,     0,     32],
                "bullet_delay"  :[3000,  3000,  2000,  2000,  2000,  3000,  2000,  2500,  3000,  2500,  2000,  3000,  3000,  2500],
                "enemy_type"    :[1,     1,     0,     0,     0,     1,     0,     2,     1,     2,     0,     1,     1,     2],
        },
        {
                "x"             :[776,   -200,  216,   360,   144,   432,   288,   432,   144,   72,    504,   432,   144,   360,   216],
                "y"             :[300,   300,   -250,  -250,  -250,  -250,  -875,  -750,  -750,  -750,  -750,  -750,  -750,  -750,  -750],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     2,     2,     3,     3,     2,     4,     4,     4,     4,     3,     3,     2,     2],
                "bullet_y_speed":[8,     8,     32,    32,    24,    24,    48,    16,    16,    16,    16,    24,    24,    32,    32],
                "bullet_x_speed":[0,     0,     32,    32,    0,     0,     48,    0,     0,     0,     0,     0,     0,     32,    32],
                "bullet_delay"  :[250,   250,   2500,  2500,  3000,  3000,  2000,  2000,  2000,  2000,  2000,  3000,  3000,  2500,  2500],
                "enemy_type"    :[4,     4,     2,     2,     1,     1,     2,     0,     0,     0,     0,     1,     1,     2,     2],
        },
    ],

    # stage 3
    [
        {
                "x"             :[144,   432,   288,   500,   150,   450,   300,   400,   200,   288],
                "y"             :[-250,  -250,  -250,  -500,  -750,  -1000, -1250, -1000, -750,  -750],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     4,     5,     5,     5,     5,     4,     4,     3],
                "bullet_y_speed":[24,    24,    32,    24,    24,    24,    24,    32,    32,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     48],
                "bullet_delay"  :[1500,  1500,  2500,  1500,  1500,  1500,  1500,  2500,  2500,  2000],
                "enemy_type"    :[0,     0,     1,     0,     0,     0,     0,     1,     1,     2],
        },
        {
                "x"             :[72,    216,   360,   504,   150,   250,   450,   216,   360,   350,   100],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -750, -500,   -500,  -500,  -1000, -750],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     5,     5,     5,     5,     4,     3,     3,     5,     4],
                "bullet_y_speed":[24,    24,    24,    24,    24,    24,    32,    48,    48,    24,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    48,    0,     0],
                "bullet_delay"  :[1500,  1500,  1500,  1500,  1500,  1500,  2500,  2000,  2000,  1500,  2500],
                "enemy_type"    :[0,     0,     0,     0,     0,     0,     1,     2,     2,     0,     1],
        },
        {
                "x"             :[72,    288,   504,   150,   500,   250,   400,   100,   350,   500,   200,   150],
                "y"             :[-250,  -250,  -250,  -500,  -750,  -750,  -1000, -750,  -1000, -1250, -1500, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     4,     5,     5,     4,     5,     3,     4,     4,     5,     3],
                "bullet_y_speed":[32,    32,    32,    24,    24,    32,    24,    48,    32,    32,    24,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    0,     0,     0,     48],
                "bullet_delay"  :[2500,  2500,  2500,  1500,  1500,  2500,  1500,  2000,  2500,  2500,  1500,  2000],
                "enemy_type"    :[1,     1,     1,     0,     0,     1,     0,     2,     1,     1,     0,     2],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750, -1000, -1000, -1250],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     4,     4,     5,     4,     5,     3,     4,     3,     5,     4,     4],
                "bullet_y_speed":[24,    24,    32,    32,    24,    24,    32,    48,    32,    48,    24,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    0,     48,    0,     0,     0],
                "bullet_delay"  :[1500,  1500,  2500,  2500,  1500,  2500,  1500,  2000,  2500,  2000,  1500,  2500,  2500],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1],
        },
       {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200,   288],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750,  -1000, -1000, -1250, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     5,     5,     5,     4,     5,     3,     4,     3,     5,     4,     4,     3],
                "bullet_y_speed":[24,    24,    16,    16,    16,    24,    16,    32,    24,    32,    16,    24,    24,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    0,     32,    0,     0,     0,     48],
                "bullet_delay"  :[2500,  2500,  1500,  1500,  1500,  2500,  1500,  2000,  2500,  2000,  1500,  2500,  2500,  2000],
                "enemy_type"    :[1,     1,     0,     0,     0,     1,     0,     2,     1,     2,     0,     1,     1,     2],
        },
        {
                "x"             :[776,   -200,  216,   360,   144,   432,   288,   432,   144,   72,    504,   432,   144,   360,   216],
                "y"             :[300,   300,   -250,  -250,  -250,  -250,  -875,  -750,  -750,  -750,  -750,  -750,  -750,  -750,  -750],
                "x_speed"       :[-24,   24,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     3,     3,     4,     4,     3,     5,     5,     5,     5,     4,     4,     3,     3],
                "bullet_y_speed":[8,     8,     48,    48,    32,    32,    48,    24,    24,    24,    24,    32,    32,    48,    48],
                "bullet_x_speed":[0,     0,     48,    48,    0,     0,     48,    0,     0,     0,     0,     0,     0,     48,    48],
                "bullet_delay"  :[200,   200,   2000,  2000,  2500,  2500,  1500,  1500,  1500,  1500,  1500,  2500,  2500,  2000,  2000],
                "enemy_type"    :[4,     4,     2,     2,     1,     1,     2,     0,     0,     0,     0,     1,     1,     2,     2],
        },
    ],

    # stage 4
    [
        {
                "x"             :[144,   432,   288,   500,   150,   450,   300,   144,   432,   288],
                "y"             :[-250,  -250,  -250,  -500,  -750,  -1000, -1250, -1250, -1250, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     4,     4,     4,     4,     4,     3,     3,     2],
                "bullet_y_speed":[16,    16,    16,    16,    16,    16,    16,    24,    24,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     32],
                "bullet_delay"  :[2000,  2000,  2000,  2000,  2000,  2000,  2000,  3000,  3000,  2500],
                "enemy_type"    :[0,     0,     0,     0,     0,     0,     0,     1,     1,     2],
        },
        {
                "x"             :[72,    216,   360,   504,   150,   250,   450,   216,   360,   350,   100],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -750,  -750,  -750,  -750,  -1000, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     3,     3,     4,     4,     4,     3,     2,     2,     4,     3],
                "bullet_y_speed":[16,    24,    24,    16,    16,    16,    24,    32,    32,    16,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    32,    0,     0],
                "bullet_delay"  :[2000,  3000,  3000,  2000,  2000,  2000,  3000,  2500,  2500,  2000,  3000],
                "enemy_type"    :[0,     1,     1,     0,     0,     0,     1,     2,     2,     0,     1],
        },
        {
                "x"             :[776,   -200,  288,   150,   500,   250,   400,   100,   350,   500,   200,   150],
                "y"             :[300,   300,   -128,  -500,  -750,  -750,  -1000, -750,  -1000, -1250, -1500, -1000],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     2,     4,     4,     3,     4,     2,     3,     3,     4,     2],
                "bullet_y_speed":[8,     8,     32,    16,    16,    24,    16,    32,    24,    24,    16,    32],
                "bullet_x_speed":[0,     0,     32,    0,     0,     0,     0,     32,    0,     0,     0,     32],
                "bullet_delay"  :[250,   250,   2500,  2000,  2000,  3000,  2000,  2500,  3000,  3000,  2000,  2500],
                "enemy_type"    :[4,     4,     2,     0,     0,     1,     0,     2,     1,     1,     0,     2],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750, -1000, -1000, -1250],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     3,     3,     4,     3,     4,     2,     3,     2,     4,     3,     3],
                "bullet_y_speed":[16,    16,    24,    24,    16,    24,    16,    32,    24,    32,    16,    24,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    0,     32,    0,     0,     0],
                "bullet_delay"  :[2000,  2000,  3000,  3000,  2000,  3000,  2000,  2500,  3000,  2500,  2000,  3000,  3000],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200,  288],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750, -1000, -1000, -1250, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,    0],
                "y_speed"       :[4,     4,     3,     3,     4,     3,     4,     2,     3,     2,     4,     3,     3,    2],
                "bullet_y_speed":[16,    16,    24,    24,    16,    24,    16,    32,    24,    32,    16,    24,    24,   32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    0,     32,    0,     0,     0,    32],
                "bullet_delay"  :[2000,  2000,  3000,  3000,  2000,  3000,  2000,  2500,  3000,  2500,  2000,  3000,  3000, 2500],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1,    2],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200,   216,   360],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750,  -1000, -1000, -1250, -1000, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[4,     4,     3,     3,     4,     3,     4,     2,     3,     2,     4,     3,     3,     2,     2],
                "bullet_y_speed":[16,    16,    24,    24,    16,    24,    16,    32,    24,    32,    16,    24,    24,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    0,     32,    0,     0,     0,     32,    32],
                "bullet_delay"  :[2000,  2000,  3000,  3000,  2000,  3000,  2000,  2500,  3000,  2500,  2000,  3000,  3000,  2500,  2500],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1,     2,     2],
        },
        {
                "x"             :[776,   -200,  288,   144,   432,   360,   216,   72,    504,   288,   144,   432,   72,   504,  216,  360],
                "y"             :[300,   300,   -250,  -250,  -250,  -375,  -375,  -375,  -375,  -375,  -375,  -375,  -750, -750, -500, -500],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     8,    8,    0,    0],
                "y_speed"       :[0,     0,     4,     4,     4,     3,     3,     3,     3,     2,     2,     2,     3,    3,    2,    2],
                "bullet_y_speed":[8,     8,     16,    16,    16,    32,    32,    32,    32,    32,    32,    32,    16,   16,   32,   32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     32,    32,    32,    0,    0,    32,   32],
                "bullet_delay"  :[250,   250,   2000,  2000,  2000,  3000,  3000,  3000,  3000,  2500,  2500,  2500,  1500, 1500, 2500, 2500],
                "enemy_type"    :[4,     4,     0,     0,     0,     1,     1,     1,     1,     2,     2,     2,     3,    3,    2,    2],
        },
    ],

    # stage 5
    [
        {
                "x"             :[144,   432,   288,   500,   150,   450,   300,   144,   432,   288],
                "y"             :[-250,  -250,  -250,  -500,  -750,  -1000, -1250, -1250, -1250, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     5,     5,     5,     5,     5,     4,     4,     3],
                "bullet_y_speed":[24,    24,    24,    24,    24,    24,    24,    32,    32,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     48],
                "bullet_delay"  :[1500,  1500,  1500,  1500,  1500,  1500,  1500,  2500,  2500,  2000],
                "enemy_type"    :[0,     0,     0,     0,     0,     0,     0,     1,     1,     2],
        },
        {
                "x"             :[72,    216,   360,   504,   150,   250,   450,   216,   360,   350,   100],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -750,  -750,  -750,  -750,  -1000, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     4,     4,     5,     5,     5,     4,     3,     3,     5,     4],
                "bullet_y_speed":[24,    32,    32,    24,    24,    24,    32,    48,    48,    24,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    48,    0,     0],
                "bullet_delay"  :[1500,  2500,  2500,  1500,  1500,  1500,  2500,  2000,  2000,  1500,  2500],
                "enemy_type"    :[0,     1,     1,     0,     0,     0,     1,     2,     2,     0,     1],
        },
        {
                "x"             :[776,   -200,  288,   150,   500,   250,   400,   100,   350,   500,   200,   150],
                "y"             :[300,   300,   -128,  -500,  -750,  -750,  -1000, -750,  -1000, -1250, -1500, -1000],
                "x_speed"       :[-42,   42,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     3,     5,     5,     4,     5,     3,     4,     4,     5,     3],
                "bullet_y_speed":[12,    12,    48,    24,    24,    32,    24,    48,    32,    32,    24,    48],
                "bullet_x_speed":[0,     0,     48,    0,     0,     0,     0,     48,    0,     0,     0,     48],
                "bullet_delay"  :[200,   200,   2000,  1500,  1500,  2500,  1500,  2000,  2500,  2500,  1500,  2000],
                "enemy_type"    :[4,     4,     2,     0,     0,     1,     0,     2,     1,     1,     0,     2],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750, -1000, -1000, -1250],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     4,     4,     5,     4,     5,     3,     4,     3,     5,     4,     4],
                "bullet_y_speed":[24,    24,    32,    32,    24,    32,    24,    48,    32,    48,    24,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    0,     48,    0,     0,     0],
                "bullet_delay"  :[1500,  1500,  2500,  2500,  1500,  2500,  1500,  2000,  2500,  2000,  1500,  2500,  2500],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200,   288],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750,  -1000, -1000, -1250, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     4,     4,     5,     4,     5,     3,     4,     3,     5,     4,     4,     3],
                "bullet_y_speed":[24,    24,    32,    32,    24,    32,    24,    48,    32,    48,    24,    32,    32,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    0,     48,    0,     0,     0,     48],
                "bullet_delay"  :[1500,  1500,  2500,  2500,  1500,  2500,  1500,  2000,  2500,  2000,  1500,  2500,  2500,  2000],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1,     2],
        },
        {
                "x"             :[216,   360,   72,    504,   400,   250,   100,   300,   150,   500,   350,   100,   200,   216,   360],
                "y"             :[-250,  -250,  -250,  -250,  -500,  -500,  -750,  -500,  -750,  -750,  -1000, -1000, -1250, -1000, -1000],
                "x_speed"       :[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[5,     5,     4,     4,     5,     4,     5,     3,     4,     3,     5,     4,     4,     3,     3],
                "bullet_y_speed":[24,    24,    32,    32,    24,    32,    24,    48,    32,    48,    24,    32,    32,    48,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    0,     48,    0,     0,     0,     48,    48],
                "bullet_delay"  :[1500,  1500,  2500,  2500,  1500,  2500,  1500,  2000,  2500,  2000,  1500,  2500,  2500,  2000,  2000],
                "enemy_type"    :[0,     0,     1,     1,     0,     1,     0,     2,     1,     2,     0,     1,     1,     2,     2],
        },
        {
                "x"             :[776,   -200,  288,   144,   432,   360,   216,   72,    504,   288,   144,   432,   72,   504,  216,  360],
                "y"             :[300,   300,   -250,  -250,  -250,  -375,  -375,  -375,  -375,  -375,  -375,  -375,  -750, -750, -500, -500],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     12,   -12,  0,    0],
                "y_speed"       :[0,     0,     5,     5,     5,     4,     4,     4,     4,     3,     3,     3,     4,    4,    3,    3],
                "bullet_y_speed":[12,    12,    24,    24,    24,    48,    48,    48,    48,    48,    48,    48,    24,   24,   48,   48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     48,    48,    48,    0,    0,    48,   48],
                "bullet_delay"  :[200,   200,   1500,  1500,  1500,  2500,  2500,  2500,  2500,  2000,  2000,  2000,  1000, 1000, 2000, 2000],
                "enemy_type"    :[4,     4,     0,     0,     0,     1,     1,     1,     1,     2,     2,     2,     3,    3,    2,    2],
        },
    ],

    # stage 6
    [
        {
                "x"             :[776,   -200,  72,    504,   288,   144,   432,   288,   5776,  -5200],
                "y"             :[300,   300,   -250,  -250,  -500,  -375,  -375,  -625,  300,   300],
                "x_speed"       :[-16,   16,    8,     -8,    0,     0,     0,     0,     -16,   16],
                "y_speed"       :[0,     0,     3,     3,     3,     2,     2,     3,     0,     0],
                "bullet_y_speed":[8,     8,     16,    16,    24,    32,    32,    24,    8,     8],
                "bullet_x_speed":[0,     0,     0,     0,     0,     32,    32,    0,     0,     0],
                "bullet_delay"  :[250,   250,   1500,  1500,  2000,  2000,  2000,  3000,  250,   250],
                "enemy_type"    :[4,     4,     3,     3,     1,     2,     2,     1,     4,     4],
        },
        {
                "x"             :[144,   288,   432,   216,   360,   4076,  -3500, 216,   360,   216,   360],
                "y"             :[-125,  -200,  -275,  -250,  -250,  300,   300,   -500,  -500,  -625,  -625],
                "x_speed"       :[12,    12,    12,    0,     0,     -16,   16,    0,     0,     0,     0],
                "y_speed"       :[4,     4,     4,     3,     3,     0,     0,     2,     2,     2,     2],
                "bullet_y_speed":[16,    16,    16,    32,    32,    8,     8,     32,    32,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     32,    32,    32,    32],
                "bullet_delay"  :[1500,  1500,  1500,  3000,  3000,  250,   250,   2500,  2500,  2500,  2500],
                "enemy_type"    :[3,     3,     3,     1,     1,     4,     4,     2,     2,     2,     2],
        },
        {
                "x"             :[776,   -200,  288,   144,   432,   72,    504,   288,   72,    504,   216,   360],
                "y"             :[300,   300,   -250,  -250,  -250,  -250,  -250,  -250,  -500,  -500,  -625,  -625],
                "x_speed"       :[-16,   16,    0,     0,     0,     8,     -8,    0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     2,     2,     2,     3,     3,     4,     2,     2,     3,     3],
                "bullet_y_speed":[8,     8,     32,    32,    32,    16,    16,    32,    32,    32,    32,    32],
                "bullet_x_speed":[0,     0,     32,    32,    32,    0,     0,     0,     32,    32,    0,     0],
                "bullet_delay"  :[250,   250,   2500,  2500,  2500,  1500,  1500,  3000,  2500,  2500,  3000,  3000],
                "enemy_type"    :[4,     4,     2,     2,     2,     3,     3,     1,     2,     2,     1,     1],
        },
        {
                "x"             :[736,   -160,  776,   -200,  72,    216,   360,   504,   144,   288,   432,   216,   360],
                "y"             :[250,   250,   400,   400,   -250,  -250,  -250,  -250,  -750,  -750,  -750,  -500,  -500],
                "x_speed"       :[-16,   16,    -16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     0,     0,     3,     3,     3,     3,     4,     4,     4,     2,     2],
                "bullet_y_speed":[8,     8,     8,     8,     24,    24,    24,    24,    16,    16,    16,    32,    32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     32,    32],
                "bullet_delay"  :[250,   250,   250,   250,   3000,  3000,  3000,  3000,  2000,  2000,  2000,  2500,  2500],
                "enemy_type"    :[4,     4,     4,     4,     1,     1,     1,     1,     0,     0,     0,     2,     2], 
        },
        {
                "x"             :[776,   -200,  72,    504,   144,   288,   432,   72,    144,   288,   432,   504,   72,   504],
                "y"             :[300,   300,   -250,  -250,  -250,  -250,  -250,  -500,  -500,  -500,  -500,  -500,  -750, -750],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     8,    -8],
                "y_speed"       :[0,     0,     4,     4,     2,     2,     2,     3,     3,     3,     3,     3,     4,    4],
                "bullet_y_speed":[8,     8,     16,    16,    32,    32,    32,    24,    24,    24,    24,    24,    16,   16],
                "bullet_x_speed":[0,     0,     0,     0,     32,    32,    32,    0,     0,     0,     0,     0,     0,    0],
                "bullet_delay"  :[250,   250,   250,   250,   2000,  2000,  2000,  3000,  3000,  3000,  3000,  3000,  1500, 1500],
                "enemy_type"    :[4,     4,     0,     0,     2,     2,     2,     1,     1,     1,     1,     1,     3,    3],
        },
        { 
                "x"             :[726,   -150,  776,   -200,  826,   -250,  72,    504,   144,   432,   288,   72,    216,   360,   504],
                "y"             :[200,   200,   400,   400,   600,   600,   -125,  -125,  -250,  -250,  -375,  -500,  -575,  -650,  -725],
                "x_speed"       :[-16,   16,    -16,   16,    -16,   16,    0,     0,     0,     0,     0,     12,    12,    12,    12],
                "y_speed"       :[0,     0,     0,     0,     0,     0,     2,     2,     2,     2,     2,     3,     3,     3,     3],
                "bullet_y_speed":[8,     8,     8,     8,     8,     8,     32,    32,    32,    32,    32,    16,    16,    16,    16],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     32,    32,    32,    32,    32,    0,     0,     0,     0],
                "bullet_delay"  :[250,   250,   250,   250,   250,   250,   2500,  2500,  2500,  2500,  2500,  3000,  1500,  1500,  1500],
                "enemy_type"    :[4,     4,     4,     4,     4,     4,     2,     2,     2,     2,     2,     3,     3,     3,     3],
        },
        {
                "x"             :[776,   -200,  288,   144,   432,   360,   216,   72,    504,   288,   144,   432,   72,   504,  216,  360],
                "y"             :[300,   300,   -250,  -250,  -250,  -375,  -375,  -375,  -375,  -375,  -375,  -375,  -750, -750, -500, -500],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     8,    -8,   0,    0],
                "y_speed"       :[0,     0,     4,     4,     4,     3,     3,     3,     3,     2,     2,     2,     3,    3,    2,    2],
                "bullet_y_speed":[8,     8,     32,    32,    32,    32,    32,    32,    32,    32,    32,    32,    16,   16,   32,   32],
                "bullet_x_speed":[0,     0,     32,    32,    32,    0,     0,     0,     0,     32,    32,    32,    0,    0,    32,   32],
                "bullet_delay"  :[250,   250,   2000,  2000,  2000,  3000,  3000,  3000,  3000,  2500,  2500,  2500,  1500, 1500, 2500, 2500],
                "enemy_type"    :[4,     4,     2,     2,     2,     1,     1,     1,     1,     2,     2,     2,     3,    3,    2,    2],
        },
        {
                "x"             :[736,   -160,  776,   -200,  504,   360,   288,   216,   72,    288,   144,   432,   72,   504,  216,  360,  288],
                "y"             :[250,   250,   400,   400,   -250,  -325,  -400,  -475,  -550,  -375,  -375,  -375,  -750, -750, -500, -500, -500],
                "x_speed"       :[-16,   16,    -16,   16,    8,     8,     8,     8,     8,     0,     0,     0,     0,    0,    0,    0,    0],
                "y_speed"       :[0,     0,     0,     0,     3,     3,     3,     3,     3,     2,     2,     2,     4,    4,    3,    3,    2],
                "bullet_y_speed":[8,     8,     8,     8,     16,    16,    16,    16,    16,    32,    32,    32,    16,   16,   32,   32,   32],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     32,    32,    32,    0,    0,    0,    0,    32],
                "bullet_delay"  :[250,   250,   250,   250,   1500,  1500,  1500,  1500,  1500,  2500,  2500,  2500,  150,  150,  2500, 2500, 100],
                "enemy_type"    :[4,     4,     4,     4,     3,     3,     3,     3,     3,     2,     2,     2,     0,    0,    1,    1,    2],
        },
    ],

    # stage 7
    [ 
        {
                "x"             :[776,   -200,  72,    504,   288,   144,   432,   288,   5776,  -5200],
                "y"             :[300,   300,   -250,  -250,  -500,  -375,  -375,  -625,  300,   300],
                "x_speed"       :[-16,   16,    12,    -12,   0,     0,     0,     0,     -16,   16],
                "y_speed"       :[0,     0,     4,     4,     4,     3,     3,     4,     0,     0],
                "bullet_y_speed":[8,     8,     24,    24,    32,    48,    48,    24,    8,     8],
                "bullet_x_speed":[0,     0,     0,     0,     0,     48,    48,    0,     0,     0],
                "bullet_delay"  :[250,   250,   1000,  1000,  2500,  2000,  2000,  2500,  250,   250],
                "enemy_type"    :[4,     4,     3,     3,     1,     2,     2,     1,     4,     4],
        },
        {
                "x"             :[144,   288,   432,   216,   360,   4076,  -3500, 216,   360,   216,   360],
                "y"             :[-125,  -200,  -275,  -250,  -250,  300,   300,   -500,  -500,  -625,  -625],
                "x_speed"       :[16,    16,    16,    0,     0,     -16,   16,    0,     0,     0,     0],
                "y_speed"       :[5,     5,     5,     4,     4,     0,     0,     3,     3,     3,     3],
                "bullet_y_speed":[24,    24,    24,    48,    48,    8,     8,     48,    48,    48,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     48,    48,    48,    48],
                "bullet_delay"  :[1000,  1000,  1000,  2500,  2500,  250,   250,   2000,  2000,  2000,  2000],
                "enemy_type"    :[3,     3,     3,     1,     1,     4,     4,     2,     2,     2,     2],
        },
        {
                "x"             :[776,   -200,  288,   144,   432,   72,    504,   288,   72,    504,   216,   360],
                "y"             :[300,   300,   -250,  -250,  -250,  -250,  -250,  -250,  -500,  -500,  -625,  -625],
                "x_speed"       :[-16,   16,    0,     0,     0,     8,     -8,    0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     3,     3,     3,     4,     4,     5,     3,     3,     4,     4],
                "bullet_y_speed":[8,     8,     48,    48,    48,    24,    24,    48,    48,    48,    48,    48],
                "bullet_x_speed":[0,     0,     48,    48,    48,    0,     0,     0,     48,    48,    0,     0],
                "bullet_delay"  :[250,   250,   2000,  2000,  2000,  1000,  1500,  2500,  2000,  2000,  2500,  2500],
                "enemy_type"    :[4,     4,     2,     2,     2,     3,     3,     1,     2,     2,     1,     1],
        },
        {
                "x"             :[736,   -160,  776,   -200,  72,    216,   360,   504,   144,   288,   432,   216,   360],
                "y"             :[250,   250,   400,   400,   -250,  -250,  -250,  -250,  -750,  -750,  -750,  -500,  -500],
                "x_speed"       :[-16,   16,    -16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0],
                "y_speed"       :[0,     0,     0,     0,     4,     4,     4,     4,     5,     5,     5,     3,     3],
                "bullet_y_speed":[8,     8,     8,     8,     32,    32,    32,    32,    24,    24,    24,    48,    48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     48,    48],
                "bullet_delay"  :[250,   250,   250,   250,   2500,  2500,  2500,  2500,  1500,  1500,  1500,  2000,  2000],
                "enemy_type"    :[4,     4,     4,     4,     1,     1,     1,     1,     0,     0,     0,     2,     2], 
        },
        {
                "x"             :[776,   -200,  72,    504,   144,   288,   432,   72,    144,   288,   432,   504,   72,   504],
                "y"             :[300,   300,   -250,  -250,  -250,  -250,  -250,  -500,  -500,  -500,  -500,  -500,  -750, -750],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     8,    -8],
                "y_speed"       :[0,     0,     5,     5,     3,     3,     3,     4,     4,     4,     4,     4,     5,    5],
                "bullet_y_speed":[8,     8,     24,    24,    48,    48,    48,    32,    32,    32,    32,    32,    24,   24],
                "bullet_x_speed":[0,     0,     0,     0,     48,    48,    48,    0,     0,     0,     0,     0,     0,    0],
                "bullet_delay"  :[250,   250,   250,   250,   1500,  1500,  1500,  2500,  2500,  2500,  2500,  2500,  1000, 1000],
                "enemy_type"    :[4,     4,     0,     0,     2,     2,     2,     1,     1,     1,     1,     1,     3,    3],
        },
        { 
                "x"             :[726,   -150,  776,   -200,  826,   -250,  72,    504,   144,   432,   288,   72,    216,   360,   504],
                "y"             :[200,   200,   400,   400,   600,   600,   -125,  -125,  -250,  -250,  -375,  -500,  -575,  -650,  -725],
                "x_speed"       :[-16,   16,    -16,   16,    -16,   16,    0,     0,     0,     0,     0,     16,    16,    16,    16],
                "y_speed"       :[0,     0,     0,     0,     0,     0,     3,     3,     3,     3,     3,     4,     4,     4,     4],
                "bullet_y_speed":[8,     8,     8,     8,     8,     8,     48,    48,    48,    48,    48,    24,    24,    24,    24],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     48,    48,    48,    48,    48,    0,     0,     0,     0],
                "bullet_delay"  :[250,   250,   250,   250,   250,   250,   2000,  2000,  2000,  2000,  2000,  1000,  1000,  1000,  1000],
                "enemy_type"    :[4,     4,     4,     4,     4,     4,     2,     2,     2,     2,     2,     3,     3,     3,     3],
        },
        {
                "x"             :[776,   -200,  288,   144,   432,   360,   216,   72,    504,   288,   144,   432,   72,   504,  216,  360],
                "y"             :[300,   300,   -250,  -250,  -250,  -375,  -375,  -375,  -375,  -375,  -375,  -375,  -750, -750, -500, -500],
                "x_speed"       :[-16,   16,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     12,   -12,  0,    0],
                "y_speed"       :[0,     0,     5,     5,     5,     4,     4,     4,     4,     3,     3,     3,     4,    4,    3,    3],
                "bullet_y_speed":[8,     8,     48,    48,    48,    48,    48,    48,    48,    48,    48,    48,    24,   24,   48,   48],
                "bullet_x_speed":[0,     0,     48,    48,    48,    0,     0,     0,     0,     48,    48,    48,    0,    0,    48,   48],
                "bullet_delay"  :[250,   250,   1500,  1500,  1500,  2500,  2500,  2500,  2500,  2000,  2000,  2000,  1000, 1000, 2000, 2000],
                "enemy_type"    :[4,     4,     2,     2,     2,     1,     1,     1,     1,     2,     2,     2,     3,    3,    2,    2],
        },
        {
                "x"             :[736,   -160,  776,   -200,  504,   360,   288,   216,   72,    288,   144,   432,   72,   504,  216,  360,  288],
                "y"             :[250,   250,   400,   400,   -250,  -325,  -400,  -475,  -550,  -375,  -375,  -375,  -750, -750, -500, -500, -500],
                "x_speed"       :[-16,   16,    -16,   16,    16,    16,    16,    16,    16,    0,     0,     0,     0,    0,    0,    0,    0],
                "y_speed"       :[0,     0,     0,     0,     5,     5,     5,     5,     5,     3,     3,     3,     5,    5,    4,    4,    3],
                "bullet_y_speed":[8,     8,     8,     8,     24,    24,    24,    24,    24,    48,    48,    48,    24,   24,   48,   48,   48],
                "bullet_x_speed":[0,     0,     0,     0,     0,     0,     0,     0,     0,     48,    48,    48,    0,    0,    0,    0,    48],
                "bullet_delay"  :[250,   250,   250,   250,   1000,  1000,  1000,  1000,  1000,  2000,  2000,  2000,  100,  100,  2000, 2000, 50],
                "enemy_type"    :[4,     4,     4,     4,     3,     3,     3,     3,     3,     2,     2,     2,     0,    0,    1,    1,    2],
        },
    ],
]



# animate enemy deaths
def death_animation(player_died = False):

    # loop through all places where there should be a death animation
    death_index_num = 0

    for x in dict['deaths']['x']:

        # draw the animation frame
        death_frame = dict['sprites']['death'][dict['animations']['deaths'][death_index_num]]

        death_rect = death_frame.get_rect(center=(x, dict['deaths']['y'][death_index_num]))

        game_window.blit(death_frame, death_rect)



        # remove the animation if it is complete
        if dict['animations']['deaths'][death_index_num] == 7:

            dict['deaths']['x'].pop(death_index_num)

            dict['deaths']['y'].pop(death_index_num)

            dict['animations']['deaths'].pop(death_index_num)


            # change variables to put the user back on the home screen
            if player_died:

                dict['game data']['wave num'] = 0

                dict['loops']['in battle'] = False
                dict['loops']['home page'] = True

                dict['deaths']['player death'] = False



                if not dict['game data']['infinite mode']:

                    dict['player data']['live num'] -= 1

                    if dict['player data']['live num'] == -1:

                        dict['loops']['play game'] = False
                        dict['loops']['in battle'] = False



        # change the animation frame if there is another to be displayed
        else: 
            
            dict['animations']['deaths'][death_index_num] += 1

        # make sure the function doesn't run if there is nothing to draw
        if dict['deaths']['x'] == []: 
            
            dict['deaths']['death'] = False



# function to draw items
def item_animations():
    
    item_index_num = 0

    # loop through every place where there should be an item
    for x in dict['items']['x']:

        # draw the item
        energy    = dict['sprites']['energy'][dict['animations']['items'][item_index_num]]

        item_rect = energy.get_rect(center=(x, dict['items']['y'][item_index_num]))

        game_window.blit(energy, item_rect)



        if dict['game data']['draw hitboxes']:

            py.draw.rect(game_window, (255, 0, 0), item_rect, 2)



        # increase a variable so that the correct frame is drawn the next time
        if dict['animations']['item last time'][item_index_num] + 125 < py.time.get_ticks():

            if dict['animations']['items'][item_index_num] < 5:
            
                dict['animations']['items'][item_index_num] = dict['animations']['items'][item_index_num] + 1

            dict['animations']['item last time'][item_index_num] = py.time.get_ticks()

        # remove the item if it is off the screen
        if x >= 1100:

            dict['items']['x'].pop(item_index_num)

            dict['items']['y'] .pop(item_index_num)

            dict['animations']['items'].pop(item_index_num)

        # move the item down
        dict['items']['y'][item_index_num] += 10



        # make sure the function doesn't run when there is nothing to draw
        if dict['items']['x'] == []: 
            
            dict['items']['item'] = False



        # check if the player is collding with the item
        if item_rect.colliderect(dict['player data']['rect']):

            # make the gun stronger
            dict['items']['total'] += 1

            dict['bullet data']['bullet delay'] -= 6

            dict['bullet data']['bullet damage'] += 1



            if dict['bullet data']['bullet speed'] < 32: 
                
                dict['bullet data']['bullet speed'] += 1



            # remove the item
            dict['items']['x'].pop(item_index_num)

            dict['items']['y'].pop(item_index_num)

            dict['animations']['items'].pop(item_index_num)

        if dict['items']['total'] >= 46: dict['bullet data']['bullet piercing'] = True

        # increase a variable so that the next item can be drawn
        item_index_num += 1



def stage_clear_animation():

    # draw each frame of the stage clear animation
    for frame in dict['sprites']['stage clear']:

        game_window.blit(dict['bg data']['bg back'], dict['bg data']['bg back rect'])

        game_window.blit(dict['bg data']['bg'], dict['bg data']['bg rect'])

        frame_rect = frame.get_rect(center=(dict['player data']['x'], dict['player data']['y']))

        game_window.blit(frame, frame_rect)

        py.time.delay(100)
        py.display.update()



    game_window.blit(dict['bg data']['bg back'], dict['bg data']['bg back rect'])

    game_window.blit(dict['bg data']['bg'], dict['bg data']['bg rect'])

    py.time.delay(100)
    py.display.update()

    # change variables to put the user back on the home screen
    dict['loops']['in battle'] = False
    dict['loops']['home page'] = False



def player_death_animation():

    # draw each frame of the player death animation
    for frame in dict['sprites']['death']:

        game_window.blit(dict['bg data']['bg'], dict['bg data']['bg rect'])

        game_window.blit(dict['bg data']['bg back'], dict['bg data']['bg back rect'])

        frame_rect = frame.get_rect(center=(dict['player data']['x'], dict['player data']['y']))

        game_window.blit(frame, frame_rect)

        py.time.delay(100)
        py.display.update()
        


    game_window.blit(dict['bg data']['bg'], dict['bg data']['bg rect'])

    game_window.blit(dict['bg data']['bg back'], dict['bg data']['bg back rect'])

    py.time.delay(100)
    py.display.update()

    # change variables to put the user back on the home screen
    dict['loops']['in battle'] = False
    dict['loops']['home page'] = False



def update_enemy(enemy):

    if dict['game data']['generate random waves']:

        if enemy.get('enemy_random', False):

            enemy['x'] += enemy['x_speed']*math.sin((enemy['enemy_random'] + py.time.get_ticks())/1000)*0.3

        else:

            enemy['x'] += enemy['x_speed']*math.sin((py.time.get_ticks())/1000)*0.3



    else:

        if enemy['enemy_type'] == 3:

            if enemy['x'] <= 0 or enemy['x'] >= WIDTH:

                enemy['x_speed'] *= -1

        enemy['x'] += enemy['x_speed']



    enemy['y'] += enemy['y_speed']

    enemy['enemy_rect'] = py.Rect(enemy['x'] - 25, enemy['y'] - 30,  50, 50) 

    if enemy['y'] > HEIGHT + 50 and not dict['game data']['disable player death']:

        death_animation(True)

        dict['loops']['in battle'] = False
        dict['loops']['home page'] = True

        if not dict['game data']['infinite mode']:

            dict['player data']['live num'] -= 1

            if dict['player data']['live num'] == -1:

                dict['loops']['play game'] = False
                dict['loops']['in battle'] = False



def render_enemy(game_window, enemy_frame, enemy):

    enemy_frame_rect = enemy_frame.get_rect(center=(enemy['x'], enemy['y']))

    game_window.blit(enemy_frame, enemy_frame_rect)

    if dict['game data']['draw hitboxes']:

        py.draw.rect(game_window, (255, 0, 0), enemy['enemy_rect'], 2)



def shoot_enemy_bullet(enemy):

    if 'last_shot_time' not in enemy:

        enemy['last_shot_time'] = 0



    if enemy['last_shot_time'] + enemy['bullet_delay'] < py.time.get_ticks():

        enemy['bullets'].append({'x': enemy['x'], 'y': enemy['y']})

        enemy['last_shot_time'] = py.time.get_ticks()



def homing_bullet(enemy, player_x, player_y, bullet):

    dist_x  = player_x - enemy['x']
    dist_y  = player_y - enemy['y']
    
    steps_number = max(abs(dist_x), abs(dist_y))

    if steps_number == 0 or enemy['bullet_x_speed'] == 0:
        return 0, 0

    stepx = float(dist_x) / (steps_number / enemy['bullet_x_speed'])
    stepy = float(dist_y) / (steps_number / enemy['bullet_y_speed'])

    bullet['x'] += stepx
    bullet['y'] += stepy



def generate_random_wave():

    offset = 100
    min_x, max_x = offset, WIDTH - offset
    min_y, max_y = -offset*3, 0

    enemy_type_min, enemy_type_max = 0, 4

    bullet_delay_min, bullet_delay_max = 100, 3000
    bullet_y_speed_min, bullet_y_speed_max = 10, 25
    bullet_x_speed_min, bullet_x_speed_max = 10, 15
    
    y_speed_min, y_speed_max = 1, 10
    x_speed_min, x_speed_max = 1, 10

    dict['enemy data']['enemy count'] += 1
    
    wave = {
                "x"             :[random.randint(min_x, max_x) for i in range(dict['enemy data']['enemy count'])],
                "y"             :[random.randint(min_y, max_y) for i in range(dict['enemy data']['enemy count'])],
                "x_speed"       :[random.randint(x_speed_min, x_speed_max) for i in range(dict['enemy data']['enemy count'])],
                "y_speed"       :[random.randint(y_speed_min, y_speed_max) for i in range(dict['enemy data']['enemy count'])],
                "bullet_y_speed":[random.randint(bullet_y_speed_min, bullet_y_speed_max) for i in range(dict['enemy data']['enemy count'])],
                "bullet_x_speed":[random.randint(bullet_x_speed_min, bullet_x_speed_max) for i in range(dict['enemy data']['enemy count'])],
                "bullet_delay"  :[random.randint(bullet_delay_min, bullet_delay_max) for i in range(dict['enemy data']['enemy count'])],
                "enemy_type"    :[random.randint(enemy_type_min, enemy_type_max) for i in range(dict['enemy data']['enemy count'])],
                "enemy_random"  :[int(random.randint(0,10)*1000) for i in range(dict['enemy data']['enemy count'])]
        }

    return wave 



def create_enemies(stage_number: int, wave_number: int, random=False):
    
    enemies_list = []

    if not dict['game data']['infinite mode']:

        stage = stages[stage_number]

        wave  = stage[wave_number]



    print('total waves: ' + str(len(stage)))

    dict['enemy data']['total enemies'] += len(wave['x'])



    if random:

        wave = generate_random_wave()



    for key, value in wave.items():

        for i in range(len(value)):

            if i >= len(enemies_list):

                enemies_list.append({

                    "bullets" : [],

                    "dead" : False

                })

            enemies_list[i][key] = value[i]

    print("total enemies: " + str(dict['enemy data']['total enemies']))

    print("Loaded enemies:", enemies_list)

    return enemies_list



def get_max_wave(stage):

    if stage >= len(stages):

        return -1 

    return len(stages[stage])



def draw_bg():

    if   dict['game data']['stage num'] <   1: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][0]
    elif dict['game data']['stage num'] <   2: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][1]
    elif dict['game data']['stage num'] <   3: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][2]
    elif dict['game data']['stage num'] <   4: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][3]
    elif dict['game data']['stage num'] <   5: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][4]
    elif dict['game data']['stage num'] <   6: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][5]
    elif dict['game data']['stage num'] <   7: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][6]
    elif dict['game data']['stage num'] ==  8: dict['bg data']['bg'] = dict['sprites']['bgs']['front'][7]

    dict['animations']['bg delay'] = 1000 / len(dict['sprites']['bgs'])

    if dict['animations']['last bg time'] + dict['animations']['bg delay'] < py.time.get_ticks():

        dict['animations']['bg num'] = (dict['animations']['bg num'] + 1) % len(dict['bg data']['bg'])

        dict['animations']['last bg time'] = py.time.get_ticks()



    dict['bg data']['bg'] = dict['bg data']['bg'][dict['animations']['bg num']]

    dict['bg data']['bg back'] = dict['sprites']['bgs']['backs'][dict['game data']['stage num'] - 1]

    dict['bg data']['bg back rect'] = dict['bg data']['bg back'].get_rect(center=(288, 512))

    game_window.blit(dict['bg data']['bg back'], dict['bg data']['bg back rect'])

    dict['bg data']['bg rect'] = dict['bg data']['bg'].get_rect(center=(288, 512))

    game_window.blit(dict['bg data']['bg'], dict['bg data']['bg rect'])



def game_loop():

    enemies_list = create_enemies(dict['game data']['stage num'], dict['game data']['wave num'], random=dict['game data']['generate random waves'])

    max_wave     = get_max_wave(dict['game data']['stage num']) - 1

    animation_num = 0

    dict['player data']['x'] = 288
    dict['player data']['y'] = 800
    dict['player data']['bullets'] = []
    last_frame_time = 0
    last_shot_time = 0
    time_passed = py.time.get_ticks()

    wave_length = dict['game data']['stage wave lengths'][dict['game data']['stage num']]

    wave_length = wave_length[dict['game data']['wave num']] * 1000

    while dict['loops']['in battle']:

        if time_passed + wave_length < py.time.get_ticks() or dict['player data']['enemies killed'] >= dict['enemy data']['total enemies']:

            

            if dict['game data']['wave num'] == max_wave:           

                dict['game data']['wave num'] = -1



            if dict['game data']['wave num'] < max_wave and dict['game data']['wave num'] != -1:

                dict['game data']['wave num'] += 1



            elif not dict['game data']['infinite mode']:

                stage_clear_animation()

                dict['game data']['stage num'] += 1
                dict['game data']['wave num'] = 0

                if dict['player data']['live num'] < 3:
                    
                    dict['player data']['live num'] += 1

                break



            print(f"loading stage: {dict['game data']['stage num']} wave: {dict['game data']['wave num']}")

            enemies_list = list(filter(lambda x : not x.get('dead', False), enemies_list))

            if dict['game data']['wave num'] != -1:

                enemies_list.extend(create_enemies(dict['game data']['stage num'], dict['game data']['wave num'], dict['game data']['generate random waves']))
            
            if dict['game data']['infinite mode']:

                enemies_list.extend(create_enemies(dict['game data']['stage num'], dict['game data']['wave num'], dict['game data']['generate random waves']))

            time_passed = py.time.get_ticks()

        events = py.event.get()
        keys   = py.key.get_pressed()

        draw_bg()

        if   keys[py.K_a]: player_frame = dict['sprites']['player']['l'][animation_num]
        elif keys[py.K_d]: player_frame = dict['sprites']['player']['r'][animation_num]
        else             : player_frame = dict['sprites']['player']['f'][animation_num]



        if keys[py.K_SPACE]:

            if last_shot_time + dict['bullet data']['bullet delay'] < py.time.get_ticks():

                # check to see if ther ehas been a lnog enough delay in between the shots
                dict['player data']['bullets'].append({'x': dict['player data']['x'], 'y': dict['player data']['y'], 'dead' : False})  

                last_shot_time = py.time.get_ticks()



        if last_frame_time + 100 < py.time.get_ticks():
            
            animation_num = (animation_num + 1) % 4

            last_frame_time = py.time.get_ticks()

        player_bullet = dict['sprites']['player']['bullets'][animation_num]

        dict['player data']['rect'] = py.Rect(dict['player data']['x'] - 16, dict['player data']['y'] - 24, 32, 32)



        # draw the player here 
        try:

            if not dict['deaths']['player death']:

                player_frame_rect = player_frame.get_rect(center=(dict['player data']['x'], dict['player data']['y']))

                game_window.blit(player_frame, player_frame_rect)

        except:

            player_frame_rect = player_frame.get_rect(center=(dict['player data']['x'], dict['player data']['y']))

            game_window.blit(player_frame, player_frame_rect)



        if dict['game data']['draw hitboxes']:

            py.draw.rect(game_window, (255, 0, 0), dict['player data']['rect'], 2)


        # this for loop loops through all the ENEMIES
        # do enemy specific stuff in here


        for key, enemy in enumerate(enemies_list):

            # setup stuff for this specific enemy
            enemy_frame_type   = dict['sprites']['enemies']['f'][enemy['enemy_type']]

            enemy_bullet_type  = dict['sprites']['enemies']['b'][enemy['enemy_type']]
            
            enemy_frame        = enemy_frame_type[animation_num]
            
            enemy_bullet_frame = enemy_bullet_type[animation_num]

            if not enemy['dead']:
            
                # update enemy position and rect
                update_enemy(enemy)  

                # draw the enemy 
                render_enemy(game_window, enemy_frame, enemy)

                # check for enemy last shot time, and shoot if possible
                shoot_enemy_bullet(enemy)

            
                # now check if the enemy has collided with the player 
                if enemy['enemy_rect'].colliderect(dict['player data']['rect']) and not dict['game data']['disable player death']:

                    # add death location data
                    dict['deaths']['x'].append(dict['player data']['x'])

                    dict['deaths']['y'].append(dict['player data']['y'])

                    dict['animations']['deaths'].append(0)

                    dict['deaths']['death'] = True

                    dict['deaths']['player death'] = True


            # now we loop through all the bullets for THIS specific enemy 
            _deleted = 0

            for i, bullet in enumerate(list(enemy['bullets'])):


                if enemy['enemy_type'] == 2:

                    homing_bullet(enemy, dict['player data']['x'], dict['player data']['y'], bullet)



                else:

                    if dict['game data']['generate random waves']:

                        bullet['x']  = enemy['x']



                    else:

                        bullet['x'] += enemy['bullet_x_speed']



                    bullet['y'] += enemy['bullet_y_speed']
                


                # bullet is off screen, delete it 
                if bullet['y'] > HEIGHT + 100 or bullet['y'] < 0:

                    del enemy['bullets'][i - _deleted]

                    _deleted += 1

                    continue
                


                # draw the bullet 
                enemy_bullet_rect = enemy_bullet_frame.get_rect(center=(bullet['x'], bullet['y']))

                game_window.blit(enemy_bullet_frame, enemy_bullet_rect)



                # calculate the bullets hitbox
                bullet_rect = py.Rect(bullet['x'] - 6, bullet['y'] - 6, 12, 12)

                if dict['game data']['draw hitboxes']:

                    py.draw.rect(game_window, (0, 255, 0), bullet_rect, 2)



                # check if it hit the player 
                if bullet_rect.colliderect(dict['player data']['rect']) and not dict['game data']['disable player death']:

                    # add death location data
                    dict['deaths']['x'].append(dict['player data']['x'])

                    dict['deaths']['y'].append(dict['player data']['y'])

                    dict['animations']['deaths'].append(0)

                    dict['deaths']['death'] = True

                    dict['deaths']['player death'] = True

                    


        # END OF ENEMY LOOP HERE, 
        # DO NOT, use the 'enemy' variable from this point on


        # loop through all player bullets here 
        _deleted = 0
        for i, bullet in enumerate(list(dict['player data']['bullets'])):

            if bullet['dead']:

                continue



            bullet['y'] -= dict['bullet data']['bullet speed']



            # check if off screen 
            if bullet['y'] < 0:

                del dict['player data']['bullets'][i - _deleted]

                _deleted += 1

                continue

            # draw the bullets 
            player_bullet_rect = player_bullet.get_rect(center=(bullet['x'], bullet['y']))

            game_window.blit(player_bullet, player_bullet_rect)

            # calculate their hitbox
            bullet_rect = py.Rect(bullet['x'] - 32, bullet['y'] - 20, 64, 40)

            if dict['game data']['draw hitboxes']:

                py.draw.rect(game_window, (255, 0, 0), bullet_rect, 2)



            # loop through all the enemies and check for collision with player bullets
            for key, enemy in enumerate(enemies_list):

                if enemy['dead']:

                    continue

                if enemy['enemy_rect'].colliderect(bullet_rect):

                    # make sure an enemy can only be shot once
                    if 'last_damage_time' not in enemy:

                        enemy['last_damage_time'] = 0



                    if enemy['last_damage_time'] + 1000 < py.time.get_ticks():

                        enemy['last_damage_time'] = py.time.get_ticks()

                        # add death location data
                        dict['deaths']['x'].append(enemy['x'])

                        dict['deaths']['y'].append(enemy['y'])

                        dict['animations']['deaths'].append(0)

                        dict['deaths']['death'] = True

                        # add item location data
                        dict['items']['x'].append(enemy['x'])

                        dict['items']['y'].append(enemy['y'])

                        dict['animations']['items'].append(0)

                        dict['animations']['item last time'].append(125 + py.time.get_ticks())

                        dict['items']['item'] = True

                        # delete enemy data
                        enemies_list[key]['dead'] = True

                        if not dict['bullet data']['bullet piercing']: 
                            
                            bullet['dead'] = True

                        # increase enemies killed
                        dict['player data']['enemies killed'] += 1
                        
                
            
        # do animations that happen when an enemy dies
        try:

            if dict['deaths']['death']: 

                if dict['deaths']['player death']: 
                    
                    death_animation(True)

                else: 
                    
                    death_animation()

        except: 
            
            death_animation()
        
        if dict['items']['item']: 
            
            item_animations()

            

        # keybindings
        if keys[py.K_a]:

            # move left
            if keys[py.K_LSHIFT]: 

                dict['player data']['x'] -= 8

            else: 

                dict['player data']['x'] -= 16



        elif keys[py.K_d]:

            # move right
            if keys[py.K_LSHIFT]: 

                dict['player data']['x'] += 8

            else: 

                dict['player data']['x'] += 16



        if keys[py.K_w]:

            # move up
            if keys[py.K_LSHIFT]: 

                dict['player data']['y'] -= 8

            else:

                dict['player data']['y'] -= 16



        elif keys[py.K_s]:

            # move down
            if keys[py.K_LSHIFT]: 

                dict['player data']['y'] += 8
                
            else: 

                dict['player data']['y'] += 16



        if dict['player data']['x'] < 0:

            dict['player data']['x'] = 0



        if dict['player data']['x'] > WIDTH:

            dict['player data']['x'] = WIDTH



        if dict['player data']['y'] > HEIGHT:

            dict['player data']['y'] = HEIGHT



        if dict['player data']['y'] < 0:

            dict['player data']['y'] = 0



        for event in events:

            if event.type == py.QUIT: 

                dict['loops']['in battle'] = False; dict['loops']['play game'] = False

        py.time.delay(delay)
        py.display.update()
        


delay = 40
# game loop
while dict['loops']['play game']:

    events = py.event.get()

    keys   = py.key.get_pressed()

    if not dict['loops']['in battle']: 
        
        dict['bg data']['bg rect'] = dict['sprites']['menu']['bg'].get_rect(center=(288, 512))

        game_window.blit(dict['sprites']['menu']['bg'], dict['bg data']['bg rect'])

        buttons_rect = dict['sprites']['menu']['buttons'].get_rect(center=(288, 700))
        
        game_window.blit(dict['sprites']['menu']['buttons'], buttons_rect)

        # placing life count
        lives_rect = dict['sprites']['lives'][dict['player data']['live num']].get_rect(center=(288, 985)); game_window.blit(dict['sprites']['lives'][dict['player data']['live num']], lives_rect)

        # place menu button highlighter
        if   menu_number == 1 and dict['loops']['home page']: highlight_rect = dict['sprites']['menu']['button highlight'].get_rect(center=(288, 572)); game_window.blit(dict['sprites']['menu']['button highlight'], highlight_rect)
        elif menu_number == 2 and dict['loops']['home page']: highlight_rect = dict['sprites']['menu']['button highlight'].get_rect(center=(288, 700)); game_window.blit(dict['sprites']['menu']['button highlight'], highlight_rect)
        elif menu_number == 3 and dict['loops']['home page']: highlight_rect = dict['sprites']['menu']['button highlight'].get_rect(center=(288, 828)); game_window.blit(dict['sprites']['menu']['button highlight'], highlight_rect)
        
        # place difficulty setting text
        if   dict['game data']['difficulty num'] == 1 and dict['loops']['home page']: normal_rect  = dict['sprites']['menu']['normal diff'].get_rect(center=(288, 700));  game_window.blit(dict['sprites']['menu']['normal diff'], normal_rect)
        elif dict['game data']['difficulty num'] == 2 and dict['loops']['home page']: endless_rect = dict['sprites']['menu']['endless diff'].get_rect(center=(288, 700)); game_window.blit(dict['sprites']['menu']['endless diff'], endless_rect)

        # placing the map
        if not dict['loops']['home page']:

            map_overlay = dict['sprites']['map'][dict['game data']['stage num']]

            dict['bg data']['bg rect'] = map_bg.get_rect(center=(288, 512))

            map_rect = map_overlay.get_rect(center=(288, 512))

            buttons_rect = map_buttons.get_rect(center=(148, 106))

            game_window.blit(map_bg, dict['bg data']['bg rect'])

            game_window.blit(map_overlay, map_rect)

            game_window.blit(map_buttons, buttons_rect)

            if   menu_number == 1: highlight_rect = dict['sprites']['menu']['button highlight'].get_rect(center=(148, 62));  game_window.blit(dict['sprites']['menu']['button highlight'], highlight_rect)
            elif menu_number == 2: highlight_rect = dict['sprites']['menu']['button highlight'].get_rect(center=(148, 150)); game_window.blit(dict['sprites']['menu']['button highlight'], highlight_rect)

            

    # keybindings
    if keys[py.K_a]:

        # move left
        if keys[py.K_LSHIFT]: 

            dict['player data']['x'] -= 4

        else: 

            dict['player data']['x'] -= 8



    elif keys[py.K_d]:

        # move right
        if keys[py.K_LSHIFT]: 

            dict['player data']['x'] += 4

        else: 

            dict['player data']['x'] += 8



    if keys[py.K_w]:

        # move up
        if keys[py.K_LSHIFT]: 

            dict['player data']['y'] -= 4

        else:

            dict['player data']['y'] -= 8



    elif keys[py.K_s]:

        # move down
        if keys[py.K_LSHIFT]: 

            dict['player data']['y'] += 4

        else: 

            dict['player data']['y'] += 8



    # set player boundaries
    if dict['player data']['x'] < 0:

        dict['player data']['x'] = 0



    if dict['player data']['x'] > WIDTH:

        dict['player data']['x'] = WIDTH



    if dict['player data']['y'] > HEIGHT:

        dict['player data']['y'] = HEIGHT



    if dict['player data']['y'] < 0:

        dict['player data']['y'] = 0



    for event in events:

    # close program
        if event.type == py.QUIT: 
                
                dict['loops']['in battle'] = False
                dict['loops']['play game'] = False

    if keys[py.K_UP]:

        # move up menu button
        if dict['loops']['home page']:

            if menu_number >= 2: 

                menu_number -= 1

                py.time.delay(250)


        else: 

            if menu_number == 2: 
                
                menu_number = 1



    if keys[py.K_DOWN]:

        # move down menu button
        if dict['loops']['home page']:

            if menu_number <= 2: 

                menu_number += 1

                py.time.delay(250)


        else:

            if menu_number == 1: menu_number = 2



    if keys[py.K_LEFT]:

        # change difficulty
        if dict['loops']['home page']:

            if menu_number == 2:

                if dict['game data']['difficulty num'] == 2: 

                    dict['game data']['difficulty num'] = 1

                    py.time.delay(250)



    if keys[py.K_RIGHT]:

        # change difficulty
        if dict['loops']['home page']:

            if menu_number == 2:

                if dict['game data']['difficulty num'] == 1: 

                    dict['game data']['difficulty num'] = 2

                    py.time.delay(250)



    if keys[py.K_RETURN]:

        # choose menu option
        if dict['loops']['home page'] and menu_number == 1:

            dict['loops']['home page'] = False



        elif not dict['loops']['home page'] and menu_number == 1: 

            reset_arrays()

            dict['loops']['in battle'] = True

            if   dict['game data']['difficulty num'] == 1: dict['game data']['infinite mode'], dict['game data']['generate random waves'] = False, False
            elif dict['game data']['difficulty num'] == 2: dict['game data']['infinite mode'], dict['game data']['generate random waves'] = True,  True

            game_loop()



        elif not dict['loops']['home page'] and menu_number == 2: 
            
            dict['loops']['home page'] = True
            
            menu_number = 1



        elif dict['loops']['home page'] and menu_number == 3: 

            dict['loops']['play game'] = False
            dict['loops']['in battle'] = False 



        py.time.delay(250)

    py.display.update()

    py.time.delay(delay)
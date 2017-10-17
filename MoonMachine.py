## Moon Machine 

## --- Importing Libraries --- ##
import random, pygame, os, math 
 
## Initiates the Pygame library
pygame.init()

## --- Variables for the Options Window --- ##
# -- Variables That Control What Is Being Displayed -- #
video_settings = False                                 
audio_settings = False                                 
controls = False                                       
resolution = True
keyboard = True
controller = False
# -- Window Loop Bools For Options And Main -- #
done_options = False
done_main = False
# -- Defining Resolution Sizes -- #
Sma = (800,460)
Med = (1280,720)
Lrg = (1600,900)
# -- Bools To Store What Resolution Was Selected -- #
# -- To Prevent Having To Read/Write Files Until -- #
# -- The Main Loop Starts                        -- #
medium = False
large = False
small = False
## --- Text Files are Read to Determine the Screen Resolution Last Used --- ##
# -- Text Is Read To Determine The Resolution -- #
x = open('GameFiles/TextFiles/settings.txt','r')                                      
text = x.readlines()

# -- Using the Info From the Text File -- #
if int(text[0]) == 0:
    small = True
    screen_res = Sma
elif int(text[0]) == 1:   
    medium = True
    screen_res = Med
elif int(text[0]) == 2:
    large = True
    screen_res = Lrg
music_volume = int(text[1])
sfx_volume = int(text[2])
x.close



## --- Indent of Buttons, When They are Pressed
button_indent = 4

## --- Fonts --- ##
font30 = pygame.font.SysFont('Calibri', 30, True, False)
font25 = pygame.font.SysFont('Calibri', 25, True, False)
font20 = pygame.font.SysFont('Calibri', 20, True, False)
## --- Colours --- ##
Black = (0,0,0)
White = (255,255,255)
Red2 = (255,0,0)
green = (9,219,16)
Gray = (128,133,145)
DarkGray = (106,107,110)
Blue = (20,224,224)
green2 = (95,232,100) 
Blue2 = (87,98,145)
Gray2 = (106,122,128)
## --- Option Colours, Colours Already Defined Are Used To Create New Colours --- ##
Button_Colour = green
ButtonI_Colour = (int(4*Button_Colour[0]/6),int(4*Button_Colour[1]/6),int(4*Button_Colour[2]/6))
Button_Outline = Black
Window_Colour = green2
WindowI_Colour = (int(4*Window_Colour[0]/6),int(4*Window_Colour[1]/6),int(4*Window_Colour[2]/6))
size_screen1 = (600,400)
screen_options = pygame.display.set_mode(size_screen1)
pygame.display.set_caption("Moon Machine Settings")
## --- Functions --- ##
# -- Draws A Check Mark -- #
def check_mark(y):
    pygame.draw.aaline(screen_options, Black, [36,47+y*30], [29,59+y*30], 1)
    pygame.draw.aaline(screen_options, Black, [25,55+y*30], [29,59+y*30], 1)
# -- Takes Coords and Demensions of Two Boxes -- #
# -- and Returns True or False Depending on   -- #
# -- Whether or not They are Touching         -- #
def check_collision(o1_x,o2_x,o1_y,o2_y,o1_w,o2_w,o1_h,o2_h):
    delta_x = abs(o1_x-o2_x)
    delta_y = abs(o1_y-o2_y)
    if o1_x > o2_x:
        if delta_x < o2_w:
            if o1_y > o2_y:
                if delta_y < o2_h:
                    return True
                else:
                    return False
            elif o1_y <= o2_x:
                if delta_y < o1_h:
                    return True
                else:
                    return False
            else:
                return False        
        else:
            return False
    elif o1_x <= o2_x:
        if delta_x < o1_w:
            if o1_y > o2_y:
                if delta_y < o2_h:
                    return True
                else:
                    return False
            elif o1_y <= o2_x:
                if delta_y < o1_h:
                    return True
                else:
                    return False
            else:
                return False        
        else:
            return False
    else:
        return False
# -- Spawns New Enemies or Entities -- #    
def spawn_enemy(enemy_number, x, y):
    # - Wisp - #
    if enemy_number == 1:
        # x pos, y pos, direction, speed, attack delay, stopped?, angle for sin in y pos, attacking?
        wisps.append([x,y,1,wisp_speed,wisp_attack_delay,False,(random.randrange(0,629))/100,False,wisp_health,False])#9
    # - Slime - #
    elif enemy_number == 2:
        # x, y, direction, speed, jumping?, gravity, jump delay
        slimes.append([x,y,1,slime_speed,False,1,random.randrange(1,slime_jump_delay+1),slime_health,False])#8
    # - Screamer - #
    elif enemy_number == 3:
        # x, y, direction, speed, sprite shuffle value, y_direction
        screamers.append([x,y,1,screamer_speed,0,1,screamer_health,0,False])#8
    # - Thief - #
    elif enemy_number == 4:
        # x, y, direction, speed, speed multiplier
        thiefs.append([x,y,1,thief_speed,1.6,thief_health,False])#6
    # -- Draws a Wisp -- #
    elif enemy_number == 5:
        snakes.append([x,y,1,snake_speed,snake_health,random.randrange(-snake_charge_frames,snake_cooldown+1),False])#6
    elif enemy_number == 6:
        tanks.append([x,y,1,tank_speed,tank_health, random.randrange(2),random.randrange(2),False])#7
    elif enemy_number == 7:
        clouds.append([x,y,1,cloud_speed,cloud_health,(random.randrange(0,629))/100,cloud_cooldown,[],False])#8
        
# Draws The Wisp Enemy
def draw_wisp(x,y,i):
    if wisps[i][9]:
        if not wisps[i][7]:  
            if (wisps[i])[2] == 1:
                screen_main.blit(wisph_blue_right,[x,y])
            elif (wisps[i])[2] == -1:
                screen_main.blit(wisph_blue_left,[x,y])
        if wisps[i][7]:  
            if (wisps[i])[2] == 1:
                screen_main.blit(wisph_red_right,[x,y])
            elif (wisps[i])[2] == -1:
                screen_main.blit(wisph_red_left,[x,y])
        wisps[i][9] = False
    else:
        if not wisps[i][7]:  
            if (wisps[i])[2] == 1:
                screen_main.blit(wisp_blue_right,[x,y])
            elif (wisps[i])[2] == -1:
                screen_main.blit(wisp_blue_left,[x,y])
        if wisps[i][7]:  
            if (wisps[i])[2] == 1:
                screen_main.blit(wisp_red_right,[x,y])
            elif (wisps[i])[2] == -1:
                screen_main.blit(wisp_red_left,[x,y])
# -- Draws The Slime Enemy -- #
def draw_slime(x,y,i):
    if slimes[i][8]:
        if slimes[i][4]:
            if (slimes[i])[2] == 1:
                screen_main.blit(slimeh_right_jump,[x,y-slime_size])
            else:
                screen_main.blit(slimeh_left_jump,[x,y-slime_size])
        else:
            if (slimes[i])[2] == 1:
                screen_main.blit(slimeh_right,[x,y])
            else:
                screen_main.blit(slimeh_left,[x,y])
        slimes[i][8] = False
    else:
        if slimes[i][4]:
            if (slimes[i])[2] == 1:
                screen_main.blit(slime_right_jump,[x,y-slime_size])
            else:
                screen_main.blit(slime_left_jump,[x,y-slime_size])
        else:
            if (slimes[i])[2] == 1:
                screen_main.blit(slime_right,[x,y])
            else:
                screen_main.blit(slime_left,[x,y])
# -- Draws The Screamer Enemy-- #
def draw_screamer(x,y,i):
    if screamers[i][8]:
        if screamers[i][4]%4 <= 1:
            if screamers[i][2] == 1:
                screen_main.blit(screamerh_right_1,[x,y])
            else:
                screen_main.blit(screamerh_left_1,[x,y])
        if screamers[i][4]%4 >= 2:
            if screamers[i][2] == 1:
                screen_main.blit(screamerh_right_2,[x,y])
            else:
                screen_main.blit(screamerh_left_2,[x,y])
        screamers[i][8] = False
    else:
        if screamers[i][4]%4 <= 1:
            if screamers[i][2] == 1:
                screen_main.blit(screamer_right_1,[x,y])
            else:
                screen_main.blit(screamer_left_1,[x,y])
        if screamers[i][4]%4 >= 2:
            if screamers[i][2] == 1:
                screen_main.blit(screamer_right_2,[x,y])
            else:
                screen_main.blit(screamer_left_2,[x,y])
# -- Draws The Thief Enemy-- #
def draw_thief(x,y,i):
    if thiefs[i][6]:
        if thiefs[i][2] == 1:
            screen_main.blit(thiefh_right,[x,y])
        else:
            screen_main.blit(thiefh_left,[x,y])
        thiefs[i][6] = False
    else:
        if thiefs[i][2] == 1:
            screen_main.blit(thief_right,[x,y])
        else:
            screen_main.blit(thief_left,[x,y])
# -- Draws The Snake Enemy -- #
def draw_snake(x,y,i):
    if snakes[i][6]:
        if snakes[i][5] <= 0:
            if snakes[i][2] == 1:
                screen_main.blit(snakeh_right_2,[x,y])
            else:
                screen_main.blit(snakeh_left_2,[x,y])        
        else:
            if snakes[i][2] == 1:
                screen_main.blit(snakeh_right_1,[x,y])
            else:
                screen_main.blit(snakeh_left_1,[x,y])
        snakes[i][6] = False
    else:
        if snakes[i][5] <= 0:
            if snakes[i][2] == 1:
                screen_main.blit(snake_right_2,[x,y])
            else:
                screen_main.blit(snake_left_2,[x,y])        
        else:
            if snakes[i][2] == 1:
                screen_main.blit(snake_right_1,[x,y])
            else:
                screen_main.blit(snake_left_1,[x,y])
# -- Draws The Tank Enemy -- #
def draw_tank(x,y,i):
    if tanks[i][7]:
        if tanks[i][2] == 1:
            if tanks[i][5]%2 == 0:
                if tanks[i][6]%4 > 1:
                    screen_main.blit(tankh_right_0_0,[x,y])
                else:
                    screen_main.blit(tankh_right_0_1,[x,y])
            else:
                if tanks[i][6]%4 > 1:
                    screen_main.blit(tankh_right_1_0,[x,y])
                else:
                    screen_main.blit(tankh_right_1_1,[x,y])
        else:
            if tanks[i][5]%2 == 0:
                if tanks[i][6]%4 > 1:              
                    screen_main.blit(tankh_left_0_0,[x,y])
                else:
                    screen_main.blit(tankh_left_0_1,[x,y])
            else:
                if tanks[i][6]%4 > 1:
                    screen_main.blit(tankh_left_1_0,[x,y])
                else:
                    screen_main.blit(tankh_left_1_1,[x,y])
        tanks[i][7] = False
    else:
        if tanks[i][2] == 1:
            if tanks[i][5]%2 == 0:
                if tanks[i][6]%4 > 1:
                    screen_main.blit(tank_right_0_0,[x,y])
                else:
                    screen_main.blit(tank_right_0_1,[x,y])
            else:
                if tanks[i][6]%4 > 1:
                    screen_main.blit(tank_right_1_0,[x,y])
                else:
                    screen_main.blit(tank_right_1_1,[x,y])
        else:
            if tanks[i][5]%2 == 0:
                if tanks[i][6]%4 > 1:              
                    screen_main.blit(tank_left_0_0,[x,y])
                else:
                    screen_main.blit(tank_left_0_1,[x,y])
            else:
                if tanks[i][6]%4 > 1:
                    screen_main.blit(tank_left_1_0,[x,y])
                else:
                    screen_main.blit(tank_left_1_1,[x,y])
# -- Draws The Cloud Enemy -- #
def draw_cloud(x,y):
    if clouds[i][8]:
        screen_main.blit(cloudh,[x,y])
        clouds[i][8] = False
    else:
        screen_main.blit(cloud,[x,y])
# -- Creates a Projectile or Vector -- #
def add_projectile(x1,y1,x2,y2,speed):
    yd = (y2-y1)
    xd = (x2-x1)
    total = abs(yd) + abs(xd)
    x_speed = int((xd/total)*speed)
    y_speed = int((yd/total)*speed)
    return [x1,y1,x_speed,y_speed,0]
# -- Draws a Projectile -- #
def draw_projectiles(enemy_number,x,y,angle):
    if enemy_number == 1:
        rotated_sprite = pygame.transform.rotate(wisp_projectile, angle)
        screen_main.blit(rotated_sprite, [x, y])
def mainloop_variables():
    global titlescreen
    global upgradescreen
    global gameover
    global gameover_sound
    global current_upgrade_pointpos
    global purchase 
    global pointon_play 
    global pointon_quit 
    global pointon_credits
    global credits_screen
    global change_pos
    global keys
    global pause
    global foreground_pos1 
    global foreground_pos2
    global background_pos1
    global background_pos2 
    global analog_values
    global button_values
    global money
    global player_projectiles
    global player_x
    global player_y
    global player_center
    global player_movement
    global player_stats
    global upgrades
    global player_damage
    global invincible
    global knockback
    global vertical_velocity
    global gravity
    global player_shots
    global shot_delay
    global jumping
    global walking
    global spawn 
    global enemy_count
    global score
    global wave_number
    global wave_pv
    global wave_difficulty_ramp
    global wisps
    global wisp_projectiles
    global slimes
    global screamers 
    global thiefs 
    global snakes 
    global tanks 
    global clouds 
    global cloud_projectiles
    global godmode
    
    ## --- Main Program Initial Variables --- ##
    titlescreen = True
    upgradescreen = False
    gameover = False
    gameover_sound = True
    current_upgrade_pointpos = upgrade_pointer_poslist[0]
    purchase = False
    pointon_play = True
    pointon_quit = False
    pointon_credits = False
    credits_screen = False
    change_pos = 0
    keys = [False,False,False,False,False,False,False,False,False,False,False]
    pause = False
    # -- Foreground And Background Starting Positions -- #
    foreground_pos1 = -screen_res[0] 
    foreground_pos2 = 2*screen_res[0]
    background_pos1 = -2*screen_res[0]
    background_pos2 = screen_res[0]

    # -- Values of controller buttons and analog sticks are 0 unless a controller is plugged in and they are redefined -- #
    analog_values = [0,0,0,0]
    button_values = [0,0,0,0,0,0,0,0]

    money = 0
    # -- Player Variables -- #
    player_projectiles = []
    player_x = int(screen_res[0]/2-player_width/2)
    player_y = screen_res[1]-player_height-ground_level
    player_center = (player_x + (int(player_width/2)),player_y + (int(player_height/2)))
    player_movement = 0
    #current_health, max_health, firerate_multiplier, damage_multiplier, speed multiplier
    player_stats = [20,20,1.0,1.0,1.0]
    #healthups, firerateups, powerups, speedups
    upgrades = [0,0,0,0,-1]

    invincible = 0 
    knockback = []
        # -- Velocity while jumping -- #
    vertical_velocity = 0
        # -- Determines the rate at which you fall -- #
    gravity = 1 * screen_res[0]/Med[0]

        # -- No shots on screen at the beggining of the code -- #
    player_shots = False

        # -- Determines the delay between shots -- #
    shot_delay = 0
        # -- You are neither jumping or walking at the begining of the game -- #
    jumping = False
    walking = False
    spawn = False

        # -- Enemy Variables -- #
    enemy_count = 0
    score = 0

    wave_number = 0
    wave_pv = 15
    wave_difficulty_ramp = 5

        # Wisps
    wisps = []
    wisp_projectiles = []
        # Slimes
    slimes = []
        # Screamers
    screamers = []
        # Thiefs
    thiefs = []
        # Snakes
    snakes = []
        # Tanks
    tanks = []
        # Clouds
    clouds = []
    cloud_projectiles = []

    godmode = [False,False]

## --- Images --- ##
moon_background = pygame.image.load("GameFiles/Images/background.png").convert()
options_pointer = pygame.image.load("GameFiles/Images/pointer.png").convert_alpha()
options_pointer = pygame.transform.scale(options_pointer,(35,35))
keyboard_controls = pygame.image.load("GameFiles/Images/keyboard_controls.png").convert_alpha()
controller_controls = pygame.image.load("GameFiles/Images/controller_controls.png").convert_alpha()

icon = os.getcwd() + '\\GameFiles\\Images\\icon.png'
icon = pygame.image.load(icon)
## --- Window Icon is Set --- ##
pygame.display.set_icon(icon)
## --- Clock initiates --- ##
clock = pygame.time.Clock()
## --- Hides the mouse for a custom pointer --- ##
pygame.mouse.set_visible(False)
## --- Options Loop Starts --- ##
while not done_options:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done_options = True
            done_main = True
## --- Getting the mouse coords --- ##
    mouse_pos = pygame.mouse.get_pos()        
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
## --- Options Background --- ##
    screen_options.blit(moon_background, [0, 0])  
## --- Video Button --- ##
    pygame.draw.rect(screen_options,(Button_Colour),[15,330,120,60])
    pygame.draw.rect(screen_options,(Button_Outline),[16,331,118,58],3)
    text = font30.render("Video", True, Black)
    screen_options.blit(text, [39, 348])
## --- Audio Button --- ##
    pygame.draw.rect(screen_options,(Button_Colour),[145,330,120,60])
    pygame.draw.rect(screen_options,(Button_Outline),[146,331,118,58],3)
    text = font30.render("Audio", True, Black)
    screen_options.blit(text, [168, 348])
## --- Controls Button --- ##
    pygame.draw.rect(screen_options,(Button_Colour),[275,330,120,60])
    pygame.draw.rect(screen_options,(Button_Outline),[276,331,118,58],3)
    text = font30.render("Controls", True, Black)
    screen_options.blit(text, [283, 348])
## --- Launch Button --- ##
    pygame.draw.rect(screen_options,(Button_Colour),[405,330,178,60])
    pygame.draw.rect(screen_options,(Button_Outline),[406,331,176,58],3)
    text = font30.render("Launch Game", True, Black)
    screen_options.blit(text, [410, 348])
## --- Video Button is Pressed --- ##
    if (pygame.mouse.get_pressed()[0])  and 15<=(mouse_x)<=135 and 330<=(mouse_y)<=390 :
        if not video_settings:
            video_settings_pos = -285
            video_settings = True
            current_settings = "video_settings"
        pygame.draw.rect(screen_options,(ButtonI_Colour),[15+button_indent,330+button_indent,120-2*button_indent,60-2*button_indent])
        text = font30.render("Video", True, Black)
        screen_options.blit(text, [39, 348])
## --- Audio Button is Pressed --- ##    
    if (pygame.mouse.get_pressed()[0])  and 145<=(mouse_x)<=265 and 330<=(mouse_y)<=390:
        if not audio_settings:
            audio_settings_pos = -285
            audio_settings = True
            current_settings = "audio_settings"
        pygame.draw.rect(screen_options,(ButtonI_Colour),[145+button_indent,330+button_indent,120-2*button_indent,60-2*button_indent])
        text = font30.render("Audio", True, Black)
        screen_options.blit(text, [168, 348])
## --- Controls Button is Pressed --- ##
    if (pygame.mouse.get_pressed()[0])  and 275<=(mouse_x)<=395 and 330<=(mouse_y)<=390:
        if not controls:
            controls_pos = -285
            controls = True
            current_settings = "controls"
        pygame.draw.rect(screen_options,(ButtonI_Colour),[275+button_indent,330+button_indent,120-2*button_indent,60-2*button_indent])
        text = font30.render("Controls", True, Black)
        screen_options.blit(text, [283, 348])
## --- Launch Button is Pressed --- ##
    if (pygame.mouse.get_pressed()[0])  and 405<=(mouse_x)<=583 and 330<=(mouse_y)<=390:
        done_options=True
        pygame.draw.rect(screen_options,(ButtonI_Colour),[405+button_indent,330+button_indent,178-2*button_indent,60-2*button_indent])
        text = font30.render("Launch Game", True, Black)
        screen_options.blit(text, [410, 348]) 
    ## --- Video Settings Display --- ##
    if video_settings:
        if video_settings_pos > 600:
            video_settings = False
        elif current_settings != "video_settings":
            video_settings_pos += 60
        elif video_settings_pos < 15:
            video_settings_pos += 60    
        pygame.draw.rect(screen_options,(Window_Colour),[video_settings_pos,10,236,310])
        pygame.draw.rect(screen_options,(Button_Outline),[video_settings_pos+1,11,234,308],4)
        ## --- Resolutions Button --- ##
        pygame.draw.rect(screen_options,(Window_Colour),[video_settings_pos+4,14,115,25])
        ## --- Resolutions Button Text --- ##    
        text = font25.render("Screen Resolutions", True, Black)
        screen_options.blit(text, [video_settings_pos+8, 15])
        ## --- Resolutions Display --- ##
        if resolution:
            text = font20.render("Small (800 x 600)", True, Black)
            screen_options.blit(text, [video_settings_pos+30, 45])
            pygame.draw.rect(screen_options,(Black),[video_settings_pos+8,45,17,17],1)
            text = font20.render("Medium (1280 x 720)", True, Black)
            screen_options.blit(text, [video_settings_pos+30, 75])
            pygame.draw.rect(screen_options,(Black),[video_settings_pos+8,75,17,17],1)
            text = font20.render("Large (1600 x 900)", True, Black)
            screen_options.blit(text, [video_settings_pos+30, 105])
            pygame.draw.rect(screen_options,(Black),[video_settings_pos+8,105,17,17],1)

            if (pygame.mouse.get_pressed()[0])  and 23<=(mouse_x)<=40 and 45 <=(mouse_y)<= 62:
                small = True
                medium = False
                large = False
                
            elif (pygame.mouse.get_pressed()[0])  and 23<=(mouse_x)<=40 and 75 <=(mouse_y)<= 92:
                small = False
                medium = True
                large = False
                
            elif (pygame.mouse.get_pressed()[0])  and 23<=(mouse_x)<=40 and 105 <=(mouse_y)<= 122:
                small = False
                medium = False
                large = True 
            if small:
                check_mark(0)
            elif medium:
                check_mark(1)
            elif large:
                check_mark(2)
    ## --- Audio Settings Display --- ##        
    if audio_settings:
        if audio_settings_pos > 600:
            audio_settings = False
        elif current_settings != "audio_settings":
            audio_settings_pos += 60
        elif audio_settings_pos < 15:
            audio_settings_pos += 60     
        pygame.draw.rect(screen_options,(Window_Colour),[audio_settings_pos,10,236,310])
        pygame.draw.rect(screen_options,(Button_Outline),[audio_settings_pos+1,11,234,308],4)
        text = font25.render("Music Volume: "+str(int(music_volume)), True, Black)
        screen_options.blit(text, [audio_settings_pos+18, 20])
        pygame.draw.rect(screen_options,Button_Outline,[audio_settings_pos+18,50,200,5],1)
        pygame.draw.line(screen_options, Button_Outline, [audio_settings_pos+18,45], [audio_settings_pos+18,60], 4)
        pygame.draw.line(screen_options, Button_Outline, [audio_settings_pos+218,45], [audio_settings_pos+218,60], 4)
        pygame.draw.line(screen_options, Button_Outline, [audio_settings_pos+18+music_volume*2,44], [audio_settings_pos+18+music_volume*2,61], 6)
        if pygame.mouse.get_pressed(0)[0] == 1 and audio_settings_pos+16.5 < mouse_x < audio_settings_pos+18+201.5 and 44 < mouse_y < 61 and audio_settings_pos == 15:
            music_volume = (mouse_x - audio_settings_pos+18)/2-18
            if music_volume < 0:
                music_volume = 0
            elif music_volume > 100:
                music_volume = 100
            pygame.mouse.set_pos([audio_settings_pos+18+music_volume*2,52])
        text = font25.render("SFX Volume: "+str(int(sfx_volume)), True, Black)
        screen_options.blit(text, [audio_settings_pos+18, 70])
        pygame.draw.rect(screen_options,Button_Outline,[audio_settings_pos+18,100,200,5],1)
        pygame.draw.line(screen_options, Button_Outline, [audio_settings_pos+18,95], [audio_settings_pos+18,110], 4)
        pygame.draw.line(screen_options, Button_Outline, [audio_settings_pos+218,95], [audio_settings_pos+218,110], 4)
        pygame.draw.line(screen_options, Button_Outline, [audio_settings_pos+18+sfx_volume*2,94], [audio_settings_pos+18+sfx_volume*2,111], 6)
        if pygame.mouse.get_pressed(0)[0] == 1 and audio_settings_pos+16.5 < mouse_x < audio_settings_pos+18+201.5 and 94 < mouse_y < 111 and audio_settings_pos == 15:
            sfx_volume = (mouse_x - audio_settings_pos+18)/2-18
            if sfx_volume < 0:
                sfx_volume = 0
            elif sfx_volume > 100:
                sfx_volume = 100
            pygame.mouse.set_pos([audio_settings_pos+18+sfx_volume*2,102])    
    ## --- Controls Display --- ##
    if controls:
        if controls_pos > 600:
            controls = False
        elif current_settings != "controls":
            controls_pos += 60
        elif controls_pos < 15:
            controls_pos += 60
        pygame.draw.rect(screen_options,(Window_Colour),[controls_pos,10,236,310])
        pygame.draw.rect(screen_options,(Button_Outline),[controls_pos+1,11,234,308],4)

        pygame.draw.rect(screen_options,(Window_Colour),[controls_pos+4,14,115,25])
        pygame.draw.rect(screen_options,(Button_Outline),[controls_pos+4,14,115,25],1)

        if (pygame.mouse.get_pressed()[0])  and 23<=(mouse_x)<=138-1 and 18 <=(mouse_y)<= 43 and controls_pos == 15:
            keyboard = True
            controller = False
        text = font25.render("Keyboard", True, Black)
        screen_options.blit(text, [controls_pos+11, 15])

        pygame.draw.rect(screen_options,(Window_Colour),[controls_pos+4+114,14,115,25])
        pygame.draw.rect(screen_options,(Button_Outline),[controls_pos+4+114,14,115,25],1)

        if (pygame.mouse.get_pressed()[0])  and 23+115<=(mouse_x)<=138+114 and 18 <=(mouse_y)<= 43 and controls_pos == 15:
            controller = True
            keyboard = False
        text = font25.render("Controller", True, Black)
        screen_options.blit(text, [controls_pos+7+114, 15])

        if keyboard:
            screen_options.blit(keyboard_controls,[controls_pos+2,35])
            pygame.draw.rect(screen_options,(WindowI_Colour),[controls_pos+5,15,113,23])
            text = font25.render("Keyboard", True, Black)
            screen_options.blit(text, [controls_pos+11, 15])

        if controller:
            screen_options.blit(controller_controls,[controls_pos+2,35])
            pygame.draw.rect(screen_options,(WindowI_Colour),[controls_pos+5+114,15,113,23])
            text = font25.render("Controller", True, Black)
            screen_options.blit(text, [controls_pos+7+114, 15])
    screen_options.blit(options_pointer, [mouse_x, mouse_y])
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

## -- Writes the New Screen Resolution to the Text Storage and Changes the Resolution --- ##
if small:
    screen_res = Sma
    lines = [0,str(int(music_volume)),str(int(sfx_volume))]

elif medium:
    screen_res = Med
    lines = [1,str(int(music_volume)),str(int(sfx_volume))]

elif large:
    screen_res = Lrg
    lines = [2,str(int(music_volume)),str(int(sfx_volume))]
with open('GameFiles/TextFiles/settings.txt','w') as x:
    x.writelines("%s\n" % l for l in lines)    

## --- Developes a Random Message From a List of Strings, and Adds it to the Title --- ##
random_message = (random.choice(["The Walnut Is Finished","Pixels Are People Too!","Snakes On The Moon?","Viva La Pluto","Jarvis Take The Wheel", "Grapic Design Is My Passion", "Let's McFreakin Lose It", "Lettuce Party"]))
main_title = ("Moon Machine: "+(random_message))
## ---  Pygame Is Initated Again --- ##
pygame.init()
## --- Screen And Title Is Set And Clock Is Defined --- ##
screen_main = pygame.display.set_mode(screen_res)
pygame.display.set_caption(main_title)
clock = pygame.time.Clock()

## --- Main Program Constants --- ##
healthup_cost = 15
firerate_cost = 25
power_cost = 30
speed_cost = 20

upgrade_scrnpos = [int((screen_res[0]-screen_res[0]/Med[0]*700)/2),int((screen_res[1]-screen_res[1]/Med[1]*400)/2)]
upgrade_iconsize = int(screen_res[0]/Med[0]*80)
upgrade_scrnsize = [int(screen_res[0]/Med[0]*700),int(screen_res[1]/Med[1]*400)]
heart1 = [[None,None,1,3],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+upgrade_iconsize*.8],healthup_cost,0,0]
heart2 = [[0,None,2,4],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+1*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],healthup_cost,0,1]
heart3 = [[1,None,12,5],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+2*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],healthup_cost,0,2]
fire1 = [[None,0,4,6],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+1*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+upgrade_iconsize*.8],firerate_cost,1,0]
fire2 = [[3,1,5,7],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+1*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+1*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],firerate_cost,1,1]
fire3 = [[4,2,12,8],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+1*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+2*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],firerate_cost,1,2]
power1 = [[None,3,7,9],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+2*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+upgrade_iconsize*.8],power_cost,2,0]
power2 = [[6,4,8,10],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+2*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+1*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],power_cost,2,1]
power3 = [[7,5,12,11],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+2*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+2*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],power_cost,2,2]
speed1 = [[None,6,10,None],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+3*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+upgrade_iconsize*.8],speed_cost,3,0]
speed2 = [[9,7,11,None],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+3*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+1*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],speed_cost,3,1]
speed3 = [[10,8,12,None],[upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+3*upgrade_scrnsize[0]/5+upgrade_iconsize*.8,upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+2*(upgrade_iconsize+30*screen_res[0]/Med[0])+upgrade_iconsize*.8],speed_cost,3,2]
nextwavebutton = [[2,None,None,13],[upgrade_scrnpos[0]+upgrade_scrnsize[0]*3.9/5,upgrade_scrnpos[1]+upgrade_scrnsize[1]*24/25],4]
quitbutton = [[None,12,None,None],[upgrade_scrnpos[0]+upgrade_scrnsize[0]*24/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*24/25],4]

                  
upgrade_pointer_poslist = [heart1,heart2,heart3,fire1,fire2,fire3,power1,power2,power3,speed1,speed2,speed3,nextwavebutton,quitbutton]
purchase_pos = [upgrade_scrnpos[0]+upgrade_scrnsize[0]*24/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*19/25]
price_pos = [upgrade_scrnpos[0]+upgrade_scrnsize[0]*21.2/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*18.4/25]
             
# -- Map Variables -- #        
screen_map_ratio = 9
map_size = screen_map_ratio*screen_res[0]
# -- Determines the position on the Y-Axis on which the player is standing -- #
ground_level = int(125 * screen_res[0]/Med[0])

player_height = int(screen_res[1]/5)
player_width = int(player_height/2)

    # -- Literally exactly what the variable is called -- #
initial_jump_velocity = 30 * screen_res[0]/Med[0]
    # -- Can you guess -- #
player_speed = int(screen_res[0]*15/Med[0])
player_damage = 10
player_damage_invuln = 40
    # -- Speed while strafing in the air -- #
jump_speed = int(player_speed)

projectile_width = int(40*screen_res[0]/Med[0])
projectile_height = int(5*screen_res[0]/Med[0])

    # -- Variable used to shuffle through sprites to create a walking animation -- #
walk = 6

change_pos_delay = 3

game_font_1 = pygame.font.SysFont('Calibri', math.ceil(25 * screen_res[0]/Med[0]), True, False)

    # -- Enemy Stuff -- #
spawn_list = []
for i in range(15):
    spawn_list.append("wisp")
for i in range(15):
    spawn_list.append("slime")
for i in range(15):
    spawn_list.append("screamer")
for i in range(15):
    spawn_list.append("thief")
for i in range(20):
    spawn_list.append("snake")
for i in range(10):
    spawn_list.append("tank")
for i in range(10):
    spawn_list.append("cloud")
    
wisp_speed = int(7 * screen_res[0]/Med[0])
wisp_attack_delay = 60
wisp_projectile_speed = 16
wisp_projectile_size = int(screen_res[0]/30)
wisp_size = int(screen_res[0]/14)
wisp_damage = 1
wisp_knockback = 30*screen_res[0]/Med[0]
wisp_health = 40
wisp_pv = 4

slime_speed = int(9 * screen_res[0]/Med[0])
slime_jump_delay = 30
slime_size = int(screen_res[0]/15)
slime_damage = 1
slime_knockback = 40 * screen_res[0]/Med[0]
slime_health = 70
slime_pv = 3

screamer_speed = 7
screamer_size = int(screen_res[0]/20)
screamer_damage = 1
screamer_knockback = 50 * screen_res[0]/Med[0]
screamer_health = 70
screamer_pv = 4
screamer_sounddelay = 90

thief_speed = 8 * screen_res[0]/Med[0]
thief_size = int(screen_res[0]/17)
thief_health = 20
thief_damage = 1
thief_knockback = 45 * screen_res[0]/Med[0]
thief_pv = 3

snake_speed = 14 * screen_res[0]/Med[0]
snake_size = int(screen_res[0]/14)
snake_health = 60
snake_damage = 1
snake_knockback = 40 * screen_res[0]/Med[0]
snake_pv = 2
snake_cooldown = 30
snake_charge_frames = 10

tank_speed = 6
tank_size = int(screen_res[0]/6)
tank_health = 200
tank_damage = 2
tank_knockback = 30 * screen_res[0]/Med[0]
tank_pv = 5

cloud_speed = 6
cloud_size = int(screen_res[0]/14)
cloud_health = 30
cloud_damage = 1
cloud_knockback = 30 * screen_res[0]/Med[0]
cloud_pv = 3
cloud_cooldown = 3
cloud_rain_size = (4*screen_res[0]/Med[0],20*screen_res[0]/Med[0])
cloud_rain_speed = 20

mainloop_variables()

## --- Loading And Scaling Sprites and Images --- ##
    # -- Player Sprites -- #
look_right = pygame.image.load("GameFiles/Sprites/look_right.png").convert_alpha()
look_right = pygame.transform.scale(look_right, (player_width, player_height))
walk_one_right = pygame.image.load("GameFiles/Sprites/walk_one_right.png").convert_alpha()
walk_one_right = pygame.transform.scale(walk_one_right, (player_width, player_height))
walk_two_right = pygame.image.load("GameFiles/Sprites/walk_two_right.png").convert_alpha()
walk_two_right = pygame.transform.scale(walk_two_right, (player_width, player_height))
look_left = pygame.image.load("GameFiles/Sprites/look_left.png").convert_alpha()
look_left = pygame.transform.scale(look_left, (player_width, player_height))
walk_one_left = pygame.image.load("GameFiles/Sprites/walk_one_left.png").convert_alpha()
walk_one_left = pygame.transform.scale(walk_one_left, (player_width, player_height))
walk_two_left = pygame.image.load("GameFiles/Sprites/walk_two_left.png").convert_alpha()
walk_two_left = pygame.transform.scale(walk_two_left, (player_width, player_height))

projectile_left = pygame.image.load("GameFiles/Sprites/projectile_left.png").convert_alpha()
projectile_left = pygame.transform.scale(projectile_left, (projectile_width, projectile_height))
projectile_right = pygame.image.load("GameFiles/Sprites/projectile_right.png").convert_alpha()
projectile_right = pygame.transform.scale(projectile_right, (projectile_width, projectile_height))
    # -- Wisp Sprites -- #
wisp_blue_left = pygame.image.load("GameFiles/Sprites/wisp_blue_left.png").convert_alpha()
wisp_blue_left = pygame.transform.scale(wisp_blue_left, (wisp_size, wisp_size))
wisp_blue_right = pygame.image.load("GameFiles/Sprites/wisp_blue_right.png").convert_alpha()
wisp_blue_right = pygame.transform.scale(wisp_blue_right, (wisp_size, wisp_size))
wisp_red_left = pygame.image.load("GameFiles/Sprites/wisp_red_left.png").convert_alpha()
wisp_red_left = pygame.transform.scale(wisp_red_left, (wisp_size, wisp_size))
wisp_red_right = pygame.image.load("GameFiles/Sprites/wisp_red_right.png").convert_alpha()
wisp_red_right = pygame.transform.scale(wisp_red_right, (wisp_size, wisp_size))
wisp_projectile = pygame.image.load("GameFiles/Sprites/wisp_projectile.png").convert_alpha()
wisp_projectile = pygame.transform.scale(wisp_projectile, (wisp_projectile_size, wisp_projectile_size))
    # -- Slime Sprites -- #
slime_right = pygame.image.load("GameFiles/Sprites/slime_right.png").convert_alpha()
slime_right = pygame.transform.scale(slime_right, [slime_size,slime_size])
slime_left = pygame.image.load("GameFiles/Sprites/slime_left.png").convert_alpha()
slime_left = pygame.transform.scale(slime_left, [slime_size,slime_size])
slime_right_jump = pygame.image.load("GameFiles/Sprites/slime_right_jump.png").convert_alpha()
slime_right_jump = pygame.transform.scale(slime_right_jump, [slime_size,2*slime_size])
slime_left_jump = pygame.image.load("GameFiles/Sprites/slime_left_jump.png").convert_alpha()
slime_left_jump = pygame.transform.scale(slime_left_jump, [slime_size,2*slime_size])
    # -- Screamer Sprites -- #
screamer_left_1 = pygame.image.load("GameFiles/Sprites/screamer_left_1.png").convert_alpha()
screamer_left_1 = pygame.transform.scale(screamer_left_1, [2*screamer_size,screamer_size])
screamer_left_2 = pygame.image.load("GameFiles/Sprites/screamer_left_2.png").convert_alpha()
screamer_left_2 = pygame.transform.scale(screamer_left_2, [2*screamer_size,screamer_size])
screamer_right_1 = pygame.image.load("GameFiles/Sprites/screamer_right_1.png").convert_alpha()
screamer_right_1 = pygame.transform.scale(screamer_right_1, [2*screamer_size,screamer_size])
screamer_right_2 = pygame.image.load("GameFiles/Sprites/screamer_right_2.png").convert_alpha()
screamer_right_2 = pygame.transform.scale(screamer_right_2, [2*screamer_size,screamer_size])
    # -- Thief Sprites -- #
thief_left = pygame.image.load("GameFiles/Sprites/thief_left.png").convert_alpha()
thief_left = pygame.transform.scale(thief_left, [thief_size,2*thief_size])
thief_right = pygame.image.load("GameFiles/Sprites/thief_right.png").convert_alpha()
thief_right = pygame.transform.scale(thief_right, [thief_size,2*thief_size])
    # -- Snake Sprites -- #
snake_left_1 = pygame.image.load("GameFiles/Sprites/snake_left_1.png").convert_alpha()
snake_left_1 = pygame.transform.scale(snake_left_1, [snake_size,snake_size])
snake_right_1 = pygame.image.load("GameFiles/Sprites/snake_right_1.png").convert_alpha()
snake_right_1 = pygame.transform.scale(snake_right_1, [snake_size,snake_size])
snake_left_2 = pygame.image.load("GameFiles/Sprites/snake_left_2.png").convert_alpha()
snake_left_2 = pygame.transform.scale(snake_left_2, [int(3*snake_size/2),snake_size])
snake_right_2 = pygame.image.load("GameFiles/Sprites/snake_right_2.png").convert_alpha()
snake_right_2 = pygame.transform.scale(snake_right_2, [int(3*snake_size/2),snake_size])
    # -- Tank Sprites -- #
tank_right_0_0 = pygame.image.load("GameFiles/Sprites/tank_right_0_0.png").convert_alpha()
tank_right_0_0 = pygame.transform.scale(tank_right_0_0, [2*tank_size,tank_size])
tank_right_0_1 = pygame.image.load("GameFiles/Sprites/tank_right_0_1.png").convert_alpha() 
tank_right_0_1 = pygame.transform.scale(tank_right_0_1, [2*tank_size,tank_size])
tank_right_1_0 = pygame.image.load("GameFiles/Sprites/tank_right_1_0.png").convert_alpha()
tank_right_1_0 = pygame.transform.scale(tank_right_1_0, [2*tank_size,tank_size])
tank_right_1_1 = pygame.image.load("GameFiles/Sprites/tank_right_1_1.png").convert_alpha()
tank_right_1_1 = pygame.transform.scale(tank_right_1_1, [2*tank_size,tank_size])
tank_left_0_0 = pygame.image.load("GameFiles/Sprites/tank_left_0_0.png").convert_alpha()
tank_left_0_0 = pygame.transform.scale(tank_left_0_0, [2*tank_size,tank_size])
tank_left_0_1 = pygame.image.load("GameFiles/Sprites/tank_left_0_1.png").convert_alpha()
tank_left_0_1 = pygame.transform.scale(tank_left_0_1, [2*tank_size,tank_size])
tank_left_1_0 = pygame.image.load("GameFiles/Sprites/tank_left_1_0.png").convert_alpha()
tank_left_1_0 = pygame.transform.scale(tank_left_1_0, [2*tank_size,tank_size])
tank_left_1_1 = pygame.image.load("GameFiles/Sprites/tank_left_1_1.png").convert_alpha()
tank_left_1_1 = pygame.transform.scale(tank_left_1_1, [2*tank_size,tank_size])
    # -- Cloud Sprites -- #
cloud = pygame.image.load("GameFiles/Sprites/cloud.png").convert_alpha()
cloud = pygame.transform.scale(cloud, [2*cloud_size,cloud_size])

## --- Damaged Enemy Sprites --- ##
    # -- Wisp Sprites -- #
wisph_blue_left = pygame.image.load("GameFiles/Sprites/wisph_blue_left.png").convert_alpha()
wisph_blue_left = pygame.transform.scale(wisph_blue_left, (wisp_size, wisp_size))
wisph_blue_right = pygame.image.load("GameFiles/Sprites/wisph_blue_right.png").convert_alpha()
wisph_blue_right = pygame.transform.scale(wisph_blue_right, (wisp_size, wisp_size))
wisph_red_left = pygame.image.load("GameFiles/Sprites/wisph_red_left.png").convert_alpha()
wisph_red_left = pygame.transform.scale(wisph_red_left, (wisp_size, wisp_size))
wisph_red_right = pygame.image.load("GameFiles/Sprites/wisph_red_right.png").convert_alpha()
wisph_red_right = pygame.transform.scale(wisph_red_right, (wisp_size, wisp_size))
    # -- Slime Sprites -- #
slimeh_right = pygame.image.load("GameFiles/Sprites/slimeh_right.png").convert_alpha()
slimeh_right = pygame.transform.scale(slimeh_right, [slime_size,slime_size])
slimeh_left = pygame.image.load("GameFiles/Sprites/slimeh_left.png").convert_alpha()
slimeh_left = pygame.transform.scale(slimeh_left, [slime_size,slime_size])
slimeh_right_jump = pygame.image.load("GameFiles/Sprites/slimeh_right_jump.png").convert_alpha()
slimeh_right_jump = pygame.transform.scale(slimeh_right_jump, [slime_size,2*slime_size])
slimeh_left_jump = pygame.image.load("GameFiles/Sprites/slimeh_left_jump.png").convert_alpha()
slimeh_left_jump = pygame.transform.scale(slimeh_left_jump, [slime_size,2*slime_size])
    # -- Screamer Sprites -- #
screamerh_left_1 = pygame.image.load("GameFiles/Sprites/screamerh_left_1.png").convert_alpha()
screamerh_left_1 = pygame.transform.scale(screamerh_left_1, [2*screamer_size,screamer_size])
screamerh_left_2 = pygame.image.load("GameFiles/Sprites/screamerh_left_2.png").convert_alpha()
screamerh_left_2 = pygame.transform.scale(screamerh_left_2, [2*screamer_size,screamer_size])
screamerh_right_1 = pygame.image.load("GameFiles/Sprites/screamerh_right_1.png").convert_alpha()
screamerh_right_1 = pygame.transform.scale(screamerh_right_1, [2*screamer_size,screamer_size])
screamerh_right_2 = pygame.image.load("GameFiles/Sprites/screamerh_right_2.png").convert_alpha()
screamerh_right_2 = pygame.transform.scale(screamerh_right_2, [2*screamer_size,screamer_size])
    # -- Thief Sprites -- #
thiefh_left = pygame.image.load("GameFiles/Sprites/thiefh_left.png").convert_alpha()
thiefh_left = pygame.transform.scale(thiefh_left, [thief_size,2*thief_size])
thiefh_right = pygame.image.load("GameFiles/Sprites/thiefh_right.png").convert_alpha()
thiefh_right = pygame.transform.scale(thiefh_right, [thief_size,2*thief_size])
    # -- Snake Sprites -- #
snakeh_left_1 = pygame.image.load("GameFiles/Sprites/snakeh_left_1.png").convert_alpha()
snakeh_left_1 = pygame.transform.scale(snakeh_left_1, [snake_size,snake_size])
snakeh_right_1 = pygame.image.load("GameFiles/Sprites/snakeh_right_1.png").convert_alpha()
snakeh_right_1 = pygame.transform.scale(snakeh_right_1, [snake_size,snake_size])
snakeh_left_2 = pygame.image.load("GameFiles/Sprites/snakeh_left_2.png").convert_alpha()
snakeh_left_2 = pygame.transform.scale(snakeh_left_2, [int(3*snake_size/2),snake_size])
snakeh_right_2 = pygame.image.load("GameFiles/Sprites/snakeh_right_2.png").convert_alpha()
snakeh_right_2 = pygame.transform.scale(snakeh_right_2, [int(3*snake_size/2),snake_size])
    # -- Tank Sprites -- #
tankh_right_0_0 = pygame.image.load("GameFiles/Sprites/tankh_right_0_0.png").convert_alpha()
tankh_right_0_0 = pygame.transform.scale(tankh_right_0_0, [2*tank_size,tank_size])
tankh_right_0_1 = pygame.image.load("GameFiles/Sprites/tankh_right_0_1.png").convert_alpha() 
tankh_right_0_1 = pygame.transform.scale(tankh_right_0_1, [2*tank_size,tank_size])
tankh_right_1_0 = pygame.image.load("GameFiles/Sprites/tankh_right_1_0.png").convert_alpha()
tankh_right_1_0 = pygame.transform.scale(tankh_right_1_0, [2*tank_size,tank_size])
tankh_right_1_1 = pygame.image.load("GameFiles/Sprites/tankh_right_1_1.png").convert_alpha()
tankh_right_1_1 = pygame.transform.scale(tankh_right_1_1, [2*tank_size,tank_size])
tankh_left_0_0 = pygame.image.load("GameFiles/Sprites/tankh_left_0_0.png").convert_alpha()
tankh_left_0_0 = pygame.transform.scale(tankh_left_0_0, [2*tank_size,tank_size])
tankh_left_0_1 = pygame.image.load("GameFiles/Sprites/tankh_left_0_1.png").convert_alpha()
tankh_left_0_1 = pygame.transform.scale(tankh_left_0_1, [2*tank_size,tank_size])
tankh_left_1_0 = pygame.image.load("GameFiles/Sprites/tankh_left_1_0.png").convert_alpha()
tankh_left_1_0 = pygame.transform.scale(tankh_left_1_0, [2*tank_size,tank_size])
tankh_left_1_1 = pygame.image.load("GameFiles/Sprites/tankh_left_1_1.png").convert_alpha()
tankh_left_1_1 = pygame.transform.scale(tankh_left_1_1, [2*tank_size,tank_size])
    # -- Cloud Sprites -- #
cloudh = pygame.image.load("GameFiles/Sprites/cloudh.png").convert_alpha()
cloudh = pygame.transform.scale(cloudh, [2*cloud_size,cloud_size])

full_heart = pygame.image.load("GameFiles/Images/full_heart.png").convert_alpha()
full_heart = pygame.transform.scale(full_heart, (int(screen_res[0]/40),int(screen_res[0]/45)))
half_heart = pygame.image.load("GameFiles/Images/half_heart.png").convert_alpha()
half_heart = pygame.transform.scale(half_heart, (int(screen_res[0]/40),int(screen_res[0]/45)))
empty_heart = pygame.image.load("GameFiles/Images/empty_heart.png").convert_alpha()
empty_heart = pygame.transform.scale(empty_heart, (int(screen_res[0]/40),int(screen_res[0]/45)))

foreground = pygame.image.load("GameFiles/Images/foreground.png").convert_alpha()
foreground = pygame.transform.scale(foreground, (3*screen_res[0],int(125*screen_res[0]/Med[0])))

background = pygame.image.load("GameFiles/Images/background.png").convert_alpha()
background = pygame.transform.scale(background, (3*screen_res[0],screen_res[1]-int(125*screen_res[0]/Med[0])))

titlescreen_background = pygame.image.load("GameFiles/Images/titlescreen_background.png").convert()
titlescreen_background = pygame.transform.scale(titlescreen_background,(screen_res))

credits_background = pygame.image.load("GameFiles/Images/credits_background.png").convert()
credits_background = pygame.transform.scale(credits_background,(screen_res))

upgrade_background = pygame.image.load("GameFiles/Images/upgrade_background.png").convert_alpha()
upgrade_background = pygame.transform.scale(upgrade_background,(upgrade_scrnsize))

gameover_display = pygame.image.load("GameFiles/Images/gameover_display.png").convert()
gameover_display = pygame.transform.scale(gameover_display,(screen_res))

healthup_available = pygame.image.load("GameFiles/Images/healthup_available.png").convert_alpha()
healthup_available = pygame.transform.scale(healthup_available,(upgrade_iconsize,upgrade_iconsize))
healthup_notavailable = pygame.image.load("GameFiles/Images/healthup_notavailable.png").convert_alpha()
healthup_notavailable = pygame.transform.scale(healthup_notavailable,(upgrade_iconsize,upgrade_iconsize))
healthup_purchased = pygame.image.load("GameFiles/Images/healthup_purchased.png").convert_alpha()
healthup_purchased = pygame.transform.scale(healthup_purchased,(upgrade_iconsize,upgrade_iconsize))

firerate_available = pygame.image.load("GameFiles/Images/firerate_available.png").convert_alpha()
firerate_available = pygame.transform.scale(firerate_available,(upgrade_iconsize,upgrade_iconsize))
firerate_notavailable = pygame.image.load("GameFiles/Images/firerate_notavailable.png").convert_alpha()
firerate_notavailable = pygame.transform.scale(firerate_notavailable,(upgrade_iconsize,upgrade_iconsize))
firerate_purchased = pygame.image.load("GameFiles/Images/firerate_purchased.png").convert_alpha()
firerate_purchased = pygame.transform.scale(firerate_purchased,(upgrade_iconsize,upgrade_iconsize))

power_available = pygame.image.load("GameFiles/Images/power_available.png").convert_alpha()
power_available = pygame.transform.scale(power_available,(upgrade_iconsize,upgrade_iconsize))
power_notavailable = pygame.image.load("GameFiles/Images/power_notavailable.png").convert_alpha()
power_notavailable = pygame.transform.scale(power_notavailable,(upgrade_iconsize,upgrade_iconsize))
power_purchased = pygame.image.load("GameFiles/Images/power_purchased.png").convert_alpha()
power_purchased = pygame.transform.scale(power_purchased,(upgrade_iconsize,upgrade_iconsize))

speed_available = pygame.image.load("GameFiles/Images/speed_available.png").convert_alpha()
speed_available = pygame.transform.scale(speed_available,(upgrade_iconsize,upgrade_iconsize))
speed_notavailable = pygame.image.load("GameFiles/Images/speed_notavailable.png").convert_alpha()
speed_notavailable = pygame.transform.scale(speed_notavailable,(upgrade_iconsize,upgrade_iconsize))
speed_purchased = pygame.image.load("GameFiles/Images/speed_purchased.png").convert_alpha()
speed_purchased = pygame.transform.scale(speed_purchased,(upgrade_iconsize,upgrade_iconsize))

health_refill = pygame.image.load("GameFiles/Images/health_refill.png").convert_alpha()
health_refill = pygame.transform.scale(health_refill,(int(screen_res[0]/Med[0]*200),int(screen_res[1]/Med[1]*100)))

main_pointer = pygame.image.load("GameFiles/Images/pointer.png").convert_alpha()
main_pointer = pygame.transform.scale(main_pointer,(int(35*screen_res[0]/Med[0]),int(35*screen_res[0]/Med[0])))
                                       
## --- Sound Files --- ##
pygame.mixer.init(frequency=22050, size=16, channels=2, buffer=4096)
before_wave = pygame.mixer.Sound("GameFiles/Sound/before_wave.wav")
before_wave.set_volume(music_volume/250)
before_wave = [before_wave,30*(pygame.mixer.Sound.get_length(before_wave)),0]
during_wave = pygame.mixer.Sound("GameFiles/Sound/during_wave.wav")
during_wave.set_volume(music_volume/200)
during_wave = [during_wave,30*(pygame.mixer.Sound.get_length(during_wave)),0]
cloud_death = pygame.mixer.Sound("GameFiles/Sound/cloud_death.wav")#
cloud_death.set_volume(sfx_volume/100)
enemy_hit = pygame.mixer.Sound("GameFiles/Sound/enemy_hit.wav")#
enemy_hit.set_volume(sfx_volume/100)
player_death = pygame.mixer.Sound("GameFiles/Sound/player_death.wav")
player_death.set_volume(sfx_volume/100)
player_hit = pygame.mixer.Sound("GameFiles/Sound/player_hit.wav")#
player_hit.set_volume(sfx_volume/100)
player_jump = pygame.mixer.Sound("GameFiles/Sound/player_jump.wav")#
player_jump.set_volume(sfx_volume/100)
player_shoot = pygame.mixer.Sound("GameFiles/Sound/player_shoot.wav")#
player_shoot.set_volume(sfx_volume/100)
screamer_death = pygame.mixer.Sound("GameFiles/Sound/screamer_death.wav")#
screamer_death.set_volume(sfx_volume/100)
screamer_general = pygame.mixer.Sound("GameFiles/Sound/screamer_general.wav")
screamer_general.set_volume(sfx_volume/100)
slime_death = pygame.mixer.Sound("GameFiles/Sound/slime_death.wav")#
slime_death.set_volume(sfx_volume/100)
slime_landing = pygame.mixer.Sound("GameFiles/Sound/slime_landing.wav")#
slime_landing.set_volume(sfx_volume/100)
snake_death = pygame.mixer.Sound("GameFiles/Sound/snake_death.wav")#
snake_death.set_volume(sfx_volume/100)
snake_general = pygame.mixer.Sound("GameFiles/Sound/snake_general.wav")
snake_general.set_volume(sfx_volume/100)
thief_death = pygame.mixer.Sound("GameFiles/Sound/thief_death.wav")#
thief_death.set_volume(sfx_volume/100)
wave_start = pygame.mixer.Sound("GameFiles/Sound/wave_start.wav")
wave_start.set_volume(sfx_volume/100)
wave_start = pygame.mixer.Sound("GameFiles/Sound/wave_start.wav")
wave_start.set_volume(sfx_volume/100)
wave_end = pygame.mixer.Sound("GameFiles/Sound/wave_end.wav")
wave_end.set_volume(sfx_volume/100)
wisp_death = pygame.mixer.Sound("GameFiles/Sound/wisp_death.wav")#
wisp_death.set_volume(sfx_volume/100)
wisp_shoot = pygame.mixer.Sound("GameFiles/Sound/wisp_shoot.wav")#
wisp_shoot.set_volume(sfx_volume/100)

current_music = before_wave

sprite_list = [look_right, walk_one_right, walk_two_right, look_left, walk_one_left, walk_two_left]
current_sprite = sprite_list[0]
walking_sprite = sprite_list[1]

## --- Main Window Starts --- ##
while not done_main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done_main = True
        ## --- If a key is pressed --- ##    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keys[0] = True    
            if event.key == pygame.K_d:
                keys[1] = True
            if event.key == pygame.K_w:
                keys[2] = True
            if event.key == pygame.K_s:
                keys[3] = True
            if event.key == pygame.K_LEFT:
                keys[4] = True
            if event.key == pygame.K_RIGHT:
                keys[5] = True
            if event.key == pygame.K_q:
                keys[6] = True
            if event.key == pygame.K_e:
                keys[7] = True
            if event.key == pygame.K_UP:
                keys[8] = True
            if event.key == pygame.K_DOWN:
                keys[9] = True
            if event.key == pygame.K_ESCAPE:
                keys[10] = True
            if event.key == pygame.K_LCTRL:
                godmode[0] = True
            if event.key == pygame.K_KP_PLUS:
                godmode[1] = True

        ## --- If a key is released --- ##
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys[0] = False
            if event.key == pygame.K_d:
                keys[1] = False
            if event.key == pygame.K_w:
                keys[2] = False
            if event.key == pygame.K_s:
                keys[3] = False
            if event.key == pygame.K_LEFT:
                keys[4] = False
            if event.key == pygame.K_RIGHT:
                keys[5] = False  
            if event.key == pygame.K_q:
                keys[6] = False
            if event.key == pygame.K_e:
                keys[7] = False
            if event.key == pygame.K_UP:
                keys[8] = False
            if event.key == pygame.K_DOWN:
                keys[9] = False
            if event.key == pygame.K_ESCAPE:
                keys[10] = False
            if event.key == pygame.K_LCTRL:
                godmode[0] = False
            if event.key == pygame.K_KP_PLUS:
                godmode[1] = False

    if player_stats[0] <= 0:
        gameover = True
        wave_time = False
    if titlescreen or upgradescreen or pause:
        if not pause and current_music == during_wave:
            current_music[0].stop()
            current_music = before_wave
            current_music[2] = 0
        wave_time = False
    else:
        if current_music == before_wave:
            current_music[0].stop()
            current_music = during_wave
            current_music[2] = 0
        wave_time = True
        
    if keys[10] and change_pos < 1 and wave_time or button_values[2] == 1 and change_pos < 1 and wave_time:
        pause = True
        change_pos = change_pos_delay
        current_upgrade_pointpos = upgrade_pointer_poslist[13]
    else:
        change_pos -= 1
            
    
    
    # -- Getting the amount of joysticks -- #
    joystick_count = pygame.joystick.get_count()
    ## --- Initiates the controller stuff, if one is plugged in --- ##
    if joystick_count != 0: 
        my_joystick = pygame.joystick.Joystick(0)
        my_joystick.init()
        ## --- Adding the values of the buttons and analogs to a list each, analog values are multiplied by 10 --- ##
        analog_values = [my_joystick.get_axis(0)*10,my_joystick.get_axis(1)*10,my_joystick.get_axis(2)*10,my_joystick.get_axis(3)*10]
        button_values = [my_joystick.get_button(0),my_joystick.get_button(1),my_joystick.get_button(2),my_joystick.get_button(3),my_joystick.get_button(4),my_joystick.get_button(5),my_joystick.get_button(6),my_joystick.get_button(7)]

    player_stats = [player_stats[0],14+2*upgrades[0],1.0+2**upgrades[1]/15,1.0+.5*upgrades[2],1.0+.2*upgrades[2]]        
    player_center = (player_x + (int(player_width/2)),player_y + (int(player_height/2)))    
    ## --- Variable for Invincibility After being hit - if its above 0 you can't be hit --- ##
    if invincible == player_damage_invuln:
        player_hit.play()
    if wave_time:
        invincible -= 1
        
    ## --- Foreground --- ##
    if not titlescreen:
        screen_main.blit(background,[background_pos1,0])
        screen_main.blit(background,[background_pos2,0])
        screen_main.blit(foreground,[int(foreground_pos1),screen_res[1]-125*screen_res[0]/Med[0]])
        screen_main.blit(foreground,[int(foreground_pos2),screen_res[1]-125*screen_res[0]/Med[0]])
        
    foreground_pos1 += player_movement
    foreground_pos2 += player_movement
    
    background_pos1 += player_movement/5
    background_pos2 += player_movement/5
    
    if foreground_pos1 <= -2*screen_res[0] and foreground_pos2 < foreground_pos1:
        foreground_pos2 += 6*screen_res[0]
    elif foreground_pos2 <= -2*screen_res[0] and  foreground_pos1 < foreground_pos2:
        foreground_pos1 += 6*screen_res[0]
    elif foreground_pos1 >= 0 and foreground_pos2 > foreground_pos1:
        foreground_pos2 -= 6*screen_res[0]
    elif foreground_pos2 >= 0 and foreground_pos1 > foreground_pos2:
        foreground_pos1 -= 6*screen_res[0]

    if background_pos1 <= -2*screen_res[0] and background_pos2 < background_pos1:
        background_pos2 += 6*screen_res[0]
    elif background_pos2 <= -2*screen_res[0] and  background_pos1 < background_pos2:
        background_pos1 += 6*screen_res[0]
    elif background_pos1 >= 0 and background_pos2 > background_pos1:
        background_pos2 -= 6*screen_res[0]
    elif background_pos2 >= 0 and background_pos1 > background_pos2:
        background_pos1 -= 6*screen_res[0]
    
    ## --- Movement --- ##
    if -5 > analog_values[0] and wave_time or  analog_values[0] > 5 and wave_time  or keys[1] and wave_time or keys[0] and wave_time:
        if analog_values[0] > 5 or keys[1]:
            if jumping:
                player_movement = -jump_speed*player_stats[4]
            else:
                player_movement = -player_speed*player_stats[4]
            current_sprite = sprite_list[0]
            
        elif analog_values[0] < -5 or keys[0]:
            if jumping:
                player_movement = jump_speed*player_stats[4]
            else:    
                player_movement = player_speed*player_stats[4]
            current_sprite = sprite_list[3]
        walking = True
    else:
        player_movement = 0
    player_center = (player_x + (int(3*player_width/7)),player_y + (int(player_height/2)))
    
   
    ## --- Knockback --- ##
    for i in range(len(knockback)):
        if i == 0:
            x = 0
        player_movement+=knockback[i-x][0]*knockback[i-x][3]
        knockback[i-x][1]-=1
        if knockback[i-x][2] and not jumping:
            vertical_velocity += int(slime_knockback/-2)
            jumping = True
            knockback[i-x][2]= False
        if knockback[i-x][1] < 1:
            knockback.pop(i-x)
            x+=1 
        
    ## --- Player Projectiles --- ##
    if button_values[5] == 1 and shot_delay <= 0 and wave_time or keys[8] and shot_delay <= 0 and wave_time:
        shot_delay = 11/player_stats[2]
        player_shoot.play()
        player_shots = True
        if looking_right:
            player_projectiles.append([player_x+player_width,player_y+5.4*player_height/10,1])
        else:
            player_projectiles.append([player_x-projectile_width,player_y+5.4*player_height/10,-1])
    if player_shots:
        shot_delay -= 1
        x = 0
        for i in range(len(player_projectiles)):
            if player_projectiles[i-x][2] == 1:
                screen_main.blit(projectile_right,[player_projectiles[i-x][0],player_projectiles[i-x][1]])
                player_projectiles[i-x][0] += 30*screen_res[0]/Med[0] + player_movement
            else:
                screen_main.blit(projectile_left,[player_projectiles[i-x][0],player_projectiles[i-x][1]])
                player_projectiles[i-x][0] -= 30*screen_res[0]/Med[0] - player_movement

            if not check_collision(player_projectiles[i-x][0],0,player_projectiles[i-x][1],0,projectile_width,screen_res[0],projectile_height,screen_res[1]):
                player_projectiles.pop(i-x)
                x+=1
            
    ## --- Jumping --- ##
    if jumping:
        player_y += vertical_velocity
        if keys[3] or analog_values[1] > 5:
            vertical_velocity += 3*gravity
        else:
            vertical_velocity += gravity
        if player_y + vertical_velocity >= screen_res[1]-player_height-ground_level:
            player_y = screen_res[1]-player_height-ground_level
            jumping = False
    elif button_values[4] == 1 and wave_time or keys[2] and wave_time:
        vertical_velocity = -initial_jump_velocity
        player_jump.play()
        jumping = True    
    
    
    ## --- Walking animation --- ##
    elif walking and wave_time: 
        if analog_values[0] > 5 or keys[1]:
            sprite_number = walk
            if sprite_number == 1 or sprite_number == 3 or sprite_number == 5:
                sprite_number += 1
            walking_sprite = sprite_list[int(sprite_number/2-1)]
            walk+=1
            if walk > 6:
                walk = 1
        elif analog_values[0] < -5 or keys[0]:
            sprite_number = walk
            if sprite_number == 1 or sprite_number == 3 or sprite_number == 5:
                sprite_number += 1
            walking_sprite = sprite_list[int(sprite_number/2+2)]
            walk+=1
            if walk > 6:
                walk = 1               
        else:
            walking = False
            
    ## --- Changing Direction --- ##
    if analog_values[2] > 5 or keys[5] and wave_time:
        current_sprite = sprite_list[0]
        if walking_sprite == sprite_list[3]:
            walking_sprite = sprite_list[0]    
        elif walking_sprite == sprite_list[4]:
            walking_sprite = sprite_list[1] 
        elif walking_sprite == sprite_list[5]:
            walking_sprite = sprite_list[2] 

    elif analog_values[2] < -5 or keys[4] and wave_time:
        current_sprite = sprite_list[3]
        if walking_sprite == sprite_list[0]:
            walking_sprite = sprite_list[3]    
        elif walking_sprite == sprite_list[1]:
            walking_sprite = sprite_list[4] 
        elif walking_sprite == sprite_list[2]:
            walking_sprite = sprite_list[5]
            
    ## --- Updating Sprites --- ##
    if invincible < 1 and not titlescreen or invincible%4 >= 2 and not titlescreen:
        if walking and not jumping:
            screen_main.blit(walking_sprite, [player_x, player_y])
        elif not walking or jumping:
            screen_main.blit(current_sprite, [player_x, player_y])

    if current_sprite == sprite_list[0] or current_sprite == sprite_list[1] or current_sprite == sprite_list[2]:
        looking_right = True
    elif current_sprite == sprite_list[3] or current_sprite == sprite_list[4] or current_sprite == sprite_list[5]:
        looking_right = False
        
    ## --- Spawning Enemies --- ##
    
    if spawn and wave_time:
        wave_start.play()
        allowed_spawn = wave_pv
        spawns = []
        while allowed_spawn > 0:
            x = random.choice(spawn_list)
            spawns.append(x)
            if x == "wisp":
                allowed_spawn -= wisp_pv
            elif x == "slime":
                allowed_spawn -= slime_pv
            elif x == "screamer":
                allowed_spawn -= screamer_pv
            elif x == "thief":
                allowed_spawn -= thief_pv
            elif x == "snake":
                allowed_spawn -= snake_pv
            elif x == "tank":
                allowed_spawn -= tank_pv
            elif x == "cloud":
                allowed_spawn -= cloud_pv
        wisp_spawns = 0
        slime_spawns = 0
        screamer_spawns = 0
        thief_spawns = 0
        snake_spawns = 0
        tank_spawns = 0
        cloud_spawns = 0
        for i in range(len(spawns)):
            if spawns[i] == "wisp":
                wisp_spawns +=1
                enemy_count +=1
            elif spawns[i] == "slime":
                slime_spawns +=1
                enemy_count +=1
            elif spawns[i] == "screamer":
                screamer_spawns +=1
                enemy_count +=1
            elif spawns[i] == "thief":
                thief_spawns +=1
                enemy_count +=1
            elif spawns[i] == "snake":
                snake_spawns +=1
                enemy_count +=1
            elif spawns[i] == "tank":
                tank_spawns +=1
                enemy_count +=1
            elif spawns[i] == "cloud":
                cloud_spawns +=1
                enemy_count +=1               
        for i in range(wisp_spawns):
            spawn_enemy(1,random.choice([random.randrange(int((map_size-screen_res[0])/-2)-wisp_size, -wisp_size),random.randrange(screen_res[0],2*screen_res[0]-int(screen_res[0]/13))]),int(screen_res[1]/5))      
        for i in range(slime_spawns): 
            spawn_enemy(2,random.choice([random.randrange(int((map_size-screen_res[0])/-2)-slime_size, -slime_size),random.randrange(screen_res[0],2*screen_res[0]-int(screen_res[0]/13))]),screen_res[1]-ground_level-slime_size)
        for i in range(screamer_spawns): 
            spawn_enemy(3,random.choice([random.randrange(int((map_size-screen_res[0])/-2)-2*screamer_size, -2*screamer_size),random.randrange(screen_res[0],int((map_size-screen_res[0])/2)+screen_res[0])]),int(screen_res[1]/3))
        for i in range(thief_spawns): 
            spawn_enemy(4,random.choice([random.randrange(int((map_size-screen_res[0])/-2)-thief_size, -thief_size),random.randrange(screen_res[0],int((map_size-screen_res[0])/2)+screen_res[0])]),screen_res[1]-ground_level-thief_size*2)
        for i in range(snake_spawns): 
            spawn_enemy(5,random.choice([random.randrange(int((map_size-screen_res[0])/-2)-snake_size, -snake_size),random.randrange(screen_res[0],int((map_size-screen_res[0])/2)+screen_res[0])]),screen_res[1]-ground_level-snake_size)
        for i in range(tank_spawns): 
            spawn_enemy(6,random.choice([random.randrange(int((map_size-screen_res[0])/-2)-2*tank_size, -2*tank_size),random.randrange(screen_res[0],int((map_size-screen_res[0])/2)+screen_res[0])]),screen_res[1]-ground_level-tank_size)  
        for i in range(cloud_spawns):
            spawn_enemy(7,random.choice([random.randrange(int((map_size-screen_res[0])/-2)-2*cloud_size, -2*cloud_size),random.randrange(screen_res[0],int((map_size-screen_res[0])/2)+screen_res[0])]),screen_res[1]/5)      
        spawn = False
    if wave_time:  
        ## --- Wisps --- ##  
        for i in range(len(wisps)):
            # -- Map Looping -- #
            if wisps[i][0] < int((map_size-screen_res[0])/-2)-int(wisp_size/2):
                wisps[i][0] = int((map_size-screen_res[0])/2)+screen_res[0]-int(wisp_size/2)
            elif wisps[i][0] > int((map_size-screen_res[0])/2)+screen_res[0]-int(wisp_size/2):
                wisps[i][0] = int((map_size-screen_res[0])/-2)-int(wisp_size/2)
            # -- Defining the center of the enemy -- #
            wisp_center = (wisps[i])[0]+int(screen_res[0]/26)
            # -- Defining the distance from the player -- #
            distance_from_player = abs(player_center[0]-wisp_center)

            # -- Direction changes if the player is passed
            if wisp_center < player_center[0]:
                (wisps[i])[2] = 1
            elif wisp_center > player_center[0]:
                wisps[i][2] = -1
            # -- The wisp stops if it is in a certain range of the player -- #    
            if distance_from_player > 2*wisp_speed or walking:
                wisps[i][5] = False 
            elif distance_from_player <= 2*wisp_speed:
                (wisps[i])[5] = True
            # -- If the wisp is in range it starts shooting -- #
            if distance_from_player < int(screen_res[0]*2/5):
                if wisps[i][4] <= 0:
                    wisp_projectiles.append(add_projectile(((wisps[i])[0]+int(wisp_size/2)-int(wisp_projectile_size/2)),((wisps[i])[1]+int(wisp_size/2)-int(wisp_projectile_size/2)),player_center[0]-int(wisp_projectile_size/2),player_center[1]-int(wisp_projectile_size/2),wisp_projectile_speed))
                    wisps[i][4] = 60    
                wisps[i][4] -= 1
            elif wisps[i][4] > 20: 
                wisps[i][4] -= 1
            if wisps[i][4] < 30 and not wisps[i][7]:
                wisps[i][7] = True
            elif wisps[i][4] < 30 and wisps[i][7]:
                wisps[i][7] = False
            else:
                wisps[i][7] = False
            draw_wisp(wisps[i][0],wisps[i][1]+50*math.sin(wisps[i][6])*screen_res[0]/Med[0],i)  
            if not wisps[i][5]:
                wisps[i][0] += wisps[i][3]*wisps[i][2]
            wisps[i][0] += player_movement
            wisps[i][6] += .25
        for i in range(len(wisp_projectiles)):
            if i == 0:
                x = 0
            wisp_projectiles[i-x][0]+=wisp_projectiles[i-x][2]+player_movement 
            wisp_projectiles[i-x][1]+=wisp_projectiles[i-x][3]
            wisp_projectiles[i-x][4]+=3
            draw_projectiles(1,wisp_projectiles[i-x][0],wisp_projectiles[i-x][1],wisp_projectiles[i-x][4])

            if not check_collision(wisp_projectiles[i-x][0],0,wisp_projectiles[i-x][1],0,wisp_projectile_size,screen_res[0],wisp_projectile_size,screen_res[1]):
                wisp_projectiles.pop(i-x)
                x+=1
                
        ## --- Slimes --- ##
        for i in range(len(slimes)):
            # -- Map Looping -- #
            if slimes[i][0] < int((map_size-screen_res[0])/-2)-int(slime_size/2):
                slimes[i][0] = int((map_size-screen_res[0])/2)+screen_res[0]-int(slime_size/2)
            elif slimes[i][0] > int((map_size-screen_res[0])/2)+screen_res[0]-int(slime_size/2):
                slimes[i][0] = int((map_size-screen_res[0])/-2)-int(slime_size/2)
            # -- Defining the center of the enemy -- #
            slime_center = slimes[i][0]+int(slime_size/2)

            distance_from_player = abs(player_center[0]-slime_center)
            draw_slime(slimes[i][0],slimes[i][1],i)
               
            if slimes[i][6] <= 0:
                slimes[i][5] = 1
                slimes[i][4] = True
                slimes[i][6] = slime_jump_delay
                
            if slimes[i][4]:
                if slimes[i][1] - screen_res[0]/Med[0]*30*slimes[i][5]  >= screen_res[1]-ground_level-slime_size and slimes[i][5] < 0:
                    slime_landing.play()
                    slimes[i][1] = screen_res[1]-ground_level-slime_size
                    slimes[i][5] = 1
                    slimes[i][4] = False
                else:
                    slimes[i][1] -= screen_res[0]/Med[0]*30*slimes[i][5]
                    slimes[i][5] -= .07
                    slimes[i][0] += slimes[i][2]*slimes[i][3] + player_movement
            else:
                if slime_center < player_center[0]:
                    slimes[i][2] = 1
                elif slime_center > player_center[0]:
                    slimes[i][2] = -1
                slimes[i][0] += player_movement
                if slimes[i][1] == screen_res[1]-ground_level-slime_size:
                    slimes[i][6] -= 1

        ## --- Screamers --- ##
        for i in range(len(screamers)):
            if screamers[i][0] < int((map_size-screen_res[0])/-2)-int(screamer_size):
                screamers[i][0] = int((map_size-screen_res[0])/2)+screen_res[0]-int(screamer_size)
            elif screamers[i][0] > int((map_size-screen_res[0])/2)+screen_res[0]-int(screamer_size):
                screamers[i][0] = int((map_size-screen_res[0])/-2)-int(screamer_size)
            screamer_center = [screamers[i][0]+screamer_size,screamers[i][1]+int(screamer_size/2)]
            screamers[i][4]+=1
            distance_from_player = abs(player_center[0]-screamer_center[0])
            draw_screamer(screamers[i][0],screamers[i][1],i)

            if screamer_center[0] < player_center[0] - screamer_size*2:
                screamers[i][2] = 1
            elif screamer_center[0] > player_center[0] + screamer_size*2:
                screamers[i][2] = -1
        
            screamers[i][0]+=add_projectile(screamers[i][0],screamers[i][1],player_center[0],player_center[1],screamer_speed)[2] + player_movement
            if abs(player_center[1]-screamer_center[1]) < int(screen_res[1]/8):
                screamers[i][7]+= math.pi/16
                screamers[i][1]+= 10*math.sin(screamers[i][7])*screen_res[0]/Med[0]
            else: 
                screamers[i][7] = 0
                screamers[i][1]+=add_projectile(screamers[i][0],screamers[i][1],player_center[0],player_center[1],screamer_speed)[3]    

        ## --- Thiefs --- ##
        for i in range(len(thiefs)):
            if thiefs[i][0] < int((map_size-screen_res[0])/-2)-int(thief_size/2):
                thiefs[i][0] = int((map_size-screen_res[0])/2)+screen_res[0]-int(thief_size/2)
            elif thiefs[i][0] > int((map_size-screen_res[0])/2)+screen_res[0]-int(thief_size/2):
                thiefs[i][0] = int((map_size-screen_res[0])/-2)-int(thief_size/2)
            # -- Defining the center of the enemy -- #
            thief_center = thiefs[i][0]+int(thief_size/2)
            direction_1 = thiefs[i][2]
            
            if thief_center < player_center[0] - thief_size:
                thiefs[i][2] = 1
                
            elif thief_center > player_center[0] + thief_size:
                thiefs[i][2] = -1 

            if direction_1 != thiefs[i][2]:
                thiefs[i][4] = .1    
            if thiefs[i][4] < 1.6:
                thiefs[i][4]*=2
            
            thiefs[i][0] += thiefs[i][2]*thiefs[i][3]*thiefs[i][4] + player_movement
            draw_thief(thiefs[i][0],thiefs[i][1],i)
            
        ## --- Snakes --- ##
        for i in range(len(snakes)):
            if snakes[i][0] < int((map_size-screen_res[0])/-2)-int(snake_size/2):
                snakes[i][0] = int((map_size-screen_res[0])/2)+screen_res[0]-int(snake_size/2)
            elif snakes[i][0] > int((map_size-screen_res[0])/2)+screen_res[0]-int(snake_size/2):
                snakes[i][0] = int((map_size-screen_res[0])/-2)-int(snake_size/2)
            if snakes[i][5] <= 0:
                snakes[i][0]+=snakes[i][3]*snakes[i][2]
            else:
                snake_center = snakes[i][0]+snake_size
                snakes[i][0]+=snakes[i][3]*snakes[i][2]/3
                if snake_center > player_center[0]:
                    snakes[i][2] = -1
                else:
                    snakes[i][2] = 1
            snakes[i][0]+=player_movement
            snakes[i][5]-=1
            if snakes[i][5] < -snake_charge_frames:
                snakes[i][5] = snake_cooldown
            draw_snake(snakes[i][0],snakes[i][1],i)
            
        ## --- Tanks --- ##
        for i in range(len(tanks)):
            if tanks[i][0] < int((map_size-screen_res[0])/-2)-tank_size:
                tanks[i][0] = int((map_size-screen_res[0])/2)+screen_res[0]-tank_size
            elif tanks[i][0] > int((map_size-screen_res[0])/2)+screen_res[0]-tank_size:
                tanks[i][0] = int((map_size-screen_res[0])/-2)-tank_size
            tank_center = tanks[i][0]+tank_size
            if tank_center > player_center[0]:
                tanks[i][2] = -1
            else:
                tanks[i][2] = 1
            tanks[i][0] += tanks[i][3]*tanks[i][2] + player_movement
            draw_tank(tanks[i][0],tanks[i][1],i)
            tanks[i][5]+=1
            tanks[i][6]+=1

        ## --- Clouds --- ##
        for i in range(len(clouds)):
            cloud_center = clouds[i][0]+cloud_size
            distance_from_player = abs(player_center[0]-cloud_center)
            if clouds[i][0] < int((map_size-screen_res[0])/-2)-cloud_size:
                clouds[i][0] = int((map_size-screen_res[0])/2)+screen_res[0]-cloud_size
            elif clouds[i][0] > int((map_size-screen_res[0])/2)+screen_res[0]-cloud_size:
                clouds[i][0] = int((map_size-screen_res[0])/-2)-cloud_size
            cloud_center = clouds[i][0]+cloud_size
            if distance_from_player > screen_res[0]/8:
                if cloud_center > player_center[0]:
                    clouds[i][2] = -1
                else:
                    clouds[i][2] = 1
            clouds[i][0] += clouds[i][2]*clouds[i][3] + player_movement
            for j in range(len(clouds[i][7])):
                if j == 0: 
                    z = 0
                clouds[i][7][j-z][0] += clouds[i][2]*clouds[i][3] + player_movement
                pygame.draw.rect(screen_main,(255,random.randrange(0,120),random.randrange(0,120)),[clouds[i][7][j-z][0],clouds[i][7][j-z][1],cloud_rain_size[0],cloud_rain_size[1]])
                clouds[i][7][j-z][1]+=cloud_rain_speed
                if clouds[i][7][j-z][1] >= screen_res[1]-ground_level:
                   clouds[i][7].pop(j-z)
                   z+=1
            clouds[i][5]+=math.pi/16
            if clouds[i][6] <= 0:
                clouds[i][6] = cloud_cooldown
                clouds[i][7].append([random.randrange(int(clouds[i][0]),int(clouds[i][0]+2*cloud_size-cloud_rain_size[0])),clouds[i][1]+3*cloud_size/4])
            clouds[i][6] -= 1
            draw_cloud(clouds[i][0],clouds[i][1]+50*math.sin(clouds[i][5])*screen_res[0]/Med[0])
            
        ## --- Collision with enemies and projectiles + Deletion --- ##
        for i in range(len(wisp_projectiles)):
            if i == 0:
                x = 0
            if check_collision(wisp_projectiles[i-x][0],player_x,wisp_projectiles[i-x][1],player_y,wisp_projectile_size,player_width,wisp_projectile_size,player_height) and invincible < 1:
                player_stats[0] -= wisp_damage
                invincible = player_damage_invuln
                wisp_projectiles.pop(i-x)
                x+=1
        for i in range(len(wisps)):
            if check_collision(wisps[i][0],player_x,wisps[i][1]+50*math.sin(wisps[i][6])*screen_res[0]/Med[0],player_y,wisp_size,player_width,wisp_size,player_height) and invincible < 1:
                player_stats[0] -= wisp_damage
                invincible = player_damage_invuln
                if wisps[i][0] >= player_x:
                    knockback.append([wisp_knockback,7,False,1])
                else:
                    knockback.append([wisp_knockback,7,False,-1])
                    
        for i in range(len(slimes)):
            if slimes[i][4]:
                if check_collision(slimes[i][0],player_x,slimes[i][1]-slime_size,player_y,slime_size,player_width,slime_size*2,player_height) and invincible < 1:
                    player_stats[0] -= slime_damage
                    invincible = player_damage_invuln
                    if slimes[i][0] >= player_x:
                        knockback.append([slime_knockback,7,True,1])
                    else:
                        knockback.append([slime_knockback,7,True,-1])    
            elif check_collision(slimes[i][0],player_x,slimes[i][1],player_y,slime_size,player_width,slime_size,player_height) and invincible < 1:
                player_stats[0] -= slime_damage
                invincible = player_damage_invuln
                if slimes[i][0] >= player_x:
                    knockback.append([slime_knockback,7,True,1])
                else:
                    knockback.append([slime_knockback,7,True,-1])
        for i in range(len(screamers)):
            if check_collision(screamers[i][0],player_x,screamers[i][1],player_y,screamer_size*2,player_width,screamer_size,player_height) and invincible < 1:
                player_stats[0] -= screamer_damage
                invincible = player_damage_invuln
                if screamers[i][0] >= player_x:
                    knockback.append([screamer_knockback,7,True,1])
                else:
                    knockback.append([screamer_knockback,7,True,-1])

        for i in range(len(thiefs)):
            if check_collision(thiefs[i][0],player_x,thiefs[i][1],player_y,thief_size,player_width,thief_size*2,player_height) and invincible < 1:
                player_stats[0] -= thief_damage
                invincible = player_damage_invuln
                if thiefs[i][0] >= player_x:
                    knockback.append([thief_knockback,7,True,1])
                else:
                    knockback.append([thief_knockback,7,True,-1])
        for i in range(len(snakes)):
            if snakes[i][5]<0: 
                if check_collision(snakes[i][0],player_x,snakes[i][1],player_y,snake_size,player_width,snake_size,player_height) and invincible < 1:
                    player_stats[0] -= snake_damage
                    invincible = player_damage_invuln
                    if snakes[i][0]+snake_size/2 >= player_center[0]:
                        knockback.append([snake_knockback,7,True,1])
                    else:
                        knockback.append([snake_knockback,7,True,-1])
            else:
                if check_collision(snakes[i][0],player_x,snakes[i][1],player_y,snake_size*1.5,player_width,snake_size,player_height) and invincible < 1:
                    player_stats[0] -= snake_damage
                    invincible = player_damage_invuln
                    if snakes[i][0]+3*snake_size/4 > player_center[0]:
                        knockback.append([snake_knockback,7,True,1])
                    else:
                        knockback.append([snake_knockback,7,True,-1])
        for i in range(len(tanks)):
            if check_collision(tanks[i][0],player_x,tanks[i][1],player_y,2*tank_size,player_width,tank_size,player_height) and invincible < 1:
                player_stats[0] -= tank_damage
                invincible = player_damage_invuln
                if tanks[i][0]+tank_size >= player_center[0]:
                    knockback.append([tank_knockback,7,True,1])
                else:
                    knockback.append([tank_knockback,7,True,-1])
        for i in range(len(clouds)):
            if check_collision(clouds[i][0],player_x,clouds[i][1],player_y,2*cloud_size,player_width,cloud_size,player_height) and invincible < 1:
                player_stats[0] -= cloud_damage
                invincible = player_damage_invuln
                if clouds[i][0]+cloud_size >= player_center[0]:
                    knockback.append([cloud_knockback,7,True,1])
                else:
                    knockback.append([cloud_knockback,7,True,-1])
            for j in range(len(clouds[i][7])):
                if j == 0:
                    z = 0
                if check_collision(clouds[i][7][j-z][0],player_x,clouds[i][7][j-z][1],player_y,cloud_rain_size[0],player_width,cloud_rain_size[1],player_height) and invincible < 1:
                    player_stats[0] -= cloud_damage
                    invincible = player_damage_invuln
                    clouds[i][7].pop(j-z)
                    z+=1
                
        ## --- Collision Between Enemies and Player Shots + Deletion --- ##
        for i in range(len(player_projectiles)):
            if i == 0:
                x = 0
            hit = False
            for j in range(len(wisps)):
                if hit:
                    break
                if j == 0:
                    z = 0
                if check_collision(player_projectiles[i-x][0],wisps[j-z][0],player_projectiles[i-x][1],wisps[j-z][1]+50*math.sin(wisps[j-z][6])*screen_res[0]/Med[0],projectile_width,wisp_size,projectile_height,wisp_size):
                    wisps[j-z][8]-=player_damage*player_stats[3]
                    wisps[j-z][9] = True
                    if wisps[j-z][8] <= 0:
                        wisps.pop(j-z)
                        z+=1
                        score+=wisp_pv
                        money+=wisp_pv
                        enemy_count -=1
                        wisp_death.play()
                    else:
                        enemy_hit.play()
                    player_projectiles.pop(i-x)
                    x+=1
                    
                    hit = True            
            for j in range(len(slimes)):
                if hit:
                    break
                if j == 0:
                    z = 0
                if slimes[j-z][4]:
                    if check_collision(player_projectiles[i-x][0],slimes[j-z][0],player_projectiles[i-x][1],slimes[j-z][1]-slime_size,projectile_width,slime_size,projectile_height,2*slime_size):
                        slimes[j-z][7]-=player_damage*player_stats[3]
                        slimes[j-z][8] = True
                        if slimes[j-z][7] <= 0:
                            slimes.pop(j-z)
                            z+=1
                            score+=slime_pv
                            money+=slime_pv
                            enemy_count -=1
                            slime_death.play()
                        else:
                            enemy_hit.play()
                        player_projectiles.pop(i-x)
                        x+=1
                        hit = True
                    
                elif check_collision(player_projectiles[i-x][0],slimes[j-z][0],player_projectiles[i-x][1],slimes[j-z][1],projectile_width,slime_size,projectile_height,slime_size):
                    slimes[j-z][7]-=player_damage*player_stats[3]
                    slimes[j-z][8] = True
                    if slimes[j-z][7] <= 0:
                        slimes.pop(j-z)
                        z+=1
                        score+=slime_pv
                        money+=slime_pv
                        enemy_count -=1
                        slime_death.play()
                    else:
                        enemy_hit.play()
                    player_projectiles.pop(i-x)
                    x+=1
                    enemy_hit.play()
                    hit = True
            for j in range(len(screamers)):
                if hit:
                    break
                if j == 0:
                    z = 0
                if check_collision(player_projectiles[i-x][0],screamers[j-z][0],player_projectiles[i-x][1],screamers[j-z][1],projectile_width,2*screamer_size,projectile_height,wisp_size):
                    screamers[j-z][6]-=player_damage*player_stats[3]
                    screamers[j-z][8] = True
                    if screamers[j-z][6] <= 0:
                        screamers.pop(j-z)
                        z+=1
                        score+=screamer_pv
                        money+=screamer_pv
                        enemy_count -=1
                        screamer_death.play()
                    else:
                        enemy_hit.play()
                    player_projectiles.pop(i-x)
                    x+=1
                    hit = True
            for j in range(len(thiefs)):
                if hit:
                    break
                if j == 0:
                    z = 0
                if check_collision(player_projectiles[i-x][0],thiefs[j-z][0],player_projectiles[i-x][1],thiefs[j-z][1],projectile_width,thief_size,projectile_height,2*thief_size):
                    thiefs[j-z][5]-=player_damage*player_stats[3]
                    thiefs[j-z][6] = True
                    if thiefs[j-z][5] <= 0:
                        thiefs.pop(j-z)
                        z+=1
                        score+=thief_pv
                        money+=thief_pv
                        enemy_count -=1
                        thief_death.play()
                    else:
                        enemy_hit.play()
                    player_projectiles.pop(i-x)
                    x+=1
                    hit = True
            for j in range(len(snakes)):
                if hit:
                    break
                if j == 0:
                    z= 0
                if snakes[j-z][5]<0:
                    if check_collision(player_projectiles[i-x][0],snakes[j-z][0],player_projectiles[i-x][1],snakes[j-z][1],projectile_width,snake_size*1.5,projectile_height,snake_size):
                        snakes[j-z][4]-=player_damage*player_stats[3]
                        snakes[j-z][6] = True
                        if snakes[j-z][4] <= 0:
                            snakes.pop(j-z)
                            z+=1
                            score+=snake_pv
                            money+=snake_pv
                            enemy_count -=1
                            snake_death.play()
                        else:
                            enemy_hit.play()
                        player_projectiles.pop(i-x)
                        x+=1
                        hit = True
                elif check_collision(player_projectiles[i-x][0],snakes[j-z][0],player_projectiles[i-x][1],snakes[j-z][1],projectile_width,snake_size,projectile_height,snake_size):
                    snakes[j-z][4]-=player_damage*player_stats[3]
                    snakes[j-z][6] = True
                    if snakes[j-z][4] <= 0:
                        snakes.pop(j-z)
                        z+=1
                        score+=snake_pv
                        money+=snake_pv
                        enemy_count -=1
                        snake_death.play()
                    else:
                        enemy_hit.play()
                    player_projectiles.pop(i-x)
                    x+=1
                    hit = True
            for j in range(len(tanks)):
                if hit:
                    break
                if j == 0:
                    z= 0
                if check_collision(player_projectiles[i-x][0],tanks[j-z][0],player_projectiles[i-x][1],tanks[j-z][1],projectile_width,tank_size*2,projectile_height,tank_size):
                    tanks[j-z][4]-=player_damage*player_stats[3]
                    tanks[j-z][7] = True
                    if tanks[j-z][4] <= 0:
                        tanks.pop(j-z)
                        z+=1
                        score+=tank_pv
                        money+=tank_pv
                        enemy_count -=1
                    else:
                        enemy_hit.play()
                    player_projectiles.pop(i-x)
                    x+=1
                    hit = True
            for j in range(len(clouds)):
                if hit:
                    break
                if j == 0:
                    z= 0
                if check_collision(player_projectiles[i-x][0],clouds[j-z][0],player_projectiles[i-x][1],clouds[j-z][1]+50*math.sin(clouds[j-z][5])*screen_res[0]/Med[0],projectile_width,cloud_size*2,projectile_height,cloud_size):
                    clouds[j-z][4]-=player_damage*player_stats[3]
                    clouds[j-z][8] = True
                    if clouds[j-z][4] <= 0:
                        clouds.pop(j-z)
                        z+=1
                        score+=cloud_pv
                        money+=cloud_pv
                        enemy_count -=1
                        cloud_death.play()
                    else:
                        enemy_hit.play()
                    player_projectiles.pop(i-x)
                    x+=1
                    hit = True
      
        score_string = (" | "+"Score: "+str(score)+" | "+"Enemies: "+str(enemy_count)+" | "+"Wave: "+str(wave_number)+" | ")
        score_text = game_font_1.render((score_string), True, White)
        screen_main.blit(score_text, [0, screen_res[1]/15])
        for i in range(int(player_stats[1]/2)):
            screen_main.blit(empty_heart,[int(screen_res[0]/35)-int(screen_res[0]/45)+int(screen_res[0]/33)*i,int(screen_res[0]/35)-int(screen_res[0]/45)])
        for i in range(int(player_stats[0]/2)):
            screen_main.blit(full_heart,[int(screen_res[0]/35)-int(screen_res[0]/45)+int(screen_res[0]/33)*i,int(screen_res[0]/35)-int(screen_res[0]/45)])
        if player_stats[0]%2 == 1 and player_stats[0] > 0:
            screen_main.blit(half_heart,[int(screen_res[0]/35)-int(screen_res[0]/45)+int(screen_res[0]/33)*int(player_stats[0]/2),int(screen_res[0]/35)-int(screen_res[0]/45)])
            
    if enemy_count == 0 and not upgradescreen and not spawn:
        wisp_projectiles = []
        cloud_projectiles = []
        upgradescreen = True
        spawn = True
        if wave_number > 0:
            wave_end.play()
        wave_number +=1
        wave_pv += wave_difficulty_ramp
        current_upgrade_pointpos = upgrade_pointer_poslist[0]
        player_stats[0] = player_stats[1]

    if gameover:
        wave_time = False
        if gameover_sound:
            pygame.mixer.quit()
            pygame.mixer.init(frequency=22050, size=16, channels=2, buffer=4096)
            player_death.play()
            gameover_sound = False
        screen_main.blit(gameover_display,[0,0])
        if keys[9] and change_pos < 1 or button_values[1] == 1 and change_pos < 1:
            titlescreen = True
            mainloop_variables()
            
    else:
        ## --- Music --- ##
        if current_music[2] <= 0:
            current_music[0].play()
            current_music[2] = current_music[1]
        current_music[2] -= 1
        
    if titlescreen:
        screen_main.blit(titlescreen_background,[0,0])
        if pointon_play:
            pointer_pos = [786/Med[0]*screen_res[0],296/Med[1]*screen_res[1]]
            if keys[9] and change_pos < 1 or button_values[1] == 1 and change_pos < 1:
                titlescreen = False
                upgradescreen = True
            elif keys[2] and change_pos < 1 or analog_values[1] < -5 and change_pos < 1:
                pointon_credits = True
                pointon_play = False
            elif keys[3] and change_pos < 1 or analog_values[1] > 5 and change_pos < 1:
                pointon_quit = True
                pointon_play = False
        elif pointon_quit:
            pointer_pos = [786/Med[0]*screen_res[0],296/Med[1]*screen_res[1]+138*screen_res[1]/Med[1]]
            if keys[9] and change_pos < 1 or button_values[1] == 1 and change_pos < 1:
                done_main = True
            elif keys[2] and change_pos < 1 or analog_values[1] < -5 and change_pos < 1:
                pointon_play = True
                pointon_quit = False
            elif keys[3] and change_pos < 1 or analog_values[1] > 5 and change_pos < 1:
                pointon_credits = True
                pointon_quit = False
        elif pointon_credits:
            pointer_pos = [786/Med[0]*screen_res[0],296/Med[1]*screen_res[1]+2*138*screen_res[1]/Med[1]]
            if keys[9] and change_pos < 1 or button_values[1] == 1 and change_pos < 1:
                credits_screen = True
                pointon_credits = False
            elif keys[2] and change_pos < 1 or analog_values[1] < -5 and change_pos < 1:
                pointon_quit = True
                pointon_credits = False
            elif keys[3] and change_pos < 1 or analog_values[1] > 5 and change_pos < 1:
                pointon_play = True
                pointon_credits = False
        if keys[9] or button_values[1] == 1 or  keys[3] or analog_values[1] > 5 or keys[2] or analog_values[1] < -5:
            change_pos = change_pos_delay
        else:
            change_pos -= 1
            
        screen_main.blit(main_pointer,pointer_pos)
        if credits_screen:
            screen_main.blit(credits_background,[0,0])
            if keys[10] or button_values[2] == 1:
                credits_screen = False
                pointon_credits = True        
    elif upgradescreen:
        screen_main.blit(upgrade_background,upgrade_scrnpos)
        
        text = game_font_1.render(str(wave_number), True, Black)
        screen_main.blit(text, [upgrade_scrnpos[0]+upgrade_scrnsize[0]*21.2/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*3.35/25])
    
        text = game_font_1.render(str(score), True, Black)
        screen_main.blit(text, [upgrade_scrnpos[0]+upgrade_scrnsize[0]*21.2/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*8.7/25])
        
        text = game_font_1.render(str(money), True, Black)
        screen_main.blit(text, [upgrade_scrnpos[0]+upgrade_scrnsize[0]*21.2/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*14.15/25])
        for i in range(3):
            for j in range(4):
                pos = [upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+j*upgrade_scrnsize[0]/5,int(upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+i*(upgrade_iconsize+30*screen_res[0]/Med[0]))]
                if j == 0:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(healthup_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(healthup_available,pos)
                    else:
                        screen_main.blit(healthup_notavailable,pos)                    
                elif j == 1:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(firerate_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(firerate_available,pos)
                    else:
                        screen_main.blit(firerate_notavailable,pos) 
                elif j == 2:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(power_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(power_available,pos)
                    else:
                        screen_main.blit(power_notavailable,pos) 
                else:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(speed_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(speed_available,pos)
                    else:
                        screen_main.blit(speed_notavailable,pos)        
        if purchase:    
            if current_upgrade_pointpos[4] == upgrades[current_upgrade_pointpos[3]]:
                screen_main.blit(main_pointer,purchase_pos)
                if keys[10] and change_pos < 1 or button_values[2] == 1 and change_pos < 1:
                    purchase = False
                elif keys[9] and change_pos < 1 or button_values[1] == 1 and change_pos < 1:
                    if money - current_upgrade_pointpos[2]*(upgrades[current_upgrade_pointpos[3]]+1) < 0:
                        pass
                    else:
                        money -= current_upgrade_pointpos[2]*(upgrades[current_upgrade_pointpos[3]]+1)
                        upgrades[current_upgrade_pointpos[3]] += 1
                        purchase = False
                else:
                    change_pos -= 1
            else:
                purchase = False
                
        elif keys[2] and change_pos < 1 or analog_values[1] < -5 and change_pos < 1:
            if current_upgrade_pointpos[0][0] != None:
                current_upgrade_pointpos = upgrade_pointer_poslist[current_upgrade_pointpos[0][0]]
        elif keys[0] and change_pos < 1 or analog_values[0] < -5 and change_pos < 1:
            if current_upgrade_pointpos[0][1] != None:
                current_upgrade_pointpos = upgrade_pointer_poslist[current_upgrade_pointpos[0][1]]
        elif keys[3] and change_pos < 1 or analog_values[1] > 5 and change_pos < 1:
            if current_upgrade_pointpos[0][2] != None:
                current_upgrade_pointpos = upgrade_pointer_poslist[current_upgrade_pointpos[0][2]]
        elif keys[1] and change_pos < 1 or analog_values[0] > 5 and change_pos < 1:
            if current_upgrade_pointpos[0][3] != None:
                current_upgrade_pointpos = upgrade_pointer_poslist[current_upgrade_pointpos[0][3]]
        elif keys[9] and change_pos < 1 or button_values[1] == 1 and change_pos < 1:
            for i in range(len(upgrade_pointer_poslist)):
                if current_upgrade_pointpos == upgrade_pointer_poslist[i]:
                    current_button = i
                    break
            if current_button < 12:
                purchase = True
            elif current_button == 12:
                upgradescreen = False
                if godmode[0] and godmode[1]:
                    upgrades = [upgrades[0],5,5,4]
            elif current_button == 13:
                titlescreen = True
                mainloop_variables()
                change_pos = change_pos_delay
        else:
            screen_main.blit(main_pointer,current_upgrade_pointpos[1])
        if keys[9] or button_values[1] == 1 or keys[1] or analog_values[0] > 5 or keys[3] or analog_values[1] > 5 or keys[0] or analog_values[0] < -5 or keys[2] or analog_values[1] < -5:
            change_pos = change_pos_delay
        else:
            change_pos -= 1
        if upgrade_pointer_poslist.index(current_upgrade_pointpos) > 11:
            purchase_text = game_font_1.render((""), True, Black)
        elif current_upgrade_pointpos[4] < upgrades[current_upgrade_pointpos[3]]:
            purchase_text = game_font_1.render(("Owned"), True, Black)
        elif current_upgrade_pointpos[4] == upgrades[current_upgrade_pointpos[3]]:
            purchase_text = game_font_1.render(str(current_upgrade_pointpos[2]*(upgrades[current_upgrade_pointpos[3]]+1)), True, Black)
        else:
            purchase_text = game_font_1.render(("Locked"), True, Black)
        screen_main.blit(purchase_text, price_pos)
    elif pause:
        screen_main.blit(upgrade_background,upgrade_scrnpos)
        for i in range(3):
            for j in range(4):
                pos = [upgrade_scrnpos[0]+(upgrade_scrnsize[0]/5-upgrade_iconsize)/2+j*upgrade_scrnsize[0]/5,int(upgrade_scrnpos[1]+15*screen_res[0]/Med[0]+i*(upgrade_iconsize+30*screen_res[0]/Med[0]))]
                if j == 0:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(healthup_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(healthup_available,pos)
                    else:
                        screen_main.blit(healthup_notavailable,pos)                    
                elif j == 1:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(firerate_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(firerate_available,pos)
                    else:
                        screen_main.blit(firerate_notavailable,pos) 
                elif j == 2:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(power_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(power_available,pos)
                    else:
                        screen_main.blit(power_notavailable,pos) 
                else:
                    if upgrades[j]-i >= 1: 
                        screen_main.blit(speed_purchased,pos)
                    elif upgrades[j]-i == 0:
                        screen_main.blit(speed_available,pos)
                    else:
                        screen_main.blit(speed_notavailable,pos) 
        text = game_font_1.render(str(wave_number), True, Black)
        screen_main.blit(text, [upgrade_scrnpos[0]+upgrade_scrnsize[0]*21.2/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*3.35/25])
    
        text = game_font_1.render(str(score), True, Black)
        screen_main.blit(text, [upgrade_scrnpos[0]+upgrade_scrnsize[0]*21.2/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*8.7/25])
        
        text = game_font_1.render(str(money), True, Black)
        screen_main.blit(text, [upgrade_scrnpos[0]+upgrade_scrnsize[0]*21.2/25,upgrade_scrnpos[1]+upgrade_scrnsize[1]*14.15/25])
        if keys[10] and change_pos < 1 or button_values[2] == 1 and change_pos < 1:
            pause = False
            change_pos = change_pos_delay
        elif keys[9] and change_pos < 1 or button_values[1] == 1 and change_pos < 1:
            pause = False
            titlescreen = True
            mainloop_variables()
        screen_main.blit(main_pointer,current_upgrade_pointpos[1])
        
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

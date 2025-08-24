

import pygame
import pygame_functions
from frame_rescaling import *
import math
from audio_loading import *
import random

# Initializing
pygame.init()
pygame.mixer.init()


# Play background loop ONCE
background_channel.play(background_loop, loops=-1)


# Game window creation
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption('Frost Run')


# Icon
icon = pygame.image.load('main_character/maincharimage.png')
pygame.display.set_icon(icon)


# Background tileset
background = pygame.image.load('finalbg.jpg')
menuimage=pygame.image.load('loadbg.png')

# Character
charimg = pygame.image.load('main_character/maincharimage.png')
charx = 400
chary = 470


# Main Char health
player_max_hp = 10
player_current_hp = player_max_hp
phealth=pygame.image.load('heart.png')

#Player score
score_counter=0
score_img=pygame.image.load('score.png')
scaled_score=pygame.transform.scale(score_img,(50,50))


# Projectile
projectile = pygame.image.load('projectile/projectile.png')
skull_projectile = pygame.image.load('projectile/skull_projectile.png')
fire_skull=pygame.image.load('projectile/fire_skull_projectile.png')
scaled_skull_projectile = pygame.transform.scale(skull_projectile, (50, 50))
scaled_fire_skull_projectile=pygame.transform.scale(fire_skull, (50, 50))
scaled_projectile = pygame.transform.scale(projectile, (70, 70))
px = 0
py = 0
px_change = 2
p_state = "ready"

#Fire Skull projectile
fp_state="ready"
fpx_change=-2
fpx=0
fpy=0


# Jumping
is_jumping = False
jump_velocity = 0
gravity = 0.03
jump_strength = 4
terminal_velocity = 3
space_held = False


# Image scaling
scaled_background = pygame.transform.scale(background, (900, 700)).convert()
scaled_maincharim = pygame.transform.scale(charimg, (100, 100))
scaled_menuim=pygame.transform.scale(menuimage,(900,700)).convert()


# Box
box_image = pygame.image.load('Box/icebox.png')
scaled_box = pygame.transform.scale(box_image, (70, 70))
boxes = []
box_spawn_time = 3500
last_box_spawn_time = pygame.time.get_ticks()


# Green enemy
#greenenemy_image = pygame.image.load('green_character/greencharimage.png')
#scaled_green_enemy = pygame.transform.scale(greenenemy_image, (100, 100))
enemies = []
enemy_spawn_time = 9000
last_green_enemy_spawn_time = pygame.time.get_ticks()
greenchar_killed=0


# Creeper
#creeper_image = pygame.image.load('cchar/cchar.png')
#scaled_creeper = pygame.transform.scale(creeper_image, (100, 100))
creeper = []
creeper_spawn_time = 2000
last_creeper_spawn_time = pygame.time.get_ticks()
creeper_killed=0

# Red enemy
redchar = []
red_enemy_spawn_time = 13000
last_red_enemy_spawn_time = pygame.time.get_ticks()
red_enemy_killed=0

# Flying enemy
fchar = []
flying_enemy_spawn_time = 5000
last_flying_enemy_spawn_time = pygame.time.get_ticks()
flies_killed=0



# Background scrolling
bg_width = scaled_background.get_width()
world_scroll = 0


# Movement
move_left = False
move_right = False
scroll_speed = 1.2


# Collision box
def is_colliding(rect1, rect2):
    return rect1.colliderect(rect2)


# Projectile function
def shoot(x, y):
    global p_state, px, py
    p_state = "shot"
    px = x + 50 
    py = y + 30
    screen.blit(scaled_projectile, (px, py))

#Skull projectile shoot
enemy_s = []
s_shoot_interval = 1500 
def skull(x, y):
    global sp_state, spx, spy
    sp_state = "shot"
    spx = x + 50 
    spy = y + 30
    screen.blit(scaled_projectile, (spx, spy))

#Fire projectile shoot 
enemy_fs = []
fs_shoot_interval = 1500 
def fireskull(x, y):
    global fp_state, fpx, fpy
    fp_state = "shot"
    fpx = x - 50 
    fpy = y - 30
    screen.blit(scaled_projectile, (fpx,fpy))
    


# Running frames as animation
no_of_frames = 4
frame_list = [smframe0, smframe1, smframe2, smframe3]
cchar_list = [scframe0, scframe1, scframe2, scframe3]
redchar_list = [srframe0, srframe1, srframe2, srframe3]
greenchar_list = [sgframe0, sgframe1, sgframe2, sgframe3]
flying_list=[sfframe0,sfframe1,sfframe2,sfframe3]
last_update = pygame.time.get_ticks()
animation_cooldown = 90
frame = 0


# Game state
running = True
game_over = False


# Player damage function
def player_damage():
    global player_current_hp, game_over
    if player_current_hp > 0:
        player_current_hp -= 1
        if player_current_hp < 0:
            player_current_hp = 0
        print(f"Player HP: {player_current_hp}")
        if player_current_hp <= 0:
            print("GAME OVER")
            game_over = True


# Damage Cooldown
last_damage_time = 0
damage_cooldown = 500


# Starting screen
def starting_screen():
    screen.blit(scaled_menuim,(0,0))  
    font = pygame.font.SysFont('couriernew', 50)
    #text = font.render("Press any key to start", True, (255, 255, 255))
    frostrun=pygame.image.load('frostrun.png')
    scaled_frostrun=pygame.transform.scale(frostrun,(600,250))
    #text_rect = text.get_rect(center=(450, 400))
    screen.blit(scaled_frostrun,(150,100))
   # screen.blit(text, text_rect)
    pygame.display.update()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting_for_key = False



# Game Over screen
def display_game_over():
    screen.blit(scaled_menuim,(0,0))  # Fill screen with black
    font = pygame.font.SysFont('couriernew', 50)
    text = font.render('GAME OVER', True, (255, 0, 0))
    screen.blit(text, (300, 230))

    font = pygame.font.SysFont('couriernew', 30)
    scoredisplay=font.render(f"Score: {int(score_counter)}", True, (255, 255, 255))
    screen.blit(scoredisplay, (370, 310))

    font = pygame.font.SysFont('couriernew', 30)
    restart_text = font.render('Press R to Restart or Q to Quit', True, (255, 255, 255))
    screen.blit(restart_text, (170, 460))
    pygame.display.update()

starting_screen()



# Main Game Loop
while running:
    #Background scrolling
    rel_scroll = world_scroll % bg_width
    screen.blit(scaled_background, (rel_scroll - bg_width, 0))
    screen.blit(scaled_background, (rel_scroll, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Key down events if game is running(upon key press)
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_d:
                    move_right = True
                if event.key == pygame.K_SPACE:
                    space_held = True
                    if not is_jumping:
                        is_jumping = True
                        jump_velocity = -jump_strength
                        jump_channel.play(jump_sound)
                if event.key == pygame.K_q:
                    if p_state == "ready":
                        shoot(charx, chary)
                        projectile_channel.play(projectile_sound)

            #Key up events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_SPACE:
                    space_held = False
                    if jump_velocity < -3:
                        jump_velocity = -3


    #Game over logic
    if game_over:
        display_game_over()
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        score_counter=0
                        greenchar_killed=0
                        creeper_killed=0
                        red_enemy_killed=0
                        flies_killed=0
                        player_current_hp = player_max_hp
                        enemies.clear()
                        creeper.clear()
                        boxes.clear()
                        world_scroll = 0
                        chary = 470
                        game_over = False
                        last_box_spawn_time = pygame.time.get_ticks()
                        last_green_enemy_spawn_time = pygame.time.get_ticks()
                        last_creeper_spawn_time = pygame.time.get_ticks()
                        break
                    elif event.key == pygame.K_q:
                        running = False
                        pygame.quit()
                        quit()
            pygame.time.delay(100)
        continue



    #Scroll world
    if move_left:
        world_scroll += scroll_speed
    if move_right:
        world_scroll -= scroll_speed



    #Apply jump physics
    if is_jumping:
        chary += jump_velocity
        jump_velocity += gravity
        if jump_velocity > terminal_velocity:
            jump_velocity = terminal_velocity



    #Character Collision box
    char_rect = pygame.Rect(charx, chary, 100, 100)
    on_box = False

    for box in boxes[:]:
        box_screen_x = box['x'] + world_scroll
        box_rect = pygame.Rect(box_screen_x, box['y'], 70, 70)

        if char_rect.colliderect(box_rect):
            if chary + 100 <= box['y'] + 15 and jump_velocity >= 0:
                chary = box['y'] - 100
                is_jumping = False
                jump_velocity = 0
                on_box = True
            elif chary >= box['y'] + 60 and jump_velocity < 0:
                chary = box['y'] + 70
                jump_velocity = 0
            elif charx + 100 >= box_screen_x and charx < box_screen_x:
                world_scroll += scroll_speed
            elif charx <= box_screen_x + 70 and charx > box_screen_x:
                world_scroll -= scroll_speed

        if box_screen_x < -70 or box_screen_x > 1000:
            boxes.remove(box)
        else:
            screen.blit(scaled_box, (box_screen_x, box['y']))

    if not on_box and chary < 470:
        is_jumping = True
    elif chary >= 470:
        chary = 470
        is_jumping = False
        jump_velocity = 0



    #Spawn boxes
    current_time = pygame.time.get_ticks()

    if current_time - last_box_spawn_time > box_spawn_time:
        new_box_x = random.randint(900, 1100) - world_scroll
        new_box_y = random.randint(300, 500)
        boxes.append({'x': new_box_x, 'y': new_box_y})
        last_box_spawn_time = current_time



    #Spawn green char
    if current_time - last_green_enemy_spawn_time > enemy_spawn_time:
        new_enemy_x = random.randint(900, 1100) - world_scroll
        new_enemy_y = 470
        enemies.append({'x': new_enemy_x, 'y': new_enemy_y, 'hp': 4})
        last_green_enemy_spawn_time = current_time



    #Spawn creeper 
    if current_time - last_creeper_spawn_time > creeper_spawn_time:
        new_creeper_x = random.randint(900, 1100) - world_scroll
        new_creeper_y = 470
        creeper.append({'x': new_creeper_x, 'y': new_creeper_y, 'hp': 3})
        last_creeper_spawn_time = current_time

    #Spawn red char
    if current_time - last_red_enemy_spawn_time> red_enemy_spawn_time:
        new_redchar_x = random.randint(900, 1100) - world_scroll
        new_redchar_y = 470
        redchar.append({'x': new_redchar_x, 'y': new_redchar_y, 'hp': 11})
        last_red_enemy_spawn_time = current_time

     #Spawn flying char
    if current_time - last_flying_enemy_spawn_time> flying_enemy_spawn_time:
        new_flying_x = random.randint(900, 1100) - world_scroll
        new_flying_y = 220
        fchar.append({'x': new_flying_x, 'y': new_flying_y, 'hp': 4})
        last_flying_enemy_spawn_time = current_time

    #Bullet movement and collision
    if p_state == "shot":
        px += px_change
        bullet_rect = pygame.Rect(px, py, 70, 70)
        screen.blit(scaled_projectile, (px, py))

        #Check for bullet collision with green char
        for enemy in enemies[:]:
            enemy_screen_x = enemy['x'] + world_scroll
            enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
            if bullet_rect.colliderect(enemy_rect):
                enemy['hp'] -= 1
                p_state = "ready"
                if enemy['hp'] <= 0:
                    enemies.remove(enemy)
                    score_counter=score_counter+1
                    greenchar_killed+=1
                break

       #Check bullet collision with creeper
        for enemy in creeper[:]:
            enemy_screen_x = enemy['x'] + world_scroll
            enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
            if bullet_rect.colliderect(enemy_rect):
                enemy['hp'] -= 1
                p_state = "ready"
                if enemy['hp'] <= 0:
                    creeper.remove(enemy)
                    score_counter=score_counter+1
                    creeper_killed+=1
                break

        #Check bullet collision with redchar
        for enemy in redchar[:]:
            enemy_screen_x = enemy['x'] + world_scroll
            enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
            if bullet_rect.colliderect(enemy_rect):
                enemy['hp'] -= 1
                p_state = "ready"
                if enemy['hp'] <= 0:
                    redchar.remove(enemy)
                    score_counter=score_counter+7
                    red_enemy_killed+=1
                break

        #Check bullet collision with flying char
        for enemy in fchar[:]:
            enemy_screen_x = enemy['x'] + world_scroll
            enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
            if bullet_rect.colliderect(enemy_rect):
                enemy['hp'] -= 1
                p_state = "ready"
                if enemy['hp'] <= 0:
                    fchar.remove(enemy)
                    score_counter=score_counter+5
                    flies_killed+=1
                break

        if px >= 900:
            p_state = "ready"



    #Check for player collision with green char
    for enemy in enemies[:]:
        enemy_screen_x = enemy['x'] + world_scroll
        enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
        if char_rect.colliderect(enemy_rect):
            if current_time - last_damage_time > damage_cooldown:
                player_damage()
                last_damage_time = current_time

    #Check for player collision with creeper
    for enemy in creeper[:]:
        enemy_screen_x = enemy['x'] + world_scroll
        enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
        if char_rect.colliderect(enemy_rect):
            if current_time - last_damage_time > damage_cooldown:
                player_damage()
                last_damage_time = current_time

    #Check for player collision with redchar
    for enemy in redchar[:]:
        enemy_screen_x = enemy['x'] + world_scroll
        enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
        if char_rect.colliderect(enemy_rect):
            if current_time - last_damage_time > damage_cooldown:
                player_damage()
                last_damage_time = current_time

     #Check for player collision with flying char
    for enemy in fchar[:]:
        enemy_screen_x = enemy['x'] + world_scroll
        enemy_rect = pygame.Rect(enemy_screen_x, enemy['y'], 100, 100)
        if char_rect.colliderect(enemy_rect):
            if current_time - last_damage_time > damage_cooldown:
                player_damage()
                last_damage_time = current_time



    #Draw green char with HP bar
    for enemy in enemies[:]:
        movement_rate=0.8
        enemy['x']=enemy['x']-movement_rate
        enemy_screen_x = enemy['x'] + world_scroll
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(frame_list):
                frame = 0
        screen.blit(greenchar_list[frame], (enemy_screen_x, enemy['y']))

         #GREEN CHAR PROJECTILE
        if 'last_shot' not in enemy:
            enemy['last_shot'] = 0  
        if current_time - enemy['last_shot'] >= s_shoot_interval:
            s = {
                'x': enemy['x'],
                'y': enemy['y'] +25,  
                'sspeed': -1.5  
            }
            enemy_s.append(s)
            enemy['last_shot'] = current_time
        
        #HP green char
        max_hp = 4
        current_hp = enemy.get('hp', 4)
        hp_bar_width = 100
        hp_ratio = current_hp / max_hp
        pygame.draw.rect(screen, (50, 50, 50), (enemy_screen_x, enemy['y'] - 10, hp_bar_width, 5))
        pygame.draw.rect(screen, (255, 0, 0), (enemy_screen_x, enemy['y'] - 10, hp_bar_width * hp_ratio, 5))



    #Draw creeper with HP bars
    for enemy in creeper[:]:
        movement_rate=1.2
        enemy['x']=enemy['x']-movement_rate
        enemy_screen_x = enemy['x'] + world_scroll
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(frame_list):
                frame = 0
        screen.blit(cchar_list[frame], (enemy_screen_x, enemy['y']))
        
        #Creeper HP
        max_hp = 3
        current_hp = enemy.get('hp', 3)
        hp_bar_width = 100
        hp_ratio = current_hp / max_hp
        pygame.draw.rect(screen, (50, 50, 50), (enemy_screen_x, enemy['y'] - 10, hp_bar_width, 5))
        pygame.draw.rect(screen, (255, 0, 0), (enemy_screen_x, enemy['y'] - 10, hp_bar_width * hp_ratio, 5))




    #Draw redchar with HP bars
    for enemy in redchar[:]:
        movement_rate=0.4
        enemy['x']=enemy['x']-movement_rate
        enemy_screen_x = enemy['x'] + world_scroll
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(frame_list):
                frame = 0
        screen.blit(redchar_list[frame], (enemy_screen_x, enemy['y']))


        #Redchar HP
        max_hp = 11
        current_hp = enemy.get('hp', 11)
        hp_bar_width = 100
        hp_ratio = current_hp / max_hp
        pygame.draw.rect(screen, (50, 50, 50), (enemy_screen_x, enemy['y'] - 10, hp_bar_width, 5))
        pygame.draw.rect(screen, (255, 0, 0), (enemy_screen_x, enemy['y'] - 10, hp_bar_width * hp_ratio, 5))





    #Draw flies with HP bars
    for enemy in fchar[:]:
        movement_rate=0.8
        enemy['x']=enemy['x']-movement_rate
        enemy_screen_x = enemy['x'] + world_scroll
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(flying_list):
                frame = 0
        screen.blit(flying_list[frame], (enemy_screen_x, enemy['y']))
        
        #Flies HP
        max_hp = 4
        current_hp = enemy.get('hp', 4)
        hp_bar_width = 100
        hp_ratio = current_hp / max_hp
        pygame.draw.rect(screen, (50, 50, 50), (enemy_screen_x, enemy['y'] - 10, hp_bar_width, 5))
        pygame.draw.rect(screen, (255, 0, 0), (enemy_screen_x, enemy['y'] - 10, hp_bar_width * hp_ratio, 5))

        #Skull projectile reset
        for s in enemy_s[:]:
            s['x'] += s['sspeed']
            screen.blit(scaled_skull_projectile, (s['x'] + world_scroll, s['y']))
            s_rect = pygame.Rect(s['x'] + world_scroll, s['y'], 50, 50)
            if char_rect.colliderect(s_rect):
                if current_time - last_damage_time > damage_cooldown:
                    player_damage()
                    last_damage_time = current_time
                enemy_s.remove(s)
                continue

            # Remove bullet if it goes off-screen
            if s['x'] < -world_scroll or s['x'] > screen.get_width() - world_scroll:
                enemy_s.remove(s)

    #Character Animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(frame_list):
            frame = 0
    screen.blit(frame_list[frame], (charx, chary))


    #Player HP
    hp_bar_width = 150
    hp_bar_height = 20
    hp_bar_x = 60
    hp_bar_y = 20
    hp_ratio = player_current_hp / player_max_hp
    pygame.draw.rect(screen, (50, 50, 50), (hp_bar_x, hp_bar_y, hp_bar_width, hp_bar_height))
    pygame.draw.rect(screen, (255, 0, 0), (hp_bar_x, hp_bar_y, hp_bar_width * hp_ratio, hp_bar_height))
    screen.blit(phealth,(20,15))
    
    #Draw score
    screen.blit(scaled_score,(400,10))
    #Draw score text
    font = pygame.font.SysFont('couriernew', 25)
    score_text= font.render(f"{int(score_counter)}", True, (0, 0, 0))
    screen.blit(score_text, (450,19))

    #Draw percentage text
    font = pygame.font.SysFont('couriernew', 25)
    hp_text = font.render(f"{int(hp_ratio * 100)}%", True, (0, 0, 0))
    screen.blit(hp_text, (hp_bar_x + hp_bar_width + 10, hp_bar_y))

    pygame.display.update()
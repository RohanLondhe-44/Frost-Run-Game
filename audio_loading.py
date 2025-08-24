import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(16)

projectile_sound = pygame.mixer.Sound('audios/fireballshot.mp3')
jump_sound = pygame.mixer.Sound('audios/jump.mp3')
move_sound = pygame.mixer.Sound('audios/movement.mp3')
background_loop = pygame.mixer.Sound('audios/backgroundtrack.ogg')
background_loop.set_volume(0.1)

jump_channel = pygame.mixer.Channel(1)
projectile_channel = pygame.mixer.Channel(2)
background_channel = pygame.mixer.Channel(3)
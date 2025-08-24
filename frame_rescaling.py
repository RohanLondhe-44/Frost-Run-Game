import pygame
import pygame_functions
#animation frames and frame rescaling

#main character
mframe0=pygame.image.load('main_character/mtile000.png')
mframe1=pygame.image.load('main_character/mtile001.png')
mframe2=pygame.image.load('main_character/mtile002.png')
mframe3=pygame.image.load('main_character/mtile003.png')

#green character
gframe0=pygame.image.load('green_character/gtile000.png')
gframe1=pygame.image.load('green_character/gtile001.png')
gframe2=pygame.image.load('green_character/gtile002.png')
gframe3=pygame.image.load('green_character/gtile003.png')

#red character
rframe0=pygame.image.load('red_character/rtile000.png')
rframe1=pygame.image.load('red_character/rtile001.png')
rframe2=pygame.image.load('red_character/rtile002.png')
rframe3=pygame.image.load('red_character/rtile003.png')

# C character
cframe0=pygame.image.load('cchar/ctile000.png')
cframe1=pygame.image.load('cchar/ctile001.png')
cframe2=pygame.image.load('cchar/ctile002.png')
cframe3=pygame.image.load('cchar/ctile003.png')

#flying character
fframe0=pygame.image.load('flying_character/ftile000.png')
fframe1=pygame.image.load('flying_character/ftile001.png')
fframe2=pygame.image.load('flying_character/ftile002.png')
fframe3=pygame.image.load('flying_character/ftile003.png')
#--------------------------RESCALING--------------------

#main character
smframe0=pygame.transform.scale(mframe0,(100,100))
smframe1=pygame.transform.scale(mframe1,(100,100))
smframe2=pygame.transform.scale(mframe2,(100,100))
smframe3=pygame.transform.scale(mframe3,(100,100))

#green character
sgframe0=pygame.transform.scale(gframe0,(100,100))
sgframe1=pygame.transform.scale(gframe1,(100,100))
sgframe2=pygame.transform.scale(gframe2,(100,100))
sgframe3=pygame.transform.scale(gframe3,(100,100))

#red character
srframe0=pygame.transform.scale(rframe0,(100,100))
srframe1=pygame.transform.scale(rframe1,(100,100))
srframe2=pygame.transform.scale(rframe2,(100,100))
srframe3=pygame.transform.scale(rframe3,(100,100))

# C character
scframe0=pygame.transform.scale(cframe0,(100,100))
scframe1=pygame.transform.scale(cframe1,(100,100))
scframe2=pygame.transform.scale(cframe2,(100,100))
scframe3=pygame.transform.scale(cframe3,(100,100))

#flying character 
sfframe0=pygame.transform.scale(fframe0,(100,100))
sfframe1=pygame.transform.scale(fframe1,(100,100))
sfframe2=pygame.transform.scale(fframe2,(100,100))
sfframe3=pygame.transform.scale(fframe3,(100,100))


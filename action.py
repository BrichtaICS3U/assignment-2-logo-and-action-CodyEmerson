# ICS3U
# Assignment 2: Action
# <Cody Emery>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from snow import Snow
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 40, 104)
BROWN = (104, 50, 0)

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

speed = 1

all_sprites_list = pygame.sprite.Group()

snowFlake1 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake1.rect.x = random.randint(0, 400)
snowFlake1.rect.y = 1

snowFlake2 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake2.rect.x = random.randint(0, 400)
snowFlake2.rect.y = 4

snowFlake3 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake3.rect.x = random.randint(0, 400)
snowFlake3.rect.y = 6

snowFlake4 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake4.rect.x = random.randint(0, 400)
snowFlake4.rect.y = 60

snowFlake5 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake5.rect.x = random.randint(0, 400)
snowFlake5.rect.y = 100

snowFlake6 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake6.rect.x = random.randint(0, 400)
snowFlake6.rect.y = 67

snowFlake7 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake7.rect.x = random.randint(0, 400)
snowFlake7.rect.y = 20

snowFlake8 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake8.rect.x = random.randint(0, 400)
snowFlake8.rect.y = 5

snowFlake9 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake9.rect.x = random.randint(0, 400)
snowFlake9.rect.y = 50

snowFlake10 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake10.rect.x = random.randint(0, 400)
snowFlake10.rect.y = 30

snowFlake11 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake11.rect.x = random.randint(0, 400)
snowFlake11.rect.y = 10

snowFlake12 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake12.rect.x = random.randint(0, 400)
snowFlake12.rect.y = 123

snowFlake13 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake13.rect.x = random.randint(0, 400)
snowFlake13.rect.y = 160

snowFlake14 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake14.rect.x = random.randint(0, 400)
snowFlake14.rect.y = 32

snowFlake15 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake15.rect.x = random.randint(0, 400)
snowFlake15.rect.y = 69

snowFlake16 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake16.rect.x = random.randint(0, 400)
snowFlake16.rect.y = 81

snowFlake17 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake17.rect.x = random.randint(0, 400)
snowFlake17.rect.y = 90

snowFlake18 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake18.rect.x = random.randint(0, 400)
snowFlake18.rect.y = 239

snowFlake19 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake19.rect.x = random.randint(0, 400)
snowFlake19.rect.y = 360

snowFlake20 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake20.rect.x = random.randint(0, 400)
snowFlake20.rect.y = 300

snowFlake21 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake21.rect.x = random.randint(0, 400)
snowFlake21.rect.y = 1

snowFlake22 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake22.rect.x = random.randint(0, 400)
snowFlake22.rect.y = 4

snowFlake23 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake23.rect.x = random.randint(0, 400)
snowFlake23.rect.y = 6

snowFlake24 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake24.rect.x = random.randint(0, 400)
snowFlake24.rect.y = 60

snowFlake25 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake25.rect.x = random.randint(0, 400)
snowFlake25.rect.y = 100

snowFlake26 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake26.rect.x = random.randint(0, 400)
snowFlake26.rect.y = 67

snowFlake27 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake27.rect.x = random.randint(0, 400)
snowFlake27.rect.y = 20

snowFlake28 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake28.rect.x = random.randint(0, 400)
snowFlake28.rect.y = 5

snowFlake29 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake29.rect.x = random.randint(0, 400)
snowFlake29.rect.y = 50

snowFlake30 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake30.rect.x = random.randint(0, 400)
snowFlake30.rect.y = 30

snowFlake31 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake31.rect.x = random.randint(0, 400)
snowFlake31.rect.y = 10

snowFlake32 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake32.rect.x = random.randint(0, 400)
snowFlake32.rect.y = 123

snowFlake33 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake33.rect.x = random.randint(0, 400)
snowFlake33.rect.y = 160

snowFlake34 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake34.rect.x = random.randint(0, 400)
snowFlake34.rect.y = 32

snowFlake35 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake35.rect.x = random.randint(0, 400)
snowFlake35.rect.y = 69

snowFlake36 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake36.rect.x = random.randint(0, 400)
snowFlake36.rect.y = 81

snowFlake37 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake37.rect.x = random.randint(0, 400)
snowFlake37.rect.y = 90

snowFlake38 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake38.rect.x = random.randint(0, 400)
snowFlake38.rect.y = 239

snowFlake39 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake39.rect.x = random.randint(0, 400)
snowFlake39.rect.y = 360

snowFlake40 = Snow(WHITE, 10, 10, random.randint(20, 80))
snowFlake40.rect.x = random.randint(0, 400)
snowFlake40.rect.y = 300

all_sprites_list.add(snowFlake1)
all_sprites_list.add(snowFlake2)
all_sprites_list.add(snowFlake3)
all_sprites_list.add(snowFlake4)
all_sprites_list.add(snowFlake5)
all_sprites_list.add(snowFlake6)
all_sprites_list.add(snowFlake7)
all_sprites_list.add(snowFlake8)
all_sprites_list.add(snowFlake9)
all_sprites_list.add(snowFlake10)
all_sprites_list.add(snowFlake11)
all_sprites_list.add(snowFlake12)
all_sprites_list.add(snowFlake13)
all_sprites_list.add(snowFlake14)
all_sprites_list.add(snowFlake15)
all_sprites_list.add(snowFlake16)
all_sprites_list.add(snowFlake17)
all_sprites_list.add(snowFlake18)
all_sprites_list.add(snowFlake19)
all_sprites_list.add(snowFlake20)
all_sprites_list.add(snowFlake21)
all_sprites_list.add(snowFlake22)
all_sprites_list.add(snowFlake23)
all_sprites_list.add(snowFlake24)
all_sprites_list.add(snowFlake25)
all_sprites_list.add(snowFlake26)
all_sprites_list.add(snowFlake27)
all_sprites_list.add(snowFlake28)
all_sprites_list.add(snowFlake29)
all_sprites_list.add(snowFlake30)
all_sprites_list.add(snowFlake31)
all_sprites_list.add(snowFlake32)
all_sprites_list.add(snowFlake33)
all_sprites_list.add(snowFlake34)
all_sprites_list.add(snowFlake35)
all_sprites_list.add(snowFlake36)
all_sprites_list.add(snowFlake37)
all_sprites_list.add(snowFlake38)
all_sprites_list.add(snowFlake39)
all_sprites_list.add(snowFlake40)

all_falling_snowFlakes = pygame.sprite.Group()
all_falling_snowFlakes.add(snowFlake1)
all_falling_snowFlakes.add(snowFlake2)
all_falling_snowFlakes.add(snowFlake3)
all_falling_snowFlakes.add(snowFlake4)
all_falling_snowFlakes.add(snowFlake5)
all_falling_snowFlakes.add(snowFlake6)
all_falling_snowFlakes.add(snowFlake7)
all_falling_snowFlakes.add(snowFlake8)
all_falling_snowFlakes.add(snowFlake9)
all_falling_snowFlakes.add(snowFlake10)
all_falling_snowFlakes.add(snowFlake11)
all_falling_snowFlakes.add(snowFlake12)
all_falling_snowFlakes.add(snowFlake13)
all_falling_snowFlakes.add(snowFlake14)
all_falling_snowFlakes.add(snowFlake15)
all_falling_snowFlakes.add(snowFlake16)
all_falling_snowFlakes.add(snowFlake17)
all_falling_snowFlakes.add(snowFlake18)
all_falling_snowFlakes.add(snowFlake19)
all_falling_snowFlakes.add(snowFlake20)
all_falling_snowFlakes.add(snowFlake21)
all_falling_snowFlakes.add(snowFlake22)
all_falling_snowFlakes.add(snowFlake23)
all_falling_snowFlakes.add(snowFlake24)
all_falling_snowFlakes.add(snowFlake25)
all_falling_snowFlakes.add(snowFlake26)
all_falling_snowFlakes.add(snowFlake27)
all_falling_snowFlakes.add(snowFlake28)
all_falling_snowFlakes.add(snowFlake29)
all_falling_snowFlakes.add(snowFlake30)
all_falling_snowFlakes.add(snowFlake31)
all_falling_snowFlakes.add(snowFlake32)
all_falling_snowFlakes.add(snowFlake33)
all_falling_snowFlakes.add(snowFlake34)
all_falling_snowFlakes.add(snowFlake35)
all_falling_snowFlakes.add(snowFlake36)
all_falling_snowFlakes.add(snowFlake37)
all_falling_snowFlakes.add(snowFlake38)
all_falling_snowFlakes.add(snowFlake39)
all_falling_snowFlakes.add(snowFlake40)

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    for snow in all_falling_snowFlakes:
        snow.moveDown(speed)
        if snow.rect.y > SCREENHEIGHT:
            snow.changeSpeed(random.randint(20, 80))
            snow.rect.y = -200
            snow.rect.x = random.randint(0, 400)
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLUE)
    all_sprites_list.draw(screen)
    pygame.draw.line(screen, BROWN, [200, 0], [200,400], 7)
    pygame.draw.line(screen, BROWN, [0, 200], [400, 200], 7)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
    all_sprites_list.draw(screen)
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()

# ICS3U
# Assignment 2: Logo, Mercedes Benz Logo
# <Cody Emery>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
WHITE = (255, 255, 255)
SILVER = (189, 191, 193)
DARKSILVER = (132, 132, 132)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

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
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    #Top of the triangle--------------------------------------------------------------------------------------------------------------
    pygame.draw.polygon(screen, SILVER, [[200, 40], [200, 200], [180, 185]])
    pygame.draw.polygon(screen, DARKSILVER, [[200, 40], [200, 200], [220, 185]])
    #Bottom left of the triangle--------------------------------------------------------------------------------------------------
    pygame.draw.polygon(screen, SILVER, [[75, 260], [200, 200], [180, 185]])
    pygame.draw.polygon(screen, DARKSILVER, [[75, 260], [200, 200], [200, 225]])
    #Bottom right of the triangle-----------------------------------------------------------------------------------------------
    pygame.draw.polygon(screen, SILVER, [[325, 260], [200, 200], [220, 185]])
    pygame.draw.polygon(screen, DARKSILVER, [[325, 260], [200, 200], [200, 225]])
    #Circle of the logo---------------------------------------------------------------------------------------------------------------
    pygame.draw.ellipse(screen, SILVER, [50, 40, 300, 300], 10)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()

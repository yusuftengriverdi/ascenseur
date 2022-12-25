# Import the pygame module
import pygame
from button import Button
import os
from time import sleep

from people import Person, People

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
        
def onClick(btn, person=None):

    btn.press()
    # call elevator function
    # add_elevator_queue()


# Initialize pygame
pygame.init()
# Font initialization
font = pygame.font.SysFont('Arial', 40)
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('icons/bg.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH, SCREEN_HEIGHT))

# Fill the screen with black
screen.blit(BACKGROUND,(0,0))

fps = 400
fpsClock = pygame.time.Clock()


buttons = []

btn0 = Button((30, 30), 0, True, font, screen, onClick)
btn1 = Button((30, 75), 1, True, font, screen, onClick)

buttons.append(btn0)
buttons.append(btn1)

IMAGE = pygame.image.load(os.path.join('icons', 'çöp_adam.png')).convert_alpha()
IMAGE = pygame.transform.scale(IMAGE,(SCREEN_WIDTH/5, SCREEN_HEIGHT/5))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super(Player, self).__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.person = Person(0, 1, type=0)
        btn = buttons[0]
        btn.onclickFunction(btn, person=self.person)

def generate_people():
    # randomly select a person. 
    player1 = Player((300, 300), IMAGE)
    # Draw the player on the screen
    screen.blit(player1.image, player1.rect)
    
# Variable to keep the main loop running
running = True

for btn in buttons:
    btn.process()

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Random people generator.
    # In this function randomly generated people are created players, who presses buttons. 

    # Update the display
    pygame.display.flip()   
    
    generate_people()

    fpsClock.tick(fps)

# ISSUE 1:
# 1.b) Buttons are not clicked visually. 
# ISSUE 2:
# 2.a) Player should move.
# 2.b) Select randomly from available options.

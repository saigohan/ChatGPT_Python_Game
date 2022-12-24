# Import Pygame
import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group
from sys import exit
import imageio

# Initiate pygame & give permission
pygame.init()

# Set up the window
X,Y=800,600
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Hikari')

# Background colour
screen.fill('Black')
pygame.display.flip()

# Limit the frame rate
clock=pygame.time.Clock()

# Game assets
# Fonts
title_font = pygame.font.Font('/Users/yonahbole/VsCode_Projects/Font/ThaleahFat.ttf',120)
button_font = pygame.font.Font('/Users/yonahbole/VsCode_Projects/Font/ThaleahFat.ttf', 80)
body_font = pygame.font.Font('/Users/yonahbole/VsCode_Projects/Font/ThaleahFat.ttf', 30)
# Surface
player = pygame.image.load('/Users/yonahbole/VsCode_Projects/Graphics/2D_wizard_pixel.png')
player = pygame.transform.scale(player,(200,200))
background = pygame.image.load('/Users/yonahbole/VsCode_Projects/Graphics/mountain.png')
background = pygame.transform.scale(background,(X,Y)) #rescale image size

# Create a sprite for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('/Users/yonahbole/VsCode_Projects/Graphics/2D_wizard_pixel.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add a jump speed and a jumping flag
        self.jump_speed = -10
        self.jumping = False

    def update(self):
        # Update the player's position based on user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

         # Update the player's jumping status
        if self.jumping:
            self.rect.y += self.jump_speed
            self.jump_speed += 1
            if self.rect.y > 230: # the initial y position
                self.jumping = False
                self.rect.y = 230
                self.jump_speed = -10
        # Check if the player should start jumping
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True

# Create a group to hold all the sprites
all_sprites = pygame.sprite.Group()

# Create an instance of the player sprite and add it to the group
player = Player(0, 230) # coord
all_sprites.add(player)

# Set up the menu options
def draw_menu():
    # Load the menu images
    background_image = pygame.image.load('/Users/yonahbole/VsCode_Projects/Graphics/night_pixel_background.jpeg')

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the title text
    title_text = title_font.render("Hikari", True, (255, 255, 255))
    screen.blit(title_text, (0.35*X, 100))

    # Draw the instructions text
    instruction_1 = body_font.render("Use the arrow keys to move", True, (255, 255, 255))
    screen.blit(instruction_1, (100, 300))

    instruction_2 = body_font.render("Press space to jump", True, (255, 255, 255))
    screen.blit(instruction_2, (100, 350))

    instruction_3 = body_font.render("Click on any key to START", True, (255, 255, 255))
    screen.blit(instruction_3, (100, 400))

# Initialize the game state
in_menu = True
# Set up the menu loop
while in_menu:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN: # if any key is typedÒ
            in_menu = False # start the game
    # Draw the menu
    draw_menu()
    # Update the display
    pygame.display.update()

# Setting the playing loop
while not in_menu:
    # for all events of the game
    for event in pygame.event.get():
        # to quit the game window
        if event.type == pygame.QUIT:
            in_menu = True
            pygame.quit()
            exit()
        # Handle the player's jump movement
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jumping = True
    # Update sprites
    all_sprites.update()
    # Load images
    screen.blit(background,(0,0)) #1st image is below the others
    all_sprites.draw(screen)
    pygame.display.update()
    # Limit frame rate (fps ceilling)
    clock.tick(60)
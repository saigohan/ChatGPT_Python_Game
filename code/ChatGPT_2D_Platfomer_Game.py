# Import Pygame
import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group
from sys import exit
# Initiate pygame & give permission
pygame.init()

# Set up the window
X,Y=800,600
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption('My Game')
# Background colour to white
screen.fill((255, 255, 255))
pygame.display.flip()
# Limit the frame rate
clock=pygame.time.Clock()

# Game assets
# Fonts
font = pygame.font.Font('/Users/yonahbole/VsCode_Projects/Font/ThaleahFat.ttf',120) #(font type, font size)
# Surface
player = pygame.image.load('/Users/yonahbole/VsCode_Projects/Graphics/2D_wizard_pixel.png')
player = pygame.transform.scale(player,(200,200))
background = pygame.image.load('/Users/yonahbole/VsCode_Projects/Graphics/mountain.png')
background = pygame.transform.scale(background,(X,Y)) #rescale image size
text = font.render('Wizardiz',False,'White') #(text info, Anti-aliasing, colour) AA=False for pixel art

# Create a sprite for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('/Users/yonahbole/VsCode_Projects/Graphics/2D_wizard_pixel.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Update the player's position based on user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

# Create a group to hold all the sprites
all_sprites = pygame.sprite.Group()

# Create an instance of the player sprite and add it to the group
player = Player(0, 230) # coord
all_sprites.add(player)

# Setting the game
running = True
while running:
    # for all events of the game
    for event in pygame.event.get():
        # to quit the game window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    # Update sprites
    all_sprites.update()

    # Load images
    screen.blit(background,(0,0)) #1st image is below the others
    all_sprites.draw(screen)
    #screen.blit(player,(0,Y*0.46)) #coords = distance from top left corner
    #screen.blit(text,(X*0.25,0))
    pygame.display.update()

    # Limit frame rate (fps ceilling)
    clock.tick(60)
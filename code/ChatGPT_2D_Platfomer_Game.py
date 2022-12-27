import pygame
import spritesheet

X,Y=800,600
screen = pygame.display.set_mode((X,Y))
clock=pygame.time.Clock()
scroll = 0

# Parallax background
# Create a list of the images
game_background =[]
for i in range (1,5):
    image = pygame.image.load("ChatGPT_Pygame/background_plx-"+ str(i)+".png").convert_alpha()
    image = pygame.transform.scale(image, (X-50, Y-100))
    game_background.append(image)
# Create scrolling images function
def draw_background():
    for x in range(5): # 5 is number of time to duplicate the images on the right
        scroll_speed = 0.5
        for image in game_background:
            screen.blit(image, ((x * game_background[0].get_width()) - scroll * scroll_speed, 0)) # x * game_background image width
            scroll_speed += 0.2 # this creates the parallax effect! Images closer to player = moving faster
# Add the ground
ground = pygame.image.load("ChatGPT_Pygame/background_ground.png")
def draw_ground():
    for x in range (17):
        scroll_speed = 2
        screen.blit(ground, (x*ground.get_width() - scroll * scroll_speed, game_background[0].get_height()))

# Player Animation
# To animate sprite sheet
animation_list = []
animation_steps = [5,5,5,5,5,5,5] # (ordered from sprite sheet) number of frames per animation (e.g. action)
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = [300,60,60,250,250,250,250] # milliseconds
frame = 0 # frame that start the animation
set_counter = 0
# To use sprite sheet
sprite_sheet_image = pygame.image.load('ChatGPT_Pygame/sheet_sprite_player.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
total_num_frames = 35
for animation in animation_steps:
    temporary_list = []
    for _ in range(animation):
        temporary_list.append(sprite_sheet.get_image(set_counter, (sprite_sheet_image.get_width()/total_num_frames)-0.5, sprite_sheet_image.get_height(), 1)) #(frame,width,height,scale) & -0.5 for adjustements
        set_counter += 1
    animation_list.append(temporary_list)

# Game Loop
run = True
action = 4 # start in sleep animation
while run:
    clock.tick(40)
    draw_background()
    draw_ground()
    # Background scrolling with key pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_RIGHT]and scroll < 1850:
        scroll += 5
     # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown[action]:
        frame += 1 # Go to next frame after x milliseconds
        last_update = current_time # Reset cooldown
        if frame >= len(animation_list[action]):
            frame = 0 # To stop when frames in list are done
    # Load sprite sheets
    screen.blit(animation_list[action][frame],(100, Y-173))
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action = 2 # walk left
                frame = 0
            elif event.key == pygame.K_RIGHT:
                action = 1 # walk right
                frame = 0
            elif event.key == pygame.K_SPACE:
                action = 3 # jump
                frame = 0
            else:
                action = 0 # iddle
                frame = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    # Right key is still being held down, set action to walking right animation
                    action = 1
                    frame = 0
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    # Left key is still being held down, set action to walking left animation
                    action = 2
                    frame = 0
                else:
                    action = 0 # iddle
                    frame = 0
    # Update screen
    pygame.display.update()
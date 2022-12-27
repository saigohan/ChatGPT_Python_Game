import pygame

X,Y=800,600
screen = pygame.display.set_mode((X,Y))
clock=pygame.time.Clock()
scroll = 0

# Parallax background
# Create a list of the images
game_background =[]
for i in range (1,5):
    image = pygame.image.load("/Users/yonahbole/VsCode_Projects/Graphics/Parallax/plx-"+ str(i)+".png").convert_alpha()
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
ground = pygame.image.load("/Users/yonahbole/VsCode_Projects/Graphics/Parallax/ground.png")
def draw_ground():
    for x in range (17):
        scroll_speed = 2
        screen.blit(ground, (x*ground.get_width() - scroll * scroll_speed, game_background[0].get_height()))

# Game Loop
run = True 
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
    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update screen
    pygame.display.update()
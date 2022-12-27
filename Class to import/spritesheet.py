import pygame

# From YouTube: Coding With Russ
# 1. https://www.youtube.com/watch?v=M6e3_8LHc7A
# 2. https://www.youtube.com/watch?v=nXOVcOBqFwM 

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image
    def get_image(self,frame,width,height,scale,):#colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),0,width,height))
        image = pygame.transform.scale(image, (width*scale,height*scale)) # Scale 3 = size*3
        #image.set_colorkey(colour) # Specify the colour that should be transparent

        return image
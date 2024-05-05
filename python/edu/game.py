import pygame
import random
# pygame setup
pygame.init()
size = pygame.display.get_desktop_sizes()
img = open("python\\red.png","r")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
running = True
mouse = pygame.mouse
mouse.get_cursor
nb = pygame.Rect(400,400,50,50)
spr = pygame.sprite.Group()

pressed = False    


ims = pygame.image.load('python\\red.png').convert_alpha()
image_sprite = [ims,ims,ims,ims]
image = image_sprite[0]

while running:
    # poll for events
    pos = mouse.get_pos()
    if(pos >= (300,300) and pos <= (500,500) and mouse.get_pressed()==(True,False,False)):
        print('you hit it')
        pressed = True
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    x = pygame.surface.Surface((100,200),10)
    # RENDER YOUR GAME HERE
    spr.draw(screen)

   

    pygame.draw.circle(screen,"yellow",(500,300),50,50,True,True,True,True)
    y=300
  

    if pressed:
        pygame.display.update()
 
       
    
        x=300
        screen.blit(image,(x,y))

         
        
 
        

    # flip() the display to put your work on screen
    pygame.display.flip()

  #  clock.tick(0)  # limits FPS to 60

pygame.quit()

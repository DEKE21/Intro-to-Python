import pygame
import pygame.camera
# pygame setup
pygame.init()
size = pygame.display.get_desktop_sizes()
 
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
running = True
mouse = pygame.mouse
mouse.get_cursor
nb = pygame.Rect(400,400,50,50)
spr = pygame.sprite.Group()
pressed = False    

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
    screen.fill("white")
    x = pygame.surface.Surface((4,4),10)
    # RENDER YOUR GAME HERE
    pygame.draw.lines(screen,"blue",True,[(0,5),(888,5)],1)
    pygame.draw.circle(screen,"yellow",(500,300),50,50,True,True,True,True)
    
    if pressed:
        y=300
        screen.fill("white")
   
        pygame.time.delay(1500)
        screen.fill("white")
        pygame.draw.circle(screen,"yellow",(500,50),50,50,True,True,True,True)
        pygame.time.delay(1500)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

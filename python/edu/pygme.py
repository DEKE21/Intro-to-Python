import pygame
import random

pygame.init()
#width & height
w, h = 500, 500
#size of the player and target
S = 10
#movement speed
vel = 2
#declarations for scoreboard
spacePressed = 0
spaceHit = 0
font = pygame.font.Font('freesansbold.ttf', 12)
#play square class 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((S, S))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
    #function to move the player
    def update(self):
        keys = pygame.key.get_pressed()
        #set up quicker movement while holding shift 
        if keys[pygame.K_LSHIFT]:
            vel = 5
        else:
            vel = 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += vel
        if keys[pygame.K_UP]:
            self.rect.y -= vel
        if keys[pygame.K_DOWN]:
            self.rect.y += vel
#target class
class Target(pygame.sprite.Sprite):
    #self and sprite init
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((S, S))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
    #random location 
    def move_random(self):
        self.rect.x = random.randint(0, 500 - S)
        self.rect.y = random.randint(0, 500 - S)

# Create window and background color
screen = pygame.display.set_mode((500, 500))
screen.fill('black')

# Creation of player and block
player = Player()
target = Target()
#random cords function 
target.move_random()

# Game loop
running = True
while running:
    # Event loop to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #elif condition to count space presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spacePressed +=1
                #if statement is used to log successful hits and new position for the target
                if player.rect.colliderect(target.rect):
                    spaceHit +=1
                    target.move_random()

    # Update player for accurate responces 
    player.update()
    #init of scoreboard 
    acc  = 0
    if spacePressed >0:
        acc = spaceHit/spacePressed 
        acc = acc*100 
        acc = "{:.2f}".format(acc)
    pressesTxt = font.render(f'pressed: {spacePressed}', True,"white")
    hitTxt = font.render(f'hit count: {spaceHit}',True,"white")
    accTxt = font.render(f'hit accuracy {acc}%',True,"white")
    pressesRect = pressesTxt.get_rect()
    hitRect = hitTxt.get_rect()
    accRect = accTxt.get_rect()
    pressesRect.center = (300 // 2, 25 // 2)
    hitRect.center = (550 // 2, 25 // 2)
    accRect.center = (800 // 2, 25 // 2)



    # refreshs screen as black
    screen.fill('black')
    #player square
    screen.blit(player.image, player.rect)
    #target square
    screen.blit(target.image, target.rect)
    #scoreboard
    screen.blit(pressesTxt, pressesRect)
    screen.blit(hitTxt,hitRect)
    screen.blit(accTxt, accRect)
    

    # Flip the display to display blits 
    pygame.display.flip()

    #frame rate limits
    pygame.time.Clock().tick(60)

pygame.quit()
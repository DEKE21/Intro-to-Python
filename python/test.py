import pygame
import random

pygame.init()
w, h = 500, 500
S = 20
vel = 2
spacePressed = 0
spaceHit = 0
font = pygame.font.Font('freesansbold.ttf', 12)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((S, S))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
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

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((S, S))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def move_random(self):
        self.rect.x = random.randint(0, 500 - S)
        self.rect.y = random.randint(0, 500 - S)

# Create the game window
screen = pygame.display.set_mode((500, 500))
screen.fill('black')

# Create the player and block
player = Player()
block = Block()
block.move_random()

# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spacePressed +=1
                if player.rect.colliderect(block.rect):
                    spaceHit +=1
                    block.move_random()

    # Update the player
    acc  = 0
    if spacePressed >0:
        acc = spaceHit/spacePressed 
        acc = acc*100 
        acc = "{:.2f}".format(acc)
    player.update()
    pressesTxt = font.render(f'pressed: {spacePressed}', True,"white")
    hitTxt = font.render(f'hit count: {spaceHit}',True,"white")
    accTxt = font.render(f'hit accuracy {acc}%',True,"white")
    pressesRect = pressesTxt.get_rect()
    hitRect = hitTxt.get_rect()
    accRect = accTxt.get_rect()
    pressesRect.center = (300 // 2, 25 // 2)
    hitRect.center = (550 // 2, 25 // 2)
    accRect.center = (800 // 2, 25 // 2)



    # Draw everything
    screen.fill('black')
    screen.blit(player.image, player.rect)
    screen.blit(block.image, block.rect)
    screen.blit(pressesTxt, pressesRect)
    screen.blit(hitTxt,hitRect)
    screen.blit(accTxt, accRect)
    

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
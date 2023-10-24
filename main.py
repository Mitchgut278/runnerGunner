import pygame, sys
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=(50,200))
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill('crimson')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 50
    
    def update(self):
        self.rect.x -= 5

player = Player()
enemy = Enemy()

players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
players.add(player)
enemies.add(enemy)

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == enemy_timer:
            enemies.add(Enemy())
    screen.fill('black')
    players.update()
    enemies.update()   
    players.draw(screen)
    enemies.draw(screen)

    pygame.display.update()
    
    clock.tick(60)
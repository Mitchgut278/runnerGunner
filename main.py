from random import choice
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
    
    def move(self, dir):
        # TODO add move animation
        if dir == 'up':
            self.rect.y -= 100
        elif dir == 'down':
            self.rect.y += 100
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill('crimson')
        self.rect = self.image.get_rect()
        self.rect.center = (1000,y_pos)
    
    def update(self):
        self.rect.x -= 5
        if self.rect.x <= -50:
            self.kill()

player = Player()
enemy = Enemy(100)

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
            y_pos = choice([100,200,300])
            enemies.add(Enemy(y_pos))
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.move('down')
            if event.key == pygame.K_UP:
                player.move('up')

        

    screen.fill('black')
    players.update()
    enemies.update()
    players.draw(screen)
    enemies.draw(screen)

    pygame.display.update()
    
    clock.tick(60)
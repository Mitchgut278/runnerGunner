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

        self.moving = False
        self.direction = ''
        self.moving_start_time = pygame.time.get_ticks()

    def player_input(self):
        if event.type == pygame.KEYDOWN:
            if not self.moving:
                self.moving = True
                self.moving_start_time = pygame.time.get_ticks()
                if event.key == pygame.K_DOWN:
                    print('here')
                    self.direction = 'down'
                if event.key == pygame.K_UP:
                    self.direction = 'up'

    def move_player(self):
        # TODO line up movement with enemies
        if self.moving:
            if self.direction == 'up':
                self.rect.y -= 3
            elif self.direction == 'down':
                self.rect.y += 3

    def cooldowns(self):
        print(self.moving)
        current_time = pygame.time.get_ticks()
        if self.moving:
            if current_time - self.moving_start_time >= 500:
                self.moving = False

    def update(self):
        self.player_input()
        self.move_player()
        self.cooldowns()
        
    # def move(self, dir):
    #     # TODO add move animation/timer
    #     if dir == 'up':
            
    #     elif dir == 'down':
            
        
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

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, enemies, False):
        print('collision')

enemy = Enemy(100)
player = pygame.sprite.GroupSingle()
enemies = pygame.sprite.Group()
player.add(Player())
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
    
    screen.fill('black')
    player.update()
    enemies.update()
    player.draw(screen)
    enemies.draw(screen)
    collision_sprite()
    pygame.display.update()
    
    clock.tick(60)
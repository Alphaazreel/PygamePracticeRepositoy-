import pygame
from pygame.sprite import _Group

class Player(pygame.sprite.Sprite):
  #Making a constructor
    def __init__(self, position):
       #Clearer of class methods 
        super().__init__()

    #Getting image
        self.image = pygame.image.load('img/sprite,svg')
        self.image = pygame.transform.smoothscale(self.image,(100, 100))
        self.rect = self.image.get_rect(midbottom = position)

    def get_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.left = self.rect.left + 3

        if keys[pygame.K_RIGHT]:
            self.rect.left -= 3

    def update(self):
        self.get_input()
        
        
        
        kill()
        
        stop()
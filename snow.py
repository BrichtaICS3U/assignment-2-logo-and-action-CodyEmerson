import pygame
from math import pi
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Snow(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, speed):
        
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.color = color
        self.width = width
        self.height = height
        self.speed = speed

        pygame.draw.ellipse(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    def moveDown(self, speed):
        self.rect.y += self.speed*speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

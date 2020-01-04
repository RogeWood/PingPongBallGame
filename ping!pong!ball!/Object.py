import pygame
from pygame.math import Vector2
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self,spx,spy,dx,dy,red,green,blue):
        pygame.sprite.Sprite.__init__(self)
        self.ballP = Vector2(spx,spy)
        self.ballV = Vector2(dx,dy)
        self.ballColor = (red,green,blue)
        self.HasCreatNewBall = True
        pygame.mixer.music.load("audio/ball_collision.mp3")

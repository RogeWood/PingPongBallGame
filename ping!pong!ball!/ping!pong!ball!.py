import pygame
from pygame.locals import *
from pygame.math import Vector2
from random import randint

pygame.init()
screen = pygame.display.set_mode((640,480))
icon = pygame.image.load("image/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("ping!pong!ball!")
fpsclock = pygame.time.Clock()
FPS = 60
running = True

barW = 60
barH = 30
barP = Vector2(200,460)
score = 0

hitBar = False
gameOver = True

balls = []

class Ball(pygame.sprite.Sprite):
    def __init__(self,spx,spy,dx,dy,red,green,blue):
        pygame.sprite.Sprite.__init__(self)
        self.ballP = Vector2(spx,spy)
        self.ballV = Vector2(dx,dy)
        self.ballColor = (red,green,blue)
        self.HasCreatNewBall = True
        pygame.mixer.music.load("audio/ball_collision.mp3")

    def moveBall(self):
        self.ballP += self.ballV

    def BallCollision(self,barPx,barPy,barW,barH):
        hitBar = False

        dis = self.ballP+self.ballV - (barPx,barPy)
        if (abs(dis.x) < barW/2) and (abs(dis.y) < barH/2):
            hitBar = True

        if self.ballP.x > screen.get_width() or self.ballP.x < 0:
            pygame.mixer.music.play()
            self.ballV.x *= -1
            self.HasCreatNewBall = False
        if hitBar or self.ballP.y < 0:
            if hitBar and self.HasCreatNewBall == False:
                pygame.mixer.music.play()
                self.ballV.y *= -1
                self.creatNewBall()
                self.HasCreatNewBall = True
            elif self.ballP.y < 0:
                pygame.mixer.music.play()
                self.ballV.y *= -1
                self.HasCreatNewBall = False

        elif self.ballP.y > screen.get_height():
            balls.clear()
            global gameOver
            gameOver = True

    def creatNewBall(self):
        global score
        score += 1
        item = Ball(self.ballP.x,self.ballP.y-15,randint(2,5),randint(2,5)*-1,randint(50,255),randint(50,255),randint(0,200))
        balls.append(item)

    def BallUpdate(self,barPx,barPy,barW,barH):
        self.moveBall()
        self.BallCollision(barPx,barPy,barW,barH)
        pygame.draw.circle(screen, self.ballColor, [int(self.ballP.x),int(self.ballP.y)],10)


def GameStart():
    screen.fill((0,0,255))

    for ball in balls:
        ball.BallUpdate(barP.x,barP.y,barW,barH)

def Menu():
    screen.fill((0,0,0))
    menuFont = pygame.font.Font("font/Roboto-Black.ttf",24)
    printPlayAgain = menuFont.render("Press the space bar to play",True,(255,255,255))
    screen.blit(printPlayAgain,(170,300))
    menuFont = pygame.font.Font("font/Roboto-Black.ttf",34)
    printScore = menuFont.render("You got "+str(score)+" point",True,(200,200,0),(100,100,255))
    screen.blit(printScore,(200,200))

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE and gameOver:
                item = Ball(0,0,5,3,255,50,50)
                balls.append(item)
                score = 0
                gameOver = False
        elif event.type == QUIT:
            running = False

    if gameOver == False:
        GameStart()
    else:
        Menu()

    mouseX, mouseY = pygame.mouse.get_pos()
    barP.x = max(min(mouseX,screen.get_width()),0)
    pygame.draw.rect(screen, (200,200,0), [barP.x-barW/2,barP.y-barH/2,barW,barH])
    pygame.display.update()
    fpsclock.tick(FPS)

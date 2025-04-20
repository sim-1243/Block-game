import pygame
class Bullet:
    x: int
    y: int
    width:int
    color=(0,0,0)
    height:int
    speed:int
    direction: bool
    def __init__(self,x,y,color,direction):
        self.x=x+23
        self.y=y+23
        self.width=7
        self.height=7
        self.color=color
        self.speed=10
        self.schaden=40
        self.direction=direction
    def move(self):
        if self.direction:
            self.x+=self.speed
        else:
            self.x -=self.speed
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
class Gas:
    x: int
    y: int
    width: int
    height: int
    color=(0,0,0)
    speed: int
    direction: bool
    def __init__(self,x,y,color,direction):
        self.x=x
        self.y=y
        self.width=15
        self.height=15
        self.color=color
        self.speed=10
        self.direction=direction
    def move(self):
        if self.direction:
            self.x+=2
        else:
            self.x-=2
        self.width+=5
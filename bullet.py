class Bullet:
    x: int
    y: int
    width:int
    color=(0,0,0)
    height:int
    speed:int
    direction: bool
    def __init__(self,x,y,color,direction):
        self.x=x+50
        self.y=y+50
        self.width=15
        self.height=15
        self.color=color
        self.speed=10
        self.direction=direction
    def move(self):
        if self.direction:
            self.x+=self.speed
        else:
            self.x -=self.speed
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
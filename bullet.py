class Bullet:
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
            self.x+=self.speed
        else:
            self.x -=self.speed

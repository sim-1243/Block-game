import color
duration=240
class healt_boost:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=15
        self.height=15
        self.color=color.blue
        self.duration=duration
    def get_used(self):
        self.duration-=1
    def __del__(self):
        pass

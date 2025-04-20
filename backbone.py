import bullet
import pygame
import color
class Player():
    def __init__(self,x,y,color):
        self.leben=100
        self.width=100
        self.height=100
        self.x=x
        self.y=y
        self.color=color
        self.bullets=[]
        self.score=0
        self.cooled=True
        self.timer=30
    def shoot(self,direction):
        self.bullets.append(bullet.Bullet(self.x,self.y,(0,0,0),direction))
        self.cooled=False
    def get_hit(self,schaden):
        self.leben-= schaden
    def heal(self):
        if self.leben < 100:
            self.leben+=0.5
    def out(self,screen_width,screen_height):
        if self.x+self.width >screen_width:
            self.x -= 10
        elif self.x < 0:
            self.x += 10
        if self.y < 0:
            self.y += 10
        elif self.y+self.height > screen_height:
            self.y -=10
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen,color.red,(self.x,self.y-25, self.leben, 15))
    def cooldown(self):
        if self.timer==0:
            self.timer=30
            self.cooled=True
        else:
            self.timer-=1
    
    def joy_move(self,joystick_id,gegner):
        joystick=pygame.joystick.Joystick(joystick_id)
        joystick_x = joystick.get_axis(0)  # Clamp x-axis value between -1 and 1
        joystick_y = joystick.get_axis(1) # Clamp y-axis value between -1 and 1
        self.cooldown()
        if joystick_y < -0.25 :  # Assuming small threshold instead of fixed values
            self.y -= 5
        elif joystick_y > 0.25 :
            self.y += 5

        if joystick_x < -0.25 :  # Assuming small threshold instead of fixed values
            self.x -= 5
        elif joystick_x > 0.25 :
            self.x += 5
        if joystick.get_button(8) and len(self.bullets) <=50 and self.cooled:
            self.shoot(richtung(self.x,gegner.x))


def collision (px,bx,py,by,pwidth,pheight,bwith,bheight):
    if px < bx + bwith and px + pwidth > bx and py< by + bheight and py + pheight> by:
        return True
    else:
        return False
def booster_collision(schaden,px,py,pwidth,pheight,lbooster,lbool):
    for i in range (len(lbooster)):
        if lbool[i] and collision(px,lbooster[i].x,py,lbooster[i].y,pwidth,pheight,lbooster[i].width,lbooster[i].height):
            schaden=schaden//2
            lbooster[i].x=px
            lbooster[i].y=py
            lbooster[i].duration-=1
            if lbooster[i].duration<=0:
                lbool[i]=False
                lbooster[i].duration=240
        i+=1
    return schaden,lbool,lbooster
def bullet_collision(schaden,score,px,py,pwidth,pheight,lbullet,lbool):
    for i in range(len(lbullet)):
        if lbool[i] and collision(px,lbullet[i].x,py,lbullet[i].y,pwidth,pheight,lbullet[i].width,lbullet[i].height):
            score+=100
            schaden=40
            lbool[i]=False
        i+=1
    return score ,schaden,lbool,lbullet
def bullet_movement(self,lbool,lcoord,px,py):
    if self:
        for i in range (len(lbool)):
            if lbool[i]:
                lcoord[i].x+=10
            else:
                lcoord[i].x=px
                lcoord[i].y=py
            i+=1
    elif not self:
        for i in range (len(lbool)):
            if lbool[i]:
                lcoord[i].x-=10
            else:
                lcoord[i].x=px
                lcoord[i].y=py
            i+=1
    return lcoord
def richtung(x1,x2):
    if x1>x2:
        return False
    elif x1<x2:
        return True
def player_out(px,py,width,height,player_width,player_height):
    if px+player_width>=width:
        px-=5
    elif px<=0:
        px+=5
    elif py+player_height*1.75>=height:
        py-=5
    elif py<=0:
        py+=5
    return px,py
def out_of_screen(x,y,screen_width,screen_height):
    if x >= screen_width or x <= 0 or y >=screen_height or y <=0:
        return  True
    return False


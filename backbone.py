def leben_verlust(wert,schaden):
    if wert !=0 and schaden !=0:
        wert-=schaden
        schaden=0
    elif wert <= 0:
        return False ,wert ,schaden
    elif wert!=0 and schaden ==0 and wert<100:
        wert+=1
    else:
        return True, wert ,schaden
    return True, wert, schaden
def collision (px,bx,py,by,pwidth,pheight,bwith,bheight):
    if px < bx + bwith and px + pwidth > bx and py< by + bheight and py + pheight> by:
        return True
    else:
        return False
def bullet_collision(self,schaden,score,px,bx,py,by,pwidth,pheight,bwith,bheight):
    if collision(px,bx,py,by,pwidth,pheight,bwith,bheight):
        score+=100
        schaden=25
        self=False
    return score ,schaden,self
def bullet_movement(self,x,y):
    if self:
        x+=10
        return x
    elif not self:
        x-=10
        return x
def richtung(x1,x2):
    if x1>x2:
        return False
    elif x1<x2:
        return True
def out_of_screen(px,py,x,y,width,height):
    if x>width:
        self=False
    elif x<0:
        self= False
    elif y>height:
        self=False
    elif y<0:
        self= False
    else:
        self= True 
    if not self:
        return px, py, False
    else:
        return x,y,True

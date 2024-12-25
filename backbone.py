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
def bullet_collision(schaden,score,px,py,pwidth,pheight,lbullet,lbool):
    for i in range(len(lbullet)):
        if lbool[i] and collision(px,lbullet[i].x,py,lbullet[i].y,pwidth,pheight,lbullet[i].width,lbullet[i].height):
            score+=100
            schaden=25
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
def out_of_screen(px,py,lcoord,lbool,width,height):
    for i in range(len(lcoord)):
        if lcoord[i].x>width:
            lbool[i]=False
            lcoord[i].x=px
        elif lcoord[i].x<0:
            lbool[i]=False
            lcoord[i].x=px
        elif lcoord[i].y>height:
            lbool[i]=False
            lcoord[i].y=py
        elif lcoord[i].y<0:
            lbool[i]=False
            lcoord[i].y=py
        i+=1
    return lcoord, lbool
def bullet_frei(kugel):
    for i in range (len(kugel)):
        if not kugel[i]:
            kugel[i]=True
            return kugel, 30
        i+=1
    return kugel,0
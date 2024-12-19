import pygame
from math import sqrt

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
    pkx=px
    pky=py
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


# Initialisierung von Pygame
pygame.init()

# Spielfenster einrichten
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Spieltitel und Icons festlegen
pygame.display.set_caption("2D Game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
i=0
enemy_ca=False
score1 =0
score = 0
enemy_d=False
kugel_ca=False
# Spielfiguren einrichten
target=False
player=True
player_x = 50
player_y = 50
player_width = 100
player_height = 100
player_color = (255, 0, 0)
kugel_c=False
enemy_c=False
# Gegner einrichten
enemy_y = screen_height // 2
enemy_width = 25
enemy_height = 25
enemy_x = screen_width - enemy_width
enemy_cy= enemy_y
enemy_cx=enemy_x
enemy_color = (0, 255, 0)
kugel_d = False
kugel_x = player_x
kugel_y = player_y
kugel_cy=kugel_y
kugel_width = 15
kugel_height = 15
kugel_color = (0,0,0)
kugel_cx= kugel_x
Kuge_hit=pygame.Rect(kugel_cx, kugel_cy, kugel_width, kugel_height)
target_y = screen_height // 2
target_width = 100
target_height = 100
target_x = screen_width - target_width
target_color = (150,37,62)
target_hit = pygame.Rect(target_x, target_y, target_width, target_height)
# Spielfeld einrichten
field_width = 800
field_height = 600
field_color = (255, 255, 255)

# Spielschleife
running = True
while running:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player= richtung(player_x,target_x)
    target=richtung(target_x,player_x)
    
    # Spielerbewegung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= 5
    elif keys[pygame.K_d]:
        player_x += 5
    if keys[pygame.K_w]:
        player_y -= 5
    elif keys[pygame.K_s]:
        player_y += 5
    if keys[pygame.K_UP]:
        target_y -=5
    elif keys[pygame.K_DOWN]:
        target_y += 5
    if keys[pygame.K_LEFT]:
        target_x -= 5
    elif keys[pygame.K_RIGHT]:
        target_x +=5
    if keys[pygame.K_e] and not kugel_c:
        kugel_c=True
        kugel_ca=True
    elif keys[pygame.K_e] and kugel_ca and i > 30:
        kugel_d = True
        i=0
        kugel_ca =False
    if keys[pygame.K_RCTRL]:
        enemy_c=True
        enemy_ca=True
    elif keys[pygame.K_RCTRL] and enemy_c and j> 30:
        enemy_d=True
        j=0
        enemy_ca=False
    if keys[pygame.K_ESCAPE]:
        running=False
        print("palyer1 hat ",score,"punkte", "player2 hat ",score1, "punkte")

    # Gegnerbewegung
    if kugel_ca:
        i+=1
    if enemy_d:
        enemy_x=bullet_movement(target,enemy_x,enemy_y)
        enemy_x,enemy_y,enemy_d=out_of_screen(target_x,target_y,enemy_x,enemy_y,screen_width,screen_height)

    else:
        enemy_x = target_x
        enemy_y = target_y
    if kugel_c:
        kugel_cx,kugel_cy,kugel_c=out_of_screen(player_x,player_y,kugel_cx,kugel_cy,screen_width,screen_height)
        kugel_cx=bullet_movement(player,kugel_cx,kugel_cy)
    else:
        kugel_cx = player_x
        kugel_cy = player_y
    if enemy_c:
        enemy_cx=bullet_movement(target,enemy_cx,enemy_cy)
        enemy_cx,enemy_cy,enemy_c=out_of_screen(target_x,target_y,enemy_cx,enemy_cy,screen_width,screen_height)
    else:
        enemy_cx = target_x
        enemy_cy =target_y
    if kugel_d:
        kugel_x=bullet_movement(player,kugel_x,kugel_y)
        kugel_x,kugel_y,kugel_d=out_of_screen(player_x,player_y,kugel_x,kugel_y,screen_width,screen_height)
    else:
        kugel_x = player_x
        kugel_y = player_y
    # Spieler-Gegner-Kollision
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height> enemy_y:
        score1 += 100
        enemy_c =False
        enemy_x =target_x
    #if pygame.Rect.colliderect(target_y, target_y-target_height, target_x, target_x-target_width):
        #score += 100
        #del(kugel)
    if player_x < enemy_cx + enemy_width and player_x + player_width > enemy_cx and player_y < enemy_cy + enemy_height and player_y + player_height> enemy_cy:
        score1 += 100
        enemy_c =False
        enemy_x =target_x
    if kugel_cx < target_x + target_width and kugel_width+kugel_cx > target_x and kugel_cy < target_y + target_height and kugel_cy + kugel_width >target_y:
        score +=100
        kugel_c = False
        kugel_cx = player_x
    elif kugel_x < target_x + target_width and kugel_width+kugel_x > target_x and kugel_y < target_y + target_height and kugel_y + kugel_width >target_y:
        score +=100
        kugel_d = False
        kugel_x = player_x
    # Spielfeld zeichnen
    screen.fill(field_color)
    pygame.draw.rect(screen, kugel_color, (kugel_cx,kugel_cy,kugel_width,kugel_height))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, kugel_color,(kugel_x,kugel_y,kugel_width,kugel_height))
    pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.draw.rect(screen, target_color,(target_x,target_y,target_width,target_height))
    pygame.draw.rect(screen, enemy_color, (enemy_cx, enemy_cy, enemy_width, enemy_height))
    # Framerate begrenzen
    clock = pygame.time.Clock()
    clock.tick(60)
    
    # Bildschirm aktualisieren
    pygame.display.flip()

# Quit Pygame
pygame.quit()

import pygame
from math import sqrt
import backbone
import bullet

# Initialisierung von Pygame
pygame.init()

# Spielfenster einrichten
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Spieltitel und Icons festlegen
pygame.display.set_caption("2D Game")
k=0
kugeln=[]
leben=100
leben_height=10
leben_x=15
leben_y=15
leben_t=100
leben_tx=screen_width -120
schaden=0
schaden1=0
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
emerg=True
while running and emerg:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player=backbone.richtung(player_x,target_x)
    target=backbone.richtung(target_x,player_x)
    
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
        kugel=bullet.Bullet(player_x,player_y,kugel_color,player)
        kugeln.append(k)
        k+=1
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
        emerg=False
        print("palyer1 hat ",score,"punkte", "player2 hat ",score1, "punkte")
    player_x,player_y=backbone.player_out(player_x,player_y,screen_width,screen_height,player_width,player_height)
    target_x,target_y=backbone.player_out(target_x,target_y,screen_width,screen_height,target_width,target_height)
    # Gegnerbewegung
    if kugel_ca:
        i+=1
    if enemy_d:
        enemy_x=backbone.bullet_movement(target,enemy_x,enemy_y)
        enemy_x,enemy_y,enemy_d=backbone.out_of_screen(target_x,target_y,enemy_x,enemy_y,screen_width,screen_height)

    else:
        enemy_x = target_x
        enemy_y = target_y
    if kugel_c:
        kugel_cx,kugel_cy,kugel_c=backbone.out_of_screen(player_x,player_y,kugel_cx,kugel_cy,screen_width,screen_height)
        kugel_cx=backbone.bullet_movement(player,kugel_cx,kugel_cy)
    else:
        kugel_cx = player_x
        kugel_cy = player_y
    if enemy_c:
        enemy_cx=backbone.bullet_movement(target,enemy_cx,enemy_cy)
        enemy_cx,enemy_cy,enemy_c=backbone.out_of_screen(target_x,target_y,enemy_cx,enemy_cy,screen_width,screen_height)
    else:
        enemy_cx = target_x
        enemy_cy =target_y
    if kugel_d:
        kugel_x=backbone.bullet_movement(player,kugel_x,kugel_y)
        kugel_x,kugel_y,kugel_d=backbone.out_of_screen(player_x,player_y,kugel_x,kugel_y,screen_width,screen_height)
    else:
        kugel_x = player_x
        kugel_y = player_y
    
    # Spieler-Gegner-Kollision
    score,schaden1,kugel_c=backbone.bullet_collision(kugel_c,schaden1,score,target_x,kugel_cx,target_y,kugel_cy,target_width,target_height,kugel_width,kugel_height)
    score,schaden1,kugel_d=backbone.bullet_collision(kugel_d,schaden1,score,target_x,kugel_x,target_y,kugel_y,target_width,target_height,kugel_width,kugel_height)
    score1,schaden,enemy_d=backbone.bullet_collision(enemy_d,schaden,score1,player_x,enemy_x,player_y,enemy_y,player_width,player_height,enemy_width,enemy_height)
    score1,schaden,enemy_c=backbone.bullet_collision(enemy_c,schaden,score1,player_x,enemy_cx,player_y,enemy_cy,player_width,player_height,enemy_width,enemy_height)
    # Spielfeld zeichnen
    running,leben,schaden=backbone.leben_verlust(leben,schaden)
    running,leben_t,schaden1=backbone.leben_verlust(leben_t,schaden1)
    if leben <=0 or leben_t <=0:
        print("palyer1 hat ",score,"punkte", "player2 hat ",score1, "punkte")
        running=False
    
    screen.fill(field_color)
    pygame.draw.rect(screen, player_color,(leben_x, leben_y, leben, leben_height))
    pygame.draw.rect(screen, player_color,(leben_tx,leben_y,leben_t,leben_height))
    pygame.draw.rect(screen, kugel_color, (kugel_cx,kugel_cy,kugel_width,kugel_height))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    if kugel_c:
        pygame.draw.rect(screen, kugel_color,(kugel.x,kugel.y,kugel.width,kugel.height))
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
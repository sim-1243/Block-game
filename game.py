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
enemy_color = (0, 255, 0)
kugel_d = False
kugel_color = (0,0,0)
target_y = screen_height // 2
target_width = 100
target_height = 100
target_x = screen_width - target_width
target_color = (150,37,62)
kugel0=bullet.Bullet(player_x,player_y,kugel_color,player)
kugel1=bullet.Bullet(player_x,player_y,kugel_color,player)
enemy0=bullet.Bullet(target_x,target_y,enemy_color,target)
enemy1=bullet.Bullet(target_x,target_y,enemy_color,target)
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
        enemy0.x=backbone.bullet_movement(target,enemy0.x,enemy0.y)
        enemy0.x,enemy0.y,enemy_d=backbone.out_of_screen(target_x,target_y,enemy0.x,enemy0.y,screen_width,screen_height)

    else:
        enemy0.x = target_x
        enemy0.y = target_y
    if kugel_c:
        kugel1.x,kugel1.y,kugel_c=backbone.out_of_screen(player_x,player_y,kugel1.x,kugel1.y,screen_width,screen_height)
        kugel1.x=backbone.bullet_movement(player,kugel1.x,kugel1.y)
    else:
        kugel1.x = player_x
        kugel1.y = player_y
    if enemy_c:
        enemy1.x=backbone.bullet_movement(target,enemy1.x,enemy1.y)
        enemy1.x,enemy1.y,enemy_c=backbone.out_of_screen(target_x,target_y,enemy1.x,enemy1.y,screen_width,screen_height)
    else:
        enemy1.x = target_x
        enemy1.y =target_y
    if kugel_d:
        kugel0.x=backbone.bullet_movement(player,kugel0.x,kugel0.y)
        kugel0.x,kugel0.y,kugel_d=backbone.out_of_screen(player_x,player_y,kugel0.x,kugel0.y,screen_width,screen_height)
    else:
        kugel0.x = player_x
        kugel0.y = player_y
    
    # Spieler-Gegner-Kollision
    score,schaden1,kugel_c=backbone.bullet_collision(kugel_c,schaden1,score,target_x,kugel1.x,target_y,kugel1.y,target_width,target_height,kugel1.width,kugel1.height)
    score,schaden1,kugel_d=backbone.bullet_collision(kugel_d,schaden1,score,target_x,kugel0.x,target_y,kugel0.y,target_width,target_height,kugel0.width,kugel0.height)
    score1,schaden,enemy_d=backbone.bullet_collision(enemy_d,schaden,score1,player_x,enemy0.x,player_y,enemy0.y,player_width,player_height,enemy0.width,enemy0.height)
    score1,schaden,enemy_c=backbone.bullet_collision(enemy_c,schaden,score1,player_x,enemy1.x,player_y,enemy1.y,player_width,player_height,enemy1.width,enemy1.height)
    # Spielfeld zeichnen
    running,leben,schaden=backbone.leben_verlust(leben,schaden)
    running,leben_t,schaden1=backbone.leben_verlust(leben_t,schaden1)
    if leben <=0 or leben_t <=0:
        print("palyer1 hat ",score,"punkte", "player2 hat ",score1, "punkte")
        running=False
    
    screen.fill(field_color)
    pygame.draw.rect(screen, player_color,(leben_x, leben_y, leben, leben_height))
    pygame.draw.rect(screen, player_color,(leben_tx,leben_y,leben_t,leben_height))
    pygame.draw.rect(screen, kugel_color, (kugel1.x,kugel1.y,kugel1.width,kugel1.height))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, kugel_color,(kugel0.x,kugel0.y,kugel0.width,kugel0.height))
    pygame.draw.rect(screen, enemy_color, (enemy0.x, enemy0.y, enemy0.width, enemy0.height))
    pygame.draw.rect(screen, target_color,(target_x,target_y,target_width,target_height))
    pygame.draw.rect(screen, enemy_color, (enemy1.x, enemy1.y, enemy1.width, enemy1.height))
    # Framerate begrenzen
    clock = pygame.time.Clock()
    clock.tick(60)
    
    # Bildschirm aktualisieren
    pygame.display.flip()

# Quit Pygame
pygame.quit()
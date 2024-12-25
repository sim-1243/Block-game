import pygame
import color
import backbone
import bullet
import booster
import random
# Initialisierung von Pygame
pygame.init()

# Spielfenster einrichten
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Spieltitel und Icons festlegen
pygame.display.set_caption("2D Game")
a=3
hboost0=booster.healt_boost(800,-35)
hboost1=booster.healt_boost(800,-35)
hboost2=booster.healt_boost(800,-35)
boost=[hboost0,hboost1,hboost2]
boosters=[False] *a
kugeln=[False] *a
enemys=[False]*a
leben=100
leben_height=10
leben_x=15
leben_y=15
leben_t=100
leben_tx=screen_width -120
schaden=0
schaden1=0
i=0
j=0
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
player_color = color.red
kugel_c=False
enemy_c=False
# Gegner einrichten
enemy_color = color.green
kugel_d = False
kugel_color = color.black
target_y = screen_height // 2
target_width = 100
target_height = 100
target_x = screen_width - target_width
target_color = (150,37,62)
kugel0=bullet.Bullet(player_x,player_y,kugel_color,player)
kugel1=bullet.Bullet(player_x,player_y,kugel_color,player)
kugel2=bullet.Bullet(player_x,player_y,kugel_color,player)
enemy0=bullet.Bullet(target_x,target_y,enemy_color,target)
enemy1=bullet.Bullet(target_x,target_y,enemy_color,target)
enemy2=bullet.Bullet(target_x,target_y,enemy_color,target)
enemy=[enemy0,enemy1,enemy2]
kugel=[kugel0,kugel1,kugel2]
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
    if keys[pygame.K_e]and i==0:
        kugeln,i=backbone.bullet_frei(kugeln)
    if keys[pygame.K_RCTRL] and j == 0:
        enemys,j=backbone.bullet_frei(enemys)
    if keys[pygame.K_ESCAPE]:
        emerg=False
        print("palyer1 hat ",score,"punkte", "player2 hat ",score1, "punkte")
    if random.randint(1,100) == 5:
        for l in range (len(boost)):
            if not boosters[l]:
                boosters[l]=True
                boost[l].x=random.randint(2,screen_width-2)
                boost[l].y=random.randint(2,screen_height-2)
            l+=1
    player_x,player_y=backbone.player_out(player_x,player_y,screen_width,screen_height,player_width,player_height)
    target_x,target_y=backbone.player_out(target_x,target_y,screen_width,screen_height,target_width,target_height)
    # Gegnerbewegung
    if i>0:
        i-=1
    if j>0:
        j-=1
    enemy=backbone.bullet_movement(target,enemys,enemy,target_x,target_y)
    enemy,enemys=backbone.out_of_screen(target_x,target_y,enemy,enemys,screen_width,screen_height)
    kugel=backbone.bullet_movement(player,kugeln,kugel,player_x,player_y)
    kugel,kugeln=backbone.out_of_screen(player_x,player_y,kugel,kugeln,screen_width,screen_height)
    # Spieler-Gegner-Kollision
    score,schaden1,kugeln,kugel=backbone.bullet_collision(schaden1,score,target_x,target_y,target_width,target_height,kugel,kugeln)
    score1,schaden,enemys,enemy=backbone.bullet_collision(schaden,score1,player_x,player_y,player_width,player_height,enemy,enemys)
    # Spieler-Booster-Kollision
    schaden,boosters,boost=backbone.booster_collision(schaden,player_x,player_y,player_width,player_height,boost,boosters)
    schaden1,boosters,boost=backbone.booster_collision(schaden1,target_x,target_y,target_width,target_height,boost,boosters)
    # Spielfeld zeichnen
    running,leben,schaden=backbone.leben_verlust(leben,schaden)
    running,leben_t,schaden1=backbone.leben_verlust(leben_t,schaden1)
    if leben <=0 or leben_t <=0:
        print("palyer1 hat ",score,"punkte", "player2 hat ",score1, "punkte")
        running=False
    
    screen.fill(field_color)
    for z in range (len(boost)):
        if boosters[z]:
            pygame.draw.rect(screen,boost[z].color,(boost[z].x,boost[z].y,boost[z].width,boost[z].height))
        z+=1
    for z in range (len(kugel)):
        if kugeln[z]:
            pygame.draw.rect(screen,kugel_color,(kugel[z].x,kugel[z].y,kugel[z].width,kugel[z].height))
        z+=1
    for z in range(len(enemy)):
        if enemys[z]:
            pygame.draw.rect(screen,enemy_color,(enemy[z].x,enemy[z].y,enemy[z].width,enemy[z].height))
        z+=1
    pygame.draw.rect(screen, player_color,(leben_x, leben_y, leben, leben_height))
    pygame.draw.rect(screen, player_color,(leben_tx,leben_y,leben_t,leben_height))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, target_color,(target_x,target_y,target_width,target_height))
    # Framerate begrenzen
    clock = pygame.time.Clock()
    clock.tick(60)
    
    # Bildschirm aktualisieren
    pygame.display.flip()

# Quit Pygame
pygame.quit()
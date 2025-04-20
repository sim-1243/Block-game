import pygame
import color
import backbone
import bullet
import booster
import random

from input import *

# Initialisierung von Pygame
pygame.init()
pygame.font.init()

# Eingabe modus
input_mode: EInputType = EInputType.Keyboard;

# Spielfenster einrichten
screen_width = 1920 / 2
screen_height = 1080 / 2
screen = pygame.display.set_mode((screen_width, screen_height))
# Spieltitel und Icons festlegen
pygame.display.set_caption("2D Game")
boost=[]
mülli=[]
debug=False
player=backbone.Player(50,50,color.red)
target=backbone.Player(1000,50,color.blue)
# tastatur=False
Font='Ubuntu-Title.ttf'
my_font=pygame.font.Font(Font,30)
player_1=True
player_2=False
running = True
while running:
    mülli.clear()
    j=0
    i=0
    k=0
    l=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    if input_mode == EInputType.Keyboard:
        #Player Move
        if keys[pygame.K_a]:
            player.x -= 5
        elif keys[pygame.K_d]:
            player.x += 5
        if keys[pygame.K_w]:
            player.y -= 5
        elif keys[pygame.K_s]:
            player.y += 5
        #/Player move
        #target move
        if keys[pygame.K_UP]:
            target.y -=5
        elif keys[pygame.K_DOWN]:
            target.y += 5
        if keys[pygame.K_LEFT]:
            target.x -= 5
        elif keys[pygame.K_RIGHT]:
            target.x +=5
        #/target move
        #players fire len(player.bullets) <=50
        if keys[pygame.K_e] and len(player.bullets) > 0 and not player.cooldown():
            player.shoot(backbone.richtung(player.x,target.x))
        if keys[pygame.K_MINUS] and len(player.bullets) > 0 and not target.cooldown():
            target.shoot(backbone.richtung(target.x,player.x))
        #/players fire
    elif input_mode == EInputType.Controller:
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        joystick=pygame.joystick.Joystick(0)
        if joystick.get_button(11):
            running=False
        if  debug and joystick.get_button(9):
            player_1=True
            player_2=False
        elif  debug and joystick.get_button(10):
            player_1=False
            player_2=True
        #Player move
        if debug and player_1:
            player.joy_move(0,target)
        elif debug:
            p=1
        else:
            player.joy_move(0,target)
        #/player move
        #target move
        try:
            if debug and player_2:
                target.joy_move(0,player)
            elif debug:
                p=0
            else :
                target.joy_move(1,player)
            #/target move
        except pygame.error:
            tastatur=True
    else:
        print("Invalider Eingabemodus!")
        exit()

    #collisionen
    for j in range (len(player.bullets)):
        player.bullets[j].move()
        if backbone.collision(target.x,player.bullets[j].x, target.y, player.bullets[j].y,target.width,target.height,player.bullets[j].width,player.bullets[j].height):
            target.get_hit(player.bullets[j].schaden)
            player.score+=100
            mülli.append(j)
        if backbone.out_of_screen(player.bullets[j].x,player.bullets[j].y,screen_width,screen_height):
            mülli.append(j)

    player.out(screen_width,screen_height)

    for m in range (len(mülli)):
        player.bullets.pop(mülli[m]-m)

    mülli.clear()

    for i in range (len(target.bullets)):
        target.bullets[i].move()
        if backbone.collision(player.x,target.bullets[i].x,player.y,target.bullets[i].y,player.width,player.height,target.bullets[i].width,target.bullets[i].height):
            player.get_hit(target.bullets[i].schaden)
            target.score+=100
            mülli.append(i)
        if backbone.out_of_screen(target.bullets[i].x,target.bullets[i].y,screen_width,screen_height):
            mülli.append(i)
    for n in range (len (mülli)):
        target.bullets.pop(mülli[n]-n)
    mülli.clear
    target.out(screen_width,screen_height)
    #/collisonen 
    #zeichnen
    screen.fill(color.weiss)
    for k in range (len(player.bullets)):
        player.bullets[k].draw(screen)
    player.draw(screen)
    for l in range (len(target.bullets)):
        target.bullets[l].draw(screen)
    target.draw(screen)
    #/zeichnen
    #check ob tot und heilen
    player.heal()
    target.heal()
    if player.leben <=0 or target.leben <=0:
        print(player.score,target.score)
        running=False
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
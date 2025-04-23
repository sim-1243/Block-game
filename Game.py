import pygame
import color
import backbone
import bullet
import booster
import random

# Initialisierung von Pygame
pygame.init()
pygame.font.init()

# Spielfenster einrichten
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
# Spieltitel und Icons festlegen
pygame.display.set_caption("2D Game")
boost=[]
mülli=[]
debug=False
player=backbone.Player(50,50,color.red)
target=backbone.Player(1000,50,color.rosa)
tastatur=False
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

    #inputs vorbereiten
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False
    
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joystick=pygame.joystick.Joystick(0)
    #/inputs vorberiten
    #print(pygame.joystick.Joystick(1).get_name())
    #print(joystick.get_name())
    #pygame.joystick.Joystick(1).rumble(0.3,0.6,200)
    #text_surf=my_font.render(str(),False,(0,0,0))

    #Debug optionen
    if joystick.get_button(1) and joystick.get_button(0):
        debug=True
        tastatur=False
    #/Debug optionen 
    #movementset
    if tastatur:
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
        #players fire
        if keys[pygame.K_e] and len(player.bullets) <=50 and player.cooldown():
            player.shoot(backbone.richtung(player.x,target.x))
        if keys[pygame.K_MINUS] and len(target.bullets) <=50 and target.cooldown():
            target.shoot(backbone.richtung(target.x,player.x))
        #/players fire
    else:
        try:
            #Controller Debug
            if  debug and joystick.get_button(9):
                player_1=True
                player_2=False
            elif  debug and joystick.get_button(10):
                player_1=False
                player_2=True
            #/Controller Debug
            #Player move
            if debug and player_1:
                running=player.joy_move(0,target)
            elif debug:
                p=1
            else:
                running=player.joy_move(0,target)
            #/player move
            #target move
            if debug and player_2:
                running=target.joy_move(0,player)
            elif debug:
                p=0
            else :
                running=target.joy_move(1,player)
            #/target move
        except pygame.error:
            tastatur=True
    #/movementset
    #collisionen
    for j in range (len(player.bullets)):
        player.bullets[j].move()
        if backbone.collision(target.x,player.bullets[j].x, target.y, player.bullets[j].y,target.width,target.height,player.bullets[j].width,player.bullets[j].height):
            target.get_hit(player.bullets[j].schaden)
            player.score+=100
            target.controll.rumble(0.3,0.6,100)
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
            player.controll.rumble(0.3,0.6,100)
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
    #screen.blit(text_surf, (screen_width//4,10))
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
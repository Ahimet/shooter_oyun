from pygame import *
from random import randint
from time import time as timer
#arka plan pop müzik
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound=mixer.Sound("fire.ogg")

#Yazılar
font.init()
font2=font.Font(None, 36)




 #görselleri ekliyoruz 
 img_back="galaxy.png"#arkaplan resmi
 img_hero="rocket.png"#oyuncu
 img_bullet="bullet.png"#mermi
 img_enemy="ufo.png"#ufo
 img_ast="asteroid.png"
 life=5 #can sayısı


 score=0#vurduğumuz düşmanlar
 lost=0#kaçırdığımız düşmanlar
 goal=10
 max_lost=3
    

 class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x,size_y, player_speed):
        sprite.Sprite.__init__(self)

    self.image=transform.scale(image.load(player_image),(size_x,size_y))
    self.speed=player_speed

    self.rect=self.image.get_rect()
    self.rect.x=player_x
    self.rect.y=player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key[K_RİGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed

    def fire (self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > win_height:
            self.rect.x = randint (80, win_height-80)
            self.rect.y=0
            lost=lost +1

class Bullet(GameSprite):
    def update(self):
        self.rect.y +=self.speed
        if self.rect.y < 0:
            self.kill()

win_width=700
win-height=500


display.set_caption("shooter-ahmet")
window=display.set_mode(win_width,win_height)
background=transform.scale(image.load(img_back),(win_width, win_height))

ship=Player(img_hero,5,win_height - 100, 80, 100, 10)

monsters=sprite.Group()
for i in range(1, 6):
    monster=Enemy(img_enemy, randint(80, win_width - 80),-40, 80, 50, randint(1,5))
    monsters.add(monster)
astreoids=sprite.Group()
    for i in range(1,3):
        astreoid=Enemy(img_ast, randint(30, win_width - 30), -40, 80, 50, randint(1,7))
        astreoids,add(astreoid)

bullets=sprite.Group()



finish=False
run=True
rel_time=False
num_fire=0
while run:
    for e in event.get():
        if e.type==QUİT:
            run=False

        elif e.type ==KEYDOWN
            if e.key ==K_SPACE
                if num_fire < 5 and rel_time == False
        fire_soun.play()
        ship.fire()

            if num _fire >= 5 and rel_time == False
            last_time = timer()
            rel_time = True
            
        if not finish:
            window.blit(backgrond,(0,0))
            text=font2.render("Sayı: "+ str(score), 1, (255,255,255))
            window.blit(text, (10,20))

            


            ship.update()
            monsters.update()
            bullets.update()

            ship.reset()
            monsters.draw(window)
            astreoids.draw(window)
            bullets.draw(window)

            if rel_time == True:
                now_time=timer()

            if now_time - last_time < 3:
                    reload=font2.render("wait, reload.....",1,(150,0,0))
                    window.blit(reload, (260,460))
             else:
                    num_fire=0
                    rel_time=False                        

                collides=sprite.groupcollider(monster,bullets,True,True)
            for c in collides:
                score=score+1:
                monster=Enemy(img_enemy, randint(80,win_width-80),-40,80,50,randint(1,5))
                monster.add(monster)

            if sprite.spritecollide(ship,monster,False) or sprite.spritecollide(ship, astreoids, False):
                sprite.spritecollide(ship,monster,True)
                sprite.spritecollide(ship,asteroid,True)
                life=life+1

                if life == 0 or lost >= max_lost::
                    finish=True
                    window.blit(lose, (200,200))

                if score >= goal:
                    finish=True
                    window.blit(win,(200,200))

               


                finish=True
                window.blit(lose,(200,200))
                text_lose=font2.render("Kaçırılan" + str(score), 1, (255,255,255)) 
                window.blit(text, (10, 20))
                window.blit(lose,(200,200))
                text_lose=font2.render("Sayı:" + str(lost), 1, (255,255,255)) 
                window.blit(text, (10, 50))

                if life ==3:
                    life_color=(0,150,0)
                if life ==2:
                    life_color=(150,150,0)
                if life ==1:
                    life_color=(150,0,0)




                text_life=font1.render(str(life),1,life_color)
                window.blit(text_life, (650,10))
            
            display.update()

else:
    finish=False
    score=0
    lost=0
    for b in bullets:
        b.kill()
    for m in monsters:
        m.kill()


    time.delay(3000)
    for i in range(1,6):
        monster=Enemy(img_enemy,randint(80,win_width - 80)-40,80,50, randint(1,5))
        monsters.add(monster)
    for i in range(1,3):
        astreoid=Enemy(img_ast, randint(30, win_width - 80), -40 , 80, 50, randint(1,7))
        astreoids.add(astreoid)


time.delay(50)
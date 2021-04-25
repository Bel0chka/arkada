from pygame import *
#основные переменные
game=True
music=100
volume=100
width=1000
height=600
hearts=3
score=0
#картинки
img_hero_up="hero_up.png"
img_hero_right="hero_right.png"
img_hero_left="hero_left.png"
img_hero_down="hero_down.png"
img_enemy_up="enemy_up.png"
img_enemy_right="enemy_right.png"
img_enemy_left="enemy_left.png"
img_enemy_down="enemy_down.png"
img_bg="background.png"
class GameSprite(sprite.Sprite):
    def __init__(self, imge, player_x, player_y, size_x, size_y, speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(imge),(size_x,size_y))

        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.angle=1
        self.sizex=size_x
        self.sizey=size_y

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def animate(self,sizex,sizey):
        if self.angle == 1:
            self.image = transform.scale(image.load(img_hero_up),(self.sizex,self.sizey))
        elif self.angle == 2:
            self.image = transform.scale(image.load(img_hero_right),(self.sizex,self.sizey))
        elif self.angle == 3:
            self.image = transform.scale(image.load(img_hero_down),(self.sizex,self.sizey))
        elif self.angle == 4:
            self.image = transform.scale(image.load(img_hero_left),(self.sizex,self.sizey))
    def update(self):
        global keys
        keys = key.get_pressed()
        if keys[K_w]:
            self.angle=1
            self.rect.y -= self.speed
        if keys[K_d]:
            self.angle=2
            self.rect.x += self.speed
        if keys[K_s]:
            self.angle=3
            self.rect.y += self.speed
        if keys[K_a]:
            self.angle=4
            self.rect.x -= self.speed
        self.animate(self.sizex,self.sizey)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global score
        if self.rect.bottom >= width:
            self.rect.y = 0
            self.rect.x = 0
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
display.set_caption("ABOBA")
window = display.set_mode((width,height))
fpsClock=time.Clock()
hero=Player(img_hero_up, 300, 300, 80, 80, 3)
back = transform.scale(image.load(img_bg),(width,height))




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    fpsClock.tick(60)
    window.blit(back,(0,0))

    hero.update()
    hero.reset()
    display.update()

from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('Змейка')
fon = transform.scale(image.load("fon.png"),(700,500))

score =1
clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_height,player_speed):
        super().__init__()
        self.image =transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def colliderect(self,sprite):
        return self.rect.colliderect(sprite.rect)













class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__(player_image,player_x,player_y,size_x,size_y,player_speed)
        self.speed_x = player_speed
        self.speed_y = 0 
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

class Tail(GameSprite):
    def __init__(self,player_image, player_x, player_y,size_x,size_y,player_speed, timer):
        super().__init__(player_image, player_x, player_y,size_x,size_y,player_speed)
        self.timer = timer
    def update(self):
        print(self.timer)
        self.timer -= 1
        if self.timer <= 0:
            print()
            self.image = transform.scale(image.load("fon.png"),(50,50))

            self.kill()


zmeykaa = Player('snakehead.png',300,430,50,50,50)
food = GameSprite('Apple.png',250,250,50,50,0)

tails = sprite.Group()


window.blit(fon,(0,0))
wait = 0

finish = False
game = True
while game:
    keys = key.get_pressed()
    if keys[K_UP]:
        zmeykaa.speed_y = -zmeykaa.speed
        zmeykaa.speed_x = 0
    if keys[K_DOWN]:
        zmeykaa.speed_y = zmeykaa.speed
        zmeykaa.speed_x = 0
    if keys[K_LEFT]:
        zmeykaa.speed_x = -zmeykaa.speed
        zmeykaa.speed_y = 0
    if keys[K_RIGHT]:
        zmeykaa.speed_x = zmeykaa.speed
        zmeykaa.speed_y = 0


        
    if wait == 0:
        wait = 30

        window.blit(fon,(0,0))
    
        zmeykaa.reset()
        zmeykaa.update()

        food.reset()
        if zmeykaa.colliderect(food):
            score +=1
            food.rect.x = randint(0,23) * 30
            food.rect.y = randint(0,16) * 30
        t = Tail('snake.png',zmeykaa.rect.x - zmeykaa.speed_x, zmeykaa.rect.y - zmeykaa.speed_y,50,50,2,score)
        tails.add(t)

        tails.update()
        tails.draw(fon)

    wait -= 1


    for e in event.get():
        if e.type == QUIT:
             game =  False


    clock.tick(FPS)
    display.update()
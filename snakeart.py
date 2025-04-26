from pygame import *
window = display.set_mode((700,500))
display.set_caption('Змейка')
fon = transform.scale(image.load("fon.png"),(700,500))


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













class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__(player_image,player_x,player_y,size_x,size_y,player_speed)
        self.speed_x = player_speed
        self.speed_y = 0 
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
       


zmeykaa = Player('snakehead.png',300,430,50,50,1)




window.blit(fon,(0,0))


finish = False
game = True
while game:
    if finish != True:
        
        window.blit(fon,(0,0))
    
        zmeykaa.reset()
        zmeykaa.update()
        
        keys = key.get_pressed()
        if keys[K_UP]:
            player.speed_y = -player_speed
            player.speed_x = 0
        if keys[K_DOWN]:
            player.speed_y = player_speed
            player.speed_x = 0
        if keys[K_LEFT]:
            player.speed_x = -player_speed
            player.speed_y = 0
        if keys[K_RIGHT]:
            player.speed_x = player_speed
            player.speed_y = 0








    






    for e in event.get():
        if e.type == QUIT:
             game =  False


    clock.tick(FPS)
    display.update()
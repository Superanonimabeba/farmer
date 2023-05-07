from pygame import *
import sys
from random import randint

init()

font.init()

text1 = font.SysFont ("Arial",40)

text2 = font.SysFont ("Timesnewroman",90)

text3 = font.SysFont ("Timesnewroman",90)

text4 = font.SysFont ("Timesnewroman",30)

text5 = font.SysFont("Arial",60)

invertar = image.load("inventar.png")

play_img = image.load("play.png")

plant_img = image.load("plant.png")

pick_img = image.load("pick.png")

settings_img = image.load("settings.png")

exit_img = image.load("exit.png")

ogorod_image = image.load("ogorod.png")

volume1_image = image.load("VOL_1.png")

volume2_image = image.load("VOL_2.png")

volume3_image = image.load("VOL_3.png")

volume4_image = image.load("VOL_4.png")

back_img = image.load("back.png")

tomato_img = image.load("tomato.png")

carrot_img = image.load("carrot.png")

potato_button_png = image.load("potato_png.png")

tomato_button_png = image.load("tomato_png.png")

carrot_seed_img = image.load("carrot_seed_img.png")

potato_seed_img = image.load("potato_seed_img.png")

tomato_seed_img = image.load("tomato_seed_img.png")

shop_menu_img = image.load("shop_menu_img.png")

carrot_button_png = image.load("carrot_png.png")

potato_img = image.load("potato.png")

money_img = image.load("money.png")

clock= time.Clock()

font = font.SysFont(None, 20)

mixer.init()

press = mixer.Sound("music/press.ogg")

mixer.music.load("music/fon_music.ogg")

mixer.music.play()

class GameSprite(sprite.Sprite):
    
    def __init__(self, s_image, player_x, player_y,size_x,size_y ,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(s_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update(self):
        keys = key.get_pressed()

        if (keys[K_a] ^ keys[K_LEFT]) and self.rect.x > 0:
            self.rect.x -= self.speed

        if (keys[K_d] ^ keys[K_RIGHT]) and self.rect.x < 1180:
            self.rect.x += self.speed

        if (keys[K_w] ^ keys[K_UP]) and self.rect.y > 0:
            self.rect.y -= self.speed

        if (keys[K_s] ^ keys[K_DOWN]) and self.rect.y < 620:
            self.rect.y += self.speed

        if (keys[K_LEFT] ^ keys[K_a]) and self.rect.x > 0:
            self.rect.x -= self.speed

        if (keys[K_RIGHT] ^ keys[K_d]) and self.rect.x < 1180:
            self.rect.x += self.speed

        if (keys[K_UP] ^ keys[K_w]) and self.rect.y > 0:
            self.rect.y -= self.speed

        if (keys[K_DOWN] ^ keys[K_s]) and self.rect.y < 620:
            self.rect.y += self.speed

class Button():
    
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
        self.clicked = False

    def draw(self,mw):
        action = False
        pos = mouse.get_pos()

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                mixer.Sound.play(press)
                self.clicked = True
                action = True

        if mouse.get_pressed()[0] == 0:
            self.clicked = False
        mw.blit(self.image, (self.rect.x,self.rect.y))
        return action

class Ogorod(sprite.Sprite):
    
    def __init__(self, plant_image, plant_x, plant_y,size_x,size_y):
        self.image = transform.scale(image.load("ogorod.png"), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = plant_x
        self.rect.y = plant_y
        self.planted = False

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
        
class Products(GameSprite):
    
    def draw_prod(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Coin(GameSprite):
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
        
play_button = Button(450,300,play_img,1)

settings_button = Button(550,300,settings_img,1)

exit_button = Button(650,300,exit_img,1)

plant_tomato = Button(450,300,tomato_button_png,1)

plant_carrot = Button(700,300,carrot_button_png,1)

plant_potato = Button(575,300,potato_button_png,1)

back_button = Button(725,300,back_img,1)

back_button_plant = Button(575,400,back_img,1)

volume_button = Button(425,300,volume3_image,1)

volume1_button = Button(575,175,volume1_image,1)

volume2_button = Button(575,275,volume2_image,1)

volume3_button = Button(575,375,volume3_image,1)

volume4_button = Button(575,475,volume4_image,1)

text_col = (255,255,255)

menu_state = "main"

money = 0

now_time = 10

game_paused = True

dis_x = 1280

dis_y = 720

FPS = 100

speed = 1

finish = False

manual = True

game = True

plant_seed = False

map = transform.scale(image.load("map.png"),(1280,720))

mw = display.set_mode((dis_x,dis_y))

shop = GameSprite("shop.png",50,150,307,293,0)

player = Player("player.png",300,500,100,100,5)

ogorod = Ogorod('ogorod.png', 1000, 450, 100, 100) 

coin = Coin('coin.png', 200, 200, 100, 100, 1)

coins = sprite.Group()

x = ogorod.rect.x

y = ogorod.rect.y

plants = sprite.Group()

state_coin = 0

tomato_seed = 5

carrot_seed = 0

potato_seed = 0

game = True

state_plant = 0

shop_menu_state = True

plant_menu_state = True

state_menu = True

tomato = Products("plant_seed.png", x + 10 , y, 70, 100 , 0) 

carrot = Products("plant_seed.png", x + 10 , y, 70, 100, 0) 

potato = Products("plant_seed.png", x + 10, y, 70 , 100, 0) 

def draw_text (text, font, text_col, x, y,):
    img = font.render(text,True,text_col)
    mw.blit(img,(x,y))

def shop_menu():
    global shop_menu_state, shop_menu_img, player
    
    while shop_menu_state:
        mw.blit(shop_menu_img,(0,0))
        for e in event.get():   
            if e.type == QUIT:
                shop_menu_state = False   
                player = Player("player.png",300,500,100,100,5)
        
        display.update()
        clock.tick(FPS)
    shop_menu_state = True
    
def plant_menu():
    global state_plant, plant_menu_state, carrot_seed, tomato_seed, potato_seed
    
    while plant_menu_state:
        for e in event.get():
                
            if e.type == QUIT:
                plant_menu_state = False
                
                    
        if plant_tomato.draw(mw):
            if tomato_seed >= 1:
                ogorod.planted = True
                plants.add(tomato)
                state_plant = 1
                plant_menu_state = False
                tomato_seed -= 1
                
            else:
                draw_text("У вас закінчилося насіння купіть у магазині", text5, (200,0,0), 50, 200)
                
        if plant_carrot.draw(mw):
            if carrot_seed >= 1:
                ogorod.planted = True
                plants.add(carrot)
                state_plant = 2
                plant_menu_state = False
                carrot_seed -= 1
            else:
                draw_text("У вас закінчилося насіння купіть у магазині", text5, (200,0,0), 50, 200)
        
        if plant_potato.draw(mw):
            if potato_seed >= 1:
                ogorod.planted = True
                plants.add(potato)
                state_plant = 3  
                plant_menu_state = False   
                potato_seed -= 1
                
            else:
                draw_text("У вас закінчилося насіння купіть у магазині", text5, (200,0,0), 50, 200)
        if back_button_plant.draw(mw):
            plant_menu_state = False
                     
        display.update()
        clock.tick(FPS)
        
def menu():
    global game_paused, menu_state, state_menu
    while state_menu:
        
        mw.blit(map,(0,0))
        if game_paused:
            
            if menu_state == "main":
            
                draw_text("TRY YOURSELF AS FARMER!",text2,text_col,50,152)
                draw_text("TRY YOURSELF AS FARMER!",text2,(200, 0, 0),52,150)
                if play_button.draw(mw):
                    start_the_game()

                if settings_button.draw(mw):
                    menu_state = "options"

                if exit_button.draw(mw):
                    sys.exit()

            if menu_state == "options":
                if volume_button.draw(mw):
                    menu_state = "volume"

                if back_button.draw(mw):
                    menu_state = "main"

            if menu_state == "volume":
                if volume1_button.draw(mw):
                    mixer.music.set_volume(0)

                if volume2_button.draw(mw):
                    mixer.music.set_volume(0.25)

                if volume3_button.draw(mw):
                    mixer.music.set_volume(0.5)

                if volume4_button.draw(mw):
                    mixer.music.set_volume(1)

                if back_button.draw(mw):
                    menu_state = "options"
                
        else:
            draw_text("Press spase to go the menu",text1,text_col,160,250)
            keys = key.get_pressed()
            if keys[K_SPACE]:
                game_paused = True
        
        for e in event.get():
            if e.type == QUIT:
                sys.exit()

        display.update()
        clock.tick(FPS)

def start_the_game():
    global tomato, now_time, money, state_menu, invertar, plant_seed, state_coin, coin, state_plant, game, plant_menu_state, potato, carrot

    while game:
        
        for e in event.get(): 
            if e.type == QUIT:
                game = False

        if not finish:
            mw.blit(map,(0,0)) 
            ogorod.update()
            ogorod.reset()
            plants.draw(mw)
            plants.update()
            coins.draw(mw)
            coins.update()
            player.update()
            shop.update()
            shop.reset()
            player.reset()
            mw.blit(money_img, (376, 15))
            mw.blit(invertar,(22,16))
            mw.blit(invertar,(144,16))
            mw.blit(invertar,(266,16))
            mw.blit(tomato_seed_img,(22,16))
            mw.blit(potato_seed_img,(144,16))
            mw.blit(carrot_seed_img,(266,16))
            draw_text(str(tomato_seed),text4,(39, 15, 144), 30, 112)
            draw_text(str(potato_seed),text4,(39, 15, 144), 152, 112)
            draw_text(str(carrot_seed),text4,(39, 15, 144), 274, 112)
            draw_text(str(money),text4,(30, 235, 0), 436, 36)
            
            if ogorod.rect.centerx - player.rect.centerx <= 100 and ogorod.rect.centery - player.rect.centery <= 100 and ogorod.rect.centerx - player.rect.centerx >= -100 and ogorod.rect.centery - player.rect.centery >= -100:
                plant_button = Button(player.rect.x - 100,player.rect.y - 100,plant_img,1)
                
                if plant_button.draw(mw):
                    if state_coin == 0:
                        plant_menu()
                        plant_menu_state = True
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                        
                if ogorod.rect.centerx - player.rect.centerx <= 100 and ogorod.rect.centery - player.rect.centery <= 100 and ogorod.rect.centerx - player.rect.centerx >= -100 and ogorod.rect.centery - player.rect.centery >= -100:
                    pick_button = Button(player.rect.x,player.rect.y - 150,pick_img,1)
                        
                if plant_seed:   
                    if pick_button.draw(mw):
                        if state_plant == 1:
                            tomato.kill()
                            tomato = Products("plant_seed.png", x + 10 , y, 70, 100 , 0) 
                    
                        if state_plant == 2:
                            carrot.kill()   
                            carrot = Products("plant_seed.png", x + 10 , y, 70, 100 , 0)                  
                    
                        if state_plant == 3:
                            potato.kill()
                            potato = Products("plant_seed.png", x + 10 , y, 70, 100 , 0) 

                        x_c = randint(200,900)
                        y_c = randint(200,650)                        
                        coin = Coin('coin.png', x_c, y_c, 100, 100, 1)
                        coins.add(coin)
                        state_coin = 1
                        plant_seed = False
                        
            if shop.rect.x - player.rect.x <= 307 and shop.rect.y - player.rect.y <= 293 and shop.rect.x - player.rect.x >= -307 and shop.rect.y - player.rect.centery >= -293:
                shop_menu()
                
            if ogorod.planted:
                now_time = now_time - 1
                    
                if  now_time <= 0:
                    if state_plant == 1:
                        tomato.kill()
                        tomato = Products("tomato.png", x - 35, y, 100, 100, 0)
                        plants.add(tomato)
                    
                    if state_plant == 2:
                        carrot.kill()
                        carrot = Products("carrot.png", x, y, 100, 100, 0)
                        plants.add(carrot)                    
                    
                    if state_plant == 3:
                        potato.kill()
                        potato = Products("potato.png", x, y, 100, 100, 0)
                        plants.add(potato)                    
                    
                    now_time = 300
                    plant_seed = True
                    ogorod.planted = False
                    
            if coins.has(coin):
                if coin.rect.centerx - player.rect.centerx <= 100 and coin.rect.centery - player.rect.centery <= 100 and coin.rect.centerx - player.rect.centerx >= -100 and coin.rect.centery - player.rect.centery >= -100:
                    if state_plant == 1:
                        money += 1
                    
                    if state_plant == 2:
                        money += 3
                    
                    if state_plant == 3:
                        money += 7
                        
                    coin.kill()
                    state_coin = 0
                    state_plant = 0

        display.update()
        clock.tick(FPS)
menu()
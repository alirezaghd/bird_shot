import pygame,sys
import random
import time
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Optional
surface: Optional['pygame.Surface'] = None

pygame.init()

class Bird():
    def __init__(self):
        self.direction = random.choice(['ltr' , 'rtl']) 
        self.speed = 10

        if self.direction == 'ltr':
            self.x = - 50 
        else:
            self.x = game.width + 50
        self.y = random.randint(0,game.height / 2)
        self.blood = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/blood.png')
        self.die = False

    def show(self):
        if self.direction == 'ltr':
           self.area = game.display.blit(self.image,[self.x,self.y])
           

        
        if self.direction == 'rtl':
           self.area = game.display.blit(pygame.transform.flip(self.image,True,False),[self.x,self.y])

        
    
    def fly(self):

        if self.direction == 'ltr':
            self.x += self.speed
        
        if self.direction == 'rtl':
             self.x -= self.speed

    
class Duck(Bird):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/duck.png')
        self.area = game.display.blit(self.image,[self.x,self.y])

    
class Stork(Bird):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/stork.png')
        self.speed = 8
        self.area = game.display.blit(self.image,[self.x,self.y])

    
class Donkey(Bird):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/donkey.png')
        self.area = game.display.blit(self.image,[self.x,self.y])

class Cloud(Bird):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/cloud1.png')
        self.area = game.display.blit(self.image,[self.x,self.y])




class Gun:
    def __init__(self):
        self.x =  game.width / 2
        self.y = game.height / 2
        self.image = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/shooter.png')
        self.score = 0
        self.sound = pygame.mixer.Sound('E:/Python Online/Jalase 12/bird_shot/sounds/shotgun.wav')
        self.b_image = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/bullet.png')
        self.bullet = 10

    def show(self):
        game.display.blit(self.image,[self.x,self.y])

    def fire(self):
        self.sound.play()
        self.bullet -= 1


class Game:
    def __init__(self):
        self.width = 852
        self.height = 480
        self.display = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/background.jpg')
        #self.background = pygame.image.load('bird_shot/image/background.jpg')
        self.fps = 30
        self.font = pygame.font.SysFont(None,40)

    def menu(self):
        #bg_menu = pygame.image.load('E:/Python Online/Jalase 12/bird_shot/image/duck-hunt-header.png')
        menu = pygame_menu.Menu(480, 852, 'Welcome To Duck Shot',theme=pygame_menu.themes.THEME_GREEN)
        duck_image = pygame_menu.BaseImage('E:/Python Online/Jalase 12/bird_shot/image/duck.png')
        duck_donkey = pygame_menu.BaseImage('E:/Python Online/Jalase 12/bird_shot/image/donkey.png')
        duck_st = pygame_menu.BaseImage('E:/Python Online/Jalase 12/bird_shot/image/stork.png')

        #background_image.draw(self.display)
        menu.add.image(duck_image, angle=20, scale=(1, 1))
        menu.add.image(duck_donkey, angle=20, scale=(1, 1))
        menu.add.image(duck_st, angle=20, scale=(1, 1))

        #mage_path, angle=0, image_id='', onselect=None, scale=(1, 1), scale_smooth=True, selectable=False,
        menu.add.text_input('Name :', default='Insert Name')
        #menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=play)
        menu.add.button('Play', game.play)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.display)
    
    def play(self):

        pygame.mouse.set_visible(False)
        my_gun = Gun()
        bird = Bird()
        duck = Duck()
        stork = Stork()
        donkey = Donkey()
        cloud = Cloud()
        ducks = []
        storks = []
        donkeys = []
        clouds = []

        pos = [my_gun.x , my_gun.y]
        self.font.render('Score : '+str(my_gun.score),True,(255,255,255))
        
        while  True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION :
                   my_gun.x = pygame.mouse.get_pos()[0]
                   my_gun.y = pygame.mouse.get_pos()[1]

                   
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :
                        my_gun.fire()

                        for duck in ducks :
                            if duck.area.collidepoint(event.pos):
                                ducks.remove(duck)
                                my_gun.score += 1
                                my_gun.bullet += 2

                                bird.die = True
                                if bird.die == True:
                                    pos_b = duck.area
                                    game.display.blit(bird.blood,event.pos)



                        for stork in storks :
                            if stork.area.collidepoint(event.pos):
                                storks.remove(stork)
                                my_gun.score += 1

                        for donkey in donkeys :
                            if donkey.area.collidepoint(event.pos):
                                donkeys.remove(donkey)
                                my_gun.score += 5
                        

            if random.random() < 0.03 :
                ducks.append(Duck())

            if random.random() < 0.02 :
                storks.append(Stork())

            if random.random() < 0.005 :
                donkeys.append(Donkey())

            if random.random() < 0.01 :
                clouds.append(Cloud())
            
      

            for duck in ducks :
                duck.fly()
            
            for stork in storks :
                stork.fly()

            for donkey in donkeys :
                donkey.fly()
            
            for cloud in clouds :
                cloud.fly()
            
            

            self.display.blit(self.background,(0,0))
            self.display.blit(self.font.render('Score : '+str(my_gun.score),True,(0,0,0)),[50,430])
            self.display.blit(my_gun.b_image,(700,427))
            self.display.blit(self.font.render('x'+str(my_gun.bullet),True,(0,0,0)),[735,430])

            my_gun.show()

            for duck in ducks:
                duck.show()
            
            for stork in storks :
                stork.show()

            for donkey in donkeys :
                donkey.show()

            for cloud in clouds:
                cloud.show()
            
            


            pygame.display.update()
            self.clock.tick(self.fps)



if __name__ == "__main__":

    game = Game()
    game.menu()
    game.play()
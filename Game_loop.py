import pygame
import time
import random

pygame.init()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


display_width = 300
display_height = 640

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

positionX = [0, 50, 85, 120, 155, 50, 85, 120, 155, 50, 85, 120, 155, 50, 85, 120, 155, 50, 85, 120, 155, 50, 85, 120, 155]
positionY = [0, 465, 465, 465, 465, 389, 389, 389, 389, 311, 311, 311, 311, 234, 234, 234, 234, 157, 157, 157, 157, 80, 80, 80, 80]

tloGra = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/tlo1.jpg')
tloMenu = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/MENU.png')
nieb = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/niebieska.png') #1
ziel = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/zielona.png') #2
pom = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/pomaranczowa.png') #3
czerw = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/czerwona.png') #4
zolt = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/zolta.png') #5
fiol = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/fioletowa.png') #6
czar = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/czarna.png') #7
bial = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/biala.png') #8

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mastermind')
clock = pygame.time.Clock()
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


all_sprites = pygame.sprite.AbstractGroup()


class Pin(pygame.sprite.Sprite):

    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((26, 26))
        #self.image.fill(white)
        #self.image.set_colorkey(white)
        self.image = color
        self.rect = self.image.get_rect()
        self.rect.center = (x+13,y+13)


#all_sprites_list = pygame.sprite.Group()
#pin = Pin
#all_sprites_list.add(Pin)

def pinColor(x,y):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 10 < mouse[0] < 35 and 535 < mouse[1] < 560 and click[0]==1:
        if click[0]==1:
            clicked = 1
            time.sleep(1)
            if clicked == 1:
                color=nieb
                pin = Pin(color, positionX[x], positionY[y])
                all_sprites.add(pin)
                all_sprites.update()
                clicked = 0

    if 50 < mouse[0] < 75 and 535 < mouse[1] < 560 and click[0]==1:
        if click[0]==1:
            clicked = 1
            time.sleep(1)
            if clicked == 1:
                color=ziel
                pin = Pin(color, positionX[x], positionY[y])
                all_sprites.add(pin)
                all_sprites.update()
                clicked = 0

    elif 90 < mouse[0] < 115 and 535 < mouse[1] < 560 and click[0]==1:
        if click[0]==1:
            clicked = 1
            time.sleep(1)
            if clicked == 1:
                color=pom
                pin = Pin(color, positionX[x], positionY[y])
                all_sprites.add(pin)
                all_sprites.update()
                clicked = 0

    elif 130 < mouse[0] < 155 and 535 < mouse[1] < 560 and click[0]==1:
        if click[0]==1:
            clicked = 1
            time.sleep(1)
            if clicked == 1:
                color=czerw
                pin = Pin(color, positionX[x], positionY[y])
                all_sprites.add(pin)
                all_sprites.update()
                clicked = 0

    elif 170 < mouse[0] < 195 and 535 < mouse[1] < 560 and click[0]==1:
        if click[0]==1:
            clicked = 1
            time.sleep(1)
            if clicked == 1:
                color=zolt
                pin = Pin(color, positionX[x], positionY[y])
                all_sprites.add(pin)
                all_sprites.update()
                clicked = 0


    elif 210 < mouse[0] < 235 and 535 < mouse[1] < 560 and click[0]==1:
        if click[0]==1:
            clicked = 1
            time.sleep(1)
            if clicked == 1:
                color=fiol
                pin = Pin(color, positionX[x], positionY[y])
                all_sprites.add(pin)
                all_sprites.update()
                clicked = 0
    all_sprites.draw(gameDisplay)





def button(x1,y1,x2,y2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "surrender":
                game_intro()
                pygame.display.update()
                clock.tick(15)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(tloMenu,(0,0))
        pygame.display.update()
        clock.tick(15)

        button(20, 150, 90, 190, "play")
        button(20, 200, 90, 240, "quit")



def game_loop():

    t = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if(click != (0,0,0)):
            print(mouse, click)
        gameDisplay.blit(tloGra,(0,0))
        button(235, 580, 585, 625, "quit")
        button(185, 5, 635, 35, "surrender")

        pinColor(1,1)
        pinColor(2,2)
        pinColor(3,3)
        pinColor(4,4)


        all_sprites.draw(gameDisplay)



        pygame.display.update()
        clock.tick(20)




game_loop()
pygame.quit()
quit()

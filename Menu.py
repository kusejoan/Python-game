import pygame
import time
import random

pygame.init()


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

tloGra = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/tlo1.jpg')
tloMenu = pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/MENU.png')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mastermind')
clock = pygame.time.Clock()

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

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(tloMenu,(0,0))
        #largeText = pygame.font.Font('freesansbold.ttf', 80)
        #TextSurf, TextRect = text_objects("MASTERMIND", largeText)
        #TextRect.center = ((display_width/2),(display_height/3))
       # gameDisplay.blit(TextSurf, TextRect)

       # pygame.draw.rect(gameDisplay, green, (100, 350, 100, 50))

        button(20, 150, 90, 190, "play")
        button(20, 200, 90, 240, "quit")


        pygame.display.update()
        clock.tick(15)


def game_loop():


    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()


        gameDisplay.blit(tloGra,(0,0))


        pygame.display.update()
        clock.tick(80)


game_intro()

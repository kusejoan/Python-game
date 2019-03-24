import pygame
import time
import random
from copy import deepcopy
#import tkinter
import easygui

random.seed()

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
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mastermind')
clock = pygame.time.Clock()

#def button(x1,y1,x2,y2,action=None):
#    mouse = pygame.mouse.get_pos()
#    click = pygame.mouse.get_pressed()
#    if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
#        if click[0] == 1 and action != None:
#            if action == "play":
#                game_loop()
#            elif action == "quit":
#                pygame.quit()
#                quit()


def button(x1,y1,x2,y2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "exit":
                pygame.quit()
                quit()
            elif action == "quit":
                game_intro()



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


class Pin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None
        self.visible = False

    def clicked(self):
        pressed = False
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < self.x+26 and self.y < mouse[1] < self.y+26:
                pressed = True
        return pressed


class Row:
    def __init__(self):
        self.pins = []
        self.marks = []


def initSprites():
    sprites = {
        "nieb" : pygame.image.load("/home/joasia/PycharmProjects/Mastermind1/niebieska.png"),
        "ziel" : pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/zielona.png'),
        "pom" : pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/pomaranczowa.png'),
        "czerw" : pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/czerwona.png'),
        "zolt" : pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/zolta.png'),
        "fiol" : pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/fioletowa.png'),
        "czar" : pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/czarna.png'),
        "bial" : pygame.image.load('/home/joasia/PycharmProjects/Mastermind1/biala.png')
    }

    return sprites

colors = ["nieb", "ziel", "pom", "czerw", "zolt", "fiol"]
checkPins = ["czar", "bial"]


def initPins():

    rows = []

    for i in range(0, 6):
        r = Row()
        rows.append(r)

        for j in range(0, 4):
            y = 465 - i*77
            x = 50 + j*35
            p = Pin(x, y)
            r.pins.append(p)

        for k in range(0,2):
            x = 210 + k*35
            y = 440 - i*77
            p = Pin(x,y)
            r.marks.append(p)

        for l in range(0,2):
            x = 210 + l*35
            y = 480 - i*77
            p = Pin(x,y)
            r.marks.append(p)

    resultRow = Row()
    for t in range(0, 4):
            y = 10
            x = 10 + t*35
            p = Pin(x, y)
            resultRow.pins.append(p)

    rows.append(resultRow)
    return rows

def draw(rows, sprites):
    for r in rows:
        for p in r.pins:
            if p.visible:
                gameDisplay.blit(sprites[p.color], (p.x, p.y))
        for p in r.marks:
            if p.visible:
                gameDisplay.blit(sprites[p.color], (p.x, p.y))

def code(resultRow):
    kod = []
    for i in range(0,4):
        los = random.randrange(6)
        kod.append(colors[los])
        resultRow.pins[i].color = colors[los]
    print(kod)
    return kod



def surrender(x1,y1,x2,y2, resultRow):
    mouse = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()
    if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
        if clic[0] == 1:
            for i in range (0,4):
                resultRow.pins[i].visible = True
            return True

def click(row):
    mouse = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()
    if press[0] == 0:
        return
    else:
        for p in row.pins:
            if p.clicked():
                clic = 1
                time.sleep(0.2)
                if clic == 1:
                    clic = 0
                    p.visible = True
                    if p.color == None:
                        p.color = colors[0]
                    else:
                        k = colors.index(p.color)
                        if k == 5:
                            p.color = colors[0]
                        else:
                            p.color = colors[k+1]

def submit(activeRow,row,kod):
    mouse = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()
    won = False
    if 15 < mouse[0] < 95 and 580 < mouse[1] < 625 and press[0] == 1:
        if activeRow < 6:
            clic = 1
            time.sleep(0.5)
            if clic == 1:
                complete, won = check(row,kod)
                if complete:
                    activeRow += 1
    else:
        activeRow = activeRow
    return activeRow, won


def check(row, kod):
    for z in range(0,4):
        print(row.pins[z])
        if row.pins[z].color == None:
            return False

    guess = [p.color for p in row.pins]
    pins = deepcopy(kod)
    black = 0
    white = 0

    for i in range(0, 4):
        if pins[i] == guess[i]:
            black += 1
            pins[i] = "nic1"
            guess[i] = "nic2"

    for p in pins:
        if p in guess:
            white += 1
            guess.remove(p)

    czarne = ["czar" for i in range(0, black)]
    biale = ["bial" for i in range(0, white)]
    result = czarne + biale
    random.shuffle(result)
    for j in range(0,len(result)):
        print(j, len(row.marks), len(result))
        row.marks[j].visible = True
        row.marks[j].color = result[j]
    won = (black == 4)
    return True, won

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
        button(20, 200, 90, 240, "exit")

def game_loop():

    gameExit = False
    activeRow = 0
    rows = initPins()
    sprites = initSprites()
    kod = code(rows[6])
    won = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

        gameDisplay.blit(tloGra,(0,0))
        a=surrender(185, 5, 635, 35, rows[6])
        button(235, 580, 285, 625, "quit")
        draw(rows, sprites)

        click(rows[activeRow])
        activeRow, won = submit(activeRow,rows[activeRow],kod)

        pygame.display.update()
        clock.tick(20)

        if a:
            easygui.msgbox("You lose", "End")
            # time.sleep(3.5)
            game_intro()

        if won:
            easygui.msgbox("You won!", "End")
            game_intro()

        if activeRow == 6:
            easygui.msgbox("You lose", "End")
            game_intro()


game_intro()
pygame.quit()
quit()




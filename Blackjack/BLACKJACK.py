import random
import time
import sys
import pygame
import math
pygame.init()
#hit between x:401 and 491 and 
#stand between 541 and 674
#double between 696 and 850 
#y between 360 and 407
pygame.display.set_caption("BLACKJACK")
icon = pygame.image.load('./imgs/poker-chip.png')
pygame.display.set_icon(icon)
background = pygame.image.load('./imgs/BlackjackBG.jpg')
nextround = pygame.image.load("./imgs/NEXTROUNF.png")
hit = pygame.image.load('./imgs/HIT.png')
stand = pygame.image.load('./imgs/STAND.png')
double = pygame.image.load('./imgs/DOUBLE.png')
split = pygame.image.load('./imgs/SPLIT.png')
bet = pygame.image.load('./imgs/BET.png')
deal = pygame.image.load('./imgs/DEAL.png')
back = pygame.image.load('./imgs/red_back.png')
DECK=[2,3,4,5,6,7,8,9,10,"ACE","JACK","QUEEN","KING",
2,3,4,5,6,7,8,9,10,"ACE","JACK","QUEEN","KING",
2,3,4,5,6,7,8,9,10,"ACE","JACK","QUEEN","KING",
2,3,4,5,6,7,8,9,10,"ACE","JACK","QUEEN","KING"]
DECK_imgs = [pygame.image.load("./imgs/2C.png"), pygame.image.load("./imgs/3C.png"), pygame.image.load("./imgs/4C.png"),pygame.image.load("./imgs/5C.png"),
pygame.image.load("./imgs/6C.png"), pygame.image.load("./imgs/7C.png"),pygame.image.load("./imgs/8C.png"),pygame.image.load("./imgs/9C.png"),pygame.image.load("./imgs/10C.png"),
pygame.image.load("./imgs/AC.png"),pygame.image.load("./imgs/JC.png"),pygame.image.load("./imgs/QC.png"),pygame.image.load("./imgs/KC.png"),
pygame.image.load("./imgs/2D.png"), pygame.image.load("./imgs/3D.png"), pygame.image.load("./imgs/4D.png"),pygame.image.load("./imgs/5D.png"),
pygame.image.load("./imgs/6D.png"), pygame.image.load("./imgs/7D.png"),pygame.image.load("./imgs/8D.png"),pygame.image.load("./imgs/9D.png"),pygame.image.load("./imgs/10D.png"),
pygame.image.load("./imgs/AD.png"),pygame.image.load("./imgs/JD.png"),pygame.image.load("./imgs/QD.png"),pygame.image.load("./imgs/KD.png"),
pygame.image.load("./imgs/2H.png"), pygame.image.load("./imgs/3H.png"), pygame.image.load("./imgs/4H.png"),pygame.image.load("./imgs/5H.png"),
pygame.image.load("./imgs/6H.png"), pygame.image.load("./imgs/7H.png"),pygame.image.load("./imgs/8H.png"),pygame.image.load("./imgs/9H.png"),pygame.image.load("./imgs/10H.png"),
pygame.image.load("./imgs/AH.png"),pygame.image.load("./imgs/JH.png"),pygame.image.load("./imgs/QH.png"),pygame.image.load("./imgs/KH.png"),
pygame.image.load("./imgs/2S.png"), pygame.image.load("./imgs/3S.png"), pygame.image.load("./imgs/4S.png"),pygame.image.load("./imgs/5S.png"),
pygame.image.load("./imgs/6S.png"), pygame.image.load("./imgs/7S.png"),pygame.image.load("./imgs/8S.png"),pygame.image.load("./imgs/9S.png"),pygame.image.load("./imgs/10S.png"),
pygame.image.load("./imgs/AS.png"),pygame.image.load("./imgs/JS.png"),pygame.image.load("./imgs/QS.png"),pygame.image.load("./imgs/KS.png")]
def isClicked(x1,x2, y1 = 360, y2 = 407):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= x1 and mouse[0] <= x2  and mouse[1] >= y1 and mouse[1] <=y2 :
        return True

def show_points():
    font = pygame.font.Font('freesansbold.ttf', 32)
    pts= font.render(str(User.points1), True, (255, 255, 255))
    screen.blit(pts, (500, 550)) 

def show_rounds(x):
    font = pygame.font.Font('freesansbold.ttf', 32)
    ptd= font.render("ROUND: " + str(x), True, (255, 255, 255))
    screen.blit(ptd, (60, 65)) 

def final(c):
    if c == 1:
        font = pygame.font.Font('freesansbold.ttf', 128)
        zz = font.render("You Won!!", True, (255, 255, 255))
        screen.blit(zz, (350, 325))
    elif c == 0:
        font = pygame.font.Font('freesansbold.ttf', 128)
        zz = font.render("You Lost!!", True, (255, 255, 255))
        screen.blit(zz, (350, 325))
    else:
        font = pygame.font.Font('freesansbold.ttf', 128)
        zz = font.render("DRAW!", True, (255, 255, 255))
        screen.blit(zz, (350, 325))
def next_round():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and isClicked(640,910,440,485):
            return True
def money():
    font = pygame.font.Font('freesansbold.ttf', 32)
    zz = font.render("wallet: " + str(User.wallet) + "$", True, (255, 255, 255))
    dd = font.render("Bet: " + str(User.bet) + "$", True, (255, 255, 255))
    screen.blit(zz, (20, 475))
    screen.blit(dd, (20,520))
    
def ShowUser(something,v):
    screen.blit(something, (550 + v,560))
def ShowDealer(something,v):
    screen.blit(something,  (550 - v,115))
def Shuffle(arr):
    for i in range(3):
        for j in range(len(arr)):
            r = random.randint(0,len(arr) - 1)
            while r == j:
                r = random.randint(0,len(arr) - 1)
            arr[j], arr[r] = arr[r], arr[j]
            DECK_imgs[j], DECK_imgs[r] = DECK_imgs[r], DECK_imgs[j]
#Checking if player points bigger than 21
def Check(player,deal):
    if player.points1 > 21:
        print(deal.cards)
        print("YOU LOST!!")
        return 2
    return 0
def enemy_points():
    font = pygame.font.Font('freesansbold.ttf', 32)
    ptz  = font.render(str(comp.points1), True, (255, 255, 255))
    screen.blit(ptz, (719, 140))
#creating a player object
class Player(object):
    def __init__(self):
        self.wallet = 5000
        self.bet = 0
        self.cards = []
        self.imgcards = []
        # we make two points attributres in case of spltting decision
        self.points1 = 0
        self.points2 = 0
    def Bet(self,x):
        if x <= self.wallet:
         self.bet += x
         self.wallet-=x
    def Getcard(self,arr,n = 2,split = False):
        if not split:
         if n == 2:
            a = arr[len(arr) - 1]
            b = arr[len(arr) - 2]
            c = DECK_imgs[len(DECK_imgs) - 1]
            d = DECK_imgs[len(DECK_imgs) - 2]
            self.cards.append(a)
            self.cards.append(b)
            self.imgcards.append(c)
            self.imgcards.append(d)
            arr.pop(len(arr) - 1)
            arr.pop(len(arr) - 1)
            DECK_imgs.pop(len(DECK_imgs) - 1)
            DECK_imgs.pop(len(DECK_imgs) - 1)
            if a == "JACK" or a == "QUEEN" or a == "KING":
                self.points1 +=10
            elif a == "ACE":
                if 11 + self.points1 <= 21:
                    self.points1+=11
                else:
                    self.points1 +=1

            else:
                self.points1+=a 
            if b == "JACK" or b == "QUEEN" or b == "KING":
                self.points1 +=10
            elif b == "ACE":
                if 11 + self.points1 <= 21:
                    self.points1+=11
                else:
                    self.points1+=1 
            else:
                self.points1+=b
              
         elif n == 1:
            a = arr[len(arr) - 1]
            d = DECK_imgs[len(DECK_imgs) - 1]
            self.cards.append(a)
            self.imgcards.append(d)
            arr.pop(len(arr) - 1)
            DECK_imgs.pop(len(DECK_imgs) - 1)
            if a == "JACK" or a == "QUEEN" or a == "KING":
                self.points1 +=10
            elif a == "ACE":
                if self.points1 + 11 <= 21:
                    self.points1+=11
                else:
                    self.points1+=1
            else:
                self.points1+=a
             
class Dealer(object):
    def __init__(self):
        self.cards = []
        self.points1 = 0
        self.imgcards = []
    def Getcard(self,arr,n = 2):
        if n == 2:
            a = arr[len(arr) - 1]
            b = arr[len(arr) - 2]
            c = DECK_imgs[len(DECK_imgs) - 1]
            d = DECK_imgs[len(DECK_imgs) - 2]
            self.cards.append(a)
            self.cards.append(b)
            self.imgcards.append(c)
            self.imgcards.append(d)
            arr.pop(len(arr) - 1)
            arr.pop(len(arr) - 1)
            DECK_imgs.pop(len(DECK_imgs) - 1)
            DECK_imgs.pop(len(DECK_imgs) - 1)
            z = random.randint(0,1)
            if a == "JACK" or a == "QUEEN" or a == "KING":
                self.points1 +=10
            elif a == "ACE":
                if self.points1 + 11 <= 21:
                    self.points1+=11
                else:
                    self.points1+=1
            else:
                self.points1+=a 
            if b == "JACK" or b == "QUEEN" or b == "KING":
                self.points1 +=10
            elif b == "ACE":
                if self.points1 + 11 <= 21:
                    self.points1+=11
                else:
                    self.points1+=1
            else:
                self.points1+=b 
        elif n == 1:
            a = arr[len(arr) - 1]
            d = DECK_imgs[len(DECK_imgs) - 1]
            self.imgcards.append(d)
            self.cards.append(a)
            arr.pop(len(arr) - 1)
            DECK_imgs.pop(len(DECK_imgs) - 1)
            if a == "JACK" or a == "QUEEN" or a == "KING":
                self.points1 +=10
            elif a == "ACE":
                if self.points1 + 11 <= 21:
                    self.points1+=11
                else:
                    self.points1+=1
            else:
                self.points1+=a    
Shuffle(DECK)
screen = pygame.display.set_mode((1280,1024))
firstTIME = True
cs = 1
pos = 60
running = True
Hits = []
Hitspos = []
First = True
dhit = 0
dchit = 0
cs = 0
cHits = []
cHitspos = [-120]
cFirst = True
isbet = 1
state = -1
round = 1
rem = 1
bb = 0
User = Player()
comp = Dealer()
dd = 1
while running:
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (10, 10))
    if round %10 == 0 and rem == 1:
        Shuffle(DECK)
        rem = 0
    show_rounds(round)
    money()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked(415,491) and isbet!=1 and state==-1 and not firstTIME:
            User.Getcard(DECK,1)
            dhit = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked(541,674) and isbet != 1 and state==-1 and not firstTIME:
            cs = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked(701,850) and isbet != 1 and state==-1 and not firstTIME:
            if User.wallet > User.bet:
              User.wallet-= User.bet
              User.bet+=User.bet
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked(255,330,616,664) and isbet == 1:
            User.Bet(500)
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked(246,355,467,511) and isbet == 1:
            if User.bet > 0:
             isbet = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked(640,910,440,485):
            bb = 1

    if firstTIME :
        comp.Getcard(DECK)
        User.Getcard(DECK)
    firstTIME = False
    if state == 0:
        dd = 1
        User.bet = 0
        screen.blit(nextround, (350, 200))
        show_points()
        enemy_points()
        ShowDealer(comp.imgcards[0],0)
        ShowDealer(comp.imgcards[1],-60)
        if len(comp.imgcards) > 2:
         for i in range(len(cHits)):
             ShowDealer(cHits[i],cHitspos[i])
        ShowUser(User.imgcards[0],0)
        ShowUser(User.imgcards[1],60)
        if len(Hits) >= 1:
         x = 20
         for i in range(len(Hits)):
           ShowUser(Hits[i],Hitspos[i]+x)
           x+=20
        final(0)
        if bb == 1:
            bb = 0
            round+=1
            rem = 1
            firstTIME = True
            cs = 1
            pos = 60
            running = True
            Hits = []
            Hitspos = []
            First = True
            dhit = 0
            dchit = 0
            cs = 0
            cHits = []
            cHitspos = [-120]
            cFirst = True
            isbet = 1
            state = -1
            for i in range(len(User.cards)):
              DECK.insert(i, User.cards[i])
              DECK_imgs.insert(i,User.imgcards[i])
            for i in range(len(comp.cards)):
              DECK.insert(i, comp.cards[i])
              DECK_imgs.insert(i,comp.imgcards[i])
            User.cards = []
            User.imgcards = []
            comp.cards = []
            comp.imgcards = []
            User.bet = 0 
            User.points1 = 0
            User.points2 = 0
            comp.points1 = 0
        pygame.display.update()
        continue
    elif state == 1:
        dd = 1
        User.bet = 0
        screen.blit(nextround, (350, 200))
        show_points()
        enemy_points()
        ShowDealer(comp.imgcards[0],0)
        ShowDealer(comp.imgcards[1],-60)
        if len(comp.imgcards) > 2:
         for i in range(len(cHits)):
             ShowDealer(cHits[i],cHitspos[i])
        ShowUser(User.imgcards[0],0)
        ShowUser(User.imgcards[1],60)
        if len(Hits) >= 1:
         x = 20
         for i in range(len(Hits)):
           ShowUser(Hits[i],Hitspos[i]+x)
           x+=20
        final(1)
        if bb == 1:
            round+=1
            rem = 1
            bb = 0
            firstTIME = True
            cs = 1
            pos = 60
            running = True
            Hits = []
            Hitspos = []
            First = True
            dhit = 0
            dchit = 0
            cs = 0
            cHits = []
            cHitspos = [-120]
            cFirst = True
            isbet = 1
            state = -1
            for i in range(len(User.cards)):
              DECK.insert(i, User.cards[i])
              DECK_imgs.insert(i,User.imgcards[i])
            for i in range(len(comp.cards)):
              DECK.insert(i, comp.cards[i])
              DECK_imgs.insert(i,comp.imgcards[i])
            User.cards = []
            User.imgcards = []
            comp.cards = []
            comp.imgcards = []
            User.bet = 0 
            User.points1 = 0
            User.points2 = 0
            comp.points1 = 0
        pygame.display.update()
        continue
    elif  state == 2:
        dd = 1
        User.bet = 0
        screen.blit(nextround, (350, 200))
        show_points()
        enemy_points()
        ShowDealer(comp.imgcards[0],0)
        ShowDealer(comp.imgcards[1],-60)
        if len(comp.imgcards) > 2:
         for i in range(len(cHits)):
             ShowDealer(cHits[i],cHitspos[i])
        ShowUser(User.imgcards[0],0)
        ShowUser(User.imgcards[1],60)
        if len(Hits) >= 1:
         x = 20
         for i in range(len(Hits)):
           ShowUser(Hits[i],Hitspos[i]+x)
           x+=20
        final(2)
        if bb == 1:
            round+=1
            rem = 1
            bb = 0
            firstTIME = True
            cs = 1
            pos = 60
            running = True
            Hits = []
            Hitspos = []
            First = True
            dhit = 0
            dchit = 0
            cs = 0
            cHits = []
            cHitspos = [-120]
            cFirst = True
            isbet = 1
            state = -1
            for i in range(len(User.cards)):
              DECK.insert(i, User.cards[i])
              DECK_imgs.insert(i,User.imgcards[i])
            for i in range(len(comp.cards)):
              DECK.insert(i, comp.cards[i])
              DECK_imgs.insert(i,comp.imgcards[i])
            User.cards = []
            User.imgcards = []
            comp.cards = []
            comp.imgcards = []
            User.bet = 0 
            User.points1 = 0
            User.points2 = 0
            comp.points1 = 0
        pygame.display.update()
        continue
    if isbet == 1:
        screen.blit(bet,(90,500)) #bet between x: 255 , 330 , y:616,664 
        screen.blit(deal,(110,350)) # deal between 246,355  , y: 467,511 
        money()
        pygame.display.update()
        continue         
    ShowUser(User.imgcards[0],0)
    ShowUser(User.imgcards[1],60)
    ShowDealer(comp.imgcards[0],0)
    ShowDealer(back,-60)
    screen.blit(hit,(250,250))
    screen.blit(stand,(400,250))
    screen.blit(double,(568,250))
    if cs == 1:
        ShowDealer(comp.imgcards[1],-60)
        while comp.points1 < User.points1 and comp.points1 <= 10:
            comp.Getcard(DECK,1)
            cHits.append(comp.imgcards[len(comp.imgcards) - 1])
            cHitspos.append(cHitspos[len(cHitspos) - 1] - 120)
            if comp.points1 > 21:
                User.wallet+=2*User.bet
                state = 1
                time.sleep(.7)
        if len(comp.imgcards) > 2:
         for i in range(len(cHits)):
             ShowDealer(cHits[i],cHitspos[i])
        if User.points1 > 21:
            state = 0
        elif User.points1 > comp.points1:
            User.wallet+= 2*User.bet
            state = 1
        elif User.points1 < comp.points1:
            state = 0
        else:
            User.wallet += User.bet
            state = 2
        
    if len(User.imgcards) > 2 and dhit == 1:
        Hits.append(User.imgcards[len(User.imgcards) - 1])
        if len(Hitspos) > 1:
            First = False
        if First:
            Hitspos.append(120)
        else:
            Hitspos.append(Hitspos[len(Hitspos) - 1] + 60)
        dhit = 0
    if len(Hits) >= 1:
     x = 20
     for i in range(len(Hits)):
        ShowUser(Hits[i],Hitspos[i]+x)
        x+=20
    show_points()
    if User.points1 > 21:
        state = 0
    money()
    pygame.display.update()


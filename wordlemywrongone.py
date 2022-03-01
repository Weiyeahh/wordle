import random, pygame, sys
from pygame.locals import *
from wordlist import wordlist 
pygame.init()

white=(255,255,255)
yellow=(255,255,102)
grey=(211,211,211)
black=(0,0,0)
green=(0,255,0)
lightgreen=(153,255,204)


word=random.choice(wordlist).upper()
print(word)
def check(word):
    gridcolor=[grey,grey,grey,grey,grey]
    for x in range(0,4):
        for y in range(0,4):
            pygame.draw.rect(window, grey, pygame.Rect(60+(x*80), 50+(y*80), 50, 50),2)

    pygame.display.set_caption("Wordle!")
    font = pygame.font.SysFont("Helvetica neue", 40)
    window.blit(font.render(guess, True, grey), (180, 530))
    spacing=0
    for turn in (0,4):
        for x in range(0,4):
            pygame.draw.rect(window, gridcolor[x], pygame.Rect(60 +spacing, 50+ (turn*80), 50, 50))
            window.blit(font.render(guess[x], True, black), (70 + spacing, 50 + (turn*80)))
            spacing+=80

    for x in range(0,4):
        if guess[x] in word:
            gridcolor[x]=yellow
        if guess[x] == word[x]:
            gridcolor[x]=green
    if gridcolor==[green,green,green,green,green]:
        return True
    
guess=""
window = pygame.display.set_mode((600, 800))
win=False
window.fill(black)
def getinput():
    turn=0
    while True:
        while turn<=5:
            for event in pygame.event.get():
                win=check(word)
                if event.type == pygame.KEYDOWN:
                    guess+=event.unicode.upper()
                    if event.key == K_RETURN:
                        if len(guess)==5:
                            turn+=1
                            if win==True:
                                window.blit("youWin",(90,200))
                                window.blit("playAgain",(60,300))
                                pygame.display.update()
                            else:
                                guess==""            
                        else:
                            window.blit("You need to enter 5 letters",(90,200))
                            guess==""
                            pygame.display.update()
                    if event.key == pygame.K_BACKSPACE:
                        guess = guess[:-1]
                    
        window.blit("You ran out of chances",(90,200))
        pygame.display.update()

getinput()
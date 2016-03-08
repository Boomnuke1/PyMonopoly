import pygame,sys,inputbox
from pygame.locals import *
pygame.init()
gameDisplay = pygame.display.set_mode((1350,700))
back =(0,200,0)
black = (0,0,0)
l1_music = pygame.mixer.Sound('music.wav')
pygame.display.set_caption("Monopoly")
board =pygame.image.load("board.png")
play = pygame.image.load("play.png")
play2 = pygame.image.load("play2.png")
icon =pygame.image.load("icon.png")
clock = pygame.time.Clock()
battleship =pygame.image.load("battleship.png")
stop = pygame.image.load("quit.png")
stop2 = pygame.image.load("quit2.png")
gexit = False
page = 1
while not gexit:
    mousePos = pygame.mouse.get_pos()
    pygame.display.set_icon(icon)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_RSHIFT or pygame.K_LSHIFT:
                shift = True
    gameDisplay.fill(back)
    if page == 1:
        pygame.mixer.Sound.play(l1_music)
        Text = pygame.font.SysFont("comicsansms",115)
        text = Text.render("Monopoly", True, black)
        gameDisplay.blit(text,(370,50))
        if 337 < mousePos[0] < 537 and 440 < mousePos[1] < 530:
            gameDisplay.blit(play2,(332,438))
            if event.type == pygame.MOUSEBUTTONDOWN:
                    page = 2
        else:
            gameDisplay.blit(play,(337,440))
    elif page == 2:
        name = inputbox.ask(gameDisplay,"Name")
        page = 3
    if 1250 < mousePos[0] <1350 and 0 < mousePos[1] < 100:
      gameDisplay.blit(stop2,(1245,0))
      if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.quit()
        quit()
    else:
      gameDisplay.blit(stop,(1250,0))
    clock.tick(60)
    pygame.display.update()
pygame.quit()
quit()

import pygame
import random
import sys
from time import sleep

BLACK = (0, 0, 0)
padWidth = 480
padHeight = 640



#   Game 관련 이미지 로드
# background = pygame.image.load('images/background.png')
# ighter =  pygame.image.load('images/fighter.png')
missile = pygame.image.load('images/missile.png')
explosion = pygame.image.load('images/explosion.png')

#   Game 관련 사운드 로드
# pygame.mixer.music.load('images/music.wav')
# pygame.mixer.music.play(-1)
# missileSound = pygame.mixer.Sound('images/missile.wav')
# gameOverSound = pygame.mixer.Sound('images/gameover.wav')



# rockImage = ['rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png',
#              'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png',
#              'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png',
#              'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png',
#              'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png',
#              'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png']
# explosionSound = ['explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav']


def drawObject(obj,x,y) :
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter
    #   pygame 초기화
    pygame.init()
    #   Game 화면창 설정
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    #   Game 타이틀 설정
    pygame.display.set_caption('파이썬 슈팅게임')

    #   Game 관련 이미지 로드
    background = pygame.image.load('images/background.png')
    fighter = pygame.image.load('images/fighter.png')

    #   Game 루프 작성
    clock = pygame.time.Clock()

def runGame() :
    global gamePad, clock, background, fighter

    #   전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    #   전투기 초기 위치 x,y
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0

    onGame=False

    #onGame이 될때 while문 종료
    while not onGame:
        for event in pygame.event.get():
            
            # 게임 프로그램 종료
            if event.type in [pygame.QUIT] :
                pygame.quit()
                sys.exit()

        #   배경 화면 그리기
        drawObject(background,0,0)
        #   배경 화면 그리기
        drawObject(fighter, x, y)

        #   게임화면을 다시 그린다.
        pygame.display.update()

        #   게임화면을 검은색으로 채우기
        gamePad.fill(BLACK)
        #   게임화면 프레임 수60
        clock.tick(60)
    #   게임 종료
    pygame.quit()

initGame()
runGame()
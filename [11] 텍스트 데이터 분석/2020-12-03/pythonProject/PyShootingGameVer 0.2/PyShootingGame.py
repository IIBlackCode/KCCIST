import pygame
import random
import sys
from time import sleep

#   전역변수
BLACK = (0, 0, 0)
padWidth = 480
padHeight = 640

rockImage = ['images/rock01.png', 'images/rock02.png', 'images/rock03.png', 'images/rock04.png', 'images/rock05.png',
             'images/rock06.png', 'images/rock07.png', 'images/rock08.png', 'images/rock09.png', 'images/rock10.png',
             'images/rock11.png', 'images/rock12.png', 'images/rock13.png', 'images/rock14.png', 'images/rock15.png',
             'images/rock16.png', 'images/rock17.png', 'images/rock18.png', 'images/rock19.png', 'images/rock20.png',
             'images/rock21.png', 'images/rock22.png', 'images/rock23.png', 'images/rock24.png', 'images/rock25.png',
             'images/rock26.png', 'images/rock27.png', 'images/rock28.png', 'images/rock29.png', 'images/rock30.png']

explosionSound = ['images/explosion01.wav', 'images/explosion02.wav', 'images/explosion03.wav', 'images/explosion04.wav']


def drawObject(obj,x,y) :
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter, missile, butterfly, explosion, missileSound, gameOverSound
    #   pygame 초기화
    pygame.init()
    #   Game 화면창 설정
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    #   Game 타이틀 설정
    pygame.display.set_caption('Kim Min Seo')

    #   Game 관련 이미지 로드
    background = pygame.image.load('images/background.png')
    fighter = pygame.image.load('images/fighter.png')
    missile = pygame.image.load('images/missile.png')
    explosion = pygame.image.load('images/explosion.png')
    butterfly = pygame.image.load('images/butterfly/butterfly.png')

    #   Game 관련 사운드 로드
    pygame.mixer.music.load('images/music.wav')
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('images/missile.wav')
    gameOverSound = pygame.mixer.Sound('images/gameover.wav')

    #   Game 루프 작성
    clock = pygame.time.Clock()

def writeScore(count) :
    global gamePad
    font = pygame.font.Font('images/NanumGothic.ttf',20)
    text = font.render('파괴한 운석 수 : '+str(count), True, (255,255,255))
    gamePad.blit(text,(10,0))

def writePassed(count) :
    global gamePad
    font = pygame.font.Font('images/NanumGothic.ttf',20)
    text = font.render('놓친 운석 수 : ' + str(count), True, (255, 0, 0))
    gamePad.blit(text,(340,0))

#   게임 메시지 출력
def writeMessage(text) :
    global gamePad, gameoverSound
    textfont = pygame.font.Font('images/NanumGothic.ttf',80)
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameoverSound.play()

    sleep(2)

    pygame.mixer.music.play(-1)
    runGame()

#   전투기 운석충돌 메시지
def crash() :
    global gamePad
    writeMessage('전투기 파괴!')

#   게임 오버 메시지 보이기
def gameOver() :
    global gamePad
    writeMessage('게임 오버!')

fpsCheck = 0
def runGame() :
    global gamePad, clock, background, fighter, missile, butterfly, fpsCheck, explosion, inShot
    global missileSound, gameOverSound

    #   미사일 좌표
    missileXY = []

    #   운석이미지중 아무거나 랜덤으로 읽어오기
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    #   운석 초기 위치
    #   X 좌표중 랜덤으로, Y좌표는 0부터[화면상 맨 위], 속도는 2프래임
    rockX = random.randrange(0, padWidth-rockWidth)
    rockY = 0
    rockSpeed = 2

    #   나비 초기 위치
    butterflyX = random.randrange(0, padWidth-rockWidth)
    butterflyY = 0
    butterflySpeed = 4

    #   전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    #   전투기 초기 위치 x,y
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
    fighterY = 0

    #   미사일에 운석이 맞았을 경우 True
    isShot = False
    #   나비가 미사일에 맞을 때 카운트
    butterflyCount = 0
    #   미사일에 나비에 맞았을 경우 True
    isShot2 = True


    shotCount = 0
    rockPassed = 0

    onGame=False

    #onGame이 될때 while문 종료
    while not onGame:

        # 게임이 진행되는동안 EVENT 설정
        for event in pygame.event.get():
            
            #   게임 프로그램 종료
            if event.type in [pygame.QUIT] :
                pygame.quit()
                sys.exit()

            #   키보드 입력 관련 설정
            if event.type in [pygame.KEYDOWN] :

                #   ← 버튼 누르면 전투기를 x좌표 -5만큼 이동
                if event.key == pygame.K_LEFT :
                    fighterX -= 5

                #   → 버튼 누르면 전투기를 x좌표 +5만큼 이동
                elif event.key == pygame.K_RIGHT :
                    fighterX += 5

                #   → 버튼 누르면 전투기를 x좌표 +5만큼 이동
                elif event.key == pygame.K_UP:
                    fighterY += 5
                    print(fighterY)
                elif event.key == pygame.K_DOWN:
                    fighterY -= 5
                    print(fighterY)

                #   space bar 누를 때 : 미사일 발사
                elif event.key == pygame.K_SPACE :

                    #   스페이스바 눌렀을 때 좌표값을 missaileXY에 담는다.
                    missileSound.play()
                    missileX = x+fighterWidth/2
                    missileY = y-fighterHeight
                    missileXY.append([missileX, missileY])

            #   버튼 누른 후에 전투기 이동
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighterY = 0

        #   1. 배경 화면 그리기
        drawObject(background,0,0)

        #   2. 이미지 화면에 그리기

        #   2 - 1 전투기 관련 설정
        #   전투기 위치 재조정 : 누를때마다 증감하는 X좌표값을 x에 저장[최종 전투기 위치값 저장]
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth :
            x = padWidth - fighterWidth

        y -= fighterY
        if y < 0:
            y = 0
        elif y > padHeight - fighterHeight:
            y = padHeight - fighterHeight


        #  Y축이 떨어지는 운석의 높이 + 운석의 길이보다 작을 때
        if  y < rockY + rockHeight:
            if(rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth) :
                crash()

        #   전투기 좌표값을 받아 화면에 그리기
        drawObject(fighter, x, y)

        #   운석 3개 놓치면 게임 오버
        if rockPassed == 3 :
            gameOver()
        #   2 - 2 미사일 관련 설정
        #   미사일좌표 배열에 미사일 X축값 저장, Y축 증가값, 화면밖 없어짐 세팅
        if len(missileXY) != 0:

            #   화면 왼쪽 최상단의 좌표값이 (0,0)
            for i, bxy in enumerate(missileXY):
                #   스페이스바 누른 순간의 x좌표값을 받아 y값만 -10씩 줄어듬 : 미사일이 올라간다.
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                #   미사일이 화면밖으로 벗어남
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        #   게임화면에 미사일 그리기
        if len(missileXY) != 0:
            for bx, by in missileXY :
                drawObject(missile, bx, by)

        #   2 - 3 운석 관련 설정

        #   운석 맞춘 점수 표시
        writeScore(shotCount)

        #   운석 아래로 떨어짐
        rockY += rockSpeed

        #   운석이 화면 벗어나는 경우
        if rockY > padHeight:

            #   랜덤 운석 이미지
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            rockPassed += 1


        writePassed(rockPassed)

        #   운석 그리기
        drawObject(rock, rockX, rockY)

        #   2 - 4 나비 관련 설정
        #   나비 아래로 떨어짐 초당 2프래임 약 5초안에 재생성
        #   화면 벗어날때마다 나비 생성
        #   2프래임 : 340 = x : 180
        #   640x = 640/3
        #   x = 640/3 * 1/640
        fpsCheck += 1
        if butterflyY > padHeight :
            fpsCheck = 0
            #   랜덤 나비 이미지
            butterflySize = butterfly.get_rect().size
            butterflyWidth = butterflySize[0]
            butterflyHeight = butterflySize[1]
            butterflyX = random.randrange(0, padWidth - butterflyWidth)
            butterflyY = 0

         #   나비 그리기
        butterflyY += butterflySpeed
        drawObject(butterfly, butterflyX, butterflyY)

        #   2 - 5 미사일 발사 화면에 그리기
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                #미사일이 운석을 맞추었을 경우
                if bxy[1] < rockY :
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth :
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                 # 미사일이 나비를 맞추었을 경우
                if bxy[1] < butterflyY:
                    if bxy[0] > butterflyX and bxy[0] < butterflyX + butterflyWidth:
                        # print(bxy[0], butterflyX, butterflyWidth)

                        print('bxy[0]:',bxy[0])
                        print('butterflyX : ', butterflyX)
                        print('butterflyWidth : ', butterflyWidth)

                        missileXY.remove(bxy)
                        if(isShot2 == False) :
                            butterflyCount +=1
                        shotCount += 1

                #미사일이 화면 밖으로 벗어난 경우
                if bxy[1] <= 0 :
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if isShot :
            #운석 폭발 그리기
            drawObject(explosion,rockX,rockY)
            # destroySound.play()

            #새로운 운석 생성
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            destroySound = pygame.mixer.Sound(random.choice(explosionSound)).play()
            isShot = False

            rockSpeed += 0.02
            if rockSpeed >= 10:
                rockSpeed = 10

        #   운석 그리기
        drawObject(rock, rockX, rockY)

        if butterflyCount == 1 :
            #나비 색 변화
            butterfly = pygame.image.load('images/butterfly/butterfly2.png')
            butterflySize = rock.get_rect().size
            butterflyWidth = rockSize[0]
            butterflyHeight = rockSize[1]

        if butterflyCount == 2 :
            #나비 색 변화
            butterfly = pygame.image.load('images/butterfly/butterfly3.png')
            butterflySize = rock.get_rect().size
            butterflyWidth = rockSize[0]
            butterflyHeight = rockSize[1]

        if butterflyCount == 3 :
            #나비 색 변화
            butterfly = pygame.image.load('images/butterfly/butterfly.png')
            butterflySize = rock.get_rect().size
            butterflyWidth = rockSize[0]
            butterflyHeight = rockSize[1]
            isShot2 = True

        if isShot2 :
            # 나비 폭발 그리기
            drawObject(explosion, butterflyX, butterflyY)
            destroySound = pygame.mixer.Sound('images/cry.wav').play()

            # 새로운 나비 생성
            butterfly = pygame.image.load('images/butterfly/butterfly.png')
            butterflySize = rock.get_rect().size
            butterflyWidth = rockSize[0]
            butterflyHeight = rockSize[1]
            butterflyX = random.randrange(0, padWidth - rockWidth)
            butterflyY = 0
            isShot2 = False
            butterflyCount = 0

        #   운석 그리기
        drawObject(butterfly, butterflyX, butterflyY)

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
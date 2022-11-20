import pygame

class GlobalVariable:
    BLACK = (0, 0, 0)
    padWidth = 480
    padHeight = 640

    rockImage = ['images/rock01.png', 'images/rock02.png', 'images/rock03.png', 'images/rock04.png',
                 'images/rock05.png',
                 'images/rock06.png', 'images/rock07.png', 'images/rock08.png', 'images/rock09.png',
                 'images/rock10.png',
                 'images/rock11.png', 'images/rock12.png', 'images/rock13.png', 'images/rock14.png',
                 'images/rock15.png',
                 'images/rock16.png', 'images/rock17.png', 'images/rock18.png', 'images/rock19.png',
                 'images/rock20.png',
                 'images/rock21.png', 'images/rock22.png', 'images/rock23.png', 'images/rock24.png',
                 'images/rock25.png',
                 'images/rock26.png', 'images/rock27.png', 'images/rock28.png', 'images/rock29.png',
                 'images/rock30.png']

    explosionSound = ['images/explosion01.wav', 'images/explosion02.wav', 'images/explosion03.wav',
                      'images/explosion04.wav']

    def initGame(self) :
        global padWidth, padHeight
        global gamePad, clock, background, fighter, missile, butterfly, explosion, missileSound, gameOverSound
        #   pygame 초기화
        pygame.init()
        #   Game 화면창 설정
        gamePad = pygame.display.set_mode((padWidth, padHeight))
        #   Game 타이틀 설정
        pygame.display.set_caption('파이썬 슈팅게임')

        #   Game 관련 이미지 로드
        background = pygame.image.load('../images/background.png')
        fighter = pygame.image.load('../images/fighter.png')
        missile = pygame.image.load('../images/missile.png')
        explosion = pygame.image.load('../images/explosion.png')
        butterfly = pygame.image.load('../images/butterfly/butterfly.png')

        #   Game 관련 사운드 로드
        pygame.mixer.music.load('../images/music.wav')
        pygame.mixer.music.play(-1)
        missileSound = pygame.mixer.Sound('../images/missile.wav')
        gameOverSound = pygame.mixer.Sound('../images/gameover.wav')

        #   Game 루프 작성
        clock = pygame.time.Clock()
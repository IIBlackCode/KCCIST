import random
import threading
from time import sleep

import pygame
from pygame.locals import *

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (250, 250, 50)
RED = (250, 50, 50)

FPS = 60

class Fighter(pygame.sprite.Sprite) :
    def __init__(self):
        super(Fighter, self).__init__()
        self.image = pygame.image.load('fighter.png') #이미지 선정
        self.rect = self.image.get_rect()
        self.rect.x = int(WINDOW_WIDTH / 2) #처음 위치 x축 선정
        self.rect.y = WINDOW_HEIGHT - self.rect.height #처음 위치 y축 선정 비행기가 나와야하므로 그만큼 빼줌
        self.dx = 0
        self.dy = 0 #방향 조작에 대한 지정

    def update(self): #움직임 처리에 대한 함수
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x < 0 or self.rect.x + self.rect.width > WINDOW_WIDTH: # 배경 x축 밖을 나갈 때 처리
            self.rect.x -= self.dx

        if self.rect.y < 0 or self.rect.y + self.rect.height > WINDOW_HEIGHT : #배경 y축 밖을 나갈 때 처리
            self.rect.y -= self.dy

    def draw(self, screen): #객체를 그려주는 함수
        screen.blit(self.image, self.rect)

    def collide(self, sprites): #충돌에 대한 함수
        for sprite in sprites : #다양한 객체를 다룰 때 쓰이는 sprite기능을 활용
            if pygame.sprite.collide_rect(self, sprite) : #충돌이 일어났을 때 그 충돌이 일어난 객체를 찾기 위한 if문
                return sprite

class Missile(pygame.sprite.Sprite):
    def __init__(self,  xpos, ypos, speed):
        super(Missile, self).__init__()
        self.image = pygame.image.load('missile.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound('missile.wav')

    def launch(self):
        self.sound.play()

    def update(self):
        self.rect.y -= self.speed #미사일은 위로 가니 - 처리
        if self.rect.y + self.rect.height < 0 : # 밖으로 나가면 없애준다.
            self.kill()

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

class Nabi(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Nabi, self).__init__()
        self.image = pygame.image.load('nabi01.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.life = 3 #초기 목숨을 3개로 지정

    def update(self):
        self.rect.y += self.speed

    def nabi2(self, surface, xpos, ypos): #1번 맞았을 때
        self.image = pygame.image.load('nabi02.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        surface.blit(self.image, self.rect) #이미지와 좌표를 받아서 출력

        self.sounds = ('tmaSti00.wav', 'tmaSti01.wav')
        self.sound = pygame.mixer.Sound(random.choice(self.sounds))
        self.sound.play()

    def nabi3(self, surface, xpos, ypos): #2번 맞았을 때
        self.image = pygame.image.load('nabi03.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        surface.blit(self.image, self.rect)

        self.sounds = ('TMaDth00.wav', 'TMaDth01.wav')
        self.sound = pygame.mixer.Sound(random.choice(self.sounds))
        self.sound.play()


    def out_of_screen(self): #화면에 나가면 True처리로 없앤다.
        if self.rect.y > WINDOW_HEIGHT :
            return True

class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Rock, self).__init__()
        rock_images = ('rock01.png','rock02.png','rock03.png','rock04.png','rock05.png','rock06.png',
                       'rock07.png','rock08.png','rock09.png','rock10.png','rock11.png','rock12.png',
                       'rock13.png','rock14.png','rock15.png','rock16.png','rock17.png','rock18.png',
                       'rock19.png','rock20.png','rock21.png','rock22.png','rock23.png','rock24.png',
                       'rock25.png','rock26.png','rock27.png','rock28.png','rock29.png','rock30.png')

        self.image = pygame.image.load(random.choice(rock_images))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT :
            return True

#텍스트 입력을 위한 함수
def draw_text(text, font, surface, x, y, main_color) : 
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

#돌에 맞추었을 때 폭발하는 처리 함수
def occur_explosion(surface, x, y):
    explosion_image = pygame.image.load('explosion.png')
    explosion_rect = explosion_image.get_rect()
    explosion_rect.x = x
    explosion_rect.y = y
    surface.blit(explosion_image, explosion_rect)

    explosion_sounds = ('explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav')
    explosion_sound = pygame.mixer.Sound(random.choice(explosion_sounds))
    explosion_sound.play()


def game_loop():
    default_font = pygame.font.Font('NanumGothic.ttf', 28)
    background_image = pygame.image.load('background.png')
    gameover_sound = pygame.mixer.Sound('gameover.wav')
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)
    fps_clock = pygame.time.Clock()

    fighter = Fighter()
    missiles = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    nabis = pygame.sprite.Group()

    occur_prob = 120  #조절 가능한 수 -> 얼마나 자주 나오게 할 거냐. 수가 클 수록 적게 나온다.
    shot_count = 0
    count_missed = 0

    done = False

    while not done:
        tick = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN : #키보드가 눌릴 때
                if event.key == pygame.K_LEFT : #왼쪽
                    fighter.dx -= 5 # 이 값은 조절 가능
                elif event.key == pygame.K_RIGHT: #오른쪽
                    fighter.dx += 5
                elif event.key == pygame.K_UP : #위
                    fighter.dy -= 5
                elif event.key == pygame.K_DOWN: #아래
                    fighter.dy += 5
                elif event.key == pygame.K_SPACE: #스페이스는 슈팅
                    missile = Missile(fighter.rect.centerx, fighter.rect.centery, 10)
                    missile.launch()
                    missiles.add(missile)

            if event.type == pygame.KEYUP : #키보드에서 손 뗄 때
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    fighter.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    fighter.dy = 0

        screen.blit(background_image, background_image.get_rect())
        
        #많이 할수록 난이도가 강해지게 갯수와 속도 조절
        occur_of_rocks = 1 + int(shot_count / 300)
        min_rock_speed = 1 + int(shot_count / 200)
        max_rock_speed = 1 + int(shot_count / 100)

        if random.randint(1, occur_prob) == 1 :
            for i in range(occur_of_rocks):
                speed = random.randint(min_rock_speed, max_rock_speed)
                rock = Rock(random.randint(0, WINDOW_WIDTH - 30), 0, speed)
                rocks.add(rock)
        
        #tick이 범위에 대한 함수라서 0~2개가 나옴.
        if tick % 3000 <= 10 :
            speed = 1
            nabi = Nabi(random.randint(0, WINDOW_WIDTH - 30), 0, speed)
            nabis.add(nabi)


        draw_text('파괴한 운석 : {}'.format(shot_count), default_font, screen, 100, 20, YELLOW)
        draw_text('놓친 운석 : {}'.format(count_missed), default_font, screen, 400, 20, RED)

        for missile in missiles:
            rock = missile.collide(rocks)
            nabi = missile.collide(nabis)
            if rock: #미사일을 돌에 맞추었을 때
                missile.kill()
                rock.kill()
                occur_explosion(screen, rock.rect.x, rock.rect.y)
                shot_count += 1

            if nabi: #미사일을 나비에 맞추었을 때
                missile.kill()
                nabi.life -= 1
                if nabi.life == 2 :
                    nabi.nabi2(screen, nabi.rect.x, nabi.rect.y)
                elif nabi.life == 1 :
                    nabi.nabi3(screen, nabi.rect.x, nabi.rect.y)
                elif nabi.life == 0 :
                    nabi.kill()
                    occur_explosion(screen, nabi.rect.x, nabi.rect.y)

        for rock in rocks:
            if rock.out_of_screen(): #화면 밖으로 나갔을 때
                rock.kill()
                count_missed += 1

        rocks.update()
        rocks.draw(screen)
        nabis.update()
        nabis.draw(screen)
        missiles.update()
        missiles.draw(screen)
        fighter.update()
        fighter.draw(screen)
        pygame.display.flip()

        if fighter.collide(rocks) or count_missed >= 3: #죽는 조건
            pygame.mixer_music.stop()
            occur_explosion(screen, fighter.rect.x, fighter.rect.y)
            pygame.display.update()
            gameover_sound.play()
            sleep(1)
            done = True

        fps_clock.tick(FPS)

    return 'game_menu'

def game_menu():
    start_image = pygame.image.load('background.png')
    screen.blit(start_image, [0, 0])
    draw_x = int(WINDOW_WIDTH / 2)
    draw_y = int(WINDOW_HEIGHT / 4)
    font_70 = pygame.font.Font('NanumGothic.ttf', 70)
    font_40 = pygame.font.Font('NanumGothic.ttf', 40)

    draw_text('슈팅 게임', font_70, screen, draw_x, draw_y, YELLOW)
    draw_text('엔터 키를 누르면', font_40, screen, draw_x, draw_y + 200, WHITE)
    draw_text('게임이 시작됩니다.', font_40, screen, draw_x, draw_y + 250, WHITE)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: #엔터키를 누르면 실행
                return 'play'
        if event.type == QUIT:
            return 'quit'

    return 'game_menu'

def main():
    global screen

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('PyShooting')

    action = 'game_menu'
    while action != 'quit' :
        if action == 'game_menu' :
            action = game_menu()
        elif action == 'play' :
            action = game_loop()

    pygame.quit()

if __name__ == "__main__":
    main()
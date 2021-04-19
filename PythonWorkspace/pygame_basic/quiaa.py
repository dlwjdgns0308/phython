import pygame
from random import *
###############################################################
#초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

#FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:/Users/이정훈/Desktop/phython/PythonWorkspace/pygame_basic/background.png")

# 캐릭터 정의
character = pygame.image.load("C:/Users/이정훈/Desktop/phython/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 0.6

# 적 정의
enemy = pygame.image.load("C:/Users/이정훈/Desktop/phython/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = 0
enemy_y_pos = 0


enemy_to_y = 15

running = True 
while running:
    dt  = clock.tick(30) 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            to_x = 0

   
    #3. 게임 캐릭터 위치 정의
    character_x_pos = character_x_pos + (to_x * dt)
    character_y_pos = character_y_pos + (to_y * dt)
    
    
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_x_pos < 0:
        character_x_pos = 0
    
    #적 위치 정의
    enemy_y_pos += enemy_to_y
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
    if enemy_y_pos == 0:
        enemy_x_pos = randint(1, 480)



    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False
    #5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    pygame.display.update()

pygame.quit()
 
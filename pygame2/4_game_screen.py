import pygame
from random import *

# 레벨에 맞게 설정
def setup(level):
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) # 20을 초과하면 20으로 처리

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    grid = [[0 for col in range(columns) for row in range(rows)]] # 5 x 9

    number = 1 # 시작 숫자를 1부터 number_count까지, 만약 5라면 5까지 숫자를 랜덤으로 배치
    while number <= number_count:
        row_idx = randrange(0, rows) # 0,1,2,3,4 중 랜덤 뽑기
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number # 숫자 지정
            number += 1

    print(grid)
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색 동그라미
    #  
# 게임화면 보여주기
def display_game_screen():
    print("Game Start")
#pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True
#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

#색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#  게임 시작 여부
start = False
# 게임 시작 전에  게임설정 함수 수행
setup(1)
# 게임 루프
running = True
while running:
    click_pos = None
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # 사용자가 클릭했을때
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    #화면 전체를 까맣게 칠함
    screen.fill(BLACK)
    if start: 
        display_game_screen() # 게임 화면표시
    else: 
        display_start_screen() # 시작 화면 표시

    # 사용자가 클릭했다면
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()

#게임 종료
pygame.quit()
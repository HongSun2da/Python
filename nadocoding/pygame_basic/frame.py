import pygame
import random

# 초기화
pygame.init()   

# 화면 설정
pygame.display.set_caption("Nado Game") # 타이틀
screen_width = 480
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load(r"E:\Development\Python\nadocoding\pygame_basic\bg.png")

# FPS
clock = pygame.time.Clock()

# 캐럭터
character = pygame.image.load(r"E:\Development\Python\nadocoding\pygame_basic\ch.png")
character_size = character.get_rect().size  
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 0.6

to_x = 0
to_y = 0

# enemy
enemy = pygame.image.load(r"E:\Development\Python\nadocoding\pygame_basic\enemy.png")
enemy_size = character.get_rect().size  
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10


# 폰트 정의 (남은 시간 표시)
game_font = pygame.font.Font(None, 40)
total_time = 30
start_ticks = pygame.time.get_ticks()   # 시작 기준


# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # FPS 설정
    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():    # 이벤트 확인
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_x = 0
            if event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP:
                to_y = 0
            if event.key == pygame.K_DOWN:
                to_y = 0                    

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 적 위치 변경
    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 캐릭터 및 enemy 위치정보
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False


    # 배경이미지
    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))  # 케릭터
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # enemy


    # 남은 시간 타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 초 단위
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False


    # 화면 출력
    pygame.display.update()         


# 프로그램 종료
pygame.quit()


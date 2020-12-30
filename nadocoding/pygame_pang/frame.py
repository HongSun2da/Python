import os
import pygame
import random

# 초기화
pygame.init()   

# 화면 설정
pygame.display.set_caption("Nado Pang") # 타이틀
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# FPS
clock = pygame.time.Clock()

# 이미지 위치 정보
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]

# 캐럭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size  
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
character_speed = 5
character_to_x = 0      # 좌우 이동 위치값

# weapon 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size  
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_speed = 10

# 무기는 여러발 발사 가능 
weapons = []

# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]
ball_speed_y = [-18, -15, -12, -9]

balls = []
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spe_y" : ball_speed_y[0]
})

# 무기, 공 삭제 변수
weapon_to_remove = -1
ball_to_remove = -1


# 폰트 정의 (남은 시간 표시)
game_time = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()   # 시작 기준

# 폰트 (Game Over)
game_font = pygame.font.Font(None, 80)


game_result = "Game Over"

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # FPS 설정
    # print("fps : " + str(clock.get_fps()))

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:          # 캐릭터 왼쪽 이동
                character_to_x -= character_speed   
            if event.key == pygame.K_RIGHT:         # 캐릭터 오른쪽 이동
                character_to_x += character_speed   
            if event.key == pygame.K_SPACE:         # 캐릭터 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            if event.key == pygame.K_SPACE:
                pass

    # 캐릭터 위치 정의                
    character_x_pos += character_to_x

    # 캐릭터 위치정보
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 범위 이탈 방지
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    


    # 무기 위치 정의      
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons ]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0 ] 

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 위치정보
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 범위 이탈 방지
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y > screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spe_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    # weapons_rect = character.get_rect()
    # weapons_rect.left = character_x_pos
    # weapons_rect.top = character_y_pos

    # 충돌 체크
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_reck = ball_images[ball_img_idx].get_rect()
        ball_reck.left = ball_pos_x
        ball_reck.top = ball_pos_y

        # 캐릭터 + 공 충돌
        if character_rect.colliderect(ball_reck):
            running = False
            break

        # 공 + 무기 충돌    
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapons_rect = weapon.get_rect()
            weapons_rect.left = weapon_pos_x
            weapons_rect.top = weapon_pos_y
            
            # 공 분해
            if weapons_rect.colliderect(ball_reck):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                if ball_img_idx < 3:
                    ball_width = ball_reck.size[0]
                    ball_height = ball_reck.size[1]

                    small_ball_reck = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_reck.size[0]
                    small_ball_height = small_ball_reck.size[1]
                    
                    # 분해 왼쪽
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2 ) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2 ) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : -3,
                        "to_y" : -6,
                        "init_spe_y" : ball_speed_y[ball_img_idx + 1]
                    })
                    # 분해 오른쪽
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width /2 ) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height /2 ) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : 3,
                        "to_y" : -6,
                        "init_spe_y" : ball_speed_y[ball_img_idx + 1]
                    })
                break
        else:
            continue
        break

    # 공 + 무기 충돌 이벤트 처리
    if ball_to_remove > -1:
        del balls[ball_to_remove]   
        ball_to_remove = -1

    if weapon_to_remove > -1:           
        del weapons[weapon_to_remove]   
        weapon_to_remove = -1

    # 공이 없는 경우 
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False    

    # 화면 그리기
    screen.blit(background, (0,0))                              # 배경
    for weapon_x_pos, weapon_y_pos in weapons:                  # 무기
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):                           # 공
        ball_pos_x = val["pos_x"]    
        ball_pos_y = val["pos_y"]    
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y ))   
    screen.blit(stage, (0, screen_height - stage_height ))      # 스테이지
    screen.blit(character, (character_x_pos, character_y_pos))  # 케릭터
    


    # 남은 시간 타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 초 단위
    timer = game_time.render("Time : " + str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False


    # 화면 출력
    pygame.display.update()         


msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()         

pygame.time.delay(2000)

# 프로그램 종료
pygame.quit()


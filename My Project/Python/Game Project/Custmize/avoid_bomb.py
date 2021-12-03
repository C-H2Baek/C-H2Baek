import pygame , random

pygame.init() # 파이게임 모듈 초기화
screen = pygame.display.set_mode((600, 800)) # 창 도는 화면을 초기화하여 표시
clock = pygame.time.Clock() # FPS 초당 프레임 변수 설정
pygame.key.set_repeat(30, 30) # 누름 반복 (키의 반응 속도 설정)

#스코어 생성
large_font = pygame.font.SysFont('Bauhaus 93', 72)
small_font = pygame.font.SysFont('Bauhaus 93', 36)
score = 0
game_over = False

bomb_image = pygame.image.load('assets/avoid_bomb/bomb.png') # 방해물 이미지 정의
#bomb = bomb_image.get_rect(left=100, top=100)
bombs = []  #빈 리스트 정의
for i in range(5): 
    bomb = bomb_image.get_rect(left=random.randint(0, 600), top=-100) #가로랜덤, 탑 -100위치
    #bomb = bomb_image.get_rect(left=(i + 1) * random.randrange(50,100), top=(i + 1) * random.randrange(100,200))
    #bomb의 위치가 생성
    bombs.append(bomb) #생성된 bomb를 리스트내 추가
girl_image = pygame.image.load('assets/avoid_bomb/girl.png') # 캐릭터 이미지 정의
girl = girl_image.get_rect(centerx=300, bottom=800)    # 게임 객체 Rect 크기 및 좌표 정보 로드
#girl.left = 300 - girl_image.get_width() // 2 # 캐릭 객체의 왼쪽 위치
#girl.top = 800 - girl_image.get_height()      # top 위치
#girl.centerx = 300 #중앙위치 x
#girl.bottom = 800  #바닥위치


while True: # running thig code
    screen.fill((0, 0, 0)) # 색상코드 0, 0, 0 으로 화면을 채움

    event = pygame.event.poll() # 게임의 이벤트를 처리한다
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN and not game_over :  #키 부분 정의 
        if event.key == pygame.K_LEFT:  #LEFT시 left값을 -5
            girl.left -= 5          
        elif event.key == pygame.K_RIGHT:   #RIGHT시 left 값을 +5
            girl.left += 5
        elif event.key == pygame.K_UP:   #UP시 top 값을 -5
            girl.top -= 5
        elif event.key == pygame.K_DOWN:   #DOWN시 top 값을 +5
            girl.top += 5
        elif event.key == pygame.K_r:   #DOWN시 top 값을 +5
            bombs.remove(bomb)
            bomb = bomb_image.get_rect(left=random.randint(0, 600 - bomb.width) , top=-100)
            bombs.append(bomb)
            game_over = False
            score = 0
    #대각선 이동 선언부
        '''
        elif event.key == pygame.K_UP & pygame.K_LEFT:   #DOWN시 top 값을 +5
            girl.top += 5
            girl.left -= 5
        elif event.key == pygame.K_DOWN:   #DOWN시 top 값을 +5
            girl.top += 5
        elif event.key == pygame.K_DOWN:   #DOWN시 top 값을 +5
            girl.top += 5
        elif event.key == pygame.K_DOWN:   #DOWN시 top 값을 +5
            girl.top += 5
        '''    

    #폭탄 드랍
    if not game_over:
        for bomb in bombs:
            bomb.top += 10
            #다시 드랍
            if bomb.top > 800: # 폭탄의 세로의 값 800에 도달
                bombs.remove(bomb)
                bomb = bomb_image.get_rect(left=random.randint(0, 600 - bomb.width) , top=-100)
                bombs.append(bomb)
                score += 1
                
                #bomb.left = random.randint(0,600 - bomb.width)
                #bomb.top = -100

        

    # 벽을 감지하는 위치
    if girl.left < 0:
        girl.left = 0
    elif girl.right > 600:
        girl.right = 600

    for bomb in bombs:
        screen.blit(bomb_image, bomb)
        if bomb.colliderect(girl): # 장해물이 캐릭터와 충돌 했을때
            game_over = True
    
    #screen.blit(girl_image, (0, 0)) # 캐릭터 이미지 배치  (x, y)
    #screen.blit(girl_image, (0, 800 - girl_image.get_height())) # x 0, y는 바닥에서 이미지의 키를 뺀값
    #screen.blit(girl_image, (300 - girl_image.get_width() // 2, 800 - girl_image.get_height()))
        # x는 가로사이즈 300 - 캐릭터길이 / 2의 값(중앙정렬)
    
    #screen.blit(bomb_image, bomb)
    #그리기
    
    screen.blit(girl_image, girl)
    #점수판 배치
    score_image = small_font.render('SCORE {}'.format(score), True, (255,255,0))
    screen.blit(score_image, (10, 10))

    #게임오버 조건시
    if game_over:
        game_over_image = large_font.render('GAME OVER', True, (255,0,0))
        game_over_image2 = small_font.render('PRESS "R" KEY TO RESTART', True, (255,255,0))
        #screen.blit(game_over_image, (300- game_over_image.get_width() //2 , 400 - game_over_image.get_height() // 2 ))
        screen.blit(game_over_image, game_over_image.get_rect(centerx=300, centery=300)) #메시지 출력 중앙2
        screen.blit(game_over_image2, game_over_image2.get_rect(centerx=300, centery=400)) #메시지 출력 중앙2
        
    pygame.display.update()
    clock.tick(30) #초당 프레임수

pygame.quit() 


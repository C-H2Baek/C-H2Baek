from tkinter import *
from Table import *
from Ball import *
from Bat import *
import random
import pygame

##### 메인부
window=Tk()
window.title("MyPingPong")

# 전역 변수 초기화
x_speed = 10 # x속도
y_speed = 0 # y속도
score_left = 0 # 왼쪽 득점판
score_right = 0  # 오른쪽 득점판
first_serve = True # 첫번째 서브 여부

#### game_flow() 함수부
def game_flow():

    global first_serve
    global score_left
    global score_right
    # 공을 일정 시간마다 움직임
    my_ball.move_next()
    window.after(30, game_flow)  # 30밀리초마다 game_flow 함수 실행 , ex 5초는 500
    
    # 공이 배트에 닿았는지 충돌 확인, 두 배트에 대해 detect_collision() 함수 실행
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    # 공이 좌우 벽에 충돌했을때 처리
    # 공의 X 좌표값이 0보다 작을 경우 왼쪽 벽에 충돌한 상황
    if(my_ball.x_posn <=0): 
        my_ball.stop_ball() # 공을 멈춤, x_speed, y_speed를 0으로 설정
        my_ball.start_position() # 공의 위치 초기화
        bat_L.start_position() # bat_L 배트 위치 초기화
        bat_R.start_position() # bat_R 배트 위치 초기화
        my_table.move_item(bat_L.rectangle, 0, 150, 25 , 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 600, 250)
        
        score_left = score_left + 1 # 왼쪽 득점 1 추가
        if(score_left >= 5):
            score_left = "WIN"
            score_right = "LOSE"
    
        first_serve = True
        my_table.draw_score(score_left, score_right)
        
        #my_ball.start_ball(x_speed=random.randrange(10,20), y_speed=random.randrange(100,200))

    # 공의 X 좌표값이 width 보다 클 경우 오른쪽 벽에 충돌한 상황
    if(my_ball.x_posn + my_ball.width >= my_table.width):
        my_ball.stop_ball() # 공을 멈춤, x_speed, y_speed를 0으로 설정
        my_ball.start_position() # 공의 위치 초기화
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 0, 150, 25 ,250)
        my_table.move_item(bat_R.rectangle, 575, 150, 600, 250)
        
        score_right = score_right + 1
        if(score_right >= 5):
            score_right = "WIN"
            score_left = "LOSE"
            
        first_serve = True
        my_table.draw_score(score_left, score_right)   
           
        #my_ball.start_ball(x_speed=random.randrange(10,20), y_speed=random.randrange(100,200))

# restart_game 함수:
def restart_game(master):
    global score_left
    global score_right
    bat_L.start_position()
    bat_R.start_position()
    my_table.move_item(bat_L.rectangle, 0, 150, 25 ,250)
    my_table.move_item(bat_R.rectangle, 575, 150, 600, 250)
    label1.destroy()

    my_ball.start_ball(x_speed=random.randrange(20,30), y_speed=random.randrange(20,30))
    if(score_left == "WIN" or score_left == "LOSE"):
        score_left = 0
        score_right = 0
        my_table.draw_score(score_left, score_right)   
###  Table 클래스를 사용해서 테이블 생성

backimg = PhotoImage(file="Images/background.png")
my_table = Table(window, 600, 400, backimg)
label1=Label(window, text="PRESS THE 'SPACE KEY'\n TO START" , font=("Showcard Gothic",30))
label1.place(x=80, y=50)

### 공 생성
# Ball(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn)
my_ball = Ball(table=my_table, x_speed=0, y_speed=0, width=25, height=25, color="red", x_posn=((600-25)/2), y_posn=((400-25)/2))

### 배트 생성
# Bat 클래스로부터 배트를 주문
# Bat(self, table, width, height, x_posn, y_posn, color, x_speed = 25, y_speed = 25)
bat_L = Bat(table=my_table, y_speed=15, width=25, height=100, color="green", x_posn=0, y_posn=((400-100)/2))
bat_R = Bat(table=my_table, y_speed=15, width=25, height=100, color="blue", x_posn=575, y_posn=((400-100)/2))

#### 함수의 실행부
game_flow()

# 스페이스바를 눌러 게임 시작 또는 재시작
window.bind("<space>", restart_game)

###  배트를 제어하기 위한 키이벤트 및 연결될 함수 지정
# window.bind("<키명>",  함수명)
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

window.mainloop()







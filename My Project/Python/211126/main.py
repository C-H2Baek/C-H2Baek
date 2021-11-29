# Breakout Main

from tkinter import *
import table, ball, bat, random


window = Tk()
window.title("MyBreakout")
my_table = table.Table(window)

bg_image = PhotoImage(file= "Images/back4.png")
my_table.canvas.create_image(2400, 800, image=bg_image, tags="bg_img")
my_table.canvas.lower("bg_img")

# 전역 변수 초기화
x_velocity = 4
y_velocity = 10
first_serve = True
TRY = 0

# ball 모듈의 Ball 클래스로부터 my_ball 인스턴스 생성
my_ball = ball.Ball(table = my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=16, height=16, colour="pink", x_start=292, y_start=392)

# bat 모듈의 Bat 클래스로부터 bat_B의 인스턴스 생성
bat_B = bat.Bat(table = my_table, width=100, height=10,
                x_posn=250, y_posn=770, colour="blue")

# 벽돌 리스트(bricks)를 생성하여 반복문을 통해 6개의 리스트 원소를 추가
bricks = []
# b=1
# while b < 7:
#     i=80 #벽돌을 x좌표 80px 간격으로 생성
#     bricks.append(bat.Bat(table= my_table, width=50, height=25, x_posn=(b*i), y_posn=75, colour="green"))
#     b = b + 1

def brick_start():
 
    i=80  # 가로간격
    j=30  # 세로간격
    for g in range(random.randrange(1,8)):      # 세로개수
        for k in range(1,random.randrange(4 ,8)):  # 가로개수
            bricks.append(bat.Bat(table= my_table, width=50, height=25, x_posn=k*i , y_posn=g+j , colour="white"))
        j=j+50  # 세로증가
    

    return bricks
    
#### 함수
def game_flow():
    global first_serve
    # 첫번째 서브를 기다립니다:
    if(first_serve==True):
        my_ball.stop_ball()
        first_serve = False

        # 벽돌에 공이 충돌하는지 감지
    for b in bricks:
        #  b번째 공이 벽돌에 충돌했다면 벽돌을 화면에서 지우고, 배열에서 삭제
        if(b.detect_collision(my_ball, sides_sweet_spot=False) != None):
            print(b.detect_collision(my_ball, sides_sweet_spot=False))
            my_table.remove_item(b.rectangle)
            bricks.remove(b)
        # 벽돌이 없다면 점수 출력
        if(len(bricks) == 0):
            my_ball.stop_ball()
            my_ball.start_position()
            bat_B.start_position()
            my_table.move_item(bat_B.rectangle, 250, 770, 350 , 780)
            my_table.draw_score("", "  YOU WIN!")     
         
            
    # 아래쪽 벽에 공이 충돌하는지 감지
    if(my_ball.y_posn >= my_table.height - my_ball.height):
        my_ball.stop_ball()
        my_ball.start_position()
        first_serve = True
        my_table.draw_score("", "  WHOOPS!")

    # 배트에 공이 출동 감지
    bat_B.detect_collision(my_ball, sides_sweet_spot=False, topnbottom_sweet_spot=True)

    my_ball.move_next() # 공 움직이기
    window.after(25, game_flow) # 50 밀리초마다 game_flow 함수 실행
# 키 이벤트(Space)가 발생하면 공을 지정한 speed로 속도를 지정
def restart_game(master):
    my_ball.start_ball(x_speed=x_velocity, y_speed=y_velocity)
    my_table.draw_score("", "")
    bat_B.start_position()
    my_table.move_item(bat_B.rectangle, 250, 770, 350 , 780)
    #width=100, height=10,x_posn=250, y_posn=770
    label1.destroy()
    brick_start()
    

label1=Label(window, text="PRESS THE 'SPACE KEY'\n TO START" , font=("Showcard Gothic",30))
label1.place(x=80, y=50)


# 스페이스 키를 게임 재시작 기능과 연결
window.bind("<space>", restart_game)

# 배트를 제어하는 키
window.bind("<Left>", bat_B.move_left)
window.bind("<Right>", bat_B.move_right)


# game_flow() 함수 실행
brick_start()
game_flow()



window.mainloop()
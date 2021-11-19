from tkinter import *
import random

##### 메인부
window=Tk()
window.title("MyPingPong")

# 전역 변수 초기화
x_speed = 10 # x속도
y_speed = 0 # y속도
score_left = 0 # 왼쪽 득점판
score_right = 0  # 오른쪽 득점판
first_serve = True # 첫번째 서브 여부

#### Table 클래스 생성
class Table :
    ### 생성자
    def __init__(self, window, width, height, bg_color, net_color) :
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.net_color=net_color

        # Table 클래스 내에서 캔버스 생성
        self.canvas=Canvas(window, width=self.width, height=self.height, bg=self.bg_color)
        self.canvas.pack()

        self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_color, dash=(15, 23))
        # 득점판 추가:
        font = ("Algerian" , 72)
        self.scoreboard = self.canvas.create_text(300, 65, font=font, fill = "darkgreen")
    ### 함수부
    # Canvas(Table)에 타원(공)을 추가하는 함수
    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)
    
    # Canvas(Table)에 직사각형(배트)를 추가하는 함수
    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.color
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
    
    # Canvas(Table)에 아이템(공과 배트)을 조작할 수 있는 함수 coords() 이용
    # coords()는 입력받은 값으로 속성값 업데이트하는 함수
    # 변경된 위치값으로 공과 배트의 위치 변경
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)

    # canvas에 득점판을 추가하는 도구:
    def draw_score(self, left, right):
        scores = str(right) + "  " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores) 

#### Ball 클래스 생성
class Ball:
    #### 생성자
    def __init__(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn):
        self.width = width          # 공의 가로 사이즈
        self.height = height        #공의 세로 사이즈
        self.x_posn = x_posn     #공의 x 좌표값
        self.y_posn = y_posn     #공의 y 좌표값
        self.color = color            #공의 색상

        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed

        # Table 클래스에 입력받은 매개변수 값 전달
        # Table 의 draw_oval() 함수 실행
        self.table = table
        self.circle = self.table.draw_oval(self)
        
    ### 함수부
    # 공이 움직이는 부분
    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed # 현재 공의 위치에 이동할 거리 x 를 추가
        self.y_posn = self.y_posn + self.y_speed # 현재 공의 위치에 이동할 거리 y 를 추가
      
        # 공이 위쪽 벽에 부딪쳤을 때:
        if(self.y_posn <= 3):
            self.y_posn = 3
            self.y_speed = -self.y_speed

        # 공이 아래쪽 벽에 부딪쳤을 때:      
        if(self.y_posn >= (self.table.height - (self.height - 3))):
            self.y_posn = (self.table.height - (self.height - 3))
            self.y_speed = -self.y_speed    

        # 공의 변경된 위치 지정 및  이동
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)    
    
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
        
    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if random.randint(0,1) else y_speed
        self.start_position()    

    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0  

#### Bat 클래스 생성
class Bat:
    #### 생성자
    def __init__(self, table, width, height, x_posn, y_posn, color, x_speed = 20, y_speed = 20):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color

        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed

        # Table 클래스에 입력받은 매개변수 값 전달
        # Table 의 draw_rectangle() 함수 실행
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    ### 함수부
    # 배트를 위로 움직이는 함수
    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed # y_speed의 값 만큼 y_posn값을 뺌
        if(self.y_posn <= 0): # bat가 위 화면에 닿으면 더이상 올라가지않게 하는 코드
            self.y_posn = 0        
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn # 변경된 y_posn 값을 y1에 반영
        y2 = self.y_posn+self.height

        # 변경된 값으로 아이템을 옮김
        # Table 클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

         # 배트를 위로 움직이는 함수
    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed # y_speed의 값 만큼 y_posn값을 더하기
        if(self.y_posn >= 300): # bat가 위 화면에 닿으면 더이상 올라가지않게 하는 코드
            self.y_posn = 300        
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn # 변경된 y_posn 값을 y1에 반영
        y2 = self.y_posn+self.height

        # 변경된 값으로 아이템을 옮김
        # Table 클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    # 공과 배트의 충돌 감지 감지 및 처리 함수
    def detect_collision(self, ball):
        collistion_direction = "" #충돌 방향 저장
        collistion = False
        feel = 5

        # 배트 변수:
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_center = top + (self.height/2)
        h_center = left + (self.width/2)

        # 공 변수:
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2    # 반지름
        v_center_b = top_b + r      # 공의 탑에서 반지름을 더하면 세로 중간
        h_center_b = left_b + r     # 공의 오른쪽이 배트의 왼쪽보다 크고, 공읜 왼쪽이 배트의 오른쪽 보다 작을때 충돌

        # 공의 바닥(y)이 배트의 탑(y)보다 크고, 공의 탑(y)이 배트의 바닥(y)보다 작고.
        # 공의 오른쪽이 배트의 왼쪽보다 크고, 공의 완쪽이 배트의 오른쪽 보다 작을 때 충돌
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collistion = True
            print("충돌")

        #만약 충돌 했다면 어느 방햐응로 충돌했는지 collision_direction에 저장
        if(collistion): # 만약 collistion 이 True라면, 측 충돌 했자면
            # 공의 오른쪽 부분이 배트의 오른쪽 부분보다 크고, 공의 왼쪽 부분이 캐트의 오른쪽 보다 작다면, 배트의 동쪽에서 공이 충돌
            if(right_b > right) and (left_b <= right) and (top_b > top-r) and( bottom_b < bottom+r):
                collistion_direction ="E"
                #abs()함수는 숫자의 부호를 제거하는 함수, 속도 값을 얻는데 사용
                #abs()함수는 공이 배트의 어느 부분에 충돌 했는지에 따라 공의 방향 변경
                ball.x_speed = abs(ball.x_speed) # 공이 양수의 값, 즉 오른쪽으로 이동

                # 공의 중심이 배트의 중심에서 얼마나 먼 거리에서 충돌이 발생했는지 계산하여 y 좌표값에 적용
                # 공의 중심이 배트의 중심보다 y 좌표값이 적은 위치(높은 위치)에서 부딛칠 경우 adjustment는 -값 공은 사선 위로 
                # 공의 중심이 배트의 중심보다 y 좌표값이 큰 위치(낮은 위치)에서 부딛칠 경우 adjustment는 +값 공은 사선 아래로 
                
                adjustment = (-(v_center - v_center_b))/(self.height/2)
                print(adjustment)
                ball.y_speed = feel * adjustment

            #공의 왼족 부분이 배트의 왼쪽 부분보다 작고, 공의 오른쪽 부분이 배트의 왼쪽 보다 크다면 배트의 서쪽에서 공이 충돌
            elif(left_b < left) and (right_b >= left) and (top_b > top-r) and( bottom_b < bottom+r):
                collistion_direction ="W"
                ball.x_speed = -abs(ball.x_speed)
                adjustment = (-(v_center - v_center_b))/(self.height/2)
                print(adjustment)
                ball.y_speed = feel * adjustment

            return (collistion, collistion_direction)
    
    # 배트의 초기 위치값 지정
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

#### game_flow() 함수부
def game_flow():

    global first_serve
    global score_left
    global score_right
    # 공을 일정 시간마다 움직임
    my_ball.move_next()
    window.after(20, game_flow)  # 30밀리초마다 game_flow 함수 실행 , ex 5초는 500
    
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
        if(score_left >= 50):
            score_left = "W"
            score_right = "L"
        first_serve = True
        my_table.draw_score(score_left, score_right)
        
        my_ball.start_ball(x_speed=random.randrange(10,20), y_speed=random.randrange(100,200))

    # 공의 X 좌표값이 width 보다 클 경우 오른쪽 벽에 충돌한 상황
    if(my_ball.x_posn + my_ball.width >= my_table.width):
        my_ball.stop_ball() # 공을 멈춤, x_speed, y_speed를 0으로 설정
        my_ball.start_position() # 공의 위치 초기화
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 0, 150, 25 ,250)
        my_table.move_item(bat_R.rectangle, 575, 150, 600, 250)
        
        score_right = score_right + 1
        if(score_right >= 50):
            score_right = "W"
            score_left = "L"
        first_serve = True
        my_table.draw_score(score_left, score_right)   
           
        my_ball.start_ball(x_speed=random.randrange(10,20), y_speed=random.randrange(100,200))

# restart_game 함수:
def restart_game(master):
    my_ball.start_ball(x_speed=random.randrange(10,20), y_speed=random.randrange(100,200))
  
###  Table 클래스를 사용해서 테이블 생성
my_table = Table(window, 600, 400, "black", "green")

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







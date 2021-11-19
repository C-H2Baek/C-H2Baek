from tkinter import *

##### 메인부
window=Tk()
window.title("MyPingPong")
'''
# 캔버스 생성
canvas=Canvas(window, width=600, height=400, bg="black")
canvas.pack()

# 캔버스 위에 선 생성
canvas.create_line(300, 0, 300, 400, width=2, fill="green", dash=(15, 23))

### 캔버스 위에 공 생성
canvas.create_oval(288, 188, 312, 212, fill="red")

### 캔버스 위에 배트 생성
canvas.create_rectangle(20, 150, 35, 250, fill="blue")
canvas.create_rectangle(565, 150, 580, 250, fill="yellow")
'''
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
        
    # 공의 변경된 위치 지정 및  이동
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)    

#### Bat 클래스 생성
class Bat:
    #### 생성자
    def __init__(self, table, width, height, x_posn, y_posn, color, x_speed = 23, y_speed = 23):
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

#### game_flow() 함수부
def game_flow():
    # 공을 일정 시간마다 움직임
    my_ball.move_next()
    window.after(30, game_flow)  # 30밀리초마다 game_flow 함수 실행 , ex 5초는 500
    

###  Table 클래스를 사용해서 테이블 생성
my_table = Table(window, 600, 400, "black", "green")

### 공 생성
# Ball(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn)
my_ball = Ball(table=my_table, x_speed=5, y_speed=0, width=24, height=24, color="red", x_posn=((600-24)/2), y_posn=((400-24)/2))


### 배트 생성
# Bat 클래스로부터 배트를 주문
# Bat(self, table, width, height, x_posn, y_posn, color, x_speed = 25, y_speed = 25)
bat_L = Bat(table=my_table, width=24, height=100, color="green", x_posn=0, y_posn=150)
bat_R = Bat(table=my_table, width=24, height=100, color="blue", x_posn=576, y_posn=150)

#### 함수의 실행부
game_flow()


###  배트를 제어하기 위한 키이벤트 및 연결될 함수 지정
# window.bind("<키명>",  함수명)
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

window.mainloop()









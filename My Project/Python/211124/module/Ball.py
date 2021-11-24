import random

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
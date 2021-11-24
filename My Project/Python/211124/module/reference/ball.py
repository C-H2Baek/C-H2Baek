import random

class Ball: #ball 클래스 선언

    def __init__(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn):
        self.width=width #가로
        self.height=height #세로
        self.x_posn=x_posn #x좌표
        self.y_posn=y_posn #y좌표
        self.color=color #컬러
        
        self.x_start=x_posn #시작위치
        self.y_start=y_posn #시작위치

        self.x_speed=x_speed #움직이는 속도(얼만큼 움직이는지)
        self.y_speed=y_speed
        
        self.table=table
        self.circle=self.table.draw_oval(self)
        
    def move_next(self): #공 움직이기 함수
        self.x_posn+=self.x_speed
        self.y_posn+=self.y_speed
        
        if(self.y_posn<=0):
            self.y_posn=0;
            self.y_speed=-self.y_speed;
        elif(self.y_posn>=(self.table.height-self.height)):
            self.y_posn=(self.table.height-self.height)
            self.y_speed=-self.y_speed;
        
        #공의 변경된 위치 지정 및 이동
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.circle,x1,y1,x2,y2)
        
        
    
    def start_ball(self,x_speed,y_speed): #전역변수 값을 불러와서 + or -
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if random.randint(0,1) else y_speed
        self.start_position()
        
    def start_position(self): #공 위치 초기화
        self.x_posn=self.x_start
        self.y_posn=self.y_start
        
    def stop_ball(self): #공 멈추기 (speed =0 ) 함수
        self.x_speed=0
        self.y_speed=0
                           

class Bat:
    def __init__(self,table,width,height,x_posn,y_posn,color,y_speed,x_speed):
        self.width=width
        self.height=height
        self.x_posn=x_posn
        self.y_posn=y_posn
        self.color=color
        
        self.x_start=x_posn
        self.y_start=y_posn
        self.y_speed=y_speed
        self.x_speed=x_speed
        
        self.table=table
        self.rect=self.table.draw_rect(self)
    
    def move_up(self,event): #bat를 up
        self.y_posn-=self.y_speed #y_speed만큼 y_posn에서 뺌
        if(self.y_posn<=0):
            self.y_posn=0
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.rect,x1,y1,x2,y2)
        
    def move_down(self,event): #bat를 dowun
        self.y_posn+=self.y_speed #y_speed만큼 y_posn에서 더함
        maxHeight=self.table.height-self.height
        if(self.y_posn>=maxHeight):
            self.y_posn=maxHeight
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.rect,x1,y1,x2,y2)
    
    def move_left(self,event):
        self.x_posn-=self.x_speed #y_speed만큼 y_posn에서 뺌
        if(self.x_posn<=0):
            self.x_posn=0
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.rect,x1,y1,x2,y2)
        
    def move_right(self,event):
        self.x_posn+=self.x_speed #y_speed만큼 y_posn에서 뺌
        maxWidth=self.table.width-self.width
        if(self.x_posn>=maxWidth):
            self.x_posn=maxWidth
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.rect,x1,y1,x2,y2)
        
    def start_position(self): #배트 위치 초기화
        self.x_posn=self.x_start
        self.y_posn=self.y_start
        
    def detect_collision(self,ball): #충돌처리 함수
        collision_direction='' #충돌방향
        collision=False #충돌하면 true
        fell=5 #각도
        
        top=self.y_posn
        bottom=self.y_posn+self.height
        left=self.x_posn
        right=self.x_posn+self.width
        v_center=top + (self.height/2) # 배트의 탑에서 배트높이/2 세로중간
        h_center=bottom + (self.width/2)
        
        top_b=ball.y_posn
        bottom_b=ball.y_posn+ball.height
        left_b=ball.x_posn
        right_b=ball.x_posn+ball.width
        r=(right_b-left_b)/2 #반지름
        v_center_b=top_b + r # 공 탑+반지름 세로중간
        h_center_b=left_b + r #공 왼쪽+반지름 가로
        
        #공의 바닥이 배트의 탑보다 크고, 공의 탑이 배트의 바닥보다 작고,
        #공의 오른쪽이 배트의 왼쪽보다 크고, 공의 왼쪽이 배트의 오른쪽보다 작을때 충돌
        if((bottom_b>top) and (top_b<bottom) and (right_b>left) and (left_b<right)):
            collision=True
        
        if(collision): #collision값이 true일때(충돌 했을떄)
            #공의 오른쪽 > 배트 오른쪽, 공의 왼쪽>배트의 오른쪽 = 동쪽에서 충돌
            if( (right_b>right) and (left_b<=right) and (top_b>top-r) and (bottom_b<bottom+r) ) :
                collision_direction="E"
                ball.x_speed=abs(ball.x_speed) #동쪽에서 충돌한 경우 오른쪽으로(x_speed를 양수로)
                
                adj=(-(v_center - v_center_b)) / (self.height/2) #공의 중심이 배트의 중심에서 얼마나 먼 거리에서 충돌했는 계산, y_speed에 적용
                ball.y_speed=fell*adj
                
            elif( (left_b<left) and (right_b>=left) and (top_b>top-r) and (bottom_b<bottom+r) ) :
                collision_direction="W"
                ball.x_speed=-abs(ball.x_speed) 
                
                adj=(-(v_center - v_center_b)) / (self.height/2)
                ball.y_speed=fell*adj
                
            return(collision,collision_direction)
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
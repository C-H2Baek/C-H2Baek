from tkinter import *

#### Table 클래스 생성
class Table :
    ### 생성자
    def __init__(self, window, width, height, img) :
        self.width=width
        self.height=height
        self.canvas=Canvas(window,width=self.width,height=self.height)
        self.canvas.create_image(self.width/2,self.height/2,image=img)
        self.canvas.pack()
        self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, dash=(15, 23), fill="white")

        # 득점판 추가:
        font = ("Algerian" , 72)
        self.scoreboard = self.canvas.create_text(300, 65, font=font, fill = "white")
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
        scores = str(right) + "   " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores) 
from tkinter import *

window=Tk()
window.title("A Dance of Fire and Ice")

class radius :
    None
class Table :
    def __init__(self, window, width, height, bg_color, net_color) :
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.net_color=net_color

        # Table 클래스 내에서 캔버스 생성
        self.canvas=Canvas(window, width=self.width, height=self.height, bg=self.bg_color)
        self.canvas.pack()

    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)

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

Field = Table(window, 800, 600, "black", "green")
RED_Ball = Ball(table=Field, x_speed=0, y_speed=0, width=50, height=50, color="red", x_posn=(800/2), y_posn=(600/2))
BLUE_Ball = Ball(table=Field, x_speed=0, y_speed=0, width=50, height=50, color="blue", x_posn=(800/2), y_posn=(600/2-100))

window.mainloop()
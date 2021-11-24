from tkinter import*
from config import*

class Table: #table 클래스 선언
    global  score_right, score_left,bg
    
    def __init__(self,window,width,height,img):            
        self.width=width
        self.height=height
        self.canvas=Canvas(window,width=self.width,height=self.height)
        self.canvas.create_image(self.width/2,self.height/2,image=img)
        self.canvas.pack()

        #Table 생성자에서 득점판 초기화
        font=("Courier 8",40)
        self.scoreboard = self.canvas.create_text(self.width/2,65,font=font,fill="purple",text=str(score_left)+" "+str(score_right))
        #Table 생성자에서 세트 득점판 초기화
        setFont=("Courier 8",20)                                    
        self.setScoreBoard = self.canvas.create_text(self.width/2,15,font=setFont,fill="white",text=str(setScore_left)+" <set> "+str(setScore_right))
        
    def draw_oval(self, oval): #ball의 데이터로 table에 그리기 함수
        x1=oval.x_posn
        x2=oval.x_posn+oval.width
        y1=oval.y_posn
        y2=oval.y_posn+oval.height
        c=oval.color
        return self.canvas.create_oval(x1,y1,x2,y2,fill=c)
    
    def draw_rect(self,rect): #bat의 데이터로 table에 그리기 함수
        x1=rect.x_posn
        x2=rect.x_posn+rect.width
        y1=rect.y_posn
        y2=rect.y_posn+rect.height
        c=rect.color
        return self.canvas.create_rectangle(x1,y1,x2,y2,fill=c)
    
    def move_item(self,item,x1,y1,x2,y2): #table내의 item위치 변경 함수
        self.canvas.coords(item,x1,y1,x2,y2)
        
    def draw_score(self,left,right): #스코어
        score=str(left)+" "+str(right)
        self.canvas.itemconfigure(self.scoreboard,text=score)
        
    def draw_setScore(self,left,right): #세트 스코어
        setScore=str(left)+" <set> "+str(right)
        self.canvas.itemconfigure(self.setScoreBoard,text=setScore)
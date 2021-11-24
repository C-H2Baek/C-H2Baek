from tkinter import*
from bat import*
from ball import*
from table import*
from config import* # 전역 변수 모듈 임포트

def game_flow():
    global  score_right, score_left, setScore_left, setScore_right,setScore
    my_ball.move_next() #공 움직이기 함수
    window.after(18,game_flow) #30ms마다 함수 재귀 호출
    
    l_bat.detect_collision(my_ball)
    r_bat.detect_collision(my_ball)
    
    if (my_ball.x_posn<=0) or (my_ball.x_posn+my_ball.width >= my_table.width) : #벽에 부딫힘    
        if my_ball.x_posn<=0: #오른쪽에 부딫혔을때
            score_right+=1
            winCheckRight="W"
            winCheckLeft="L"
            my_table.draw_score(winCheckLeft,winCheckRight)
            if(score_right==3): #3점이면 세트 스코어 ++
                setScore+=1
                score_right=0
                winCheckRight="Player-R"
                winCheckLeft=str(setScore)+" Set Win"                
                my_table.draw_score(winCheckLeft,winCheckRight)
                setScore_right+=1
                my_table.draw_setScore(setScore_left,setScore_right)
                if(setScore_right==3): #세트스코어 3점이면 최종 우승
                    setScore=0
                    setScore_left=setScore_right=0
                    winCheckRight="WINNER*"
                    winCheckLeft="*Player-R"                
                    my_table.draw_score(winCheckLeft,winCheckRight)
                    my_table.draw_setScore(setScore_left,setScore_right)   
                      
        elif my_ball.x_posn+my_ball.width >= my_table.width:
            score_left+=1
            winCheckRight="L"
            winCheckLeft="W"
            my_table.draw_score(winCheckLeft,winCheckRight)
            if(score_left==3): #3점이면 세트 스코어 ++
                setScore+=1
                score_left=0
                winCheckRight="Player-L"
                winCheckLeft=str(setScore)+" Set Win"                
                my_table.draw_score(winCheckLeft,winCheckRight)
                setScore_left+=1
                my_table.draw_setScore(setScore_left,setScore_right)
                if(setScore_left==3): #세트스코어 3점이면 최종 우승
                    setScore=0
                    setScore_left=setScore_right=0
                    winCheckRight="WINNER*" 
                    winCheckLeft="*Player-L"               
                    my_table.draw_score(winCheckLeft,winCheckRight)
                    my_table.draw_setScore(setScore_left,setScore_right)     
        
        my_ball.stop_ball() #공 멈춤
        my_ball.start_position() #공 위치 초기화
        l_bat.start_position()
        r_bat.start_position()
        my_table.move_item(r_bat.rect, 575, 150, 590, 250)
        my_table.move_item(l_bat.rect, 20, 150, 35, 250)
                
                    
def restart_game(event):
    my_ball.start_ball(x_speed,y_speed)
    l_bat.start_position()
    r_bat.start_position()
    my_table.move_item(r_bat.rect, 575, 150, 590, 250)
    my_table.move_item(l_bat.rect, 20, 150, 35, 250)
    my_table.draw_score(score_left,score_right)
    
 
window=Tk();
window.title("PingPong")


bg=PhotoImage(file="png/table.png")
my_table=Table(window,600,400,bg)#Table클래스의 인스턴스 생성
my_ball=Ball(my_table,24,24,"red",0,0,288,188) #Ball클래스의 인스턴스 생성
l_bat=Bat(my_table,15,100,20,150,"green",30,30) #Bat클래스의 왼쪽 배트 인스턴스 생성
r_bat=Bat(my_table,15,100,575,150,"blue",30,30) #Bat클래스의 오른쪽 배트 인스턴스 생성

window.bind("w",l_bat.move_up)
window.bind("s",l_bat.move_down)
window.bind("a",l_bat.move_left)
window.bind("d",l_bat.move_right)
window.bind("<Up>",r_bat.move_up)
window.bind("<Down>",r_bat.move_down)
window.bind("<Left>",r_bat.move_left)
window.bind("<Right>",r_bat.move_right)
window.bind("<space>",restart_game)

game_flow()

window.mainloop()
# tkinter는 파이썬에서 GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
from tkinter import *

# Tk( )는 기본이 되는 윈도우를 반환, 루트 윈도우(Root Window) 또는 베이스 윈도우(Base Window)라고 함

window=Tk()

window.title("Window Practice")

window.geometry("1000x1600")

#윈도우 창의 크기 변경 가능 여부 설정, TRUE/FALSE or 1/0
window.resizable(width=1 , height=1)

#라벨은 문자를 표현할 수 있는 위젯
#위젯은 생성하고 디스플레이 하는 2STEP

label1=Label(window, text="SWEET~~ Phtyon" , font=("Matura MT Script Capitals",15))
label2=Label(window, text="hardly", font=("Matura MT Script Capitals", 30), fg="blue")
label3=Label(window, text="Studying" , font=("Matura MT Script Capitals",15) ,bg ="teal", width=20, height=5, anchor=SW)

label1.pack()
label2.pack()
label3.pack()

button1= Button(window,text="파이썬 종료",fg="red", command=quit)
button1.pack()

photo1=PhotoImage(file="Images\gif\Lion.gif")
image1=Label(window, image=photo1)
image2=Label(window, image=photo1)
image3=Label(window, image=photo1)
image1.pack()
image2.pack()
image3.pack()

# 화면을 구성하고 처리
# 윈도우 창에 키보드 누르기. 마우스 클릭 등
window.mainloop()

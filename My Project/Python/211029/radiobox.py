from tkinter import *


window=Tk()
window.geometry("200x200")

#함수 정의 부분
#위젯명.configure(옵션=값)은 해당 위젯의 옵션 값을 변경하는 함수
#var 변수의 값에 따라 윈도우 하단 라벨의 텍스트를 변경
def RadioB() :
    if var.get()==1:
        label1.configure(text="파이썬")
    elif var.get()==2:
        label1.configure(text="C++")
    else :
        label1.configure(text="Java")

#메인 코드 부분
#IntVar()는 정수형 형식의 변수를 생성하는 함수
var=IntVar()
rb1=Radiobutton(window, text="파이썬", variable=var, value=1, command=RadioB)
rb2=Radiobutton(window, text="C++", variable=var, value=2 ,command=RadioB)
rb3=Radiobutton(window, text="Java", variable=var, value=3 ,command=RadioB)

label1=Label(window, text="선택한 언어 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()


button1= Button(window,text="파이썬 종료",fg="red", command=quit)
button1.pack()

window.mainloop()
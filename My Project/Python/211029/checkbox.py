from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Window Practice")
#window.geometry("800x800")


#함수 정의 부분
def CheckB() :
    if chk.get()==0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

#메인 코드 부분
chk=IntVar()
cb1=Checkbutton(window, text="클릭하세요", variable=chk, command=CheckB)

cb1.pack()


button1= Button(window,text="파이썬 종료",fg="red", command=quit)
button1.pack()

window.mainloop()
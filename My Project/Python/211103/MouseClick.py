from tkinter import *
from tkinter import messagebox

# 함수 정의 부분
def clickLeft(event) :
    messagebox.showinfo("마우스" , "마우스 왼쪽 버튼이 클릭됨")
def clickRight(event) :
    messagebox.showinfo("마우스" , "마우스 오른쪽 버튼이 클릭됨")
def clickImage(event) :
    messagebox.showinfo("마우스" , "사진에서 마우스가 클릭됨")    

# 메인 코드 부분
window=Tk()
window.geometry("500x500")

photo = PhotoImage(file="Images\gif\cat2.gif")
label1= Label(window, image=photo)

label1.bind("<Button>", clickImage)

window.bind("<Button-1>", clickLeft)
window.bind("<Button-3>", clickRight)

label1.pack( expand=1 , anchor = CENTER)
window.mainloop()
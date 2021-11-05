from tkinter import *
from time import *

# 변수 선언 부분
fnameList=["jeju1.gif"]
#fnameList=[""]
#photoList=[None] * 9
num=0

for i in range(1,9):
    fnameList.append("/jeju" + str(i+1)  + ".gif")

# 함수 선언 부분
def clickNext() :
    global num
    num +=1
    if num > 8 :
        num = 0
    photo = PhotoImage(file="Images/gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

def clickPrev() :
    global num 
    num -=1
    if num < 0 :
        num = 8
    photo = PhotoImage(file="Images/gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

def pageUp(event) :
    clickNext()

def pageDown(evevt) :
    clickPrev()

# 메인 코드 부분
window=Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

window.bind("<Prior>", pageUp)
window.bind("<Next>",pageDown)

btnPrev=Button(window, text="<< Prev", command = clickPrev)
btnNext=Button(window, text="Next >>" , command = clickNext)

photo=PhotoImage(file="Images/gif/"+fnameList[0])
pLabel=Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15 , y=50)

window.mainloop()
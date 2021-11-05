from tkinter import *
from time import *

# 변수 선언 부분
fnameList=["a1.png"]

num=0

for i in range(1,9):
    fnameList.append("a" + str(i+1)  + ".png")

# 함수 선언 부분
def clickNext() :
    global num
    num +=1
    if num > 8 :
        num = 0
    photo = PhotoImage(file="Images/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    TextFile.configure(text=fnameList[num])
    
def clickPrev() :
    global num 
    num -=1
    if num < 0 :
        num = 8
    photo = PhotoImage(file="Images/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    TextFile.configure(text=fnameList[num])

def pageUp(event) :
    clickNext()

def pageDown(evevt) :
    clickPrev()

# 메인 코드 부분
window=Tk()
window.geometry("850x600")
window.title("사진 앨범 보기")

window.bind("<Prior>", pageUp)
window.bind("<Next>",pageDown)

backimg = PhotoImage(file="Images/back3.png")
labelImage = Label(window,image=backimg)
labelImage.place(x=-2, y=-2)

button9=PhotoImage(file="Images/clo9.png")
button3=PhotoImage(file="Images/clo3.png")
btnPrev=Button(window, image=button9, relief="flat", command = clickPrev)
btnNext=Button(window, image=button3, relief="flat", command = clickNext)

print(fnameList)
TextFile=Label(window, text=fnameList[num], font="Castellar")

photo=PhotoImage(file="Images/"+fnameList[0])

pLabel=Label(window, image=photo)

btnPrev.place(width=30, height=35, x=35, y=20)
TextFile.place(x=415, y=20)
btnNext.place(width=30, height=35, x=70, y=20)
pLabel.place(x=35, y=100)

window.mainloop()

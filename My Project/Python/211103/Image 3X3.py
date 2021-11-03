from tkinter import *

window=Tk()
window.geometry("210x210")

# 변수 선언 부분
btnList=[None] * 9
photoList=[None] * 9

xPos, yPos = 0 , 0
i = 0

for y in range(0,3) :
    for x in range(0,3) :
        photoList[i]=PhotoImage(file="Images\gif\puz"+str(i+1) + ".gif" )
        btnList[i]=Button(window, image=photoList[i])
        btnList[i].place(x=xPos, y=yPos)
        i+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()
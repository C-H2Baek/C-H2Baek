from tkinter import *
window = Tk()
window.geometry("")
window.title("Buttons")
'''
button1 = Button(window, text="버튼")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
'''

#반복문과 리스트를 활용하여 소스코드 수정하기
'''
button = [None]*12
xPos, yPos =0,0
i=0

for y in range(3) :
    for x in range(4) :
        button[i] = Button(window ,text="버튼"+str(i+1))
        button[i].place(x=xPos, y=yPos)
        xPos+=50
        i+=1
    xPos=0
    yPos+=30    

window.mainloop()
'''
#버튼을 이미지로 표현하기
imagefile = [None] *10
imagelable = [None] *10

for i in range(1,10,1):
    imagefile[i] = PhotoImage(file="Images\gif\puz"+str(i)  + ".gif")
    imagelable[i] = Label(window, image=imagefile[i])
    imagelable[i].pack(side=LEFT)








window.mainloop()
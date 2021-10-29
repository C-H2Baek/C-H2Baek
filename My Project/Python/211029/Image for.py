from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Window Practice")
#window.geometry("800x800")

label1=Label(window, text="IMAGE ALBUM" , font=("Matura MT Script Capitals",15))
label1.pack()



'''''''''
    filename1= PhotoImage(file = "Images\gif\Lion.gif")
    imagelable1 = Label(window, image=filename1)
    imagelable1.pack(side=LEFT)

    filename2 = PhotoImage(file = "Images\gif\Lion.gif")
    imagelable2 = Label(window, image=filename2)
    imagelable2.pack(side=LEFT)

    filename3 = PhotoImage(file = "Images\gif\Lion.gif")
    imagelable3 = Label(window, image=filename3)
    imagelable3.pack(side=LEFT)
    '''''''''

filename = [None] *10
imagelable = [None] *10

for i in range(1,10,1):
    filename[i] = PhotoImage(file="Images\gif\puz"+str(i)  + ".gif")
    imagelable[i] = Label(window, image=filename[i])
    imagelable[i].pack(side=LEFT)

#함수 정의 부분
def myFunc() :
    if chk.get()==0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

#메인 코드 부분
chk=IntVar()
cb1=Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)

cb1.pack()


button1= Button(window,text="파이썬 종료",fg="red", command=quit)
button1.pack()

window.mainloop()
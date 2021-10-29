from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Window Practice")
#window.geometry("800x800")

#배경이미지 표시
BackG = PhotoImage(file="Images/gif/jeju5.gif")
BackImage = Label(window,image=BackG)
BackImage.place(x=-2, y=-2)

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
'''
filename = [None] *10
imagelable = [None] *10

for i in range(1,10,1):
    filename[i] = PhotoImage(file="Images\gif\puz"+str(i)  + ".gif")
    imagelable[i] = Label(window, image=filename[i])
    imagelable[i].pack(side=LEFT)

#함수 정의 부분
def CheckB() :
    if chk.get()==0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

def RadioB() :
    if var.get()==1:
        label1.configure(text="파이썬")
    elif var.get()==2:
        label1.configure(text="C++")
    else :
        label1.configure(text="Java")
'''

def VoteA() :
    if ani.get()==1 :
        VoteImage.configure(image=photo1)
        label.configure(text="dog")
     
    elif ani.get()==2 :
        VoteImage.configure(image=photo2)
        label.configure(text="cat")
    else :
        VoteImage.configure(image=photo3)
        label.configure(text="other")    


#메인 코드 부분
'''
chk=IntVar()
cb1=Checkbutton(window, text="클릭하세요", variable=chk, command=CheckB)
cb1.pack()

var=IntVar()
rb1=Radiobutton(window, text="파이썬", variable=var, value=1, command=RadioB)
rb2=Radiobutton(window, text="C++", variable=var, value=2 ,command=RadioB)
rb3=Radiobutton(window, text="Java", variable=var, value=3 ,command=RadioB)

label1=Label(window, text="선택한 언어 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()
'''
#이곳
ani=IntVar()
VoteText=Label(window, text="좋아하는 동물 투표" ,fg="blue", font=("궁서체",20))
rb6=Radiobutton(window, text="Dog", variable=ani, value=1, command=VoteA)
rb7=Radiobutton(window, text="Cat", variable=ani, value=2, command=VoteA)
rb8=Radiobutton(window, text="Rabbit", variable=ani, value=3, command=VoteA)
rb9=Button(window, text="Show Animal", command=VoteA)

photos=PhotoImage(file="Images\gif\jeju3.gif")
photo1=PhotoImage(file="Images\gif\dog3.gif")
photo2=PhotoImage(file="Images\gif\cat2.gif")
photo3=PhotoImage(file="Images\gif\dog4.gif")

VoteImage=Label(window, width=300, height=300 ,text="",  bg="white", image=photos)

VoteText.pack(padx=5, pady=5)
rb6.pack(padx=5, pady=5)
rb7.pack(padx=5, pady=5)
rb8.pack(padx=5, pady=5)
rb9.pack(padx=5, pady=5)
VoteImage.pack(padx=5, pady=5)

label = Label(window, text="어떤 동물을 좋아하니?")
label.pack()

button1= Button(window,text="파이썬 종료",fg="red", command=quit)
button1.pack()

window.mainloop()
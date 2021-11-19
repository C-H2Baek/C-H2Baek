from tkinter import *

window=Tk()
window.title("MyPingPong")

# 캔버스 생성
canvas=Canvas(window, width=600, height=400, bg="black")
canvas.pack()

# 캔버스 위에 선생성
canvas.create_line(300 , 0 , 300 , 400 , width=2, fill="green" , dash=(15,23))

# 캔버스 위에 공 생성
canvas.create_oval(288 , 188 , 312 , 212 , fill="red")

# 캔버스 위에 배트 생성
canvas.create_rectangle(20, 150, 35, 250, fill="blue")
canvas.create_rectangle(565, 150, 580, 250, fill="yellow")

window.mainloop()
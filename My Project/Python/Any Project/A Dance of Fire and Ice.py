from tkinter import *
import time

def exit():
    global STOP
    STOP=1

# Make a Canvas
boundx, boundy=400,300
root=Tk()
root.protocol("WM_DELETE_WINDOW", exit)
canvas=Canvas(root, width=boundx, height=boundy)
canvas.pack()
wall=PhotoImage(file='main_img.jpg')
canvas.create_image(0,0,image=wall, anchor=NW)
canvas.create_text(350,265,text='ball.py\n'  'lexlove')
canvas.create_rectangle(315,280,400,282)

# Make a ball
x, y=boundx/2, boundy/2
dx, dy=5,5
size=10
ball= canvas.create_oval(x,y,x+size, y+size,fill='white')
   

# Make a sound
try:
    import tkSnack
    tkSnack.initializeSnack(root)
    sound=tkSnack.Sound()
    sound.read('Blip.wav')
except:
    def playsound(): pass
else:
    def playsound(): sound.play()

# Make the ball!
STOP=0
while not STOP:
    x += dx
    y += dy
    if (x<0) and (dx<0):
        dx= -dx
        x -= 2*x
        playsound()
    elif (x+size >boundx) and (dx>0):
        dx= -dx
        x -=2*(x+size - boundx)
        playsound()
   
    if (y<0) and (dy <0):
        dy= -dy
        y -=2*y
        playsound()
    elif (y+size > boundy) and (dy>0):
        dy = -dy
        y -= 2*(y+size - boundy)
        playsound()
    canvas.coords(ball, x, y, x+size, y+size)
    time.sleep(0.1)
    canvas.update()
else:
    root.destroy()
    root.quit()
# 미니 포토샵
# 포토샵과 같은 소프트웨어를 "영상처리(Image Processing) 프로그램" 이라 함
# 원칙적으로 영상처리에 대한 이론과 알고리즘을 익힌 후 미니 포토샵 프로그램을 작성하면 좋음
# 현실적으로 이론은 배제하고 화면에 구현되는 것 위주로 진행

# 주의 1. 이미지 파일명이나 저장괸 경로에 한글이 들어가면 안됨
# 주의 2. 이미지 크기는 가로와 세로가 동일해야 함
# 주의 3. 처리하는 속도가 다소 오래 걸림

# 사용할 라이브러리 또는 모듈을 임포트
from ctypes import pointer
from os import access
from tkinter import *
# 파일 입출력을 위한 모듈
from tkinter.filedialog import *
from tkinter.font import BOLD
# 숫자나 문자를 입력 받기 위한 모듈
from tkinter.simpledialog import *
# 설치한 이미지 처리 기능을 제공하는 이미지매직의 라이브러리 임포트
# GIF 뿐 아니라 JPG, PNG 같은 이미지를 모두 처리하기 위해 외부 라이브러리 이미지 매직 사용
from wand.image import *

import pyautogui

# 모든 함수들이 공통적으로 사용할 전역 변수 선언부 
window, canvas, paper = None, None, None
photo, photo2 = None, None              # photo 원본, photo2 사본
oriX, oriY, newX, newY = 0 , 0 , 0 , 0         # 원본 이미지의 폭과 높이를 저장하는 함수
readFp = None

# 함수 정의부, 각 메뉴를 선택할 때 실행 될 함수 선언
# displayImage(이미지, 가로사이즈, 세로사이즈) : 이미지를 화면에 출력하는 함수
def displayImage(img, width, height) :
    global window, canvas, canvas2, paper, photo, photo2, oriX, oriY, newX, newY
    #window.geometry(str(width)+"x"+str(height))
    if canvas !=None :
        canvas.destroy()

    # 새 캔버스 생성. 처리된 이미지의 가로 세로 사이즈대로 생성
    # 캔버스의 흰색 테두리 없애기 bd=0, highlightthickness=0
    #canvas=Canvas(window, width=width, height=height, bg='#626262' , bd=0 , highlightthickness=0)
    canvas=Canvas(window, width=840, height=793, bg='#333333' , bd=0 , highlightthickness=0)
    canvas2=Canvas(window, width=118, height=118, bg='#333333' , bd=0 , highlightthickness=0)
    # 새 캔버스에 붙일 종이(paper) 생성, 처리돤 이미지의 가로 세로 사이즈대로 생성
    paper=PhotoImage(width=width, height=height)
    #paper2=PhotoImage(width=width, height=height)
    
    # 새 캔버스에 종이(paper)를 붙임 (차후 그 종이 위에 처리된 이미지를 출력)
    # 생성될 페이퍼의 위치는 캔버스의 가로 세로 사이즈의 중간 위치
    canvas.create_image((840/2, 793/2), image=paper, state="normal")
    canvas2.create_image((118/2, 118/2), image=paper, state="normal")
    #canvas.place((width/2, height/2), image=paper, state="normal")

    # 새 캔버스와 새 종이 위에 처리된 이미지를 출력
    # maake_blob(format=None) 는 이미지를 바이너리 코드로 변환해 주는 함수, 배열의 형태로 저장
    # 흰 종이에 사진을 출력하기 위해 이미지 파일의 모든 점(픽셀)에 접근
    # 이미지의 픽셀 하나하나에 접근하여 rgb 값을 각각 배열의 형태로 저장 [blob[0]r,blob[0]g,blog[0]b,blod[1]r,blob[1]g,blob[1]b...
    '''
    blob = img.make_blob(format = 'RGB')
        
    for i in range(0, width) :
        for k in range(0, height) :
            r = blob[(i * 3 * width) + (k * 3) + 0]     # blob[0], blob[3], blob[6], blob[9]...의 값을 r에 저장
            g = blob[(i * 3 * width) + (k * 3) + 1]     # blob[1], blob[4], blob[7], blob[10]...의 값을 g에 저장
            b = blob[(i * 3 * width) + (k * 3) + 2]     # blob[2], blob[5], blob[8], blob[11]...의 값을 b에 저장
            # paper에 칼라로 점을 찍어줌, 세로로 높이만큼 찍고 가로를 너비만큼 반복
            paper.put("#%02x%02x%02x" % (r,g,b) , (k,i))
    '''
    # for 문으로 하나의 좌표씩 표현하는 방식 시간 다소 걸림 아래문으로 대체
    paper.put(photo2.make_blob(format="png"))
    #paper2.put(photo2.make_blob(format="png"))
    canvas.place(x=73, y=45)            
    canvas2.place(x=951, y=87)            

def func_clear() :
    if photo2 == None :
        return
    canvas.destroy()
    canvas2.destroy()

    TextFile=Label(window, text="Cleared\t\t\t\t" , font=BOLD ,fg='white' , bg='#292c31')
    TextFile.place(x=630, y=11)

    fileMenu.entryconfigure("Clear File", state=DISABLED)
    fileMenu.entryconfigure("Save File", state=DISABLED)
    fileMenu.entryconfigure("Reset File", state=DISABLED)

    imageMenu1.entryconfigure("Zoom", state=DISABLED)
    imageMenu1.entryconfigure("Vertical Inverse", state=DISABLED)
    imageMenu1.entryconfigure("Horizontal Inverse", state=DISABLED)
    imageMenu1.entryconfigure("Rotate", state=DISABLED)
    imageMenu2.entryconfigure("Color Adjustment", state=DISABLED)
    imageMenu2.entryconfigure("Brightness", state=DISABLED)
    imageMenu2.entryconfigure("Sharpness", state=DISABLED)
    imageMenu2.entryconfigure("Blur", state=DISABLED)
    imageMenu2.entryconfigure("Gray Scale", state=DISABLED)

    Xpoint=Label(window, text='0\t\t', font=BOLD ,fg='white' , bg='#292c31')
    Xpoint.place(x=1125, y=90)
    Ypoint=Label(window, text='0\t\t', font=BOLD ,fg='white' , bg='#292c31')
    Ypoint.place(x=1125, y=110)

    Ximg=Label(window, text='0\t\t', font=BOLD ,fg='white' , bg='#292c31')
    Ximg.place(x=1125, y=135)
    Yimg=Label(window, text='0\t\t', font=BOLD ,fg='white' , bg='#292c31')
    Yimg.place(x=1125, y=155)

def func_open() :
    # 전역 변수 선언
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    readFp = askopenfilename(parent=window, filetypes=(("All Image Files", "*.jpg;*.jpeg;*.bmp;*.png;.*.tif;*.gif"),("All Files","*.*")))
    
    # 버튼 활성화
    imageMenu1.entryconfigure("Zoom", state=ACTIVE)
    imageMenu1.entryconfigure("Vertical Inverse", state=ACTIVE)
    imageMenu1.entryconfigure("Horizontal Inverse", state=ACTIVE)
    imageMenu1.entryconfigure("Rotate", state=ACTIVE)
    imageMenu2.entryconfigure("Color Adjustment", state=ACTIVE)
    imageMenu2.entryconfigure("Brightness", state=ACTIVE)
    imageMenu2.entryconfigure("Sharpness", state=ACTIVE)
    imageMenu2.entryconfigure("Blur", state=ACTIVE)
    imageMenu2.entryconfigure("Gray Scale", state=ACTIVE)

    fileMenu.entryconfigure("Clear File", state=ACTIVE)
    fileMenu.entryconfigure("Save File", state=ACTIVE)
    fileMenu.entryconfigure("Reset File", state=ACTIVE)

    # 파일 경로표시 라벨
    
    print(readFp)
    string=readFp
    p=string.split('/')
    s=len(p)

    TextFile=Label(window, text=p[s-1] , font=BOLD ,fg='white' , bg='#292c31')
    #TextFile.configure(text=readFp)
    TextFile.place(x=630, y=11)

    # photo는 처음 불러들인 원본 이미지
    photo = Image(filename=readFp)
    oriX = photo.width
    oriY = photo.height

    # photo2는 처리 결과를 저장 할 변수
    photo2 = photo.clone()      # 원본 이미지의 photo를 복사하여 photo2에 저장
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)        # 화면에 이미지를 출력하는 displayImage() 함수 호출 

    # 포인터 및 이미지 좌표 값 출력
    currentmouseX, currentmouseY = pyautogui.position()
    print("Current Mouse Pointer Location" , currentmouseX, currentmouseY)

    Xpoint=Label(window, text=currentmouseX, font=BOLD ,fg='white' , bg='#292c31')
    Xpoint.place(x=1125, y=90)
    Ypoint=Label(window, text=currentmouseY, font=BOLD ,fg='white' , bg='#292c31')
    Ypoint.place(x=1125, y=110)

    Ximg=Label(window, text=newX, font=BOLD ,fg='white' , bg='#292c31')
    Ximg.place(x=1125, y=135)
    Yimg=Label(window, text=newY, font=BOLD ,fg='white' , bg='#292c31')
    Yimg.place(x=1125, y=155)

def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY     # 전역 변수 선언
    # photo2는 func_open() 함수를 싱행하면 생성됨
    # 파일을 열지 않았다면 저장하기를 눌렀을 때 함수를 빠져나감
    if photo2 == None :
        return
    # 대화 상자로부터 넘겨받은 파일의 정보를 saveFp에 저장
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG File","*.jpg;*.jpeg"), ("All Files" , "*.*")))
    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)

#원본 이미지대로 되돌리는 함수
def func_reset():
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY     # 전역 변수 선언
    if photo2 == None :
        return
    photo2 = photo.clone()      # 원본 이미지의 photo를 복사하여 photo2에 저장
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)        # 화면에 이미지를 출력하는 displayImage() 함수 호출 

def func_exit() :
    window.quit()
    window.destroy()

# 확대, 확대할 배수를 입력받아 그 배수만큼 이미지의 크기를 확대함
def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2 == None :
        return
     # askinteger() 함수를 실행해 대화 상자로 확대할 배수 입력받음
    scale = float(askinteger("Expansion", "Magnified multiples(2~9)", minvalue=2, maxvalue=9))
    #photo2 = photo.clone()
    photo2.resize( int(oriX * scale) , int(oriY * scale) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

# 축소, 축소할 배수를 입력받아 그 배수만큼 이미지의 크기를 축소함
def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2 == None :
        return
     # askinteger() 함수를 실행해 대화 상자로 축소할 배수 입력받음    
    scale = float(askinteger("Shrink", "Shrink multiples(2~9)", minvalue=2, maxvalue=9))
    #photo2 = photo.clone()
    photo2.resize( int(oriX / scale) , int(oriY / scale) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_btn_zoom_in():
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2 == None :
        return
    
    photo2.resize( float(oriX * 2.1) , int(oriY * 2.1) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_btn_zoom_out():
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2 == None :
        return
    
    photo2.resize( float(oriX / 2.1) , int(oriY / 2.1) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

# 상하 반전, flip()
def func_rotate12():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2 == None :
        return
    #photo2 = photo.clone()
    photo2.flip()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY) # 화면에 이미지를 출력하는 displayImage() 함수 호출

# 좌우 반전, flop()
def func_rotate9():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2 == None :
        return
    #photo2 = photo.clone()
    photo2.flop()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY) # 화면에 이미지를 출력하는 displayImage() 함수 호출

def func_inverse():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2 == None :
        return
    degree = askinteger("Rotate", "Input the angle to rotate (0~360)", minvalue=0, maxvalue=360)
    #photo2 = photo.clone()
    photo2.rotate(degree)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 처리2 > 밝게 / 어둡게
# 대화창을 통해 정수를 입력받아 그 수만큼 이미지의 명도를 조정
# Wand 라이브러리에서 제공하는 modulate(명도값, 채도값, 색상값)함수를 사용
# 명도는 modulate(명도값, 100, 100)함수를 사용
# 원본의 명도값이 100 이므로 100 이상은 '밝게', 100 이하는 '어둡게' 처리
# 밝게, modulate(밝기값, 100, 100)함수에 100~200값 입력

def func_lighter():
    global window,canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    value = askinteger("Lighten", "Input the value (100~200)", minvalue=100, maxvalue=200)
    #photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY) 

def func_darker():
    global window,canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    value = askinteger("Darken", "Input the value(0~100)", minvalue=0, maxvalue=100)
    #photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_sharpness():
    global window,canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    value = askinteger("Sharpness", "Input the value(100~200)", minvalue=100, maxvalue=200)
    #photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_blur():
    global window,canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    value = askinteger("Blur", "input the value(0~100)", minvalue=0, maxvalue=100)
    #photo2 = photo.clone()
    photo2.filter()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_hue():
    global window,canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    value = askinteger("Hue", "input the value(0~200)", minvalue=0, maxvalue=200)
    #photo2 = photo.clone()
    photo2.modulate(100, 100, value)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_saturation():
    global window,canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    value = askinteger("Saturation", "input the value(0~200)", minvalue=0, maxvalue=200)
    #photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 처리2 > 흑백 이미지
# 이미지의 type 값을 "grayscale"로 설정
def func_grayscale():
    global window,canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    #photo2 = photo.clone()
    #photo2.modulate(100, 0, 100)
    photo2.type="grayscale"
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 메인 코드 부분
window=Tk()
window.geometry("1170x854")
window.title("미니 포토샵(ver 0.3)" )

# 배경 백그라운드
backimg = PhotoImage(file="Images/editor_background.png")
labelImage = Label(window,image=backimg)
labelImage.place(x=-2, y=-2)

# 메뉴 생성
# 1. 메뉴 자체 생성 및 화면에 디스플레이
# 메뉴자체이름=Menu(부모 윈도우)
# 부모 윈도우.config(menu=메뉴자체이름)
mainMenu = Menu(window)
window.config(menu=mainMenu)

# 2. 상위 메뉴 생성
# 상위메뉴이름 = Menu(메뉴자체이름)
# 메뉴자체이름.add_cascade(label="상위 메뉴 텍스트" , menu=상위메뉴이름) 
# add_cascade() 메소드는 메뉴자체와 상위 메뉴를 연결
fileMenu = Menu(mainMenu, tearoff=0)
imageMenu1 = Menu(mainMenu, tearoff=0)
imageMenu2 = Menu(mainMenu, tearoff=0)

mainMenu.add_cascade(label="File" , menu=fileMenu)
mainMenu.add_cascade(label="Image Process1" , menu=imageMenu1) 
mainMenu.add_cascade(label="Image Process2" , menu=imageMenu2)

'''
# 파일 이름 표시 오픈 함수로 이동
TextFile=Label(window, text=readFp, font=BOLD ,fg='white' , bg='#292c31')
TextFile.place(x=630, y=11)
'''

# 3. 하위 메뉴 생성
# 상위메뉴이름.add_command(label="하위 메뉴 이름" , command=함수명)
# add_command() 메소드는 하위 메뉴 항목 생성
fileMenu.add_command(label="Clear File", command=func_clear , state=DISABLED)
fileMenu.add_separator()
fileMenu.add_command(label="Open File", command=func_open)
fileMenu.add_command(label="Save File", command=func_save , state=DISABLED)
fileMenu.add_separator()
fileMenu.add_command(label="Reset File", command=func_reset, state=DISABLED)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=func_exit)

sub_zoom=Menu(imageMenu1, tearoff=0)
imageMenu1.add_cascade(label="Zoom", menu=sub_zoom, state=DISABLED)
sub_zoom.add_command(label="Zoom In", command=func_zoomin)
sub_zoom.add_command(label="Zoom Out", command=func_zoomout)

imageMenu1.add_separator()

imageMenu1.add_command(label="Vertical Inverse", command=func_rotate12, state=DISABLED)
imageMenu1.add_command(label="Horizontal Inverse", command=func_rotate9, state=DISABLED)
imageMenu1.add_command(label="Rotate", command=func_inverse, state=DISABLED)

sub_adjust=Menu(imageMenu2, tearoff=0)
imageMenu2.add_cascade(label="Color Adjustment", menu=sub_adjust, state=DISABLED)
sub_adjust.add_command(label="Hue", command=func_hue)
sub_adjust.add_command(label="Saturation", command=func_saturation)

sub_bright=Menu(imageMenu2, tearoff=0)
imageMenu2.add_cascade(label="Brightness", menu=sub_bright, state=DISABLED)
sub_bright.add_command(label="Lighten", command=func_lighter)
sub_bright.add_command(label="Darken", command=func_darker)

imageMenu2.add_separator()
imageMenu2.add_command(label="Sharpness", command=func_sharpness, state=DISABLED)
imageMenu2.add_command(label="Blur", command=func_blur, state=DISABLED)
imageMenu2.add_separator()

imageMenu2.add_command(label="Gray Scale", command=func_grayscale, state=DISABLED)

# 4.버튼 생성
btnClear=Button(window, relief="flat", command=func_clear, font=BOLD , bg='#292c31', fg='white' , text ="🏠" )
#btnClear.attributes('-alpha', 0.3)
btnClear.place(width=25, height=25, x=10, y=10)
btnClear.place(width=67, height=600, x=3, y=55)
btnzoomin=Button(window, relief="flat", command=func_btn_zoom_in())
btnzoomout=Button(window, relief="flat", command=func_btn_zoom_out())
btnzoomin.place(width=25, height=25, x=1000, y=250)
btnzoomout.place(width=25, height=25, x=900, y=250)




# 5. 마우스 포인터 좌표 표시

currentmouseX, currentmouseY = pyautogui.position()
print("Current Mouse Pointer Location" , currentmouseX, currentmouseY)

Xpoint=Label(window, text=currentmouseX, font=BOLD ,fg='white' , bg='#292c31')
Xpoint.place(x=1125, y=90)
Ypoint=Label(window, text=currentmouseY, font=BOLD ,fg='white' , bg='#292c31')
Ypoint.place(x=1125, y=110)

Ximg=Label(window, text=newX, font=BOLD ,fg='white' , bg='#292c31')
Ximg.place(x=1125, y=135)
Yimg=Label(window, text=newY, font=BOLD ,fg='white' , bg='#292c31')
Yimg.place(x=1125, y=155)


window.mainloop()

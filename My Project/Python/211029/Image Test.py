# 라벨, 라디오버튼, 버튼, 이미지 모두 활용

from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("애완동물 선택 하기")

# 배경이미지 표시
backimg = PhotoImage(file="Images/gif/jeju1.gif")
labelImage = Label(window,image=backimg)
labelImage.place(x=-2, y=-2)

# 함수 정의 부분

# var 변수의 값에 따라 윈도우 하단 라벨의 이미지를 변경
# 위젯명.configure(옵션=값)은 해당 위젯의 옵션 값을 변경해주는 함수
def  myFunc() :
    if var.get() == 1 :
        labelImage.configure(image=photo1)
        label.configure(text="강아지를 좋아하시네요.^^")
    elif var.get() == 2 :
        labelImage.configure(image=photo2)
        label.configure(text="고양이를 좋아하시네요.^^")
    else :
        labelImage.configure(image=photo3)
        label.configure(text="토끼를 좋아하시네요.^^")
    
# 메인 코드 부분
# 타이틀 텍스트 생성
labelText = Label(window, text="좋아하는 동물 투표  ", fg="blue", font=("나눔고딕", 16))
# IntVar()는 정수형 형식의 변수를 생성하는 함수
var = IntVar()
#rb1 라디오 버튼을 선택하면 var의 값으로 1이 대입됨
rb1 = Radiobutton(window, text="강아지", variable=var, value=1, command=myFunc)
#rb2 라디오 버튼을 선택하면 var의 값으로 2이 대입됨
rb2 = Radiobutton(window, text="고양이", variable=var, value=2, command=myFunc)
#rb3 라디오 버튼을 선택하면 var의 값으로 3이 대입됨
rb3 = Radiobutton(window, text="토끼", variable=var, value=3, command=myFunc)
#buttonOk 버튼을 선택하면 myFunc 함수 실행
buttonOk = Button(window, text="사진 보기", command=myFunc)

# 각각의 라디오 버튼과 연결된 이미지 지정
photo1 = PhotoImage(file="Images/gif/dog4.gif")
photo2 = PhotoImage(file="Images/gif/cat.gif")
photo3 = PhotoImage(file="Images/gif/dog3.gif")

# 이미지 위젯 labelImage 생성, 빈 이미지 표시
labelImage = Label(window, width=200, height=200, bg="#fff",  image=photo1)

# 제목 텍스트, 3개의 라디오 버튼, 버튼, 이미지 표시
# padx=5, pady=5 는 가로 세로 여백 지정
labelText.pack(padx=5, pady=5)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
buttonOk.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)

label = Label(window, text="어떤 동물을 좋아하세요?")
label.pack(padx=5, pady=5)

window.mainloop()

from tkinter import *


def getTextSize(input):
    """
    get size of the input text
    input: target text string
    """
    button = Button(window, text=input)
    button.pack()
    button.update()
    button.pack_forget()
    return (button.winfo_height(), button.winfo_width())


def getImageSize(input):
    """
    get size of the input image
    input: target image's path string
    """
    img = PhotoImage(file=input)
    button = Button(window, image=img)
    button.pack()
    button.update()
    button.pack_forget()
    return (button.winfo_height(), button.winfo_width())


def makeTable(targetwidget, col, row):
    """
    make table of target widget with rows and columns
    targetwidget: object
    row: row int
    col: column int
    """
    result = [[0] * col for _ in range(row)]
    for y in range(col):
        for x in range(row):
            result[y][x] = targetwidget()
    return result


def configTable(table, increment=0, endword="", **kwargs):
    """
    change config of all objects in table at once
    table: object made by makeTable function
    configstring: config with using string
    """
    col = len(table)
    row = len(table[0])
    maxlen = len(str(col * row - 1))
    for key, value in kwargs.items():
        for y in range(col):
            for x in range(row):
                if increment:
                    a = str(y * row + x)
                    if len(a) < maxlen:
                        a = "0" * (maxlen - len(a)) + a
                    table[y][x][key] = value + a + endword
                else:
                    table[y][x][key] = value + endword


def showTable(table, height, width, x0=0, y0=0):
    """
    place table with same height and width distance
    x0, y0 could be given with origin coordinate based by left, upper end point
    """
    col = len(table)
    row = len(table[0])
    for y in range(col):
        for x in range(b_row):
            table[y][x].place(x=x0 + x * width, y=y0 + y * height)


def hideTable(table):
    """
    hide table
    """
    col = len(table)
    row = len(table[0])
    for y in range(col):
        for x in range(b_row):
            table[y][x].place_forget()


# make root
window = Tk()
window.geometry("500x500")
window.update()  # you should use method update before getting height and width
w_height, w_width = window.winfo_height(), window.winfo_width()

# 1. set button table that has text
b_col = 3
b_row = 3
button = makeTable(Button, b_col, b_row)
configTable(button, 1, text="button")
txt_height, txt_width = getTextSize("button00")
showTable(button, txt_height, txt_width, 0, (w_height - txt_height * b_col) / 2)
hideTable(button)
del button # delete button table

# 2. set  button table that has image
b_col = 3
b_row = 3
rel_path = "Images\gif"
button = makeTable(Button, b_col, b_row)
# relative path depends on workspace's path in VS code
image = makeTable(PhotoImage, b_col, b_row)
configTable(image, 1, ".gif", file=rel_path + "\puz")
for y in range(b_col):
    for x in range(b_row):
        button[y][x].config(image=image[y][x]) ## hard to use configTable function!!!!
img_height, img_width = getImageSize(rel_path + "\puz1.gif")
showTable(button, img_height, img_width, 0, (w_height - img_height * b_col) / 2)

window.mainloop() # must need

'''
Tkinter를 이용한 간단한 그림판 어플리케이션
'''
from tkinter import *
from tkinter.colorchooser import askcolor

def paint(event):
    x1, y1 = (event.x - brush_size.get()), (event.y - brush_size.get())
    x2, y2 = (event.x + brush_size.get()), (event.y + brush_size.get())
    canvas.create_oval(x1, y1, x2, y2, fill=current_color.get(), outline=current_color.get())
    print(f"Drawing at: ({event.x}, {event.y})")

def change_color():
    color = askcolor(color=current_color.get())[1]
    if color:
        current_color.set(color)

def use_eraser():
    current_color.set("white")

def clear_canvas():
    canvas.delete("all")

root = Tk()
root.title("그림판")

current_color = StringVar()
current_color.set("black")

brush_size = IntVar()
brush_size.set(5)

canvas = Canvas(root, bg="white", width=600, height=400)
canvas.pack()

canvas.bind("<B1-Motion>", paint)

# 색상 선택 버튼
color_button = Button(root, text="색상 선택", command=change_color)
color_button.pack(side=LEFT)

# 지우개 버튼
eraser_button = Button(root, text="지우개", command=use_eraser)
eraser_button.pack(side=LEFT)

# 캔버스 초기화 버튼
clear_button = Button(root, text="초기화", command=clear_canvas)
clear_button.pack(side=LEFT)

# 브러시 크기 조절 슬라이더
brush_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL, variable=brush_size, label="브러시 크기")
brush_slider.pack(side=LEFT)

root.mainloop()


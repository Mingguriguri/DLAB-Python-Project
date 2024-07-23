'''
Tkinter를 이용한 간단한 계산기 어플리케이션
'''
from tkinter import *

def btn_click(value):
    global expression
    if value == "=":
        try:
            result = str(eval(expression))
            lbl_result.config(text=result)
            expression = ""
        except:
            lbl_result.config(text="오류")
            expression = ""
    elif value == "C":
        expression = ""
        lbl_result.config(text="")
    elif value == "←":
        expression = expression[:-1]
        lbl_result.config(text=expression)
    else:
        if value == '.' and expression and expression[-1] == '.':
            return
        expression += value
        lbl_result.config(text=expression)

expression = ""
root = Tk()
root.title("계산기")

lbl_result = Label(root, text="", height=2, font=("Arial", 24), bg="white", anchor="e")
lbl_result.grid(row=0, column=0, columnspan=4, sticky="we")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '←'
]

row_val = 1
col_val = 0

for btn_text in buttons:
    Button(root, text=btn_text, width=5, height=2, font=("Arial", 18), command=lambda x=btn_text: btn_click(x)).grid(row=row_val, column=col_val, sticky="we")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# 마지막 행에 추가 버튼(Clear와 Backspace)
Button(root, text='C', width=5, height=2, font=("Arial", 18), command=lambda: btn_click('C')).grid(row=row_val, column=0, sticky="we")
Button(root, text='←', width=5, height=2, font=("Arial", 18), command=lambda: btn_click('←')).grid(row=row_val, column=1, sticky="we")

root.mainloop()

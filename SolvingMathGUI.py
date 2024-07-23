import tkinter as tk
from tkinter import messagebox
import sympy as sp

def solve_quadratic(a, b, c):
    x = sp.Symbol('x')
    equation = sp.Eq(a * x**2 + b * x + c, 0)
    solutions = sp.solve(equation, x)
    return solutions

def solve_linear_system(a1, b1, c1, a2, b2, c2):
    x, y = sp.symbols('x y')
    equation1 = sp.Eq(a1 * x + b1 * y, c1)
    equation2 = sp.Eq(a2 * x + b2 * y, c2)
    solutions = sp.solve((equation1, equation2), (x, y))
    return solutions

def quadratic_solver():
    try:
        a = float(entry_quad_a.get())
        b = float(entry_quad_b.get())
        c = float(entry_quad_c.get())
        solutions = solve_quadratic(a, b, c)
        messagebox.showinfo("이차 방정식의 해", f"이차 방정식의 해: {solutions}")
    except ValueError:
        messagebox.showerror("입력 오류", "모든 값을 정확히 입력하세요.")

def linear_solver():
    try:
        a1 = float(entry_lin_a1.get())
        b1 = float(entry_lin_b1.get())
        c1 = float(entry_lin_c1.get())
        a2 = float(entry_lin_a2.get())
        b2 = float(entry_lin_b2.get())
        c2 = float(entry_lin_c2.get())
        solutions = solve_linear_system(a1, b1, c1, a2, b2, c2)
        messagebox.showinfo("연립방정식의 해", f"연립방정식의 해: {solutions}")
    except ValueError:
        messagebox.showerror("입력 오류", "모든 값을 정확히 입력하세요.")

root = tk.Tk()
root.title("수학 문제 풀이 프로그램")

# 이차 방정식 섹션
frame_quad = tk.Frame(root, padx=10, pady=10)
frame_quad.pack(pady=10)

tk.Label(frame_quad, text="이차 방정식 (ax^2 + bx + c = 0)").grid(row=0, columnspan=2)

tk.Label(frame_quad, text="a:").grid(row=1, column=0)
entry_quad_a = tk.Entry(frame_quad)
entry_quad_a.grid(row=1, column=1)

tk.Label(frame_quad, text="b:").grid(row=2, column=0)
entry_quad_b = tk.Entry(frame_quad)
entry_quad_b.grid(row=2, column=1)

tk.Label(frame_quad, text="c:").grid(row=3, column=0)
entry_quad_c = tk.Entry(frame_quad)
entry_quad_c.grid(row=3, column=1)

button_solve_quad = tk.Button(frame_quad, text="해 구하기", command=quadratic_solver)
button_solve_quad.grid(row=4, columnspan=2, pady=10)

# 연립방정식 섹션
frame_lin = tk.Frame(root, padx=10, pady=10)
frame_lin.pack(pady=10)

tk.Label(frame_lin, text="연립방정식").grid(row=0, columnspan=2)

tk.Label(frame_lin, text="첫 번째 방정식 (a1*x + b1*y = c1)").grid(row=1, columnspan=2)

tk.Label(frame_lin, text="a1:").grid(row=2, column=0)
entry_lin_a1 = tk.Entry(frame_lin)
entry_lin_a1.grid(row=2, column=1)

tk.Label(frame_lin, text="b1:").grid(row=3, column=0)
entry_lin_b1 = tk.Entry(frame_lin)
entry_lin_b1.grid(row=3, column=1)

tk.Label(frame_lin, text="c1:").grid(row=4, column=0)
entry_lin_c1 = tk.Entry(frame_lin)
entry_lin_c1.grid(row=4, column=1)

tk.Label(frame_lin, text="두 번째 방정식 (a2*x + b2*y = c2)").grid(row=5, columnspan=2)

tk.Label(frame_lin, text="a2:").grid(row=6, column=0)
entry_lin_a2 = tk.Entry(frame_lin)
entry_lin_a2.grid(row=6, column=1)

tk.Label(frame_lin, text="b2:").grid(row=7, column=0)
entry_lin_b2 = tk.Entry(frame_lin)
entry_lin_b2.grid(row=7, column=1)

tk.Label(frame_lin, text="c2:").grid(row=8, column=0)
entry_lin_c2 = tk.Entry(frame_lin)
entry_lin_c2.grid(row=8, column=1)

button_solve_lin = tk.Button(frame_lin, text="해 구하기", command=linear_solver)
button_solve_lin.grid(row=9, columnspan=2, pady=10)

root.mainloop()

import sympy as sp

def solve_quadratic(a, b, c):
    x = sp.Symbol('x')
    equation = sp.Eq(a * x ** 2 + b * x + c, 0)
    solutions = sp.solve(equation, x)
    return solutions


def solve_linear_system(a1, b1, c1, a2, b2, c2):
    x, y = sp.symbols('x y')
    equation1 = sp.Eq(a1 * x + b1 * y, c1)
    equation2 = sp.Eq(a2 * x + b2 * y, c2)
    solutions = sp.solve((equation1, equation2), (x, y))
    return solutions


while True:
    print("\n1. 이차 방정식의 해 구하기")
    print("2. 연립방정식의 해 구하기")
    print("3. 종료")

    action = input("원하는 작업을 선택하세요: ")

    if action == '1':
        a = float(input("a 값을 입력하세요: "))
        b = float(input("b 값을 입력하세요: "))
        c = float(input("c 값을 입력하세요: "))
        solutions = solve_quadratic(a, b, c)
        print(f"이차 방정식의 해: {solutions}")
    elif action == '2':
        a1 = float(input("첫 번째 방정식의 a 값을 입력하세요: "))
        b1 = float(input("첫 번째 방정식의 b 값을 입력하세요: "))
        c1 = float(input("첫 번째 방정식의 c 값을 입력하세요: "))
        a2 = float(input("두 번째 방정식의 a 값을 입력하세요: "))
        b2 = float(input("두 번째 방정식의 b 값을 입력하세요: "))
        c2 = float(input("두 번째 방정식의 c 값을 입력하세요: "))
        solutions = solve_linear_system(a1, b1, c1, a2, b2, c2)
        print(f"연립방정식의 해: {solutions}")
    elif action == '3':
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "除数不能为零"
    return x / y

print("欢迎使用简单计算器！")
print("可用的运算符：+、-、*、/")

while True:
    try:
        num1 = float(input("请输入第一个数字："))
        operator = input("请输入运算符：")
        num2 = float(input("请输入第二个数字："))

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("无效的运算符，请重新输入。")
            continue

        print(f"{num1} {operator} {num2} = {result}")

        choice = input("是否继续计算？(y/n)：")
        if choice.lower() != 'y':
            break
    except ValueError:
        print("输入无效，请输入有效的数字。")
    
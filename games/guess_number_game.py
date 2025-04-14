import random

# 生成 1 到 100 之间的随机数
number = random.randint(1, 100)
attempts = 0

print("欢迎来到猜数字游戏！我已经想好了一个 1 到 100 之间的数字，你可以开始猜啦。")

while True:
    try:
        # 获取用户输入
        guess = int(input("请输入你猜测的数字："))
        attempts += 1
        if guess < number:
            print("猜的数字太小了，再试试！")
        elif guess > number:
            print("猜的数字太大了，再试试！")
        else:
            print(f"恭喜你，猜对了！你一共用了 {attempts} 次尝试。")
            break
    except ValueError:
        print("输入无效，请输入一个整数。")
    
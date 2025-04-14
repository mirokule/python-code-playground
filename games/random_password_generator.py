import random
import string

print("欢迎使用随机密码生成器！")
while True:
    try:
        length = int(input("请输入你想要的密码长度："))
        if length <= 0:
            print("密码长度必须为正整数，请重新输入。")
            continue
        # 定义所有可能的字符
        all_characters = string.ascii_letters + string.digits + string.punctuation
        # 生成随机密码
        password = ''.join(random.choice(all_characters) for i in range(length))
        print(f"生成的随机密码是：{password}")

        choice = input("是否继续生成密码？(y/n)：")
        if choice.lower() != 'y':
            break
    except ValueError:
        print("输入无效，请输入一个整数。")
    
def encrypt(text):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + 3
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            else:
                if shifted > ord('z'):
                    shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def decrypt(text):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - 3
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            else:
                if shifted < ord('a'):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted

while True:
    print("请选择操作：")
    print("1. 加密文字")
    print("2. 解密文字")
    print("3. 退出")
    choice = input("输入你的选择 (1/2/3): ")

    if choice == '1':
        text = input("请输入要加密的文字: ")
        encrypted_text = encrypt(text)
        print(f"加密后的文字: {encrypted_text}")
    elif choice == '2':
        text = input("请输入要解密的文字: ")
        decrypted_text = decrypt(text)
        print(f"解密后的文字: {decrypted_text}")
    elif choice == '3':
        break
    else:
        print("无效的选择，请重新输入。")
    
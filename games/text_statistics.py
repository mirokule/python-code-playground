while True:
    text = input("请输入一段文字（输入 'q' 退出）: ")
    if text.lower() == 'q':
        break
    # 统计字符数
    char_count = len(text)
    # 统计单词数
    word_count = len(text.split())
    # 统计句子数
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    print(f"字符数: {char_count}")
    print(f"单词数: {word_count}")
    print(f"句子数: {sentence_count}")
    
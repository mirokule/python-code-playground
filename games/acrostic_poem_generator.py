import random

# 定义一些常用的诗句片段
lines = [
    "春风得意马蹄疾", "夏荷映日别样红", "秋霜染尽枫林醉", "冬雪纷飞映月浓",
    "青山绿水皆入画", "碧海蓝天共成诗", "白云悠悠映晴空", "翠竹亭亭立幽篁"
]

def generate_acrostic_poem(keywords):
    poem = []
    for keyword in keywords:
        random_line = random.choice(lines)
        new_line = keyword + random_line[1:]
        poem.append(new_line)
    return poem

while True:
    input_keywords = input("请输入关键字，用空格分隔（输入 'q' 退出）: ")
    if input_keywords.lower() == 'q':
        break
    keywords = input_keywords.split()
    poem = generate_acrostic_poem(keywords)
    print("生成的藏头诗如下:")
    for line in poem:
        print(line)
    
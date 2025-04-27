from bs4 import BeautifulSoup

# 示例 HTML 文档
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>示例页面</title>
</head>
<body>
    <h1 id="main-title">欢迎来到示例页面</h1>
    <p class="content">这是一个段落。</p>
    <p>另一个段落。</p>
    <ul>
        <li>列表项 1</li>
        <li>列表项 2</li>
    </ul>
    <a href="https://www.example.com" class="link">示例链接</a>
</body>
</html>
"""

# 1. 解析 HTML 文档
soup = BeautifulSoup(html_doc, 'html.parser')

# 2. 提取标签内容
title = soup.title.string
print("页面标题:", title)

# 3. 查找标签
# 查找第一个 class 为 content 的 p 标签
first_p = soup.find('p', class_='content')
print("第一个 class 为 content 的 p 标签内容:", first_p.string)

# 查找所有的 p 标签
all_p = soup.find_all('p')
print("所有 p 标签内容:")
for p in all_p:
    print(p.string)

# 4. 遍历文档树
# 访问父标签
h1 = soup.h1
parent = h1.parent
print("h1 标签的父标签:", parent.name)

# 访问子标签
ul = soup.ul
print("ul 标签的子标签:")
for child in ul.children:
    print(child.string)

# 访问兄弟标签
first_li = ul.li
next_li = first_li.next_sibling.next_sibling  # 处理换行符
print("第一个 li 标签的下一个兄弟标签内容:", next_li.string)

# 5. 处理属性
a = soup.a
# 获取属性
href = a['href']
print("链接的 href 属性:", href)

# 修改属性
a['href'] = 'https://www.new-example.com'
print("修改后的链接标签:", a)

# 6. 清理和格式化 HTML
formatted_html = soup.prettify()
print("格式化后的 HTML:")
print(formatted_html)
    
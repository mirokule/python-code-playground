import requests

# 1. 发送 GET 请求
def send_get_request():
    url = 'https://httpbin.org/get'
    try:
        response = requests.get(url)
        # 检查响应状态码
        if response.status_code == 200:
            print("GET 请求成功，响应内容：")
            print(response.json())
        else:
            print(f"GET 请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"请求发生错误：{e}")

# 2. 发送 POST 请求
def send_post_request():
    url = 'https://httpbin.org/post'
    data = {'key': 'value'}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("POST 请求成功，响应内容：")
            print(response.json())
        else:
            print(f"POST 请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"请求发生错误：{e}")

# 3. 发送 PUT 请求
def send_put_request():
    url = 'https://httpbin.org/put'
    data = {'key': 'new_value'}
    try:
        response = requests.put(url, data=data)
        if response.status_code == 200:
            print("PUT 请求成功，响应内容：")
            print(response.json())
        else:
            print(f"PUT 请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"请求发生错误：{e}")

# 4. 发送 DELETE 请求
def send_delete_request():
    url = 'https://httpbin.org/delete'
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            print("DELETE 请求成功，响应内容：")
            print(response.json())
        else:
            print(f"DELETE 请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"请求发生错误：{e}")

# 5. 设置请求头
def send_request_with_headers():
    url = 'https://httpbin.org/get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("带请求头发送 GET 请求成功，响应内容：")
            print(response.json())
        else:
            print(f"带请求头发送 GET 请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"请求发生错误：{e}")

# 6. 处理 Cookies
def handle_cookies():
    url = 'https://httpbin.org/cookies/set?name=example'
    try:
        # 发送请求设置 Cookies
        response = requests.get(url)
        if response.status_code == 200:
            cookies = response.cookies
            print("设置的 Cookies：", cookies)
            # 使用 Cookies 发送新的请求
            new_response = requests.get('https://httpbin.org/cookies', cookies=cookies)
            if new_response.status_code == 200:
                print("使用 Cookies 发送请求成功，响应内容：")
                print(new_response.json())
            else:
                print(f"使用 Cookies 发送请求失败，状态码：{new_response.status_code}")
        else:
            print(f"设置 Cookies 请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"请求发生错误：{e}")


if __name__ == "__main__":
    print("--- 发送 GET 请求 ---")
    send_get_request()
    print("\n--- 发送 POST 请求 ---")
    send_post_request()
    print("\n--- 发送 PUT 请求 ---")
    send_put_request()
    print("\n--- 发送 DELETE 请求 ---")
    send_delete_request()
    print("\n--- 带请求头发送请求 ---")
    send_request_with_headers()
    print("\n--- 处理 Cookies ---")
    handle_cookies()
    
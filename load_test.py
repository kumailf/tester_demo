import threading
import requests
import time

# 登录接口的 URL
url = "http://example.com/login"

# 登录请求的数据
data = {
    "username": "testuser",
    "password": 12345  # 假设密码是整数
}

# 每个线程执行的函数
def login_request():
    try:
        response = requests.post(url, json=data)
        print(f"Response status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

# 线程数
num_threads = 100

# 创建并启动线程
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=login_request)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print("All threads completed.")
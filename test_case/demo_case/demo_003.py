import requests
import json

# 设置请求头部
header = {'Authorization': 'Bearer 2bcbde6f3d05480988abae32ae111833'}

# 设置文件路径和文件类型
file_path = r'../../data/suidao1.jpeg'
file_type = 'image/jpeg'

# 确保文件存在
try:
    # with open(file_path, 'rb') as file:
    # 创建文件元组，包括文件名、文件对象和内容类型
    upload_files = {'file': open(r'../../data/suidao1.jpeg', 'rb')}

    # 设置URL
    url = 'https://v1.2.tunnelprj.com/oa/admin-api/system/file/procedure/upload'

    # 发送POST请求，上传文件
    response = requests.post(url=url, files=upload_files, headers=header, verify=False)

    # 检查响应状态码
    if response.status_code == 200:
        print("文件上传成功！")
        # 如果需要，可以处理响应内容
        # response_data = response.json()
        # print(response_data)
    else:
        print("文件上传失败！")
        # 打印错误信息
        print("响应状态码:", response.status_code)
        # 如果服务器返回了错误信息，通常会在响应内容中
        print("响应内容:", response.text)

except FileNotFoundError:
    print(f"文件 {file_path} 未找到！")

except requests.RequestException as e:
    # 捕获请求异常，并打印异常信息
    print("请求异常:", e)

print(response.text)

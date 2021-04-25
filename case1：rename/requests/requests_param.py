import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
}

# 1、url中直接带参数
# url = 'https://www.baidu.com/s?wd=李龙辉'
#
# response = requests.get(url, headers=headers)
#
# with open('url.html', 'wb') as f:
#     f.write(response.content)


# 2、params参数传入
url = 'http://www.baidu.com/s?'
# 参数
data = {'wd': '李龙辉'}
# 请求
response = requests.get(url, headers=headers, params=data)

with open('url+params.html', 'wb') as f:
    f.write(response.content)
import requests

url = 'http://www.baidu.com'

response = requests.get(url)

print(response.content.decode())
print(len(response.content))
print(response.status_code)


#coding=utf-8
import requests
import urllib

url = 'https://www.hao123.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
}

temp = 'BAIDUID=3F35EBC055D93E593FD77C84D97A6760:FG=1; newloc=湖南|长沙|长沙; loc2=2|湖南|长沙; s_ht_pageid=16; v_pg=normal; hz=0; ft=1; hword=17; Hm_lvt_0703cfc0023d60b244e06b5cacfef877=1614310454,1614948486,1615865928,1615943930; org=1; BDUSS=JzSGFvc35KenpGWTNXMS1-NnBvZ1NzeWRYODd1aEVaVHltMVV4LTlIcWQtM2hnRVFBQUFBJCQAAAAAAAAAAAEAAAB9-TgJbGlsb25naHVpMTExMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ1uUWCdblFgTH; tnwhiteft=XzFYUBclcMPGIANCmytknWnBQaFYTzclnHmkPHbYrHf4nZY; Hm_lpvt_0703cfc0023d60b244e06b5cacfef877=1615949490; __bsi=7591021143893275774_00_46_R_N_5_0303_c02f_Y'

cookie_list = temp.split('; ')

# str1 = urllib.parse.quote('湖南|长沙|长沙')
# cookies = {'newloc': str1}
#
# str2 = urllib.parse.quote('2|湖南|长沙')
cookies = {}

for cookie in cookie_list:
    cookies[cookie.split('=')[0]] = urllib.parse.quote(cookie.split('=')[-1])

print(cookies)

#
response = requests.post(url, headers=headers, cookies=cookies, timeout=30)
#
with open('cookie2.html', 'wb') as f:
    f.write(response.content)


# response = requests.get(url)
# print(response.cookies)
#
# cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
# print(cookie_dict)
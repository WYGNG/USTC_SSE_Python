# encoding:utf-8
# Author: Du
# Version: 1.0.0 2019.10.19
import requests
from lxml import etree
import re


# 调用get_cookie()获得登陆后cookie。返回值'-1'表示登陆失败。
header = {
    "Connection": "keep-alive",
    "Host": "www.pfchina.com.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

url = "http://www.pfchina.com.cn/index.asp"

parameter = {
    'V': "/index.asp",
    "UserId": "--------",
    "PWD": "--------",
    'x': "30",
    'y': "15"
}


# 判断之前cookie是否可用，不可用则使用login方法获取，记录后返回新的cookie
def getCookie():
    cookieFile = open("../doc/cookieFile.txt", "r")
    cookie = cookieFile.read()
    cookieFile.close()
    header["Cookie"] = cookie
    response = requests.get(url, headers=header)
    response.encoding = 'gbk'
    # print(response.text)
    page = etree.HTML(response.text)
    flag = 0
    try:
        userName = page.xpath("//body/div[1]/div[1]/div/div/span/strong/text()")
        if userName[0] != "--------":
            print("Cookie不可用。")
            cookie = login()
        else:
            flag = 1
            print("Cookie可用: " + cookie)
    except:
        print("Cookie不可用。")
        cookie = login()
    if flag == 0 and cookie != '-1':
        cookieFile = open("../doc/cookieFile.txt", "w")
        cookieFile.write(cookie)
        cookieFile.close()
    return cookie


# 登录函数，登陆成功返回cookie，失败返回-1
def login():
    print("正在登录更新Cookie...")
    header["Referer"] = "http://www.pfchina.com.cn/index.asp"
    loginUrl = "http://www.pfchina.com.cn/verify/login.asp?V=%2Findex.asp&UserId=%CB%D5%D6%DD%C0%A5%C1%EB&PWD" \
               "=--------&x=30&y=15 "
    print(loginUrl)
    res = requests.get(loginUrl, headers=header)
    print(res.headers)
    c = res.headers['Set-Cookie']

    try:
        if re.search("regCookie", c).group() is None:
            print("登录失败，请确认账号状态！")
            return '-1'
        else:
            print("Cookie更新成功: " + c)
            return c
    except:
        print("登录失败，请确认账号状态！")
        return '-1'


if __name__ == '__main__':
    cookie = getCookie()
    # print("Cookie: " + cookie)

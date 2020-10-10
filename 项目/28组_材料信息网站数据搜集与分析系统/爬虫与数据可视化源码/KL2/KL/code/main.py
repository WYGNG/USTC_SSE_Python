# encoding:utf-8
# Version:2.0.0 2019.10.18
from KL.code.getCookie import getCookie
from KL.code.categories import *
from KL.code.getPage import getPage


def main():
    cookie = getCookie()
    if cookie == '-1':
        return 0
    # 需要测试哪一个就将哪个getPage函数注释去掉
    # getPage(cookie, BOPPD)
    getPage(cookie, CPPD)
    # getPage(cookie, BOPETD)
    # getPage(cookie, BOPETW)
    # getPage(cookie, PPDFHZ)
    # getPage(cookie, PPZSH)
    # getPage(cookie, PEZSH)


if __name__ == '__main__':
    main()

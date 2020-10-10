# encoding:utf-8
"""
不同类的编号和关键字的定义
1 - BOPPD: BOPP日评
2 - CPPD: CPP日评
3 - BOPETD: BOPET日评
4 - BOPETW: BOPET周评
5 - PPDFHZ：[PP出厂]:地方/合资企业PP出厂价格汇总
6 - PPZSH: [PP出厂]:国内中石化PP出厂价格汇总
7 - PE:[PE出厂]：中石化PE出厂价格一览
"""


class BOPPD:
    id = '1'
    number = "001401"
    keywords = "BOPP日评"


class CPPD:
    id = '2'
    number = "020701"
    keywords = "CPP日评"


class BOPETD:
    id = '3'
    number = "100501"
    keywords = "BOPET日评"


class BOPETW:
    id = '4'
    number = "100501"
    keywords = "BOPET周评"


class PPDFHZ:
    id = '5'
    number = "010401"
    keywords = "地方/合资企业PP出厂"


class PPZSH:
    id = '6'
    number = "010401"
    keywords = "国内中石化"


class PEZSH:
    id = '7'
    number = "030401"
    keywords = "中石化PE出厂"

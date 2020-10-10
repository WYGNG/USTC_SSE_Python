import requests
from lxml import etree
import pandas
import datetime

INFO = []

# 获取网页源代码
def get_html(page):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,' + str(page) + '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
    except Exception as e:
        print('获取源码失败:%s' % e)
    return html.text

# xpath网页
def get_information(html):
    # etree.HTML()可以用来解析字符串格式的HTML文档对象，将传进去的字符串转变成_Element对象。作为_Element对象，可以方便的使用xpath()方法。
    html = etree.HTML(html)
    # XPath即为XML路径语言，它是一种用来确定XML(标准通用标记语言的子集)文档中某部分位置的语言。
    list = html.xpath("//p[@class='t1 ']/span/a/@href")
    return list

# 解析网页
def parse_html(html):
    info = []
    # 使用zip()来使一个循环并行遍历两个列表
    for url in get_information(html):
        try:
            html = requests.get(url)
            html.encoding = html.apparent_encoding
            res = etree.HTML(html.text)
            position = res.xpath("//div[@class='cn']/h1/text()")[0].strip()
            # print(position)
            salary = res.xpath("//div[@class='cn']/strong/text()")[0]
            # print(salary)
            company_name = res.xpath("//p[@class='cname']/a/text()")[0]
            # print(company_name)
            city = res.xpath("//p[@class='msg ltype']/text()")[0].strip()
            # print(city)
            experience = res.xpath("//p[@class='msg ltype']/text()")[1].strip()
            # print(experience)
            education = res.xpath("//p[@class='msg ltype']/text()")[2].strip()
            # print(education)
            # welfare = ",".join(re.findall(re.compile(r'<span class="sp4">(.*?)</span>', re.S), html))
            company_type = res.xpath("//p[@class='at']/text()")[0].strip()
            # print(company_type)
            company_scale = res.xpath("//p[@class='at']/text()")[1].strip()

            item = {'position': position, 'salary': salary, 'company_name': company_name, 'city': city, 'experience': experience,
                    'education': education, 'company_type': company_type, 'company_scale': company_scale}
            print(item)
            info.append(item)
        except:
            pass

    return info

def main():
    start_time = datetime.datetime.now()
    print('*' * 20)
    # 待采集的起始页码
    start_page = int(input("请输入起始页码："))
    # 待采集的终止页码
    end_page = int(input("请输入终止页码："))
    print('*' * 20)
    for page in range(start_page, end_page + 1):
        print("正在爬取第" + str(page) + "页数据...")
        html = get_html(page)
        info = parse_html(html)
        INFO.extend(info)

    # 输出csv数据
    information = pandas.DataFrame(INFO)
    information.to_csv('java_info.csv')

    end_time = datetime.datetime.now()
    print('*' * 100)
    print('开始时间：', start_time)
    print('结束时间：', end_time)
    print('共计用时：', end_time - start_time)
    print('*' * 100)


if __name__ == '__main__':
    main()
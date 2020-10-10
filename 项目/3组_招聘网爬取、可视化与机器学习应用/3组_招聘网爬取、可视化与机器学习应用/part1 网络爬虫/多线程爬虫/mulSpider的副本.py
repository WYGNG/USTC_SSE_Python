import threading
from queue import Queue
from lxml import etree
import requests
import csv
import datetime

exitFlag_Parse = False
exitFlag_get = False
exitFlag_Save = False
urlQueue = Queue()
contentQueue = Queue()
itemQueue = Queue()
# 锁
lock = threading.Lock()


class UrlSpider(threading.Thread):
    def __init__(self, threadName, pageQueue):
        super(UrlSpider, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

    def run(self):
        # print("启动" + self.threadName)
        global urlQueue
        while True:
            if self.pageQueue.empty():
                break
            else:

                page = self.pageQueue.get(False)
                url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,' + str(page) + '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
                html = requests.get(url, headers=self.headers)
                selector = etree.HTML(html.text)
                content_field = selector.xpath("//div[@class='dw_table']/div[@class='el']")
                for li in content_field:
                    try:
                        job_url = li.xpath(".//p[@class='t1 ']/span/a/@href")[0]
                        # print(job_url)
                        urlQueue.put(job_url)
                    except:
                        pass
        # print("结束" + self.threadName)


class GetHtmlSpider(threading.Thread):
    def __init__(self, threadName):
        super(GetHtmlSpider, self).__init__()
        self.threadName = threadName
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

    def run(self):
        # print("启动" + self.threadName)
        global contentQueue, urlQueue, exitFlag_get
        while not exitFlag_get:
            try:
                url = urlQueue.get(False)
                html = requests.get(url, headers=self.headers)
                html.encoding = html.apparent_encoding
                contentQueue.put(html.text)
                # print(html.text)
            except:
                pass
        # print("结束" + self.threadName)


class ParseSpider(threading.Thread):
    def __init__(self, threadName):
        super(ParseSpider, self).__init__()
        self.threadName = threadName

    def run(self):
        # print("启动" + self.threadName)
        global contentQueue, itemQueue, exitFlag_Parse
        while not exitFlag_Parse:
            try:
                content = contentQueue.get(False)
                res = etree.HTML(content)
                job_filed = res.xpath("//div[@class='cn']")
                item = []
                for li in job_filed:
                    position = li.xpath(".//h1/text()")[0].strip()
                    # print(position)
                    salary = li.xpath(".//strong/text()")[0]
                    # print(salary)
                    company_name = li.xpath(".//p[@class='cname']/a/text()")[0]
                    # print(company_name)
                    city = li.xpath(".//p[@class='msg ltype']/text()")[0].strip()
                    # print(city)
                    experience = li.xpath(".//p[@class='msg ltype']/text()")[1].strip()
                    # print(experience)
                    education = li.xpath(".//p[@class='msg ltype']/text()")[2].strip()
                    # print(education)
                    item.extend([position, salary, company_name, city, experience, education])

                company_field = res.xpath("//div[@class='com_tag']")
                for lu in company_field:
                    company_type = lu.xpath(".//p[@class='at']/text()")[0].strip()
                    # print(company_type)
                    company_scale = lu.xpath(".//p[@class='at']/text()")[1].strip()
                    # print(company_scale)
                    # company_major = res.xpath("//p[@class='at']/a/text()")[2].strip()
                    # print(company_major)
                    item.extend([company_type, company_scale])
                print(item)
                itemQueue.put(item)
            except:
                pass
        # print("结束" + self.threadName)


class SaveSpider(threading.Thread):
    def __init__(self, threadName, file_name):
        super(SaveSpider, self).__init__()
        self.threadName = threadName
        self.file_name = file_name
        self.writer = csv.writer(self.file_name)

    def run(self):
        # print("启动" + self.threadName)
        global exitFlag_Save, itemQueue, lock
        while not exitFlag_Save:
            try:
                item = itemQueue.get(block=False)
                # print(content)
                with lock:
                    self.writer.writerows([item])
                itemQueue.task_done()
            except:
                pass
        # print("结束" + self.threadName)


def main():
    start_time = datetime.datetime.now()
    # 采集的数据存储在本地磁盘的文件名
    file_name = open('java_info.csv', 'a', newline="")
    writer = csv.writer(file_name)
    writer.writerow(['position', 'salary', 'company_name', 'city', 'experience', 'education', 'company_type', 'company_scale'])
    print('*' * 20)
    # 待采集的起始页码
    start_page = int(input("请输入起始页码："))
    # 待采集的终止页码
    end_page = int(input("请输入终止页码："))
    print('*' * 20)

    pageQueue = Queue()

    for page in range(start_page, end_page + 1):
        pageQueue.put(page)

    # 初始化采集url线程
    threadUrls = []
    urlSpiderList = ["urlThread1", "urlThread2", "urlThread3", "urlThread4", "urlThread5", "urlThread6", "urlThread7"]
    for threadName in urlSpiderList:
        thread = UrlSpider(threadName, pageQueue)
        thread.start()
        threadUrls.append(thread)

    # 初始化获取html.text线程
    threadgetHtml = []
    gethtmlSpiderList = ["gethtmlThread1", "gethtmlThread2", "gethtmlThread3", "gethtmlThread4", "gethtmlThread5", "gethtmlThread6"]
    for threadName in gethtmlSpiderList:
        thread = GetHtmlSpider(threadName)
        thread.start()
        threadgetHtml.append(thread)

    # 初始化解析线程
    threadParse = []
    parseSpideList = ["parseThread1", "parseThread2", "parseThread3", "parseThread4", "parseThread5", "parseThread6", "parseThread7", "parseThread8", "parseThread9", "parseThread10",
                    "parseThread11", "parseThread12", "parseThread13", "parseThread14", "parseThread15", "parseThread16", "parseThread17", "parseThread18", "parseThread19", "parseThread20"
                     ]
    for threadName in parseSpideList:
        thread = ParseSpider(threadName)
        thread.start()
        threadParse.append(thread)

    # 初始化存储线程
    threadSave = []
    saveSpiderList = ["saveThread1", "saveThread2", "saveThread3"]
    for threadName in saveSpiderList:
        thread = SaveSpider(threadName, file_name)
        thread.start()
        threadSave.append(thread)

    # 等待队列被清空
    while not pageQueue.empty():
        pass

    # 等待采集线程结束
    for thread in threadUrls:
        thread.join()

    # 等待队列被清空
    while not urlQueue.empty():
        pass

    global exitFlag_get
    exitFlag_get = True

    for thread in threadgetHtml:
        thread.join()

    while not contentQueue.empty():
        pass

    global exitFlag_Parse
    exitFlag_Parse = True

    for thread in threadParse:
        thread.join()

    while not itemQueue.empty():
        pass

    global exitFlag_Save
    exitFlag_Save = True

    for thread in threadSave:
        thread.join()

    with lock:
        file_name.close()

    end_time = datetime.datetime.now()
    print('*' * 100)
    print('开始时间：', start_time)
    print('结束时间：', end_time)
    print('共计用时：', end_time - start_time)
    print('*' * 100)

if __name__ == "__main__":
    main()
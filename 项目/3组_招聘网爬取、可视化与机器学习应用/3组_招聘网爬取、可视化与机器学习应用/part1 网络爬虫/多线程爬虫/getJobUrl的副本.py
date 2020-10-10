import threading
from queue import Queue
from lxml import etree
import requests
import datetime

exitFlag_Parse = False

class UrlSpider(threading.Thread):

    def __init__(self, threadName, pageQueue, urlQueue):
        super(UrlSpider, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.urlQueue = urlQueue
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

    def run(self):
        print("启动" + self.threadName)
        while not exitFlag_Parse:
            try:
                page = self.pageQueue.get(False)
                url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,' + str(page) + '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
                html = requests.get(url, headers=self.headers)
                selector = etree.HTML(html.text)
                content_field = selector.xpath("//div[@class='dw_table']/div[@class='el']")
                for li in content_field:
                    try:
                        job_url = li.xpath(".//p[@class='t1 ']/span/a/@href")[0]
                        # print(job_url)
                        self.urlQueue.put(job_url)
                    except:
                        pass
            except:
                pass

        print("结束" + self.threadName)


def main():
    start_time = datetime.datetime.now()
    print('*' * 20)
    # 待采集的起始页码
    start_page = int(input("请输入起始页码："))
    # 待采集的终止页码
    end_page = int(input("请输入终止页码："))
    print('*' * 20)


    pageQueue = Queue()
    urlQueue = Queue()

    for page in range(start_page, end_page + 1):
        pageQueue.put(page)

    # 初始化采集线程
    threadUrls = []
    urlSpiderList = ["urlThread1", "urlThread2", "urlThread3", "urlThread4", "urlThread5", "urlThread6"]
    for threadName in urlSpiderList:
        thread = UrlSpider(threadName, pageQueue, urlQueue)
        thread.start()
        threadUrls.append(thread)

    # 等待队列被清空
    while not pageQueue.empty():
        pass

    global exitFlag_Parse
    exitFlag_Parse = True
    # 等待采集线程结束
    for thread in threadUrls:
        thread.join()

    end_time = datetime.datetime.now()
    print('*' * 100)
    print('开始时间：', start_time)
    print('结束时间：', end_time)
    print('共计用时：', end_time - start_time)
    print('*' * 100)

if __name__ == "__main__":
    main()


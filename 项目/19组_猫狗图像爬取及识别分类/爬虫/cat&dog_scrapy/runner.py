import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from cat.spiders.cat_spider import CatSpiderSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(CatSpiderSpider)
process.start()

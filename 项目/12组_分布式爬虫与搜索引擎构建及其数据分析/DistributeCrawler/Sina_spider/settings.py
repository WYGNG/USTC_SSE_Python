# encoding=utf-8

BOT_NAME = ['Sina_spider']

SPIDER_MODULES = ['Sina_spider.spiders']
NEWSPIDER_MODULE = 'Sina_spider.spiders'

DOWNLOADER_MIDDLEWARES = {
    "Sina_spider.middleware.UserAgentMiddleware": 401,
    'Sina_spider.middleware.RedirectMiddleware': 400,
    "Sina_spider.middleware.CookieMiddleware": 402,
}
ITEM_PIPELINES = {
    'Sina_spider.pipelines.ElasticsearchPipeline': 1
}
COOKIES_ENABLED = False
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}
SCHEDULER = 'Sina_spider.scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'Sina_spider.scrapy_redis.queue.MySpiderQueue'
#
# REDIS_NODES = [{"host": "redis1", "port": "6379"},
#                # {"host": "redis2", "port": "8002"},
#                # {"host": "redis3", "port": "8003"},
#                # {"host": "redis4", "port": "8004"},
#                # {"host": "redis5", "port": "8005"},
#                # {"host": "redis6", "port": "8006"}
#                ]
# #
# 种子队列的信息
REDIE_URL = None
REDIS_HOST = 'redis1'
REDIS_PORT = 6379

# 去重队列的信息
FILTER_URL = None
FILTER_HOST = 'redis1'
FILTER_PORT = 6379
FILTER_DB = 0


LOG_LEVEL = 'INFO'  # 日志级别
DOWNLOAD_DELAY = 0  # 间隔时间
CONCURRENT_REQUESTS = 20  # 默认为16
CONCURRENT_REQUESTS_PER_DOMAIN = 20
# CONCURRENT_ITEMS = 100
# CONCURRENT_REQUESTS_PER_IP = 1
# REDIRECT_ENABLED = False


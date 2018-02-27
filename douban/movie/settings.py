#encoding: utf-8

BOT_NAME = "movie"

SPIDER_MODULES = ["spiders"]
NEWSPIDER_MODULE = "spiders"

ITEM_PIPELINES = {
    "pipelines.JsonWriterPipeline" : 1,
    "pipelines.MoviePipeline": 3,
}

DOWNLOADER_MIDDLEWARES = {
    "misc.middlewares.CustomUserAgentMiddleware": 401,
    "misc.middlewares.CustomCookieMiddleware": 701,
    "misc.middlewares.CustomHeadersMiddleware": 551,
    #"misc.middlewares.proxyMiddleware": 201,
}


#广度优先
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = "scrapy.squeue.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeue.FifoMemoryQueue"

#布隆过滤
DUPEFILTER_CLASS = "misc.bloomfilter.BLOOMDupeFilter"

WEBSERVICE_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = "INFO"
LOG_STDOUT = False
#LOG_FILE = "/var/log/scrapy_douban_movie.log"
#RETRY_ENABLED = False
#DOWNLOAD_TIMEOUT = 15
DOWNLOAD_DELAY = 7
COOKIES_ENABLES=False

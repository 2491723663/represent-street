# Scrapy settings for AmazonTest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Amazon_su'

SPIDER_MODULES = ['Amazon_su.spiders']
NEWSPIDER_MODULE = 'Amazon_su.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = 'ERROR'


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#开启headers设置cookie的配置
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language':'h-CN,zh;q=0.9',
  'accept-encoding':'gzip, deflate',
  'upgrade-insecure-requests':'1',
  #'cookie':'session-id=136-5529720-3328761; i18n-prefs=USD; ubid-main=133-5660816-5363143; session-id-eu=257-2101056-5793269; ubid-acbuk=260-4910239-7744262; s_pers=%20s_fid%3D187A3C3CD67FEFBC-2FFDB0D6E686FE9A%7C1761920768571%3B%20s_dl%3D1%7C1604156168572%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1604156168575%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271604154368578%2527%255D%255D%7C1761920768578%3B; session-id-time=2082787201l; s_fid=3A12F7C0ADECDEDD-0E3555974BC6FCE0; s_vn=1636534592951%26vn%3D1; regStatus=pre-register; lc-main=en_US; session-id-time-eu=2236210063l; x-acbuk="lHNb1@yo9qZ?vCy5SJ@H1VUrQgIvSee2wFCmAqLffw2dGDKa2q8NZpL4AbHPy?kK"; at-main=Atza|IwEBIOCVW_F9VCZzG5decp0iDhtqsbPRKwxQYZn9JjiNMlWVYSoipjFOZh-CPp6tOcHsvROzFuhIg1MzGH0rzcr2RAc_fwaix-Xn9Y7-lgga2BzV_4bbxgON1IbfEyftsfz2JR8vIwPyaGPKbkH6B_EO-0fD_PjInV_8DLuHqe9OjK2hvFXNYgZNHgFfqfmHQC20LMCqyR0BIFq-SkPnE0BT4n_66CCMLFulPfmUOFl8cvoYptf_x3OfH6IcZ2JKdPbCrMAj4iARxqhyFHNGYjx-MUrE431Z8CFrpucYBw5xrpsa23TGHVQ_HDHkgiJLpvzdcII; sess-at-main="E4HgM2dAZoY4PVBu+s7ynvdIm6vKNR/icMU74yb96tk="; s_nr=1605687172656-Repeat; s_vnum=2036334690956%26vn%3D3; s_dslv=1605687172660; x-amz-captcha-1=1606056870683070; x-amz-captcha-2=bOPkybjvKxTBKO5DugVtjw==; session-token=mZXba7LAn/OAnCWNMZ3HXHPle1d0/yS4RRDnDo7bGoN5PkStGovzNPzNGD4KfOmnK6I/HfQ9AUC8PMDvwII5ddiS/1O8gItfExe4jMbxXXU0+AXj8E/AjTHLm09ZchR5AvcGCOGjD45s6VXBVqNwZKICtMiO/7SkfNWsj//7DMxGzIUvU76kDzazAYK0de7z;',
 # 'Host':'www.amazon.com',


}
#download_timeout = 10



# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'AmazonTest.middlewares.AmazontestSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
#See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'Amazon_su.middlewares.AmazonSuDownloaderMiddleware': 543,
   #'scrapy.downloadermiddlewares.retry.RetryMiddleware' : None,
}


# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'AmazonTest.pipelines.mysqlPipeline': 300,
   'Amazon_su.pipelines.MongoPipeline': 300,
    #存取结果放入到redis
   #'scrapy_redis.pipelines.RedisPipeline': 301,
}
MONGO_URI='localhost'
MONGO_DATABASE='Amazon'
MONGO_PORT=27017

#scrapy-redis
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#MONGD_URI ='mongodb://admin:root@192.168.110.177:27017'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False


#REDIS_URL = 'redis://192.168.:6379'
# REDIS_HOST = '192.168.110.73'
# REDIS_PORT = 6379
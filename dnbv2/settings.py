# Scrapy settings for dnbv2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dnbv2'

SPIDER_MODULES = ['dnbv2.spiders']
NEWSPIDER_MODULE = 'dnbv2.spiders'

DOWNLOADER_CLIENT_TLS_METHOD = "TLSv1.2"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT ='PostmanRuntime/7.26.8'

HTTPERROR_ALLOWED_CODES  =[403]
# DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
# DUPEFILTER_CLASS = True

# USER_AGENT = 'quotesbot (+http://www.yourdomain.com)'
# USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 3

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
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Cookie': 'SSLB=0; ak_bmsc=B81D3D7BC8247FE82A867972B2EB61A2~000000000000000000000000000000~YAAQJ40sMcLl/et5AQAAWNLw/wzs0juobJvdSPa1GBaIH4KM3ERseD/mcZcyfj1brNblcNT5XXDdItyemLVqht4Kc9ZtecnkOlhobhjHah9BuVnY1p1+0whBOn2aO1L/a0Rgew+IAI7aktd7DBJ1nXatEdpVkSo0xWgLxCthyWn2sHz2MUOlFBDMJ7l01MWOb1Bm8/nTckqHLQU5g3dWbAV+vsgnO44bHmUfkfkFdu2Zmx9bck4fnJk4S4AsG+cj/oXL5OXxHriFQbAyuFk1lEOy7WlVytn0WJ9IOpIqkJ162iZjOi9USNKioX3tMHRRDxQgjMAdmlkY2PMu/hLxtvt2T9j+S+ATIEiz73DyhsrrC4q0Bw0aWg=='
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dnbv2.middlewares.Dnbv2SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dnbv2.middlewares.Dnbv2DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'dnbv2.pipelines.Dnbv2Pipeline': 300,
#}

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

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

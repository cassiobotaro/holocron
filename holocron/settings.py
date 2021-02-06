BOT_NAME = "holocron"
SPIDER_MODULES = ["holocron.spiders"]
NEWSPIDER_MODULE = "holocron.spiders"
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0"  # noqa: E501
}
# DOWNLOAD_DELAY = 0.25
SPLASH_URL = "http://localhost:8050"
DOWNLOADER_MIDDLEWARES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,  # noqa:E501
}
SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
}
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"

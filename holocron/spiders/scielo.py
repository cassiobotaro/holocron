# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from pathlib import Path
import uuid
import math


class ScieloSpider(scrapy.Spider):
    name = "scielo"
    allowed_domains = ["search.scielo.org"]

    def start_requests(self):
        parameters = urlencode(
            {
                "q": getattr(self, "query", ""),
            }
        )
        yield scrapy.Request(f"https://search.scielo.org/?{parameters}")

    def parse(self, response):
        number_of_articles = int(
            response.css("#TotalHits::text").get(default="0").replace(" ", "")
        )
        pages = math.ceil(number_of_articles / 50)
        urls = []
        for page in range(1, pages + 1):
            parameters = urlencode(
                {
                    "q": getattr(self, "query", ""),
                    "from": ((page - 1) * 50) + 1,
                    "output": "ris",
                    "count": 50,
                    "page": page,
                    "format": "summary",
                }
            )
            urls.append(f"/?{parameters}")
        yield from response.follow_all(
            urls, callback=self.export_ris
        )

    def export_ris(self, response):
        file_uuid = uuid.uuid4()
        Path(f"articles/{file_uuid}.ris").write_bytes(response.body)

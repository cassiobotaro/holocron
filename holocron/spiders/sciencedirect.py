# -*- coding: utf-8 -*-
import uuid
import scrapy
from urllib.parse import urlencode
from pathlib import Path


class SciencedirectSpider(scrapy.Spider):
    name = "sciencedirect"
    allowed_domains = ["sciencedirect.com"]

    def start_requests(self):
        parameters = urlencode({"show": 100, "qs": getattr(self, "query", "")})
        yield scrapy.Request(
            "https://www.sciencedirect.com/search?"
            f"{parameters}"
        )

    def save_article(self, response):
        file_uuid = uuid.uuid4()
        Path(f"articles/{file_uuid}.ris").write_bytes(response.body)

    def parse(self, response):
        ids = response.css(".result-item-content h2 a::attr(href)").getall()
        ids = [id_.split("/")[-1] for id_ in ids]
        file_export_url = (
            "https://www.sciencedirect.com/sdfe/arp/cite"
            "?pii={}&format=application%2Fx-research-info-systems"
            "&withabstract=true"
        )
        yield from response.follow_all(
            (file_export_url.format(id) for id in ids),
            callback=self.save_article,
        )
        next_page = response.xpath(
            "//a[@data-aa-name='srp-next-page']/@href"
        ).get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)

# -*- coding: utf-8 -*-
import uuid
import scrapy


class SciencedirectSpider(scrapy.Spider):
    name = "sciencedirect"
    allowed_domains = ["sciencedirect.com"]
    start_urls = [
        "https://www.sciencedirect.com/search/advanced?"
        "qs=water%20AND%20leak%2A%20AND%20geophysic%2A&show=100"
    ]

    def save_article(self, response):
        file_uuid = uuid.uuid4()
        with open(f"articles/{file_uuid}.ris", "w") as f:
            f.write(response.body.decode("utf-8"))

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

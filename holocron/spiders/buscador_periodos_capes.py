# -*- coding: utf-8 -*-
import scrapy


class BuscadorPeriodosCapesSpider(scrapy.Spider):
    name = "buscador.periodicos.capes"
    allowed_domains = ["buscador.periodicos.capes.gov.br"]
    start_urls = ["https://buscador.periodicos.capes.gov.br/V?func=find-db-1"]

    def parse_areas(self, response):
        for anchor in response.css("a"):
            area = anchor.css("::text").get()
            self.log(f"listing {area}")
            id_area = anchor.css("::attr(id)").re_first(r"\d+")
            yield response.follow(
                url=f"/V/{self.session_token}/"
                f"?func=find-db-1-body-sub&sequence={id_area}",
                callback=self.parse_subareas,
                meta={"area": area},
            )

    def parse_subareas(self, response):
        for anchor in response.css("a"):
            subarea = anchor.css("::text").get()
            self.log(f"listing {subarea}")
            subarea_id = anchor.css("::attr(id)").re_first(r"\d+")
            yield response.follow(
                url=f"/V/{self.session_token}/?"
                f"func=find-db-1-category&mode=category&sequence={subarea_id}",
                callback=self.parse_bases,
                meta={"area": response.meta["area"], "subarea": subarea},
            )

    def parse_bases(self, response):
        area = response.meta["area"]
        subarea = response.meta["subarea"]
        for anchor in response.css("#nomedabase a"):
            yield {
                "name": anchor.css("::text").get(),
                "url": anchor.attrib["href"],
                "area": area,
                "subarea": subarea,
            }

        next_page = response.css("a[title='Próxima Página']::attr(href)").get()
        if next_page:
            yield response.follow(
                url=next_page,
                callback=self.parse_bases,
                meta={"area": area, "subarea": subarea},
            )

    def parse(self, response):
        self.session_token = response.css("body::attr(onload)").re_first(
            r"setCookie\(\"(.+)\","
        )
        yield response.follow(
            f"/V/{self.session_token}/?func=find-db-1-body-cat",
            callback=self.parse_areas,
        )

import scrapy
from googleScraper.items import GooglescraperItem
from scrapy.http.request import Request


class searchSpider(scrapy.Spider):
    name = "search"

    def start_requests(self):
        query = ""
        url = "https://www.google.com/search?tbm=isch&source=hp&biw=1853&bih=951&ei=TE07XJGUBpukyAOK077gCw&q={}&oq={}&gs_l=img.3..35i39j0l9.14333.14733..15768...0.0..0.113.410.2j2......1....1..gws-wiz-img.....0.bWFw5xwCwZ8"
        with open("to_search.txt") as o:
            for line in o:
                query = line.strip()
                query = "+".join(query.split(" "))
                url_query = url.format(query, query)
                yield Request(
                    url=url_query,
                    callback=self.parse,
                    meta={"title": " ".join(query.split("+"))},
                )

    def parse(self, response):

        urls = response.css("img::attr(src)").extract()
        for i in range(0, len(urls)):
            yield GooglescraperItem(
                name=response.request.meta["title"] + "_" + str(i + 1), url=urls[i]
            )


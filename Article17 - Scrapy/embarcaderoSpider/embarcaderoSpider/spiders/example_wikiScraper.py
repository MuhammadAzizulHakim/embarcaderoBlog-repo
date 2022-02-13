import scrapy
class ArticleSpider(scrapy.Spider):
    name = "wiki_spider"

    def start_requests(self):
        urls = [
            "https://en.wikipedia.org/wiki/Web_scraping",
            "https://en.wikipedia.org/wiki/Data_mining",
            "https://en.wikipedia.org/wiki/Text_mining",
            "https://en.wikipedia.org/wiki/Information_retrieval",
            "https://en.wikipedia.org/wiki/Embarcadero_Technologies",
            "https://en.wikipedia.org/wiki/Microsoft_Windows",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Delphi_(software)",
            "https://en.wikipedia.org/wiki/C%2B%2B",
            "https://en.wikipedia.org/wiki/Object-oriented_programming"]
        return [scrapy.Request(url = url, callback = self.parse)
            for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css("h1::text").extract_first()
        print("URL is: {}".format(url))
        print("Title is: {}".format(title))
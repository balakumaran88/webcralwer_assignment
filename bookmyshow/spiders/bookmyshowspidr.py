import scrapy
from bookmyshow.items import BookmyshowItem

class BookMyShow(scrapy.Spider):
     name="bookmyshow"
     start_urls=['https://in.bookmyshow.com/pune/movies']

     def parse(self, response):
         self.logger.info('hello this is bookmyshow spider')
         movies=response.css("div.__col-now-showing")
         items = BookmyshowItem()
         for movie in movies.css("div.card-container"):
             items['title'] = movie.xpath('.//@data-title').extract_first()
             items['language'] = " ".join(movie.xpath('.//@data-language-filter').extract_first().split('|')[1:])
             items['genre'] = " ".join(movie.xpath('.//@data-genre-filter').extract_first().split('|')[1:])
             items['url'] = movie.xpath('.//a/@href').extract_first()
             yield items

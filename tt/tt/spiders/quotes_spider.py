import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class QuotesSpider(scrapy.Spider):
	name = "quotes"

	def start_requests(self,start_url):
      
        for url in start_url:
            scrapy.Request(url=url, callback=self.parse)
	

	def parse(self,response):
		new_urls  = response.xpath('//*[@href]/@href').extract()
		return new_urls

	

		


		
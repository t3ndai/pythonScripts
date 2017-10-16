import scrapy 

from euros.items import EurosItem

class EuroPics(scrapy.Spider):
	name = "euros"
	allowed_domains = ["shesfreaky.com"]
	start_urls = [ 
		"http://www.shesfreaky.com/photos"
	]

	def parse(self, response):
		image = EurosItem()
		images = response.xpath("/html/body/section/div[1]/div[1]/div[7]/a")
		return image 
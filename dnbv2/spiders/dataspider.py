import os
import scrapy
path = os.getcwd()
# par_path = os.path.abspath(os.path.join(path, os.pardir))

class Dnbv2spider(scrapy.Spider):
    name = "data"

    def start_requests(self):
        file = getattr(self, 'file', None)+".txt"
        

        urls = [
        ]
        # print(par_path)
        with open(os.path.join(path,"dnbv2","temp",file),'r', encoding='utf-8') as my_file:
            for line in my_file:
                urls.append(line)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response,"-------------------")
        # print(response.xpath('//li[@class="empCon"]/span[2]/text()').get())
        print(response.xpath('//h2[@class="profile_header_title"]/text()').get())

        print(response.xpath('//a[@id="hero-company-link"]/@href').get())
        print(response.xpath('//span[@class="company_country"]/text()').get())
        print(response.xpath('//span[@class="company_summary"]/text()').get())
        print(response.xpath('//li[@class="empCon"]/span[2]/text()').get())
        print(response.xpath('//li[@class="year_started"]/span[2]/text()').get())
        print(response.xpath('//li[@class="founded"]/span[2]/text()').get())
        print(response.xpath('//div[@name="parent"]/div[1]/a/text()').get())

        yield{
            "name":response.xpath('//h2[@class="profile_header_title"]/text()').get(),
            "website":response.xpath('//a[@id="hero-company-link"]/@href').get(),
            "country":response.xpath('//span[@class="company_country"]/text()').get(),
            "summary":response.xpath('//span[@class="company_summary"]/text()').get(),
            "employeeCount":response.xpath('//li[@class="empCon"]/span[2]/text()').get(),
            "yearStarted":response.xpath('//li[@class="year_started"]/span[2]/text()').get(),
            "yearIncorporated":response.xpath('//li[@class="founded"]/span[2]/text()').get(),
            "industry":response.xpath('//span[@class="profile-industry-item"]/text() | //span[@class="profile-industry-item"]/a/text()').getall(),
            "parent":response.xpath('//div[@name="parent"]/div[1]/a/text()').get()


        }
    



# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('small.author::text').get(),
#                 'tags': quote.css('div.tags a.tag::text').getall(),
#             }
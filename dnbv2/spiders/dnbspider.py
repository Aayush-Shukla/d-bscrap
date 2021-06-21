import os
import scrapy
import json
path = os.getcwd()
# par_path = os.path.abspath(os.path.join(path, os.pardir))

class Dnbv2dnbspider(scrapy.Spider):
    name = "dnb"

    def start_requests(self):
        # file = getattr(self, 'file', None)+".json"
        

        # urls = ["https://www.dnb.com/business-directory/company-profiles.adani_green_energy_limited.9ddf6abeffc5b426d53cd0aaf76e919d.html",
        # "https://www.dnb.com/business-directory/company-profiles.adani_green_energy_limited.9ddf6abeffc5b426d53cd0aaf76e919d.html"
        # ]
        # print(par_path)
        # with open(os.path.join(path,"dnbv2","temp",file),'r') as f:
        #     data = json.load(f)
        #     for company in data:
        #         for url in company['links']:
        #             print(company["name"],url,"============================================================")
                    
        #             yield scrapy.Request(url=url,dont_filter=True, callback=self.parselink, meta={"args":company,"url":url})
        yield scrapy.Request(url=r"https://www.dnb.com/business-directory/top-results.html?term=marico%20middle%20east%20fze&page=1",dont_filter=True, callback=self.parselink)

        
        # for url in urls:
        #     print("-------------------------------------===========================================22222222")
        #     yield scrapy.Request(url=url,dont_filter=True, callback=self.parse)

    def parselink(self, response):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(response.css('.search_result .col-md-4 .primary_name a').get())
        # print(response.css('a[href]').getall())
            
        filename = "ffl" + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

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
            "excel_name":response.meta.get("args")['name'],
            "excel_country":response.meta.get("args")['country'],
            "name":response.xpath('//h2[@class="profile_header_title"]/text()').get(),
            "country":response.xpath('//span[@class="company_country"]/text()').get(),
            "dnb_url":response.meta.get("url"),
            "website":response.xpath('//a[@id="hero-company-link"]/@href').get(),
            "parent":response.xpath('//div[@name="parent"]/div[1]/a/text()').get(),
            
            "yearStarted":response.xpath('//li[@class="year_started"]/span[2]/text()').get(),
            "yearIncorporated":response.xpath('//li[@class="founded"]/span[2]/text()').get(),
            "employeeCount":response.xpath('//li[@class="empCon"]/span[2]/text()').get(),
            "industry":response.xpath('//span[@class="profile-industry-item"]/text() | //span[@class="profile-industry-item"]/a/text()').getall(),
            
            "summary":response.xpath('//span[@class="company_summary"]/text()').get()


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
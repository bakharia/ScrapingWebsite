import scrapy
import pandas as pd
import json
from scrapy.exceptions import CloseSpider

# API http://api.serpstack.com/
# KEY da1549565f1c9ed0b7b4c712dbd74d96


class PriceItemsSpider(scrapy.Spider):
    name = 'price_items'

    df = pd.read_csv('/home/bakharia/assignment/Task4/Task4/Greendeck Business Analyst Assignment Task 4 - Sheet1.csv') #CSV file to be referenced
    index = 0 #used to keep track of different google search codes

    allowed_domains = ['api.serpstack.com']
    start_urls = [f'http://api.serpstack.com/search?access_key=da1549565f1c9ed0b7b4c712dbd74d96&query=site:oneill.com/fr "{df.iloc[index,2]}"&auto_location=0&location=france&gl=fr']

    def parse(self, response):
        results = json.loads(response.body)
        
        #Checking if the product exists on the website
        if results['organic_results']: 
            results = results['organic_results'][0]
        else:
            yield{
                'Price(Euros)': 'Not available',
                'Product Page URL': 'Not available'
            }
            self.index += 1
            
            if self.index < 130: #checking to see if the all the data has been scraped
                
                yield scrapy.Request(
                    url=f'http://api.serpstack.com/search?access_key=da1549565f1c9ed0b7b4c712dbd74d96&query=site:oneill.com/fr "{self.df.iloc[self.index,2]}"&auto_location=0&location=france&gl=fr',
                    callback=self.parse,
                     headers={
                         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                     }
                 )
                 
            else:
                raise CloseSpider('Reached last page...') 
        
        self.index += 1 #moving to the next reference code
       
        #navigating to the product url to scrape its price 
        yield response.follow(url=results['url'], callback=self.parse_items, dont_filter = True, 
            headers={
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                        'referer': None
                    },
            meta={
                'link': results['url']
                }
        )

    def parse_items(self, response): #parsing items from the product's web page
        
        yield{
            'Price(Euros)': response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/span/span[2]/span/@content').get(),
            'Product Page URL': response.request.meta['link']
        }
        
        if self.index < 130: #checking to see if the all the data has been scraped
            yield scrapy.Request(
                url = f'http://api.serpstack.com/search?access_key=da1549565f1c9ed0b7b4c712dbd74d96&query=site:oneill.com/fr "{self.df.iloc[self.index,2]}"&auto_location=0&location=france&gl=fr', 
                callback=self.parse, 
                headers={
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                }
            )
        else:
           raise CloseSpider('Reached last page...') 

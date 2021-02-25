import scrapy
import json
from scrapy.exceptions import CloseSpider

#API https://www.next.co.uk/clearance/results/search?w=*&af=gender:men%20gender:men%20&srt=24
#IMG https://xcdn.next.co.uk/COMMON/Items/Default/Default/ItemImages/Sale/446036.jpg

#here the website had infinite scrolling and the items were being loaded from an API, also image urls didnt have their complete path so I had to extract from the
#console

class ClearShopSpider(scrapy.Spider):
    name = 'clear_shop'

    INCREMENT_BY = 24 #Only 24 items were being loaded on each API call, so for successive calls the offset had to be incremented by 24
    offset = 0

    allowed_domains = ['next.co.uk/']
    start_urls = ['https://www.next.co.uk/clearance/results/search?w=*&af=gender:men%20gender:men%20&srt=0']

    def parse(self, response):
        #checking if we the api still exists
        if(response.status == 500):
            raise CloseSpider('Reached last page...')

        items = json.loads(response.body)
        
        for item in items:
            price = item.get('History')
            if price:
                price = price['PriceHistory'] #I chose price history here since in the api no direct price was given and price history is also not of fixed size
            yield{
                'Name': item.get('Name'),
                'Brand': item.get('Brand'),
                'Price': price,
                'Image_url': f"https://xcdn.next.co.uk/COMMON/Items/Default/Default/ItemImages/Sale{item.get('SearchImage')}",  #getting the complete image url
                'Product_url': item.get('Url')
            }

        self.offset += self.INCREMENT_BY
        yield scrapy.Request(
            url = f'https://www.next.co.uk/clearance/results/search?w=*&af=gender:men%20gender:men%20&srt={self.offset}',
            callback=self.parse,
            dont_filter = True
        )

import scrapy
import os
from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader
from Task2.items import Task2Item
from Task2.pipelines import Task2Pipeline
#I have used splash here since items were linked to javascript

class SnowboardSpider(scrapy.Spider):
    name = 'snowboard'
    allowed_domains = ['blue-tomato.com']
    start_urls = ['https://blue-tomato.com/']

    saveLocation = os.getcwd()

    custom_settings = { # For downloading the images pipeline items priority and storage location is being set
        "ITEM_PIPELINES": {'scrapy.pipelines.images.ImagesPipeline': 1},
        "IMAGES_STORE": saveLocation
    }
    
    home = 0 # check if we are on the home page, kind of a flag as two scripts are required for different cases

    #Usinng splash,
    # In the first script I am accessing the websites home page to change the location and then clicking on snowboard category to reach the desired web page.
    # In the second script I just load the page.
    def script(self, n):
        if n == 0:
            self.home += 1
            _script = """
                function main(splash, args)
                    splash.private_mode_enabled = false
                    splash:on_request(function(request)
                        request:set_header('User-Agent',  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
                    end)
                    assert(splash:go(args.url))
                    assert(splash:wait(0.5))  
                    country_btn = assert(splash:select("#languageAndCountryFlyout"))
                    country_btn:mouse_click()
                    assert(splash:wait(0.5))
                    country = assert(splash:select("a[href ^='/de-AT/']"))
                    country:mouse_click()
                    assert(splash:wait(1))
                    category = assert(splash:select_all(".js-category"))
                    category[5]:mouse_click()
                    assert(splash:wait(0.5))
                    category[5]:mouse_click()
                    assert(splash:wait(2))
                    return splash:html()
                end
                """
            return _script
        else:
            _script="""
                function main(splash, args)
                    splash.private_mode_enabled = false
                    splash:on_request(function(request)
                        request:set_header('User-Agent',  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
                    end)
                    assert(splash:go(args.url))
                    assert(splash:wait(2))
	                return splash:html()
                    end
                    """
            return _script

    def start_request(self):
        yield SplashRequest(url = 'https://blue-tomato.com/', callback=self.parse, endpoint="execute", args={
            'lua_source': self.script(self.home)
        })

    def parse(self, response):
        
        for snowboard in response.xpath("//li[@class='productcell ']"): #loading web page elements
            
            details = snowboard.xpath('normalize-space(.//span[2]/a/div/div/p/text())').get()
            details = details.split(' ')
            image_url = snowboard.xpath('.//span[1]/img/@data-src').get()
            
            if not image_url:
                image_url = snowboard.xpath(' .//span[1]/img/@src').get()
            yield{
                'Name': details[-1],
                'Brand': ' '.join(details[:-1]),
                'Price': snowboard.xpath('normalize-space(.//span[2]/span/text())').get(),
                'Image_url': f"https:{image_url}",
                'Product_url': response.urljoin(snowboard.xpath('(.//span[2]/a/@href)').get()),
            }

            #for downloading images
            loader = ItemLoader(item = Task2Item(), selector= snowboard) 
            absolute_url = f"https:{image_url}"
            loader.add_value('image_urls', absolute_url)
            loader.add_value('image_name', ''.join(snowboard.xpath(".//span[1]/img/@alt").get()))
            yield loader.load_item()

        #getting next page's link
        next_page = response.urljoin(response.xpath("//section[@class='filter'][2]/div[2]/nav/ul/li[3]/a/@href").get())
        if next_page:#checking if it exists
          yield SplashRequest(url = next_page, callback= self.parse, endpoint='execute', args={
            'lua_source': self.script(self.home)
        })

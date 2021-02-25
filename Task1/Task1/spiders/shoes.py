import scrapy
#I chose to use cookies in this code since it was making scraping much easier

class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    allowed_domains = ['matchesfashion.com'] # the domain to be reffered to

    def start_requests(self):

        #url here is the first link to be hit and call back calls the function to called on laoding of the page
        yield scrapy.Request(url = 'https://www.matchesfashion.com/intl/mens/shop/shoes?page=1&noOfRecordsPerPage=240&sort=', callback=self.parse, headers={ 
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Cookie': 'plpLayoutMobile=2; plpLayoutTablet=2; plpLayoutDesktop=3; plpLayoutLargeDesktop=4; SESSION_TID=KGS8YPMQFULS6-JB04WM; _pxhd=0ba0b7584f5d322dd63a5216338c92387e8a6a826b5504ab74eb7a3ff8c67238:494f90c0-187a-11eb-bcc6-3351de1ef953; language=en; loggedIn=false; saleRegion=ROW; _dy_csc_ses=t; _dy_c_exps=; fsm_uid=4e472802-ac85-51a4-e93a-f9a792525710; AMCVS_62C33A485B0EB69A0A495D19%40AdobeOrg=1; _dycnst=dg; _ga=GA1.2.112806565.1603819909; _gid=GA1.2.2008585027.1603819909; _dyid=3958664958825748869; _dyjsession=4999df1411180b87ac22ed0281b3b9ab; _dy_geo=IN.AS.IN_DL.IN_DL_New%20Delhi; _dy_df_geo=India..New%20Delhi; _fbp=fb.1.1603819909517.22722100; _cs_c=0; s_cc=true; _pin_unauth=dWlkPVpHRmpaVE15TldZdFl6aGhNQzAwTW1RekxUaG1PRFl0WXpnMU9UUTVaVGRoWWpCbQ; _gcl_au=1.1.188477212.1603819911; rskxRunCookie=0; rCookie=ki0npzzffq3murlth4zslkgs8yrty; sizeTaxonomy=""; gender=mens; _dy_c_att_exps=; _dyid_server=3958664958825748869; _pxvid=494f90c0-187a-11eb-bcc6-3351de1ef953; ab-user-id=14; signed-up-for-updates=true; country=DEU; billingCurrency=EUR; indicativeCurrency=""; _dyfs=1603820171439; _dycst=dk.l.c.ws.; cb-shown=true; cb-enabled=accepted; fsm_sid=044c5461-22a3-e228-2254-a00e76ea9d14; dy_fs_page=www.matchesfashion.com%2Fintl%2Fmens; _gat_ga_launch=1; JSESSIONID=s6~E4D4414F602AC0905651CD77E4AB5456; AMCV_62C33A485B0EB69A0A495D19%40AdobeOrg=1075005958%7CMCIDTS%7C18563%7CMCMID%7C37470743692731149954173231591479963314%7CMCAAMLH-1604486259%7C12%7CMCAAMB-1604486259%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1603888659s%7CNONE%7CvVersion%7C4.4.1; defaultSizeTaxonomy=MENSSHOESEUITSEARCH; _dy_ses_load_seq=36783%3A1603881466046; gpv_pn=mens%3Ashop%3Ashoes; _dy_lu_ses=4999df1411180b87ac22ed0281b3b9ab%3A1603881466896; _dy_toffset=0; _dy_soct=1003595.1005104.1603881457*1011332.1019298.1603881466*1022774.1040843.1603881466*1001485.1001871.1603881466*1005435.1008201.1603881466; AWSALB=QebTuXiNJFnC5j+Ai2q44PuDm5IfT8/OiQ2sLcOStYCEREKklzR0EWslgTl8iwupAorqT/mdNFeguHWViWIulHM3mtetlPMOwQtIt3qkJUlZ/vYkkTPnfzbf+tXa; AWSALBCORS=QebTuXiNJFnC5j+Ai2q44PuDm5IfT8/OiQ2sLcOStYCEREKklzR0EWslgTl8iwupAorqT/mdNFeguHWViWIulHM3mtetlPMOwQtIt3qkJUlZ/vYkkTPnfzbf+tXa; _cs_id=5db0e0eb-9bbd-a27f-d2ac-657f03592d35.1603819910.4.1603881468.1603881459.1.1637983910420.Lax.0; _cs_s=2.1; sailthru_pageviews=2; s_sq=%5B%5BB%5D%5D; _uetsid=4cabc4d0187a11eba1f2570f96f68a7c; _uetvid=4cac6060187a11eba52ddd4883ac60f0; lastRskxRun=1603881468828; sailthru_content=3a19aaad7fa1bfc26cd6a1dda47cf67c18e717a1e84a3855783ff5c6e9c0bc342689d7ddf369291ccf84176d6b49e68b973a97067d5166bd3b56377001a5bed2; sailthru_visitor=0e39db28-adff-4be5-b2aa-e04c0509f54d; _px2=eyJ1IjoiOWZhMGZjZTAtMTkwOS0xMWViLWE3YzQtZDliNTk3NGRjZDc4IiwidiI6IjQ5NGY5MGMwLTE4N2EtMTFlYi1iY2M2LTMzNTFkZTFlZjk1MyIsInQiOjE2MDM4ODE5Njk5NTEsImgiOiI2ZGI0N2YyNmE1YmNjZGYwNGFjNTM2MWJjZjM4YTZkMjM1ZDQ4YTkyZTc4YThlM2IxMjRmMGZlMGE0OGVhMzM0In0='
        }) #user agent and cookie had to set get the relevant information

    def parse(self, response):
        shoes = response.xpath("//div[@class='lister__item__inner']")

        for shoe in shoes:
            yield {
                'name'        : shoe.xpath(".//a/div[@class='lister__item__details']/text()").get(),
                'brand'       : shoe.xpath(".//a/div[@class='lister__item__title']/text()").get(),
                'price'       : shoe.xpath(".//a/div[@class='lister__item__price']/span/text()").get(),
                'image_url'   : response.urljoin(shoe.xpath(".//div/a/img/@data-original").get()),
                'product_url' : response.urljoin(shoe.xpath(".//div/a/@href").get())
            }

        #the url of the next page from the next page button on the page
        next_page = response.urljoin(response.xpath("//li[@class = 'next'][1]/a/@href").get()) 
        if next_page:
            yield scrapy.Request(url = next_page, callback= self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                'Cookie': 'plpLayoutMobile=2; plpLayoutTablet=2; plpLayoutDesktop=3; plpLayoutLargeDesktop=4; SESSION_TID=KGS8YPMQFULS6-JB04WM; _pxhd=0ba0b7584f5d322dd63a5216338c92387e8a6a826b5504ab74eb7a3ff8c67238:494f90c0-187a-11eb-bcc6-3351de1ef953; language=en; loggedIn=false; saleRegion=ROW; _dy_csc_ses=t; _dy_c_exps=; fsm_uid=4e472802-ac85-51a4-e93a-f9a792525710; AMCVS_62C33A485B0EB69A0A495D19%40AdobeOrg=1; _dycnst=dg; _ga=GA1.2.112806565.1603819909; _gid=GA1.2.2008585027.1603819909; _dyid=3958664958825748869; _dyjsession=4999df1411180b87ac22ed0281b3b9ab; _dy_geo=IN.AS.IN_DL.IN_DL_New%20Delhi; _dy_df_geo=India..New%20Delhi; _fbp=fb.1.1603819909517.22722100; _cs_c=0; s_cc=true; _pin_unauth=dWlkPVpHRmpaVE15TldZdFl6aGhNQzAwTW1RekxUaG1PRFl0WXpnMU9UUTVaVGRoWWpCbQ; _gcl_au=1.1.188477212.1603819911; rskxRunCookie=0; rCookie=ki0npzzffq3murlth4zslkgs8yrty; sizeTaxonomy=""; gender=mens; _dy_c_att_exps=; _dyid_server=3958664958825748869; _pxvid=494f90c0-187a-11eb-bcc6-3351de1ef953; ab-user-id=14; signed-up-for-updates=true; country=DEU; billingCurrency=EUR; indicativeCurrency=""; _dyfs=1603820171439; _dycst=dk.l.c.ws.; cb-shown=true; cb-enabled=accepted; fsm_sid=044c5461-22a3-e228-2254-a00e76ea9d14; dy_fs_page=www.matchesfashion.com%2Fintl%2Fmens; _gat_ga_launch=1; JSESSIONID=s6~E4D4414F602AC0905651CD77E4AB5456; AMCV_62C33A485B0EB69A0A495D19%40AdobeOrg=1075005958%7CMCIDTS%7C18563%7CMCMID%7C37470743692731149954173231591479963314%7CMCAAMLH-1604486259%7C12%7CMCAAMB-1604486259%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1603888659s%7CNONE%7CvVersion%7C4.4.1; defaultSizeTaxonomy=MENSSHOESEUITSEARCH; _dy_ses_load_seq=36783%3A1603881466046; gpv_pn=mens%3Ashop%3Ashoes; _dy_lu_ses=4999df1411180b87ac22ed0281b3b9ab%3A1603881466896; _dy_toffset=0; _dy_soct=1003595.1005104.1603881457*1011332.1019298.1603881466*1022774.1040843.1603881466*1001485.1001871.1603881466*1005435.1008201.1603881466; AWSALB=QebTuXiNJFnC5j+Ai2q44PuDm5IfT8/OiQ2sLcOStYCEREKklzR0EWslgTl8iwupAorqT/mdNFeguHWViWIulHM3mtetlPMOwQtIt3qkJUlZ/vYkkTPnfzbf+tXa; AWSALBCORS=QebTuXiNJFnC5j+Ai2q44PuDm5IfT8/OiQ2sLcOStYCEREKklzR0EWslgTl8iwupAorqT/mdNFeguHWViWIulHM3mtetlPMOwQtIt3qkJUlZ/vYkkTPnfzbf+tXa; _cs_id=5db0e0eb-9bbd-a27f-d2ac-657f03592d35.1603819910.4.1603881468.1603881459.1.1637983910420.Lax.0; _cs_s=2.1; sailthru_pageviews=2; s_sq=%5B%5BB%5D%5D; _uetsid=4cabc4d0187a11eba1f2570f96f68a7c; _uetvid=4cac6060187a11eba52ddd4883ac60f0; lastRskxRun=1603881468828; sailthru_content=3a19aaad7fa1bfc26cd6a1dda47cf67c18e717a1e84a3855783ff5c6e9c0bc342689d7ddf369291ccf84176d6b49e68b973a97067d5166bd3b56377001a5bed2; sailthru_visitor=0e39db28-adff-4be5-b2aa-e04c0509f54d; _px2=eyJ1IjoiOWZhMGZjZTAtMTkwOS0xMWViLWE3YzQtZDliNTk3NGRjZDc4IiwidiI6IjQ5NGY5MGMwLTE4N2EtMTFlYi1iY2M2LTMzNTFkZTFlZjk1MyIsInQiOjE2MDM4ODE5Njk5NTEsImgiOiI2ZGI0N2YyNmE1YmNjZGYwNGFjNTM2MWJjZjM4YTZkMjM1ZDQ4YTkyZTc4YThlM2IxMjRmMGZlMGE0OGVhMzM0In0='
            })


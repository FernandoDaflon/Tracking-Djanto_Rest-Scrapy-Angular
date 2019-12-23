import scrapy
from scrapy_splash import SplashRequest


class AfSpiderSpider(scrapy.Spider):
    name = 'af_spider'
    allowed_domains = ['www.afklcargo.com/mycargo/shipment/detail']

    script = '''
                function main(splash, args)
                      splash.private_mode_enabled = false
                      splash:on_request(function(request)
                            request:set_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')
                        end)
                      url = args.url
                      assert(splash:go(url))  
                      assert(splash:wait(12))
                      splash:set_viewport_full()
                      return {
                        image = splash:png(),
                        html = splash:html()
                      }
                end

            '''

    def start_requests(self):
        # awb = input('AWB:')
        # yield SplashRequest(url="https://www.afklcargo.com/mycargo/shipment/detail/" + awb, callback=self.parse, endpoint="execute", args={
        #     'lua_source': self.script
        # })
        yield SplashRequest(url="https://www.afklcargo.com/mycargo/shipment/detail/057-84529664", callback=self.parse,
                            endpoint="execute", args={
                'lua_source': self.script
            })

    def parse(self, response):
            # print(response.body)
            for flight_data in response.xpath('//div/*[@class="l-flight-schedule ng-star-inserted"]'):
                origemt = flight_data.xpath("normalize-space((.//div/span/text()))").get(),
                origem = origemt[0]
                destinot = flight_data.xpath("normalize-space((.//div/span[2]/text()))").get(),
                destino = destinot[0]
                Iata_flightt = flight_data.xpath("normalize-space(.//div[3]/span[1]/text())").get() + flight_data.xpath("normalize-space(.//div[3]/span[2]/text())").get(),
                Iata_flight = Iata_flightt[0]
                ETDt = flight_data.xpath("normalize-space((.//div/div[1]/span[1]/text()))").get(),
                ETD = ETDt[0]
                ETAt = flight_data.xpath("normalize-space((.//div[4]/div[2]/span/text()))").get(),
                ETA = ETAt[0]
                Status = flight_data.xpath("normalize-space(.//div[6]/span/text())").get()

                yield {
                    'ori': origem,
                    'des': destino,
                    'flight_no': Iata_flight,
                    'eta': ETA,
                    'etd': ETD,
                    'status': Status
                }


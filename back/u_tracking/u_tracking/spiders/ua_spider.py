import scrapy
from scrapy_splash import SplashRequest


class UaSpiderSpider(scrapy.Spider):
    name = 'ua_spider'
    allowed_domains = ['www.unitedcargo.com']


    script = '''
                    function main(splash, args)
                          splash.private_mode_enabled = false
                          splash:on_request(function(request)
                                request:set_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')
                            end)
                          url = args.url
                          assert(splash:go(url))  
                          assert(splash:wait(10))
                          splash:set_viewport_full()
                          return {
                            image = splash:png(),
                            html = splash:html()
                          }
                    end

                '''

    def start_requests(self):

        # awb = input('AWB:')
        # yield SplashRequest(url="https://www.unitedcargo.com/OurNetwork/TrackingCargo1512/Tracking.jsp?id=" + awb + '&pfx=016', callback=self.parse, endpoint="execute", args={
        #     'lua_source': self.script
        # })

        yield SplashRequest(url="https://www.unitedcargo.com/OurNetwork/TrackingCargo1512/Tracking.jsp?id=36854031&pfx=016", callback=self.parse,
                            endpoint="execute",  args={
                'lua_source': self.script
         })

    def parse(self, response):

        # print(response.body)
        # print('')
        # print('=============')
        # print('')
        # yield response.xpath("//*[@id=''MovementDetails0'][contains[text(), 'Manifested')].text()")
        # Status = response.xpath('//*[@id="MovementDetails0"]/ul[8]/li[2]/text()').get()
        # Status = response.xpath('//*[@id="MovementDetails0"]/ul/li[2]/text()').extract()
        # iata = response.xpath("//*[contains(text(),'Manifested')]/following-sibling::node()[2]/text()").get()
        # status = response.xpath("//*[contains(text(),'Manifested')]/text()").get()
        # ori = response.xpath("//*[contains(text(),'Manifested')]/following::li[3]/div[1]/text()").get()
        # des = response.xpath("//*[contains(text(),'Manifested')]/following::li[3]/div[3]/text()").get()
        # eta = response.xpath("//*[contains(text(),'Manifested')]/following::li[3]/div[4]/text()").get()
        # etd = response.xpath("//*[contains(text(),'Manifested')]/following::li[3]/div[2]/text()").get()

        # for flight_data in response.xpath('//*[@id="MovementDetails0"]//ul')[1:]:
        for flight_data in response.xpath('//*[@id="MovementDetails0"]//ul'):
            dados_concat = flight_data.xpath('.//li//text()').getall()
            # dados_concat = flight_data.xpath('.//li//text()')[1:4].getall()
            print(dados_concat)
            pass
        print('')
        print('=============')
        print('')
        for flight_data2 in response.xpath('//*[@id="MovementDetails0"]//ul')[1:]:
            ori_concat = flight_data2.xpath('.//li//text()')[7].get()
            des_concat = flight_data2.xpath('.//li//text()')[4].get()
            iata_concat = flight_data2.xpath('.//li//text()')[3].get()
            etd_concat = flight_data2.xpath('.//li//text()')[6].get()
            eta_concat = flight_data2.xpath('.//li//text()')[8].get()
            status_concat = flight_data2.xpath('.//li//text()')[1].get()

            print('{} - {} - {} - {} - {} - {}'.format(ori_concat, des_concat, iata_concat, etd_concat, eta_concat,
                                                       status_concat))



            print('')
            print('=============')
            print('')
            yield {
                'ori': ori_concat,
                'des': des_concat,
                'flight_no': iata_concat,
                'eta': eta_concat,
                'etd': etd_concat,
                'status': status_concat
            }

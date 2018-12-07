
import json
import datetime
import dateparser

from urllib.parse import urlparse
from scrapy import Spider, Request


class Weather(Spider):
    # 中国天气爬虫
    name = 'zgtq'
    start_urls = ['http://www.weather.com.cn/textFC/hb.shtml']
    # 用于后续增添抓取源时作为区分标记: 如该网站挂了
    site = urlparse(start_urls[0]).netloc

    def parse(self, response):
        for url in response.css(".lqcontentBoxheader a::attr(href)").extract():
            url = response.urljoin(url)
            yield Request(url, callback=self.parse_provinces)

    def parse_provinces(self, response):
        for url in response.css("div.hanml > div:nth-child(1) td.last a::attr(href)").extract():
            url = response.urljoin(url)
            yield Request(url, callback=self.parse_cityies_and_counties)

    def parse_cityies_and_counties(self, response):
        # 获取当天实时数据、6天预测数据
        seven_day = response.css(".sky")
        days = []
        for i, day in enumerate(seven_day):
            d = {}
            d['weather'] = day.css('.wea::text').extract_first().strip()
            # 温度有三种情况：-10℃,7℃/-8℃,7/-8℃
            high_temp = day.css('.tem span::text').extract_first()
            low_temp = day.css('.tem i::text').extract_first()
            if not high_temp:
                # -10℃
                d['temperature'] = low_temp
            else:
                *low_temp, temp_unit = low_temp
                low_temp = ''.join(low_temp)
                if high_temp[-1] == temp_unit:
                    # 7℃/-8℃
                    d['temperature'] = '~'.join([low_temp, high_temp])
                else:
                    # 7/-8℃
                    d['temperature'] = '~'.join([low_temp, high_temp]) + temp_unit
            if i == 0:
                wind = day.css('.win span::attr(title)').extract()
                # 只有一个风向：如果18点以后抓取会有该情况
                # 或者：全天一个风向
                if len(wind) == 1 or \
                        wind[0] == wind[1]:
                    wind = wind[0]
                else:
                    wind = '转'.join(wind)
                d['wind_direction'] = wind
                d['wind_level'] = day.css('.win i::text').extract_first()
            days.append(d)

        # 只获取了当天温度走势图数据
        # 湿度、降水量等看后续需求添加
        hour3data = json.loads(response.css('script').re_first('var hour3data=(.+?)\s*</script'))
        hours = []
        for hour in hour3data['1d']:
            d = {}
            data = hour.split(',')
            d['time'] = data[0]
            d['weather'] = data[2]
            d['temperature'] = data[3]
            d['wind_direction'] = data[4]
            d['wind_level'] = data[5]
            hours.append(d)

        # 获取生活指数数据
        _, index = response.css(".curve_livezs")
        indexs = index.css('.show li')
        idxs = []
        for index in indexs:
            d = {}
            d['title'] = index.css('em::text').extract_first().strip()
            d['advice'] = index.css('p::text').extract_first()
            if d['advice']:
                d['advice'] = d['advice'].strip()
            else:
                # 无建议
                d['advice'] = ''
            is_star = index.css("span em")
            if not is_star:
                d['level'] = index.css('span::text').extract_first().strip()
            else:
                stars = index.css('.star')
                # 减肥指数用星表示
                d['level'] = str(len(stars)) + '星'
            idxs.append(d)

        # 其它标注
        location = response.css(
                "body > div.con.today.clearfix > div.left.fl > div.ctop.clearfix > div.crumbs.fl").xpath(".//text()").re("\w+")
        location = '-'.join(location)
        pub_time = response.css("#update_time::attr(value)").extract_first()
        pub_time = dateparser.parse(pub_time)
        url = response.url
        craw_time = datetime.datetime.now()

        # 填充数据
        item = {}
        item['location'] = location
        item['pub_time'] = pub_time
        item['from_url'] = url
        item['craw_time'] = craw_time
        item['today'], *item['days'] = days
        item['hours'] = hours
        item['indexs'] = idxs
        yield item

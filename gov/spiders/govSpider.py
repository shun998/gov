# -*- coding: utf-8 -*-
import re

import scrapy

from gov.items import GovItem


class GovspiderSpider(scrapy.Spider):
    name = 'govSpider'
    allowed_domains = ['banshi.beijing.gov.cn']
    start_urls = [
        'http://banshi.beijing.gov.cn/pubtask/task/1/110101000000/d2c3e807-269b-4c52-ae29-1ce3a7709c21.html?locationCode=110101000000',
        'http://banshi.beijing.gov.cn/pubtask/task/1/110101000000/f2dae3ba-a26a-4828-a90c-08643c28342b.html?locationCode=110101000000',
        'http://banshi.beijing.gov.cn/pubtask/task/1/110000000000/945eba28-ba6c-401c-b861-3b1373eda4c4.html?locationCode=110000000000',
        'http://banshi.beijing.gov.cn/pubtask/task/1/110101000000/e74ed284-7ea3-4c1e-b2c5-8337bf1e1463.html?locationCode=110101000000']

    def parse(self, response):
        item = GovItem()
        type = response.xpath('/html/body/div[2]/div/p[2]/span/text()').get()
        located = response.xpath('//div[@class="bszn-city-d"]//span/text()').get()
        body = response.xpath('//*[@id="basic-main"]/table/tr[3]/td[2]/text()').get()
        time = str(response.xpath('//*[@id="basic-main"]/table/tr[4]/td[2]/text()').get()).strip()
        address = str(response.xpath('//*[@id="basic-main"]/table/tr[5]/td[2]/text()').get()).strip()
        obj = re.compile(
            r'var process = .*?"PHASE_APPROVE":"(?P<PHASE_APPROVE>.*?)",.*?"PHASE_RESULT":"(?P<PHASE_RESULT>.*?)".*?material.*?"M_INDEX":"(?P<M_INDEX>.*?)","M_NAME":"(?P<M_NAME>.*?),.*?"}];',
            re.S)
        result = obj.finditer(str(response.text))
        for it in result:
            process = it.group('PHASE_APPROVE')
            M_INDEX = it.group('M_INDEX')
            M_NAME = it.group('M_NAME')
            # print(condition, M_INDEX, M_NAME)
            material = [M_INDEX, M_NAME]
        condition = response.xpath('//*[@id="basic-main"]/table/tr[17]/td[2]/text()').get()
        method = response.xpath('/html/body/div[3]/div/div[3]/div[2]/div[1]/p[2]/span[1]/text()').get()
        item['type'] = type
        item['located'] = located
        item['body'] = body
        item['time'] = time
        item['address'] = address
        item['process'] = process
        item['material'] = material
        item['condition'] = condition
        item['method'] = method
        # print(item)
        yield item

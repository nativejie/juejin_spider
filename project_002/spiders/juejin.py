# -*- coding: utf-8 -*-
import scrapy
import json
from project_002.items import Project002Item

class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['www.juejin.im']
    start_urls = ['http://www.juejin.im/']
    headers = {
        "X-Agent": "Juejin/Web",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Content-Type": "application/json",
        "Host": "web-api.juejin.im",
        "Origin": "https://juejin.im"
    }

    def parse(self, response):
        pass

    def parse_item(self, response):
        print('进入此步骤,响应为')
        item = Project002Item()
        edges = json.loads(response.text)['data']['articleFeed']['items']['edges']
        temp = []
        for edge in edges:
            node = edge['node']
            temp.append({"title": node['title'], "url": node['originalUrl'], "like": node['likeCount'], 'content': node['content'], 'user': node['user']['username'], 'updated_date': node['updatedAt'], 'category': node['category']['name'], 'article_id': node['id']})
        item = temp
        return item

    def start_requests(self):
        url = 'https://web-api.juejin.im/query'
        query_date = {"operationName":"","query":"","variables":{"first":100,"after":"","order":"MONTHLY_HOTTEST"},"extensions":{"query":{"id":"21207e9ddb1de777adeaca7a2fb38030"}}}
        response = scrapy.Request(url, method="POST",headers=self.headers, body=json.dumps(query_date),callback=self.parse_item)
        yield response

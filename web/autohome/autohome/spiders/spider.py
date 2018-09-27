# Author: Charles
# 公众号: Charles的皮卡丘
# 爬虫主程序
import json
from scrapy import Spider, Request
from autohome.items import AutohomeItem


class mySpider(Spider):
	name = 'autohome'
	allowed_domains = ['you.autohome.com.cn/']
	def start_requests(self):
		for page in range(4828):
			yield Request('https://you.autohome.com.cn/summary/getsearchresultlist?ps=20&pg={}&type=3&tagCode=&tagName=&sortType=3'.format(page), self.parse)
	def parse(self, response):
		result = json.loads(response.text).get('result').get('hitlist')
		item = AutohomeItem()
		for page in result:
			item['title'] = page.get('title')
			item['author'] = page.get('author')
			item['authorId'] = page.get('authorId')
			item['publishDate'] = page.get('publishDate')
			item['updateDate'] = page.get('updateDate')
			item['topicId'] = page.get('topicId')
			item['viewCount'] = page.get('viewCount')
			item['replyCount'] = page.get('replyCount')
			item['url'] = 'https://you.autohome.com.cn/' + page.get('url')
			item['content'] = page.get('content')
			yield item
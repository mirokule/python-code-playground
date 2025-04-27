import scrapy
import random
import time


class ImdbTop250Spider(scrapy.Spider):
    name = 'imdb_top250'
    start_urls = ['https://www.imdb.com/chart/top/']

    # 模拟不同的 User - Agent
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    ]

    def start_requests(self):
        for url in self.start_urls:
            # 随机选择一个 User - Agent
            headers = {
                'User - Agent': random.choice(self.user_agents)
            }
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # 随机暂停一段时间，模拟人类浏览行为
        time.sleep(random.uniform(1, 3))

        for movie in response.css('tbody.lister - list tr'):
            name = movie.css('td.titleColumn a::text').get()
            rating = movie.css('td.ratingColumn.imdbRating strong::text').get()
            yield {
                'name': name,
                'rating': rating
            }

        # 处理分页（如果有）
        next_page = response.css('a.next - page::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            headers = {
                'User - Agent': random.choice(self.user_agents)
            }
            yield scrapy.Request(next_page_url, headers=headers, callback=self.parse)

import asyncio
import aiohttp
import urllib
import sys

# Relative import
from utils.urlDictonary import urlDict

# path to be appended
sys.path.append("../../src")


class ProductScrapper:
    def __init__(self, search_keyword):
        self.search_keyword = search_keyword

    def url_mapper(self, url, body):
        pass

    async def assign_task(self, url):
        search_url = urlDict[url]['url'] + urllib.parse.quote_plus(self.search_keyword)
        print(search_url)
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(search_url, ssl=False) as resp:
                body = await resp.text()
                return self.url_mapper(url, body)

        return 1

    async def scrape_data(self):
        tasks = []
        for url in urlDict:
            html = asyncio.create_task(ProductScrapper.assign_task(self, url))
            tasks.append(html)
        await asyncio.gather(*tasks)


# Use the Person class to create an object, and then execute the printname method:

x = ProductScrapper("iphone 12")
data = asyncio.run(x.scrape_data())

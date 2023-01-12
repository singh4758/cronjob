import asyncio
import aiohttp
import urllib
import time

from src.utils.urlDictonary import urlDict

from src.utils.urlMapper import switcher


class PriceScrapper:

    def __init__(self, search):
        self.search = search
        self.product_list = []

    async def html_scrape(self, url, session):
        search_url = urlDict[url]['url'] + self.search
        async with session.get(search_url, ssl=False) as resp:
            print("Scrapping" + " " + url + " " + "started........")
            body = await resp.text()
            res = switcher.get(url)(body)
            self.product_list.extend(res)
            print("Scrapping" + " " + url + " " + "end")
            return res

    async def api_scrape(self, url, session):
        fetch_url = urlDict[url]['url'](self.search, 0)
        print("Scrapping" + " " + url + " " + "started........")
        async with session.get(fetch_url, ssl=False) as resp:
            body = await resp.json()
            res = switcher.get(url)(body)
            self.product_list.extend(res)
            print("Scrapping" + " " + url + " " + "end")
            return res

    async def create_task(self):
        tasks = []
        async with aiohttp.ClientSession(trust_env=True) as session:
            start_time = time.time()
            self.search = urllib.parse.quote_plus(self.search)
            for url in urlDict:
                if urlDict[url]['type'] == 'api':

                    task = asyncio.create_task(self.api_scrape(url, session))
                else:
                    task = asyncio.create_task(self.html_scrape(url, session))
                tasks.append(task)
            await asyncio.gather(*tasks)
            end_time = time.time() - start_time
            print("end_time", end_time)

    def get_scrapped_price(self):
        print(self.product_list)
        asyncio.run(self.create_task())
        return self.product_list

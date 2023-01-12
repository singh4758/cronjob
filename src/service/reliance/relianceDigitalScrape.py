import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def reliance_digital_scrape(body, search_query):
    url = f"https://www.reliancedigital.in/search?q={search_query}:relevance"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.minimize_window()
    browser.get(url)

    response = requests.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    productdiv = soup.find_all("div", class_="sp grid")

    def getoffers(producturl):
        page = requests.get(producturl)
        pagecontent = page.content
        offersoup = BeautifulSoup(pagecontent, "html.parser")
        offers = []
        offerlist = offersoup.find_all("li", class_="pdp__listStyle")
        for offer in offerlist:
            offers.append(offer.get_text())
        return offers

    items = []
    for div in productdiv:
        productdetails = div.find("div", class_="slider-text")
        name = productdetails.find("p", class_="sp__name")
        price = div.find("span", {"class": "TextWeb__Text-sc-1cyx778-0 gimCrs"})
        MRP = div.find("span",
                       {"class": "TextWeb__Text-sc-1cyx778-0 StyledPriceBoxM__MRPText-sc-1l9ms6f-0 eJjyJG eBIoyL"})
        discount = div.find("span", {"class": "TextWeb__Text-sc-1cyx778-0 jhOcrk Block-sc-u1lygz-0 jCopvF"})
        image_url = "https://www.reliancedigital.in" + div.select('div img')[0]['data-srcset']
        productlinktag = div.find("a", href=True)
        getproductlink = productlinktag.get("href")
        product_url = f"https://www.reliancedigital.in{getproductlink}"

        if name is not None:
            name = name.get_text()
        if price is not None:
            price = price.get_text()
        if MRP is not None:
            MRP = MRP.get_text()
        if discount is not None:
            discount = discount.get_text()

        availableoffers = getoffers(product_url)

        data = {
            "name": name,
            "price": price,
            "productURL": product_url,
            "productImageURL": image_url,
            "source": "https://www.reliancedigital.in/",
            "description": "xyz",
            # "offers": availableoffers,
        }
        print(data)
        items.append(data)

    return items
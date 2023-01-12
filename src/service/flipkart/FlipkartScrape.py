from bs4 import BeautifulSoup


def flipkart_scrape(body):
    productList = []

    soup1 = BeautifulSoup(body, 'html.parser')
    for data1 in soup1.findAll('div', class_='_2kHMtA'):
        productURL = data1.find('a', attrs={'class': '_1fQZEK'}, href=True).get("href")
        names = data1.find('div', attrs={'class': '_4rR01T'})
        price = data1.find('div', attrs={'class': '_30jeq3 _1_WHN1'})

        image = data1.find('img', attrs={'class': '_396cs4'})
        specification = data1.find('div', attrs={'class': 'fMghEO'}).find('ul', attrs={'class': '_1xgFaf'})

        jsonStr = {
            "name": names.text,
            "price": int(''.join(filter(lambda i: i.isdigit(), price.text))),
            "productURL": f"https://www.flipkart.com{productURL}",
            "productImageURL": image.get('src'),
            "source": "https://bl-i.thgim.com/public/migration_catalog/article18208673.ece/alternates/FREE_960/bl29_IT_New%20Flipkart%20Logo.jpg",
            #"description": f'{specification}'
        }
        productList.append(jsonStr)
    return productList

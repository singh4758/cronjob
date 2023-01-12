from flask import Blueprint, request
from ..priceScrapper.PriceScrapper import PriceScrapper
from flask_cors import cross_origin


price_scrap = Blueprint('price_scrap', __name__)


def filtering_list(products, filter_by):
    data = filter_by['search'].split(" ")
    filtered_products= []
    for product in products:
        product_valid=False
        for value in data:
            if value.lower() in product["name"].lower():
                product_valid=True
            else:
                product_valid=False

        if product_valid:
            filtered_products.append(product)

    print(filtered_products)

    if filter_by["min_price"] != 0 and filter_by["max_price"] != 0:
        filtered_products = [product for product in filtered_products if
                             float(filter_by["min_price"]) < float(product["price"]) < float(
                                 filter_by["max_price"])]


    return filtered_products
@price_scrap.get('/api/productPriceList')
@cross_origin()
def get_price():
    params = {
        "search": request.args.get('search'),
        "min_price": request.args.get('min_price'),
        "max_price": request.args.get('max_price')
    }
    price_scrapper = PriceScrapper(params['search'])
    res = price_scrapper.get_scrapped_price()
    data= filtering_list(res , params)
    return data

 

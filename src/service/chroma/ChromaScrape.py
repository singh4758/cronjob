
def chroma_scrape(body):
    items = []
    response = body
    for product in response['products']:
        product_info = {
            "name": product.get('name'),
            "price": product.get('price').get('value'),
            "productURL": product.get('url'),
            "productImageURL": product.get('plpImage'),
            "source": "https://png2.cleanpng.com/sh/05cd025d8ec737dd3a86f1702701f850/L0KzQYm3VcI6N5D2hJH0aYP2gLBuTfNzd54yjNN9YT3qgrF8kL1kepDyeZ91b3fsiH7qigR6NZRqhuZ7ZT3xf7rrgb10fZ93geVucoOweMrrhgJiapJpRadrMHToSIS5UsRlOWg1RqIENUG1RoW8UcUzP2c4UKIBNkG4QIm1kP5o/kisspng-crom-tata-group-croma-logix-city-centre-noida-sunrisers-hyderabad-5b0de83224d170.0951264515276380661508.png",
            # "description": product.get('quickviewdesc')
        }
        items.append(product_info)
    return items

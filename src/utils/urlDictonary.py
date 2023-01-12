def chroma_url(search, page):
    base_url = "https://api.croma.com/product/allchannels/v1/search"
    append_data = f"?currentPage={page}&query={search}"
    return base_url + append_data


urlDict = {
    # "amazon": {
    #     "url": "https://amazon.in/s?k=",
    #     "base_url": "https://amazon.in/"
    # },
    "flipkart": {
        "url": "https://flipkart.com/search?q=",
        "base_url": "https://flipkart.com",
        "type": 'html',
    },
    "chroma": {
        "url": chroma_url,
        "base_url": "https://www.croma.com/",
        "type": "api"
    },
    # "reliance-digital" : {
    #     "url": f"https://www.reliancedigital.in/search?q=",
    #     "base_url": "https://www.reliancedigital.in",
    #     "type": 'html',
    # }
}

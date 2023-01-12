
from src.service.chroma.ChromaScrape import chroma_scrape
from src.service.flipkart.FlipkartScrape import flipkart_scrape
from src.service.reliance.relianceDigitalScrape import reliance_digital_scrape

switcher = {
    # "amazon": amazon_scrape,
    "flipkart": flipkart_scrape,
    "chroma": chroma_scrape,
    "reliance-digital": reliance_digital_scrape
}
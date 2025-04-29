from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

data = {
    "asin": "TESTING123D",
    "title": "Mark 1adsf"
}

class Product(Model):
    __keyspace__ = "scraper_app"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")

class ProductScrapeEvent(Model):
    __keyspace__ = "scraper_app"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")
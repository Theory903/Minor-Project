from elasticsearch import Elasticsearch
from scrapy.crawler import CrawlerProcess
from web_crawler import Crawler  # Replace mymodule with the module containing your spider

def index_to_elasticsearch(items):
    # Initialize Elasticsearch client with proper URL scheme
    es = Elasticsearch(['http://localhost:9200'])  # Use 'http' or 'https' depending on your setup
    
    # Index each item into Elasticsearch
    for item in items:
        es.index(index='webpages', body=item)

def run_crawler():
    # Run the Scrapy crawler
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json'
    })
    process.crawl(Crawler)
    process.start()

    # Read crawled data from the output file
    with open('output.json', 'r') as f:
        items = f.readlines()

    # Index crawled data into Elasticsearch
    index_to_elasticsearch(items)

if __name__ == "__main__":
    run_crawler()

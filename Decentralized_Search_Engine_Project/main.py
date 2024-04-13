import sys
from src.backend.services.web_crawler import WebCrawler
from src.backend.services.indexing_service import IndexingService

def main():
    print("Welcome to Decentralized Search Engine!")
    print("Initializing web crawler...")
    base_urls = ["https://example.com"]  # Example base URLs, replace with your own
    index_service = IndexingService("index_data")
    crawler = WebCrawler(base_urls, index_service)
    crawler.crawl()
    print("Crawling completed.")

    print("Indexing crawled data...")
    indexer = IndexingService()
    indexer.index()
    print("Indexing completed.")

    print("Search engine ready.")

    while True:
        query = input("Enter your search query (type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting search engine.")
            break
        search_service = SearchService()
        results = search_service.search(query)
        print("Search results:")
        for result in results:
            print(result)

if __name__ == "__main__":
    main()

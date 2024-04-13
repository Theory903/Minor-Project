from robobrowser import RoboBrowser
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os
browser = RoboBrowser(parser='lxml', history=True)

# Define the schema for the index
schema = Schema(title=TEXT(stored=True), content=TEXT)

# Create the index in memory (you can also create it on disk)
index_dir = "/Users/theory903/Documents/WORK/PROJECT/Search Engine/index"

# Create the directory if it doesn't exist
if not os.path.exists(index_dir):
    os.makedirs(index_dir)

# Create the index
index = create_in(index_dir, schema)
# Initialize RoboBrowser
browser = RoboBrowser()

# Define a function to crawl a website and index its content
def crawl_and_index(url):
    browser.open(url)
    title = browser.select('title')[0].text.strip()
    content = '\n'.join([p.text.strip() for p in browser.select('p')])
    
    # Add the content to the index
    writer = index.writer()
    writer.add_document(title=title, content=content)
    writer.commit()

# Crawl and index a sample website
crawl_and_index("https://example.com")

# Implement search functionality
def search(query):
    with index.searcher() as searcher:
        query_parser = QueryParser("content", index.schema)
        parsed_query = query_parser.parse(query)
        results = searcher.search(parsed_query)
        for result in results:
            print("Title:", result['title'])
            print("Content:", result['content'])
            print()

# Perform a sample search
search("example")


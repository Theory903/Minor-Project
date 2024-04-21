import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque, defaultdict
import logging
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Allowed protocols
allowed_protocols = ['http', 'https']

# URLs to crawl
unprocessed_urls = deque(["https://www.example.com"])

# Processed URLs
processed_urls = set()

# Inverted index
inverted_index = defaultdict(list)

# Stopwords
stop_words = set(stopwords.words('english'))

while unprocessed_urls:
    url = unprocessed_urls.popleft()

    # Check if the URL has already been processed
    if url in processed_urls:
        continue

    try:
        # Parse the URL and check if the protocol is allowed
        parsed_url = urlparse(url)
        if parsed_url.scheme not in allowed_protocols:
            logging.warning(f"Skipping {url} due to unsupported protocol")
            continue

        # Fetch the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text content and tokenize
        text = soup.get_text()
        tokens = word_tokenize(text.lower())
        filtered_tokens = [token for token in tokens if token not in stop_words and re.match(r'^\w+$', token)]

        # Update the inverted index
        for token in filtered_tokens:
            inverted_index[token].append(url)

        # Extract links and add to the unprocessed URLs
        links = [urljoin(url, link.get("href")) for link in soup.find_all("a")]
        for link in links:
            if link not in processed_urls and link not in unprocessed_urls:
                unprocessed_urls.append(link)

        # Mark the URL as processed
        processed_urls.add(url)

    except requests.exceptions.RequestException as e:
        logging.warning(f"Error processing {url}: {e}")
        continue

# Search function
def search(query):
    query_tokens = word_tokenize(query.lower())
    query_tokens = [token for token in query_tokens if token not in stop_words and re.match(r'^\w+$', token)]

    relevant_urls = set()
    for token in query_tokens:
        relevant_urls.update(inverted_index[token])

    return list(relevant_urls)

# Example usage
query = "example search query"
results = search(query)
print(f"Search results for '{query}':")
for result in results:
    print(result)
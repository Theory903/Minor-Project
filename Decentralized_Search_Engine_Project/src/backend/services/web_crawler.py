import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib import robotparser
import queue
import time

class Crawler:
    def __init__(self, seed_url, limit=10, delay=5, user_agent='Mozilla/5.0'):
        self.seed_url = seed_url
        self.url_queue = queue.Queue()
        self.seen_urls = set()
        self.url_queue.put(seed_url)
        self.limit = limit
        self.crawled_count = 0  
        self.delay = delay
        self.user_agent = user_agent
        self.robots = {}

    def crawl(self):
        while not self.url_queue.empty() and self.crawled_count < self.limit:  
            url = self.url_queue.get()
            if url in self.seen_urls:
                continue
            self.seen_urls.add(url)
            try:
                html = self.fetch_html(url)
                if html:
                    self.parse_and_enqueue(url, html)
                    self.crawled_count += 1  
            except requests.exceptions.RequestException as e:
                print(f"Error crawling {url}: {e}")
            time.sleep(self.delay)  

    def fetch_html(self, url):
        try:
            response = requests.get(url, headers={'User-Agent': self.user_agent}, timeout=10)
            response.raise_for_status()  
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_and_enqueue(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        domain = urlparse(url).netloc
        self.respect_robots_txt(domain)
        for link in soup.find_all('a'):
            link_url = link.get('href')
            if link_url and link_url.startswith('http'):
                absolute_url = urljoin(url, link_url)
                if self.is_allowed(absolute_url, domain) and absolute_url not in self.seen_urls:  
                    self.url_queue.put(absolute_url)
        print(f"Crawled: {url}")

    def respect_robots_txt(self, domain):
        if domain not in self.robots:
            robots_url = urljoin(self.seed_url, '/robots.txt')
            rp = robotparser.RobotFileParser()
            rp.set_url(robots_url)
            rp.read()
            self.robots[domain] = rp

    def is_allowed(self, url, domain):
        rp = self.robots[domain]
        return rp.can_fetch(self.user_agent, url)

# Define seed URL
seed_url = "https://www.example.com"

# Create crawler instance
crawler = Crawler(seed_url, limit=10)

# Start crawling
crawler.crawl()

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import colorama

colorama.init()
GREEN = colorama.Fore.GREEN
BLUE = colorama.Fore.BLUE
RESET = colorama.Fore.RESET

total_books = 0
title_books = []

def get_books(url):
    urls = set()
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    for h3 in soup.find_all('h3'):
        for a in h3.find_all('a'):
            global total_books 
            total_books += 1
            title = a.get('title', 'No title attribute')
            print(f"{GREEN}[{total_books}] {title}{RESET}")
            title_books.append(title)
    urls.add(f"http://books.toscrape.com/catalogue/page-{url_page}.html")
    return urls

url_page = 1

def crawl(url, max_urls=50):
    global url_page
    url_page += 1
    books = get_books(url)
    for link in books:
        if url_page > max_urls:
            break
        crawl(link, max_urls=max_urls)

if __name__ == "__main__":
    crawl(f"http://books.toscrape.com/catalogue/page-{url_page}.html")
    print(f"{BLUE}The requested scrape returned {total_books} titles.{RESET}")
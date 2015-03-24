__author__ = 'hernandeznp'

from lxml import html
from bs4 import BeautifulSoup
import requests
import re


def main():
    page = requests.get('http://www.homophone.com/search?type=begin&q=A')
    data = page.text
    soup = BeautifulSoup(data)
    pages = soup.h5.text
    page_match = re.match(r'Page ([0-9]+) / ([0-9]+)', pages)
    if page_match:
        current_page = page_match.group(1)
        last_page = page_match.group(2)
        print("Current page: ", current_page)
        print("Last page: ", last_page)
    else:
        print("No match")

if __name__ == "__main__":
    main()

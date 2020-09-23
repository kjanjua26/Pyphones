"""
Python wrapper for the website: https://www.homophone.com/
Gets the homophones of a word.
"""

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import re

class Pyphones:
    
    def __init__(self, word):
        self.word = word
        self.url = "https://www.homophone.com/search?page={}&type=&q={}"
        self.homophones = {self.word: []}
        
    def get_the_page(self, page_no=1):
        """
        Get the page content.

        Returns
            str: the content of the page.
        """
        url = self.url.format(page_no, self.word)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup

    def get_the_page_nos(self):
        """
        Get the total number of pages

        Returns
            int: the total number of the pages.
        """
        soup = self.get_the_page()
        pages = soup.find_all('div', attrs={'class':'col-sm-9'})
        total_pages = pages[0].find('h5').text.split('/')[-1].strip()
        return int(total_pages)

    def get_the_homophones(self):
        """
        Get the homophones of the word.

        Returns
            dict: {word: [list_of_homophones]} against each word.
        """
        total_pages = self.get_the_page_nos()
        for ix in range(total_pages):
            page_no = ix + 1
            soup = self.get_the_page(page_no)
            raw_homophones = soup.find_all('div', attrs={'class': 'well well-lg'})
            for elem in range(len(raw_homophones)):
                raw_homophones_2 = raw_homophones[elem].find_all('a', attrs={'class': 'btn word-btn'})
                list_of_homophones = list(raw_homophones_2)
                if any(list_of_homophones):
                    local_homophones = []
                    for tag_of_homophone in list_of_homophones:
                        homophone = tag_of_homophone.text
                        local_homophones.append(homophone)
                    self.homophones[self.word].append(local_homophones)

        return self.homophones
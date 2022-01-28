import bs4

from chans import Post, Board
from bs4 import BeautifulSoup
import requests


class FourChan(Board):
    def __init__(self):
        self.__base_link__ = "https://boards.4channel.org"

    def get_board(self, name):
        url = "{}/{}/".format(self.__base_link__, name)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        threads: [bs4.Tag] = soup.find_all(class_="thread")
        posts = []

        for th in threads:
            posts.append(Post("Unknown", str(th.find(class_="postMessage"))))

        return posts

import sys
import requests
from bs4 import BeautifulSoup

Host = 'https://www.ptt.cc'


def fetch_soup_from_url(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return BeautifulSoup(res.text, 'html.parser')


def parse_post(post_url):
    soup = fetch_soup_from_url(post_url)
    content = soup.findAll("div", {"class": "bbs-screen bbs-content"})
    meta_data = soup.findAll("span", {"class": "article-meta-value"})

    print 'author: %s' % meta_data[0].text
    print 'board: %s' % meta_data[1].text
    print 'title: %s' % meta_data[2].text
    print 'time: %s' % meta_data[3].text
    #print 'content:\n%s' % content[0].text


def parse_board(post_url):
    soup = fetch_soup_from_url(post_url)
    titles = soup.findAll("div", {"class": "title"})
    for t in titles:
        try:
            uri = t.find('a')['href']
            parse_post(Host + uri)
        except:
            print 'post had been deleted'


if __name__ == "__main__":
    board = 'NBA' # default board
    if len(sys.argv) > 1:
        board = sys.argv[1]
    parse_board('%s/bbs/%s/index.html' % (Host, board))

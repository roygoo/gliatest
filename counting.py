from collections import Counter

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]


def find_top3_file(urls_list):
    top_list = Counter(map(lambda x: x.split('/')[-1].rstrip('/'), urls_list)).most_common()
    for i in range(3):
        print '%s %d' % top_list[i]


if __name__ == "__main__":
    find_top3_file(urls)
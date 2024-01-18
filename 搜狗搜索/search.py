import requests


def search_home():
    url = 'https://www.sogou.com/web?query=腊八'
    resp = requests.get(url)
    html = resp.text
    print(html)
    print('是否抓取到:', '今天是腊八' in html)







if __name__ == '__main__':
    search_home()
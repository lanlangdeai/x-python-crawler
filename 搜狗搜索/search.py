import requests


def search_home():
    url = 'https://www.sogou.com/web?query=腊八'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',

    }
    resp = requests.get(url, headers=headers)
    html = resp.text
    print(html)
    print('是否抓取到:', '腊八节是汉族传统节日' in html)







if __name__ == '__main__':
    search_home()
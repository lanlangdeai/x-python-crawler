import requests


def search_page():
    url = 'https://game.51.com/search/action/game/'
    # 使用参数的方式调用get请求
    params = {
        'q': '传奇'
    }
    resp = requests.get(url, params=params)
    with open('game51.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.text)


def main():
    search_page()


if __name__ == '__main__':
    main()

import requests


'''
抓取百度热搜
'''

url = 'https://www.baidu.com'


def fetch_home_content():
    res = requests.get(url)
    res.encoding = 'utf-8'
    print(res.status_code)
    print(res.text)
    print('百度热搜' in res.text)

def re_doing(content: str):
    print(content)


def main():
    # 请求数据
    content = fetch_home_content()

    # re_doing(content)


if __name__ == '__main__':
    main()
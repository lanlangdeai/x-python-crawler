import requests


def home_page():
    url = 'https://www.eastmoney.com/'
    resp = requests.get(url)
    # 其中有中文, 需要设置字符集
    resp.encoding = 'utf-8'
    print(resp.encoding)
    with open('eastmoney.html', 'w', encoding='utf-8') as fp:
    # with open('eastmoney.html', 'w') as fp:
        # 需要指定打开文件的字符集 encoding="utf-8" 即可
        # UnicodeEncodeError: 'gbk' codec can't encode character '\xef' in position 0: illegal multibyte sequence
        fp.write(resp.text)


def main():
    # 抓取主页面
    home_page()



if __name__ == '__main__':
    main()
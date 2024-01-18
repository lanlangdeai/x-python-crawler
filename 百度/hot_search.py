import requests
from lxml import etree

'''
抓取百度热搜
'''

url = 'https://www.baidu.com/'


def fetch_home_content():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    }

    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    print(res.status_code)
    # print(res.text)
    print('百度热搜' in res.text)

    tree = etree.HTML(res.text)
    li_list = tree.xpath('//ul[@id="hotsearch-content-wrapper"]/li')
    print('热搜数量:', len(li_list))
    for item in li_list:
        # print(item)
        # 名称
        titles = item.xpath('./a/span[2]/text()')
        print('标题:', titles)

        links = item.xpath('./a/@href')
        print('链接地址:', links)

        sorts = item.xpath('./a/span[1]/text()')
        print('排名:', sorts)

        tags = item.xpath('./span/text()')
        print('标签:', tags)






def re_doing(content: str):
    print(content)


def main():
    # 请求数据
    content = fetch_home_content()

    # re_doing(content)


if __name__ == '__main__':
    main()
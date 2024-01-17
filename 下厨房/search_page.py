import requests
from lxml import etree

def main():
    url = 'http://www.xiachufang.com/search/?keyword=年夜饭'
    res = requests.get(url)
    # print(res.text)

    # 解析数据
    html = etree.HTML(res.text, etree.HTMLParser())
    li_list = html.xpath("/html/body/div[4]/div/div/div[1]/div[1]/div/div[2]/div[1]/ul//li")
    # [] 中括号中包含匹配表达式
    for item in li_list:
        # print(etree.tostring(item, encoding='utf-8'))
        img_src = item.xpath("./dev/a/dev")
        print(img_src)

        break


if __name__ == '__main__':
    main()
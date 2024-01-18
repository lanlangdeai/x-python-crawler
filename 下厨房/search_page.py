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
        print(etree.tostring(item, encoding='utf-8').decode('utf-8'))
        # img_src = item.xpath("./dev/a/dev")
        # print(img_src)
        print(item)

        # 名称
        name = item.xpath('./div/div/p[@class="name"]/a/text()')
        real_name = name[0].strip()
        print('名称:', real_name, len(real_name))
        # 获取属性, 前面需要添加/进行区分
        img = item.xpath('./div/a/div/img/@data-src')
        print('图片链接:', img[0])

        # 评分
        score = item.xpath('./div/div/p[@class="stats"]/span[contains(@class, "green-font")]/text()')
        print(score)
        print('评分:', score[0])

        # 作者
        author = item.xpath('./div/div/p[@class="author"]/a/text()')
        print('作者:', author[0])

        break


if __name__ == '__main__':
    main()
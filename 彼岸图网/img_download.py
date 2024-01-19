import requests
from lxml import etree


def download_img_to_local(img_url):
    # 发送请求,获取二进制数
    img_data = requests.get(img_url).content

    img_name = img_url.split('/')[-1]
    with open('./imgs/' + img_name, 'wb') as fp:
        fp.write(img_data)


def home_img():
    # 抓取五页数据
    for i in range(1, 6):
        print('当前页码: {0}'.format(i))
        if i == 1:
            url = 'https://pic.netbian.com/index.html'
        else:
            url = 'https://pic.netbian.com/index_%d.html' % i
        print('当前链接地址:', url)
        resp = requests.get(url)
        resp.encoding = 'gbk'
        content = resp.text
        print(content)
        # print('大波浪美女' in content)
        html = etree.HTML(content)

        li_list = html.xpath('//*[@id="main"]/div[3]/ul[@class="clearfix"]/li')
        print('素材数量:', len(li_list))
        for li in li_list:
            print(li)
            # title = li.xpath('./a/@title')[0]  # 有些不存在title属性
            title = li.xpath('./a/b/text()')[0]
            print('标题:', title)

            # 存在不同的标签, 使用不同的匹配规则, 获取数据
            img_urls = li.xpath('./a/span/img/@src | ./a/img/@src')
            print('multiple img urls:', img_urls)
            #
            # img_url = 'https://pic.netbian.com' + li.xpath('./a/span/img/@src')[0]
            # print('图片链接:', img_url)
            img_url = 'https://pic.netbian.com' + img_urls[0]

            download_img_to_local(img_url)


def main():
    home_img()


if __name__ == '__main__':
    main()

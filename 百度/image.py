import requests
from urllib.request import urlretrieve

def image_download():
    '''
    下载百度图片
    '''
    image_url = 'https://img0.baidu.com/it/u=160780349,781446406&fm=253&fmt=auto&app=120&f=JPEG?w=1024&h=576'
    # 方法1
    # content = requests.get(image_url).content  # 获取二进制图片
    # print(content)
    # with open('mv.jpeg', 'wb') as fp:
    #     fp.write(content)

    # 方法2
    urlretrieve(image_url, 'mv2.jpeg')



def main():
    image_download()


if __name__ == '__main__':
    main()
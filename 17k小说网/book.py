import os.path
import sys

import requests
import pandas as pd
from datetime import datetime
from lxml import etree


def book_shelf():
    url = 'https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919'

    # 获取cookie
    sess = requests.Session()
    login_url = 'https://passport.17k.com/ck/user/login'
    data = {
        'loginName': '18610614805',
        'password': 'z1234567'
    }
    ret = sess.post(login_url, data=data)
    print('登录后信息:', ret.json())
    print('=========================')

    headers = {
        # 'Cookie': 'GUID=dc7194a5-9519-4b37-b649-985def9f4955; BAIDU_SSP_lcr=https://www.baidu.com/link?url=AgadKk0nyvUTy9FNmq3bkV_3zSVEgGs5r8iu3msMs2K&wd=&eqid=ecb508b600202cec0000000465a9d05f; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1705627752; acw_sc__v2=65a9fe74ecf6ae23789035400ef28b56a59d74f1; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F10%252F90%252F93%252F102919390.jpg-88x88%253Fv%253D1705639703829%26id%3D102919390%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B3d45584LT%26e%3D1721191704%26s%3D67f38ad7e82ef064; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22102919390%22%2C%22%24device_id%22%3A%2218d1f56152e4c4-090ba1be749fa1-d726b59-1446808-18d1f56152fa53%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22dc7194a5-9519-4b37-b649-985def9f4955%22%7D; ssxmod_itna=QqUxBDcDg7=eqiKGHD8Cb5xDq47uiOLLubbODqGN5eoDZDiqAPGhDCbbIRiT4bq44=KYmbY351nQYp4GLWboPxp=MmfyeDHxY=DU=7+xoD4RKGwD0eG+DD4DWDmmHDnxAQDjxGp9uXwV=Dm4GWSqDgB4GgejiD0RU9tuiD4qDBGhdDKd29DGYUQnUQEkGta7=D0L=DjdrD/8DHcA63s=F=BwdDtqDRDAtD8wHUDtQDChHl0TIxC07=Q9x=CI+Gi70WtqGynFHlGCUQ=KtVRkism443mYL2bvP=+bht00xPiG4eFB5oYD4PWDP7DPYDK7vxcDDGRo/Dq4D===; ssxmod_itna2=QqUxBDcDg7=eqiKGHD8Cb5xDq47uiOLLubbODA=nY4D/KKGDFh+TI6P+iKrK8ApqqRK8AcUtyDti9D3=1=uh+ki4fhAN=xgrjPGFCBMKP0+p9hdFet9+=CcFZ/RQurOsTSYZD2shnw1th5eqoWtMeFGEEqzrCwdOG5atGitXEHWNry=KxYzcOgD79OiQZcTMPnisPArv3Fp6lF1UD5Cftqv9cKzUKmsh35Ap/FjQ3qF5QQFKgGs2FFsB6wfGi1Es/acQ4dFfS0ICkfXpFozSp9zAqOiupEM7udLEvuotfrf4OoFsvKC7rx3DQbE1MSKVMosuFiDdc+G+gkKgNQgkFSNu7hel=b2FtBWERwooNYnQwjzhg=xRFvfwGOTcgsGnGxuGS8pem7fbppn78e8bCFB2ilkbPqNE3=Cj1S3ECOHU076q88rAB4YS3Fr2rQpipQ+6kT86P+6m3jLVQOspLsQPD7j4Ah6nL97GvQ4AYHG1q=7HOGHqBDDjKDeTq4D=; Hm_lpvt_9793f42b498361373512340937deb2a0=1705639754'
        #           'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    }
    resp = sess.get(url, headers=headers)
    data = resp.json()

    table = pd.DataFrame(columns=['作品ID', '作品名称', '作者ID', '作者名称', '分类', '最新章节', '更新时间'])

    for idx, info in enumerate(data.get('data')):
        print(info)
        book_id = info.get('bookId')
        book_name = info.get('bookName')
        update_time = datetime.fromtimestamp(info.get('lastUpdateChapter').get('publishTime') / 1000).strftime('%Y-%m-%d %H:%M:%S')
        table.loc[idx+1] = [
            book_id,
            book_name,
            info.get('authorId'),
            info.get('authorPenName'),
            info.get('bookCategory').get('name'),
            info.get('lastUpdateChapter').get('name'),
            update_time
        ]

        # 将对应的章节对应抓取
        dir_name = './' + info.get('bookName')
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        # 抓取章节列表
        chapter_list_url = f'https://www.17k.com/list/{book_id}.html'
        print('请求URL:', chapter_list_url)
        headers['referer'] = 'https://www.17k.com/list/3581860.html'
        ret = sess.get(chapter_list_url, headers=headers)
        ret.encoding = 'utf-8'
        chapter_content = ret.text
        with open('tmp.html', 'w') as f:
            f.write(chapter_content)
        print(chapter_content)
        html = etree.HTML(chapter_content)
        items = html.xpath('/html/body/div[5]/dl/dd/a')
        print(items)
        for item in items:
            print('************** 开始抓取章节信息 ***************')
            content_url = 'https://www.17k.com' + item.xpath('./@href')
            print('章节URL:', content_url)
            title = item.xpath('./span/text()')
            print('章节标题:', title)
            # 抓取章节内容
            res = sess.get(content_url, headers=headers)
            content = res.text

            html2 = etree.HTML(content)
            ps = html2.xpath('//*[@id="readArea"]/div[1]/div[2]/p')
            page_content = []
            for p in ps:
                p_content = p.xpath('./text()')
                page_content.append(p_content)
            page_content_str = ''
            if page_content:
                page_content_str = "\n".join(page_content)
            # 保存到text文件中
            file_name = os.path.join(dir_name, title+'.txt')
            with open(file_name, 'w', encoding='utf-8') as fp:
                fp.write(page_content_str)



    # table.to_excel('17k小说合集.xlsx', index=False)

    '''
    根据作品名称进行分类,单独的文件夹
    Excel中统一存储作品的信息
        作者ID
        作者名称
        分类
        bookID
        作品名称
        最新章节
        更新时间
    文档中存储具体的内容:
        章节名称作为文件名称
    '''

if __name__ == '__main__':
    book_shelf()
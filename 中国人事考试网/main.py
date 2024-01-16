import requests


def search_page():

    url = 'http://www.cpta.com.cn/category/search'
    data = {
        "keywords": "人事",
        "搜 索": "搜索"
    }

    '''
POST /category/search HTTP/1.1
Host: www.cpta.com.cn
Connection: keep-alive
Content-Length: 68
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://www.cpta.com.cn
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://www.cpta.com.cn/category/search.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: acw_tc=7ae1d14d17053653123535101ef8b9630d9876bb548fcb0679c46b4c6b; Hm_lvt_779e393db65c6343f5f6c8ac6b0ff458=1705365312; Hm_lpvt_779e393db65c6343f5f6c8ac6b0ff458=1705365436

    '''
    # 需要添加UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0'
    }


    resp = requests.post(url, data=data, headers=headers)
    resp.encoding = 'utf-8'
    with open('cpta.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.text)


def main():
    search_page()



if __name__ == '__main__':
    main()
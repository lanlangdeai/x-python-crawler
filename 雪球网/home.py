import requests


def home_news():
    url = 'https://xueqiu.com/?category=livenews'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
        # 'Cookie': 'acw_tc=276077b017056259935284314e87b686fdeb291ce2a5dbd2f7c15f646fb181; xq_a_token=4418c7deafa5b566e73966d73045c92752601c18; xqat=4418c7deafa5b566e73966d73045c92752601c18; xq_r_token=3400e25ce554d6c07b8d65bb450064b80039b8a7; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwNzE4MDMzNSwiY3RtIjoxNzA1NjI1OTg0MTUzLCJjaWQiOiJkOWQwbjRBWnVwIn0.RSROzUa9LRv6WRwBfhtXI-YVXmF5C7oGZPONVWR4zhfyM3wRTHZwlusTszyuKfXAaC0V8J-odz7t7uBk1Wz3S3V0oSTyywP_UpxDP9hFGSdVDue9XRVfdW4Q5XOZ9ag2On5nGKnDQjbFfi_N1Y4dw3Q0p_ITtDMd_bCcq9cO29GWGJlK3WXbgyZ6gqmJne1xRKfHVOMPVLX5JS6x_29ulPH-0J2KT6cT4psg2MrPS44kI4sJCOY5vidU2IJfrzef0VCVzas0nfuRfX-7X-pgZIC_JajnSGebnM8aulrI7FvBso43caL0jyOxZewtubSp0_JKvt9HQrABYNNRynFVQw; cookiesu=821705625993541; u=821705625993541; Hm_lvt_1db88642e346389874251b5a1eded6e3=1705625993; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1705625993; device_id=20689a535f2e73e94410a4df2866844a',

    }

    # 保留访问中设置的cookie, 之后就是常规操作
    sess = requests.Session()
    home_url = 'https://xueqiu.com/'
    sess.get(home_url, headers=headers)

    resp = sess.get(url, headers=headers)
    resp.encoding = 'utf-8'
    content = resp.text
    print(content)

    print('国内商品期货' in content)



if __name__ == '__main__':
    home_news()
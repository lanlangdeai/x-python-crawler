import requests


def demo():
    url = 'https://www.baidu.com'
    res = requests.get(url)
    print(res.status_code)

def main():
    demo()


if __name__ == '__main__':
    main()
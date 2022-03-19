import json
from time import strftime, sleep

import requests


def request_url():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/1e7fa5d4-67b6-40bf-a96b-06d1a9ef5717'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'

    }
    res = requests.get(url, headers=head)
    dict1 = json.loads(res.text)
    # 商品名字
    name = dict1["data"]["name"]
    # 规格
    spec = dict1["data"]["spec"]
    # 价格
    price = str(int(dict1["data"]["price"]) / 100)
    # 原价
    market_price = str(int(dict1["data"]["market_price"]) / 100)
    # 详细内容
    share_content = dict1["data"]["share_content"]
    print("-------------商品：" + name + "-------------")
    print("规格：" + spec)
    print("原价：" + price)
    print("原价/折扣价：" + price + "/" + market_price)
    print("详细内容：" + share_content)


# 获取时间
def time():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/1e7fa5d4-67b6-40bf-a96b-06d1a9ef5717'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'

    }
    res = requests.get(url, headers=head)
    dict1 = json.loads(res.text)
    # 商品名字
    name = dict1["data"]["name"]
    # 价格
    price = str(int(dict1["data"]["price"]) / 100)
    print("-------------" + name +"的价格变动"+ "-------------")
    #终止程序时，不会报错
    try:
        while (True):
            nowTimeAndPrint = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price)
            print(nowTimeAndPrint)
            sleep(5)
    except:
        print("程序结束")

#主函数
if __name__ == '__main__':
    request_url()
    print("\n")
    time()
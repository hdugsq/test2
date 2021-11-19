# -*- coding: utf-8 -*-
# import csv
# import json






###写数据到csv文件
# # 定义第一行
# header = ['id', 'name']
# # 2条数据
# d1 = [1, "xiaoming"]
# d2 = [2, "lucy"]
# # 打开csv文件，newline作用是去掉空行，不加结果之间会有一个空行
# with open('test.csv', 'w', newline='') as f:
#     # 建立写入对象
#     writer = csv.writer(f)
#     # 写入数据
#     writer.writerow(header)
#     writer.writerow(d1)
#     writer.writerow(d2)



# ###写字典到csv文件
# with open('names.csv', 'w', newline='') as csvfile:
#     # 定义名称，也就是header
#     fieldnames = ['first_name', 'last_name']
#     # 直接将fieldnames写入,写入字典使用DictWriter方法
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     # 调用writeheader方法加入header
#     writer.writeheader()
#     # 写入字典数据
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# ###读取csv文件
# with open('names.csv', 'r') as f:
#     # 创建reader对象
#     reader = csv.reader(f)
#     # reader是可迭代对象，可以通过for循环获取内容
#     for row in reader:
#         print(row)

# with open('names.csv', 'r') as f:
#     # 定义字典阅读对象
#     reader = csv.DictReader(f)
#     # 打印第一行名称
#     print(reader.fieldnames)
#     # 循环打印字典内容
#     for row in reader:
#         print(row['first_name'], row['last_name'])

# ##json dump
# content = ['id','name']
# with open("names.json","w") as fp:
#     json.dump(content, fp=fp)
#
#
# ## json load
# with open('names.json') as fp:
#     name = json.load(fp)
# print(name)


# import json
# from bs4 import BeautifulSoup
# import requests
# #
# try:
#     url = 'https://www.lagou.com/zhaopin/Python/2/?filterOption=2&sid=561ef29b8b34467ebff821db7b95f715'
#     header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#               'Referer': 'https://www.lagou.com/'}
#     req = requests.get(url, headers=header)
#     req.raise_for_status()
#     req.encoding = req.apparent_encoding
#     response = req.text
#     print(response)
# except:
#     print("spider fail")
#
# # 生成soup实例
# soup = BeautifulSoup(response, 'lxml')
# # 获取class=‘list_item_top’的div标签
# divlist = soup.find_all('div', class_='list_item_top')
# # 定义空列表
# content = []
# # 通过循环，获取需要的内容
# for list in divlist:
#     # 职位名称
#     job_name = list.find('h3').string
#     # 职位详细页面
#     link = list.find('a', class_="position_link").get('href')
#     # 招聘的公司
#     company = list.find('div', class_='company_name').find('a').string
#     # 薪水
#     salary = list.find('span', class_='money').string
#     print(job_name, company, salary, link)
#     content.append({'job': job_name, 'company': company, 'salary': salary, 'link': link})
#
# with open('lagou.json', 'w') as fp:
#     json.dump(content, fp=fp, indent=4)


import requests
from bs4 import BeautifulSoup
import csv

url='https://movie.douban.com/top250'

def download_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        data = res.text
        return data
    except:
        print("spider fail")

if __name__=='__main__':
    # print(download_page(url).decode())
    soup=BeautifulSoup(download_page(url), 'html.parser')
    # print(soup.prettify())
    content=soup.find_all('div', class_="hd")
    # print(content)
    # print(soup.title.string)


    f = open("movie.csv", "w")
    writer = csv.writer(f)
    writer.writerow(['id', 'name'])
    i=0
    for k in content:
        a=k.find_all('span')
        # print(a)
        i=i+1
        print(i, a[0].string)
        writer.writerow([i, a[0].string])
    f.close()


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/25 15:53
# @Author: haifeng
# @File  : t.py
# 批量下载资金html文件

import os
import re
import time
import os.path
import requests
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

# Download Function
def download_html(code, filename, url):
    headers = {
        'User-Agent': UserAgent().random,
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        with open(filename, "wb") as fout:
            fout.write(r.content)
        print("suceed:", code)
    else:
        print("fail:", r.status_code)

# 解析html
file_dir = "./target1"
files = file_name(file_dir)
for i in range(len(files)):
    print(i, files[i])
    if ".html" in files[i]:
        htmlPath = "./target1/"+files[i]
        htmlfile = open(htmlPath, 'r', encoding="gbk")
        htmlpage = htmlfile.read()

        soup = BeautifulSoup(htmlpage, "html.parser")
        body_tag = soup.body

        try:
            # Get Fund
            body_tag2 = body_tag.find("div", class_="box").find_all("td")
            for value in body_tag2:
                shtml = value.find('a')['href']
                raw_code = re.findall(r'【(.*)】', str(value))
                code = str(raw_code)[2:8]
                print(shtml, code)

                filename = "./FundTarget/{}.html".format(code)
                print(filename)
                if os.path.isfile(filename) == False:
                    download_html(code, filename, shtml)
                else:
                    print("文件已存在：", filename)
                #time.sleep(1)
                # break

        except:
            print(htmlPath+"————error")


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/25 15:53
# @Author: haifeng
# @File  : t.py
import os
import pandas as pd
from bs4 import BeautifulSoup
import re


# files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录),此处为所有待解析网页
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


csvPath = "./WZH/fund_prep.csv"

list_code = []
list_fund = []

# 解析html
# target目录下所有网页
file_dir = "./target1"
files = file_name(file_dir)
for i in range(len(files)):
    print(i, files[i])
    if ".html" in files[i]:
        htmlPath = "./target1/" + files[i]
        htmlfile = open(htmlPath, 'r', encoding="gbk")
        htmlpage = htmlfile.read()
        soup = BeautifulSoup(htmlpage, "html.parser")
        body_tag = soup.body

        try:
            # 获取所有Fund公司
            body_tag2 = body_tag.find("div", class_="box").find_all("a", limit=None)
            for value in body_tag2:
                code = re.findall(r'【(.*)】', str(value))
                list_fund.append(value.string)
                list_code.append(str(code)[2:8])

        except:
            print(htmlPath + "————error")

print(len(list_code), len(list_fund))
d = {'基金': list_fund,'基金代码': list_code}
dataframe = pd.DataFrame(d)
columns = ['基金','基金代码']
dataframe.to_csv(csvPath, index=False, columns=columns)

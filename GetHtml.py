#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/25 15:53
# @Author: haifeng
# @File  : t.py
import os
import pandas as pd
from bs4 import BeautifulSoup


# files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录),此处为所有待解析网页
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


csvPath = "myJob1/company_prep.csv"

# list_job = []
# list_sex = []
# list_age = []
list_code = []
# list_name = []
list_company = []

# 解析html
# target目录下所有网页
file_dir = "target1"
files = file_name(file_dir)
for i in range(len(files)):
    print(i, files[i])
    if ".html" in files[i]:
        htmlPath = "target1/" + files[i]
        htmlfile = open(htmlPath, 'r', encoding="gbk")
        htmlpage = htmlfile.read()

        soup = BeautifulSoup(htmlpage, "html.parser")
        #  instition_Name=soup.title.string.split(" ")[0].split("(")[1][:-1]
        code = soup.title.string.split(" ")[0].split("(")[1][:-1]
        body_tag = soup.body

        try:
            # 获取序号
            body_tag1 = body_tag.find("div", class_="m_box gssj_scroll", id="share").find("tbody").find_all("td", class_="")

            for value in body_tag1:
                list_code.append(str(code))

            body_tag2 = body_tag.find("div", class_="m_box gssj_scroll", id="share").find("tbody").find_all("p", class_="institionName")
            for value in body_tag2:
                list_company.append(value.string)

        except:
            print(htmlPath + "————error")

print(len(list_code), len(list_company))

d = {'公司': list_company,'股票代码': list_code}
dataframe = pd.DataFrame.from_dict(d)
columns = ['公司','股票代码']
dataframe.to_csv(csvPath, index=False, columns=columns)

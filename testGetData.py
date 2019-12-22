#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/25 15:53
# @Author: haifeng
# @File  : t.py
# @Desc  : 批量获取控股公司信息并存储成csv

import os
import pandas as pd
from bs4 import BeautifulSoup

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

csvPath = "control_company_prep.csv"

list_job = []
list_sex = []
list_age = []
list_code = []
list_name = []
list_company = []

# 解析html
file_dir = "../target"
files = file_name(file_dir)

for i in range(len(files)):
    print(i, files[i])
    if ".html" in files[i]:
        htmlPath = "../target/"+files[i]
        htmlfile = open(htmlPath, 'r', encoding="gbk")
        htmlpage = htmlfile.read()

        soup = BeautifulSoup(htmlpage, "html.parser")
        code = soup.title.string.split(" ")[0].split("(")[1][:-1]
        body_tag = soup.body

        try:
            # 获取公司
            body_tag2 = body_tag.find("div", class_="m_box gssj_scroll", id="share").find("tbody").find_all("p", class_="institionName")
            for value in body_tag2:
                list_code.append(str(code))
                list_company.append(value.string)
        except:
            print(htmlPath+"————error")

print(len(list_code), len(list_company))
dataframe = pd.DataFrame({'公司': list_company, '股票代码': list_code})
columns = ['公司', '股票代码']
dataframe.to_csv(csvPath, index=False, columns=columns)

#获取相似基金数据

import os
import re
import pandas as pd
from bs4 import BeautifulSoup

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

csvPath = "WZH/similar_fund_prep.csv"

list_fund = []
list_code = []
list_Entitycode = []

# 解析html
file_dir = "Normal"
files = file_name(file_dir)
for i in range(len(files)):
    print(i, files[i])
    if ".html" in files[i]:
        htmlPath = "Normal/"+files[i]
        htmlfile = open(htmlPath, 'r', encoding="gbk")
        htmlpage = htmlfile.read()

        soup = BeautifulSoup(htmlpage, "html.parser")
        EntityCode = (re.findall(r"\d+", str(soup.title)))[0]

        body_tag = soup.body

        try:
            # 获取同系基金
            body_tag1 = body_tag.find("div", class_="col_lr lr01 jrj-clear mt").\
                find("div", class_="left").find_all("td", class_="bfLeft")
            for value in body_tag1:
                #print(value)
                shtml = value.find('a')['href']
                fundName = value.find("a").string
                raw_code = re.findall(r"\d+", str(shtml))
                fundCode = raw_code[0]
                list_fund.append(fundName)
                list_code.append(fundCode)
                list_Entitycode.append(EntityCode)
        except:
            print(htmlPath+"————error")

#写入csv文件
dataframe = pd.DataFrame({'FundName':list_fund, 'FundCode':list_code, 'EntityCode':list_Entitycode})
columns = ['FundName','FundCode','EntityCode']
dataframe.to_csv(csvPath, index=False, columns=columns)
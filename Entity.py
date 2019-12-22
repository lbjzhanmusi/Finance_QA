import re
import csv
import pandas as pd
import tushare as ts

#构建基金实体
# # 读取“资金”实体
fundList = []
data = pd.read_csv("WZH/fund_prep.csv")
sign = 0
for indexs in data.index:
    name = data.loc[indexs].values[0]
    code = str(data.loc[indexs].values[1]).zfill(6)
    fundList.append([800000+indexs+1, name, code, "Fund"])

with open("WZH/kg/fund.csv","w",newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index:ID", "name", "code", ":LABEL"])
    for i in range(len(fundList)):
        writer.writerows([fundList[i]])
        print(i, fundList[i], len(fundList))

# # 创建“ST_股票”的关系
stockList = []
data = pd.read_csv("WZH/kg/stock.csv")
for indexs in data.index:
    id = data.loc[indexs].values[0]
    code = str(data.loc[indexs].values[2]).zfill(6)
    print(id, code)
    stockList.append([id, code])
print("done")

stList = []
data = pd.read_csv("WZH/kg/st.csv")
for indexs in data.index:
    id = data.loc[indexs].values[0]
    st = data.loc[indexs].values[1]
    print(id, st)
    stList.append([id, st])
print("done")

stock_st_list = []
data = pd.read_csv("WZH/stock_st_prep.csv")
for indexs in data.index:
    st_name = str(data.loc[indexs].values[1])
    st_code = str(data.loc[indexs].values[0]).zfill(6)
    stock_id = ""
    for j in range(len(stockList)):
        if st_code == stockList[j][1]:
            stock_id = stockList[j][0]
            break
        st_id = ""
    for j in range(len(stList)):
        if st_name == stList[j][1]:
            st_id = stList[j][0]
            break
    if stock_id!="" and st_id!="":
        stock_st_list.append([stock_id, st_id, "ST属于", "ST属于"])
print("done relation")

# 存储关系
with open("WZH/kg/stock_st.csv","w",newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
    for i in range(len(stock_st_list)):
        writer.writerows([stock_st_list[i]])
        print(i, stock_st_list[i])
print("done store")
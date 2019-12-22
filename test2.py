import os
import tushare as ts
print(ts.__version__)

#3获取股票行业信息
df = ts.get_industry_classified()
csvPath = "WZH/stock_industry_prep.csv"
ts.get_industry_classified().to_csv(csvPath, index=False)

#获取股票概念信息
df = ts.get_concept_classified()
csvPath = "WZH/stock_concept_prep.csv"
df.to_csv(csvPath, index=False)

#3获取地域分类
df = ts.get_area_classified()
csvPath = "WZH/stock_area_prep11.csv"
df.to_csv(csvPath, index=False)

#2019第二季度业绩
df = ts.get_report_data(2019,2)
csvPath = "WZH/stock_report201902_prep.csv"
df.to_csv(csvPath, index=False)


#ST获取
df = ts.get_st_classified()
csvPath = "WZH/stock_st_prep.csv"
df.to_csv(csvPath, index=False)

#暂停上市列表
df2 = ts.get_suspended()
csvPath = "WZH/get_suspended.csv"
df2.to_csv(csvPath, index=False)

#中小板分类
df2 = ts.get_sme_classified()
csvPath = "WZH/sme.csv"
df2.to_csv(csvPath, index=False)

stock_info = ts.get_stock_basics()
CODE_LIST = []
for i in stock_info.index:
    CODE_LIST.append(i)
print(CODE_LIST)

#3获取A股基本信息
data = ts.get_stock_basics()
csvPath = "WZH/test_stock.csv"
data.to_csv(csvPath, index=False)

stockList = []
data = ts.get_stock_basics()
for indexs in data.index:
   name = data.loc[indexs].values[1]
   code = str(data.loc[indexs].values[0]).zfill(6)
   stockList.append([indexs, name, code])
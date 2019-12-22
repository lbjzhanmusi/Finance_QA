import re
import csv
import pandas as pd 
import tushare as ts

# # 读取“高管”实体
# stockList = []
# data = ts.get_stock_basics()
# for indexs in data.index:
#     stockList.append(indexs)
# # print(stockList)
#
# executiveList = []
# data = pd.read_csv("WZH/executive_prep.csv")
# sign = 0
# for indexs in data.index:
#     name = data.loc[indexs].values[0]
#     sex = data.loc[indexs].values[1]
#     age = data.loc[indexs].values[2]
#     code = str(data.loc[indexs].values[3]).zfill(6)
#     job = data.loc[indexs].values[4]
#     if code in stockList:
#         sign = sign + 1
#         executiveList.append([100000+sign, name, sex, age, code, job, "高管"])
# with open("WZH/kg/executive.csv","w",newline='',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["index:ID", "name", "sex", "age", "code", "job", ":LABEL"])
#     for i in range(len(executiveList)):
#         writer.writerows([executiveList[i]])
#         print(i, executiveList[i], len(stockList))

# 创建“公司”实体
# sign = 0
# stockList2 = []
'''
stockList = []
data = pd.read_csv("myJob1/stock_concept_prep.csv")
for indexs in data.index:
    name = data.loc[indexs].values[1]
    code = str(data.loc[indexs].values[0]).zfill(6)
    if [name, code] not in stockList:
        stockList.append([name, code])
        stockList2.append([sign, name, code])
        sign = sign + 1
'''
# data = ts.get_stock_basics()
# for indexs in data.index:
#     status = "normal"
#     if "ST" in data.loc[indexs].values[0]:
#         status = "ST"
#     sign = sign + 1
#     stockList2.append([200000+sign, data.loc[indexs].values[0], indexs, status, "企业"])
# with open("myJob1/kg/stock.csv","w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["index:ID", "name", "code", "status", ":LABEL"])
#     for i in range(len(stockList2)):
#         writer.writerows([stockList2[i]])
#         print(i, stockList2[i])

# #　创建“概念”实体
# conceptList = []
# data = pd.read_csv("myJob1/stock_concept_prep.csv")
# for indexs in data.index:
#     concept = data.loc[indexs].values[2]
#     if concept not in conceptList:
#         conceptList.append(concept)
# with open("myJob1/kg/concept.csv","w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["index:ID", "name", ":LABEL"])
#     for i in range(len(conceptList)):
#         writer.writerows([[300000+i+1, conceptList[i], "概念"]])
#         print(i, conceptList[i])

# # 创建“行业”实体
# industryList = []
# data = pd.read_csv("myJob1/stock_industry_prep.csv")
# for indexs in data.index:
#     industry = data.loc[indexs].values[2]
#     if industry not in industryList:
#         industryList.append(industry)
# with open("myJob1/kg/industry.csv","w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["index:ID", "name", ":LABEL"])
#     for i in range(len(industryList)):
#         writer.writerows([[400000+i+1, industryList[i], "行业"]])
#         print(i, industryList[i])

# # 创建“area”实体
# AreaList = []
# data = pd.read_csv("WZH/stock_area_prep.csv")
# for indexs in data.index:
#     industry = data.loc[indexs].values[2]
#     if industry not in AreaList:
#         AreaList.append(industry)
# with open("WZH/kg/area.csv","w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["index:ID", "name", ":LABEL"])
#     for i in range(len(AreaList)):
#         writer.writerows([[500000+i+1, AreaList[i], "地域"]])
#         print(i, AreaList[i])


# # 读取“控股公司”实体
# stockList = []
# data = ts.get_stock_basics()
# for indexs in data.index:
#     stockList.append(indexs)
# # print(stockList)
#
# ctrlCompanyList = []
# data = pd.read_csv("WZH/control_company_prep.csv")
# sign = 0
# for indexs in data.index:
#     name = data.loc[indexs].values[0]
#     code = str(data.loc[indexs].values[1]).zfill(6)
#     if code in stockList:
#         sign = sign + 1
#         ctrlCompanyList.append([700000+sign, name, code, "控股公司"])
#
# with open("WZH/kg/ctrlCompany.csv","w",newline='',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["index:ID", "name", "code", ":LABEL"])
#     for i in range(len(ctrlCompanyList)):
#         writer.writerows([ctrlCompanyList[i]])
#         print(i, ctrlCompanyList[i], len(stockList))

# # 创建”高管“和”公司“的关系
# executiveList = []
# codeList = []
# data = pd.read_csv("WZH/kg/executive.csv")
# for indexs in data.index:
#     index = data.loc[indexs].values[0]
#     name = data.loc[indexs].values[1]
#     code = str(data.loc[indexs].values[4]).zfill(6)
#     job = data.loc[indexs].values[5]
#     if code not in codeList:
#         codeList.append(code)
#     executiveList.append([index, name, code, job])
# print("done...")
#
# stockList = []
# data = pd.read_csv("WZH/kg/stock.csv")
# for indexs in data.index:
#     index = data.loc[indexs].values[0]
#     name = data.loc[indexs].values[1]
#     code = str(data.loc[indexs].values[2]).zfill(6)
#     stockList.append([index, name, code])
# print("done...")
#
# # 双重循环
# execute_stock_List = []
# num = 0
# for i in range(len(executiveList)):
#     sign = ""
#     for j in range(len(stockList)):
#         if str(executiveList[i][2]) == str(stockList[j][2]):
#             str1 = re.sub('"','', executiveList[i][3])
#             execute_stock_List.append([executiveList[i][0], stockList[j][0], str1, "董事会成员"])
#             sign = "1"
#             break
#     if len(sign) == 0:
#         num = num + 1
#         print(num, str(executiveList[i][0])+" , "+str(executiveList[i][2]), len(stockList), len(executiveList[i][2]))
# print("done...")
#
# # 存储去重后股票
# with open("WZH/kg/executive_stock.csv","w",newline='',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
#     for i in range(len(execute_stock_List)):
#         writer.writerows([execute_stock_List[i]])
#         print(i, execute_stock_List[i])

# #　创建“行业_股票”的关系
# stockList = []
# data = pd.read_csv("WZH/kg/stock.csv")
# for indexs in data.index:
#     id = data.loc[indexs].values[0]
#     code = str(data.loc[indexs].values[2]).zfill(6)
#     print(id, code)
#     stockList.append([id, code])
#
# industryList = []
# data = pd.read_csv("WZH/kg/industry.csv")
# for indexs in data.index:
#     id = data.loc[indexs].values[0]
#     industry = data.loc[indexs].values[1]
#     print(id, industry)
#     industryList.append([id, industry])
#
# stock_industry_list = []
# data = pd.read_csv("WZH/stock_industry_prep.csv")
# for indexs in data.index:
#     stock = str(data.loc[indexs].values[0]).zfill(6)
#     industry = data.loc[indexs].values[2]
#     stock_id =  ""
#     for j in range(len(stockList)):
#         if stock == stockList[j][1]:
#             stock_id = stockList[j][0]
#             break
#     industry_id = ""
#     for j in range(len(industryList)):
#         if industry == industryList[j][1]:
#             industry_id = industryList[j][0]
#             break
#     if stock_id!="" and industry_id!="":
#         stock_industry_list.append([stock_id, industry_id, "行业属于", "行业属于"])
#
# # 存储关系
# with open("WZH/kg/stock_industry.csv","w",newline='',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
#     for i in range(len(stock_industry_list)):
#         writer.writerows([stock_industry_list[i]])
#         print(i, stock_industry_list[i])

# # 创建“概念_股票”的关系
# stockList = []
# data = pd.read_csv("WZH/kg/stock.csv")
# for indexs in data.index:
#     id = data.loc[indexs].values[0]
#     code = str(data.loc[indexs].values[2]).zfill(6)
#     print(id, code)
#     stockList.append([id, code])
#
# conceptList = []
# data = pd.read_csv("WZH/kg/concept.csv")
# for indexs in data.index:
#     id = data.loc[indexs].values[0]
#     concept = data.loc[indexs].values[1]
#     print(id, concept)
#     conceptList.append([id, concept])
#
# stock_concept_list = []
# data = pd.read_csv("WZH/stock_concept_prep.csv")
# for indexs in data.index:
#     stock = str(data.loc[indexs].values[0]).zfill(6)
#     concept = data.loc[indexs].values[2]
#     stock_id =  ""
#     for j in range(len(stockList)):
#         if stock == stockList[j][1]:
#             stock_id = stockList[j][0]
#             break
#     concept_id = ""
#     for j in range(len(conceptList)):
#         if concept == conceptList[j][1]:
#             concept_id = conceptList[j][0]
#             break
#     if stock_id!="" and concept_id!="":
#         stock_concept_list.append([stock_id, concept_id, "概念属于", "概念属于"])
#
# # 存储关系
# with open("WZH/kg/stock_concept.csv","w",newline='',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
#     for i in range(len(stock_concept_list)):
#         writer.writerows([stock_concept_list[i]])
#         print(i, stock_concept_list[i])


# #　创建“地域_股票”的关系
# stockList = []
# data = pd.read_csv("WZH/kg/stock.csv")
# for indexs in data.index:
#     id = data.loc[indexs].values[0]
#     code = str(data.loc[indexs].values[2]).zfill(6)
#     print(id, code)
#     stockList.append([id, code])
#
# AreaList = []
# data = pd.read_csv("WZH/kg/area.csv")
# for indexs in data.index:
#     id = data.loc[indexs].values[0]
#     area = data.loc[indexs].values[1]
#     print(id, area)
#     AreaList.append([id, area])
#
# stock_area_list = []
# data = pd.read_csv("WZH/stock_area_prep.csv")
# for indexs in data.index:
#     stock = str(data.loc[indexs].values[0]).zfill(6)
#     area = data.loc[indexs].values[2]
#     stock_id =  ""
#     for j in range(len(stockList)):
#         if stock == stockList[j][1]:
#             stock_id = stockList[j][0]
#             break
#     area_id = ""
#     for j in range(len(AreaList)):
#         if area == AreaList[j][1]:
#             area_id = AreaList[j][0]
#             break
#     if stock_id!="" and area_id!="":
#         stock_area_list.append([stock_id, area_id, "地域属于", "地域属于"])
#
# # 存储关系
# with open("WZH/kg/stock_area.csv","w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
#     for i in range(len(stock_area_list)):
#         writer.writerows([stock_area_list[i]])
#         print(i, stock_area_list[i])


# # 创建”控股公司“和”股票公司“的关系
# ctrlCompanyList = []
# codeList = []
# data = pd.read_csv("WZH/kg/ctrlCompany.csv")
# for indexs in data.index:
#     index = data.loc[indexs].values[0]
#     name = data.loc[indexs].values[1]
#     code = str(data.loc[indexs].values[2]).zfill(6)
#     if code not in codeList:
#         codeList.append(code)
#     ctrlCompanyList.append([index, name, code])
# print("done1...")
#
# stockList = []
# data = pd.read_csv("WZH/kg/stock.csv")
# for indexs in data.index:
#     index = data.loc[indexs].values[0]
#     name = data.loc[indexs].values[1]
#     code = str(data.loc[indexs].values[2]).zfill(6)
#     stockList.append([index, name, code])
# print("done2...")
#
# # 双重循环
# execute_stock_List = []
# num = 0
# for i in range(len(ctrlCompanyList)):
#     sign = ""
#     for j in range(len(stockList)):
#         if str(ctrlCompanyList[i][2]) == str(stockList[j][2]):
#             str1 = re.sub('"','', ctrlCompanyList[i][2])
#             execute_stock_List.append([ctrlCompanyList[i][0], stockList[j][0], str1, "控股公司"])
#             sign = "1"
#             break
#     if len(sign) == 0:
#         num = num + 1
#         print(num, str(ctrlCompanyList[i][0])+" , "+str(ctrlCompanyList[i][2]), len(stockList), len(ctrlCompanyList[i][2]))
# print("done3...")
#
# # 存储去重后股票
# with open("WZH/kg/ctrlCompany_stock.csv","w",newline='',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
#     for i in range(len(execute_stock_List)):
#         writer.writerows([execute_stock_List[i]])
#         print(i, execute_stock_List[i])

# Check in FundList And get
def getFundIndex(code, fundList=[]):
    for i in range(len(fundList)):
        if str(code) == str(fundList[i][2]).zfill(6):
            fundIndex = fundList[i][0]
            return fundIndex
    return None

# 存储关系数据到CSV
def storeDataToCSV(csvPath, storeList=[]):
    with open(csvPath, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
        for i in range(len(storeList)):
            writer.writerows([storeList[i]])
            #print(i, storeList[i])


# 创建”基金同类基金“的关系
# 加载基金列表
fundList = []
FundData = pd.read_csv("WZH/kg/fund.csv")
for indexs in FundData.index:
    index = FundData.loc[indexs].values[0]
    FundName = FundData.loc[indexs].values[1]
    FundCode = FundData.loc[indexs].values[2]
    fundList.append([index, FundName, FundCode])
print("done1 load fundList",len(fundList))

#加载关系表并建立基金联系
similar_fund_relation_list = []
codeList = []
failed_list = []
SimilarData = pd.read_csv("WZH/similar_fund_prep.csv")
for indexs in SimilarData.index:
    fundName = SimilarData.loc[indexs].values[0]
    FundCode = str(SimilarData.loc[indexs].values[1]).zfill(6)
    EntityCode = str(SimilarData.loc[indexs].values[2]).zfill(6)
    FundCodeIndex = getFundIndex(FundCode, fundList)
    EntityCodeIndex = getFundIndex(EntityCode, fundList)
    if FundCodeIndex and EntityCodeIndex and FundCodeIndex != EntityCodeIndex:
        if([FundCodeIndex, EntityCodeIndex, "同类基金", "同类基金"] not in similar_fund_relation_list):
            similar_fund_relation_list.append([FundCodeIndex, EntityCodeIndex, "同类基金", "同类基金"])
#成功存储CSV
storeDataToCSV("WZH/kg/similar_fund_relation.csv", similar_fund_relation_list)

print("done3 store success!")

# else:
# 失败情况存储csv
# failed_list.append([fundName, FundCode, EntityCode])
# storeDataToCSV("WZH/similar_fund_relation_failed.csv", failed_list)
# print("Failed", fundName, FundCode, EntityCode)

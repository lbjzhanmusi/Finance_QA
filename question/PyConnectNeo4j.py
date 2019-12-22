#coding=utf-8
from py2neo import Graph,Node,Relationship
from py2neo import RelationshipMatcher

# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='960822')

#搜索既属于金融行业，也有外资背景的企业
res = graph.run("match(:Industry{name:'金融行业'})<-[:industry_of]-(c:Company)-[concept_of]->(:Concept{name:'外资背景'}) return c.name").data() #list类型
#print(res)
for k,v in res[0].items():
    print(v)

# graph查询
res = graph.run("match(:Company{code:'300390'})-[:industry_of]->(n) return n.name").data() #list类型
print(res)
for k,v in res[0].items():
    print(v)


# 查找图数据库中所有关系
relMatch = RelationshipMatcher(graph)
relList = list(relMatch.match(r_type="行业属于"))
for i in relList:
   print(i)


#graph.run("MATCH (n:leafCategory) RETURN n LIMIT 25").to_data_frame()  # dataframe型
#graph.run("MATCH (n:leafCategory) RETURN n LIMIT 25").to_table()  # table
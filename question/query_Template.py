# coding=utf-8
import kg_query as kg
import sys
reload(sys)
sys.setdefaultencoding("utf8")

class query_Template(object):
    def __init__(self):
        self.kg_query = kg.neo4j_graph()

    def __cypher2json(self, cypher_text):
        query_result = self.kg_query.data(cypher_text)
        value = []
        [value.append(item[key].encode('utf-8')) for item in query_result for key in item]
        return value

    def __company_type__(self, query):
        code = query[2]
        cypher_text = """
        match (:Company {{code:'{company_code}'}})-[:industry_of]->(n) return n.name
        """.format(company_code=code)
        query_result = self.kg_query.data(cypher_text)
        value = []
        [value.append((item[key])) for item in query_result for key in item]
        if value == []:
            result = "没找到答案"
            return result
        else:
            result = str(value[0])
            return result

    def __same_fund__(self, query):
        name = query[2]
        cypher_text = """
        MATCH (:Fund {{name:'{fund_name}'}})<-[:samefund_of]->(m)  return m.name
        """.format(fund_name=name)
        value = self.__cypher2json(cypher_text)
        result = "、".join(value)
        return result

    def __foreign_background__(self, query):
        name = query[2]
        cypher_text = """
        match(:Industry{{name:'{industry_name}'}})<-[:industry_of]-(c:Company)-[concept_of]->(:Concept{{name:'外资背景'}}) return c.name
        """.format(industry_name=name)
        value = self.__cypher2json(cypher_text)
        result = "、".join(value)
        return result

    def __industry_concept__(self, query):
        name1 = query[2]
        name2 = query[3]
        cypher_text = """
           match(:Industry{{name:'{industry_name}'}})<-[:industry_of]-(c:Company)-[concept_of]->(:Concept{{name:'{concept_name}'}}) return c.name
           """.format(industry_name=name1, concept_name=name2)
        value = self.__cypher2json(cypher_text)
        result = "、".join(value)
        return result

    def __company_stackcode__(self, query):
        name = query[2]
        cypher_text = """
           MATCH (m :Company) where m.name ='{company_name}' return m.code
           """.format(company_name=name)
        query_result = self.kg_query.data(cypher_text)
        value = []
        [value.append((item[key])) for item in query_result for key in item]
        if value == []:
            result = "没找到答案"
            return result
        else:
            result = str(value[0])
            return result

    def kg_query_api(self, query):
        query_index = int(query[1])
        if query_index == 1:
            result = self.__company_type__(query)
        elif query_index == 2:
            result = self.__same_fund__(query)
        elif query_index == 3:
            result = self.__foreign_background__(query)
        elif query_index == 4:
            result = self.__industry_concept__(query)
        elif query_index == 5:
            result = self.__company_stackcode__(query)
        else:
            result = "None"
        return result

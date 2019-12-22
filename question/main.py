import os
import aiml
import query_Template as q_T

q_Template = q_T.query_Template()

wyc_bot = aiml.Kernel()
print("The current path : " + os.path.split(os.path.realpath(__file__))[0])
wyc_bot.learn(os.path.split(os.path.realpath(__file__))[0] + "/Template/std-startup.xml")

wyc_bot.respond("load wyc bot")

print(u"\n您好，我是小小小小小冰：\n")
while True:
    input_message = raw_input("Enter your message >>")
    if len(input_message) > 60:
        a = wyc_bot.respond(u"句子长度过长")
        print (a)
        continue

    elif input_message.strip() == '':
        b=wyc_bot.respond(u"无")
        print (b)
        continue
    if input_message == 'q':
        exit()
    else:
        # print(inp ut_message.encode('utf-8'))
        response = wyc_bot.respond(input_message)
        if response == "":
            ans = wyc_bot.respond(u'找不到答案')
        elif response[0] == "%":
            query_list = response.replace(" ", "").split("%")
            response = q_Template.kg_query_api(query_list)
            print(response)
        # 号开头说明没有匹配到答案
        elif response.__contains__("NoMatchingTemplate"):
            pass
        else:
            print(response)

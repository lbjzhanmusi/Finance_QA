import json
import requests

#按照分页来
movie_type = ['剧情', '喜剧', '动作', '爱情', '科幻', '动画', '悬疑',
              '惊悚', '恐怖', '犯罪', '同性', '音乐', '歌舞', '传记',
              '历史', '战争', '西部', '奇幻', '冒险', '灾难', '武侠']
movie_zone = ['中国大陆', '美国', '香港', '台湾', '日本',
              '韩国', '英国', '法国', '德国', '意大利',
              '西班牙', '印度', '泰国', '俄罗斯', '伊朗',
              '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦']
for type in movie_type:
    for zone in movie_zone:
        for i in range(0,10000,20):
            print("i is:", i)
            url = str("https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={页面}&genres="+ type + "&countries="+ zone +"").format(页面 = i)
            print(url)
            try:
                txt = requests.get(url)
                data = json.loads(txt.text)["data"]
            except:
                print("over size:")
                break
            if len(data) == 0:
                break;
            for each in data:
                print(each)
                #save data
# _*_ coding:utf-8 _*_ 
import json
import jieba.analyse

'''

本module用来用作搜索模块的检索函数
'''

if __name__=='__main__':

    json_path=u'../json/search.json'

else:
    from config import ROOT
    json_path=u'%s/json/search.json'%ROOT

class Search(object):


    def __init__(self,):

        self.read_json_to_list()

    def read_json_to_list(self,):

        with open(json_path,'r')as f:
            r=f.read().decode('utf-8','ignore')
        search_list=json.loads(r)
        for d in search_list:
            d['keyword']=set(d['keyword'])

        self.search_list=search_list


    @classmethod
    def analyse_text(self,text):
        ##将输入进行分词

        tags = jieba.analyse.extract_tags(text, topK=20, withWeight=False,)
        return set(tags)

    def get_search_list_by_keyword(self,keyword):
        result=[]
        search_tags=self.analyse_text(text=keyword)
        

        for line in self.search_list:
            keyword_tags=line.get('keyword')
            # print u' '.join(search_tags)
            # print u' '.join(keyword_tags)
            u=keyword_tags.intersection(search_tags)
            u=list(u)
            if u:
                # print u'find path =%s by keyword=%s'%(line.get('filepath'),keyword)
                d=dict(filepath=line.get('filepath'),keyword=u)
                result.append(d)

            else:
                pass

        if result:
            search_list=self.order_search_list(result)
        else:
            search_list=[]

        return search_list


    def order_search_list(self,List):
        ##根据匹配到的关键词的多少进行排序，后期可以根据book的热度给与更高的权重进行排序
        t=[]
        for d in List:
            keyword_list=d.get('keyword')
            filepath=d.get('filepath')
            length=len(keyword_list)
            t.append((length,filepath))

        t=sorted(t,reverse=True)
        order_list=[]
        for length,filepath in t:
            for d in List:
                if filepath==d.get('filepath'):
                    line=dict(filepath=d.get('filepath'),keyword=d.get('keyword'))
                    order_list.append(line)

        return order_list









def test():

    search=Search()
    keyword=u'舌头'
    search_list=search.get_search_list_by_keyword(keyword=keyword)
    for d in search_list:
        filepath=d.get('filepath')
        keyword=d.get('keyword')
        keyword=u' '.join(keyword)
        print filepath,keyword



if __name__ =='__main__':

    test()








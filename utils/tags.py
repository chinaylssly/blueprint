# _*_ coding:utf-8 _*_ 
import json
from collections import OrderedDict

'''
本模块用来检索tags模块
'''

if __name__=='__main__':

    json_path=u'../json/tags.json'

else:
    # json_path=u'json/tags.json'
    from config import ROOT
    json_path=u'%s/json/tags.json'%ROOT

class Tags(object):


    def __init__(self,):

        self.read_json()
        self.get_tag_dict()


    
    def read_json(self,):

        with open(json_path,'r')as f:

            self.content=f.read().decode('utf-8','ignore')
            self.lines=self.content.strip().split('\n')


    def get_tags(self,):

        tags=json.loads(self.lines[0]).get('tags')
        return tags


    def get_tag_dict(self,):

        tag_dict=OrderedDict()
        for line in self.lines[2:]:

            d=json.loads(line)
            key=d.keys()[0]
            vaule=d.values()[0]
            tag_dict[key]=vaule

        self.Dict=tag_dict

    def get_path_by_tag(self,tag):

        return self.Dict.get(tag)




def test():

    t=Tags()
    tags=t.get_tags()
    # print tags


if __name__ =='__main__':

    test()








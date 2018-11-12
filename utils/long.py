#_*_ coding:utf-8 _*_
import os,sys
import json


'''
本module用来获取static下long foldor
'''

if __name__=='__main__':
    ROOT='../'
else:    
    from config import ROOT

class Long(object):


    def __init__(self,):

        self.get_book()
        self.get_item()

    def get_book(self,):


        folder=u'static/long'
        self.path=u'%s/%s'%(ROOT,folder)
        self.books=os.listdir(self.path)


    def get_item(self,):

        item_dict={}

        for book in self.books:

            folder=u'%s/%s'%(self.path,book)
            filenames=os.listdir(folder)

            stat=[(os.path.getmtime(u'%s/%s'%(folder,filename)),filename) for filename in filenames]

            order_stat=sorted(stat)
            order_filename=[item[1] for item in order_stat]
            l=[]
            
            for index,value in enumerate(order_filename):
                d=dict(index=index+1,item=value.rsplit('.',1)[0])
                l.append(d)
            item_dict[book]=l

        self.item_dict=item_dict



def test():

    LONG=Long()
    item_dict=LONG.item_dict

    print json.dumps(item_dict,ensure_ascii=False)



if __name__=='__main__':

    test()





 

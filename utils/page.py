#_*_ coding:utf-8 _*_

'''
本函数用来分页，以及获取每一页每一条数据的start，begin索引
'''
class Page(object):

    @classmethod
    def get_index(self,total=308,per=30,page=3):

        if total%per==0:
            pages=total/per
        else:
            pages=total/per+1

        self.pprint(u'总页码为：%s'%pages)

        begin=(page-1)*per+1

        end=begin+per
        #得到第page页的第一项和最后一项

        if end>total:
      
            end=total

            self.pprint(u'最后一页不足%d条，还剩%d条信息'%(per,(end-begin)))
        
        self.pprint(u'第%d页开始索引为%d'%(page,begin))
        self.pprint(u'第%d页结束索引为%d'%(page,end))
        self.pprint(u'总信息%d条的项目，以%d条为一页，可以分为%d页'%(total,per,pages))
        self.pprint(u'---------------------------------')
        
        return begin,end,pages

    @classmethod
    def get_next(self,page=8,pages=10):

        last_page=page-1
        next_page=page+1
        
        if last_page<1:
            last_page=1
            
        if next_page>pages:
            next_page=pages
            
        self.pprint(u'第%d页的上一页页码是：%d'%(page,last_page))
        self.pprint(u'第%d页的下一页页码是：%d'%(page,next_page))
        self.pprint(u'------------------------------')
        
        return last_page,next_page


    @classmethod
    def get_list(self,page=8,pages=50,echo=5):


        sub=page-echo
        add=page+echo

        if sub<1:
            
            if add<=pages:
                l=[x for x in range(1,add+1)]
                
            else:
                l=[x for x in range(1,pages+1)]
                
        else:
            if add<=pages:
                l=[x for x in range(sub,add+1)]
                
                
            else:
                l=[x for x in range(sub,pages+1)]
                
        self.pprint(u'当前页相邻的页码数为：%s'%l)
        self.pprint(u'------------------------------')
        return l   

    @classmethod
    def pprint(self,stdout):

        if __name__ =='__main__':

            print stdout




def test():

    Page.get_index()
    Page.get_next()
    Page.get_list(3,3,2)



if __name__ =='__main__':

    test()

    


    




    

    
    
    

    

    
        
    

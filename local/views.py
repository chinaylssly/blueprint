# _*_ coding:utf-8 _*_ 

from flask import render_template
from config import PATH
from local import local
##默认命名空间在上级目录
import os
# from functools import wraps

# from run import is_login
from utils.is_login import is_login 



@local.route('/')
@is_login
def category():

    categorys=os.listdir(PATH)

    return render_template('local/category.html',categorys=categorys)

@local.route('/<category>')
@is_login
def book(category):

    book_path=u'%s/%s'%(PATH,category)
    books=os.listdir(book_path)

    return render_template('local/book.html',books=books,category=category)

@local.route('/<category>/<book>')
@is_login
def item(category,book):

    item_path=u'%s/%s/%s'%(PATH,category,book)
    items=get_items(item_path)

    return render_template('/local/item.html',book=book,items=items,category=category)


@local.route('/<category>/<book>/<index>')
@is_login
def read(category,book,index):
    folder=u'%s/%s/%s'%(PATH,category,book)
    List=get_items(folder)

    for page,Dict in enumerate(List):

        ids=Dict.get('index')
        item=Dict.get('item')

        if int(index) == ids:

            filename=u'%s/%s-%s.txt'%(folder,ids,item)
            with open(filename,'r')as f:
                content=f.read()

            content=content.decode('utf-8','ignore')
            lines=content.split('\n')

            last_index=max(page-1,0)
            next_index=min(page+1,len(List)-1)

            last_exp=u'上一章'
            next_exp=u'下一章'

            if last_index==0:

                last_exp=u'首章'

            if next_index==len(List)-1:

                next_exp=u'终章'

            last_page=List[last_index]
            next_page=List[next_index]





            break



    return render_template('/local/read.html',category=category,item=item,lines=lines,book=book,last_page=last_page,next_page=next_page,last_exp=last_exp,next_exp=next_exp)





def get_items(item_path):

    
    filenames=os.listdir(item_path)

    d={}
    items=[]
    for filename in filenames:

        l=filename.split(u'-')
        if len(l)==1:
            continue
        ##去除无索引item

        index=l[0]
        item=l[1]

        d[int(index)]=item

    keys=sorted(d.keys())
    for key in keys:

        index=key
        item=d[key]

        items.append(dict(index=index,item=item.split('.')[0]))

    return items



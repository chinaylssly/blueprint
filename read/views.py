# _*_ coding:utf-8 _*_ 

from flask import render_template
from read import read
import os
from config import ROOT
from utils.is_login import is_login
from utils.long import Long


LONG=Long()

@read.route('/')
@is_login
def books():
    
    book_books=get_books()
    long_books=LONG.books

    books=book_books+long_books

    return render_template('/read/book.html',books=books)


@read.route('/<book>')
@is_login
def items(book):

   
    try:
        items=get_items(book=book)

    except:
        items=LONG.item_dict.get(book)


    return render_template('/read/item.html',book=book,items=items)


@read.route('/<book>/<int:index>')
@is_login
def read(book,index):

    folder=u'%s/static/book/%s'%(ROOT,book)

    if os.path.exists(folder):
        List=get_items(book)

        for page,Dict in enumerate(List):

            ids=Dict.get('index')
            item=Dict.get('item')

            if index == ids:

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

    else:

        item_dict=LONG.item_dict
        List=item_dict.get(book)

        if List:

            length=len(List)
            item=List[index-1].get('item')
            filename=u'%s.txt'%item
            last_index=max(1,index-1)
            next_index=min(length,index+1)

            last_page=List[last_index-1]
            next_page=List[next_index-1]

            filepath=u'%s/static/long/%s/%s'%(ROOT,book,filename)
            with open(filepath,'r')as f:

                    content=f.read()

            content=content.decode('utf-8','ignore')
            lines=content.split('\n')

            last_exp=u'上一章'
            next_exp=u'下一章'

            if last_index==1:

                last_exp=u'首章'

            if next_index==length:

                next_exp=u'终章'

        else:

            return u'404 not found %s'%book








    return render_template('/read/read.html',item=item,lines=lines,book=book,last_page=last_page,\
                                                next_page=next_page,last_exp=last_exp,next_exp=next_exp)



def get_items(book):

    folder=u'%s/static/book/%s'%(ROOT,book)
    filenames=os.listdir(folder)

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




def get_books():

    path=u'%s/static/book'%(ROOT)

    folders=os.listdir(path)
    ##传入template字符串为unicode编码
        
    return folders
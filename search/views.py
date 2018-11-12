# _*_ coding:utf-8 _*_ 

from flask import render_template,redirect,request,session
from search import search
import logging
from utils.is_login import is_login
from utils.search import Search
from utils.page import Page


SEARCH=Search()



logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        # filename=log_file,
                        # filemode='a'
                        ) 

@search.route('/',methods=['get'])
# @is_login
def index():

    return render_template('search/search.html') 


@search.route('/keyword',methods=['post'])
@is_login
def post_result():
    global temp
    form=request.form
    keyword=form['keyword']

    if not isinstance(keyword,unicode):
        keyword=keyword.decode('utf-8','ignore')


    result=SEARCH.get_search_list_by_keyword(keyword=keyword)
    # session['search']=(result,keyword)
    temp=(result,keyword)

    return redirect('/search/result/1')


@search.route('/result/<int:page>')
def result(page):
    # data=session.get('search')
    data=temp
    result=data[0]
    search_keyword=data[1]
    total=len(result)
    begin,end,pages=Page.get_index(page=page,total=total,per=20)
    page_result=result[begin:end]

    page_list=Page.get_list(pages=pages,page=page,echo=5)

    jinja_list=[]
    for d in page_result:

        filepath=d.get('filepath')
        keyword=d.get('keyword')
        keyword_str=u','.join(keyword)
        l=filepath.split('/')
        book=l[-1].split('.')[0]
        category=l[-2]
        finish=l[-3]
        jinja_list.append([finish,category,book,keyword_str])


    next_page=min(pages,page+1)
    last_page=max(1,page-1)

    return render_template('search/result.html',current_page=page,total=total,keyword=search_keyword,page_list=page_list,pages=pages,last_page=last_page,\
                                                next_page=next_page,jinja_list=jinja_list,)








# _*_ coding:utf-8 _*_ 

from flask import render_template,redirect,request
from tags import tags
import os
import logging
from utils.is_login import is_login
from utils.tags import Tags
from utils.page import Page


Tag=Tags()


@tags.route('/')
# @is_login
def show_tags():

    keywords=Tag.get_tags()
    return render_template('tags/tags.html',keywords=keywords) 

@tags.route('/<tag>/<int:page>')
@is_login
def tag_tail(tag,page):

    paths=Tag.get_path_by_tag(tag)
    length=len(paths)

    begin,end,pages=Page.get_index(total=length,per=30,page=page)

    infos=paths[begin:end]
    lines=[]
    for info in infos:

        l=info.split('/')
        book=l[-1].split('.')[0]
        category=l[-2]
        finish=l[-3]

        lines.append((finish,category,book))

    page_list=Page.get_list(page=page,echo=5,pages=pages)

    last_page=max(1,page-1)
    next_page=min(pages,page+1)


    return render_template('/tags/tag.html',lines=lines,page_list=page_list,last_page=last_page,next_page=next_page,tag=tag,current_page=page,pages=pages)








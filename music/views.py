# _*_ coding:utf-8 _*_ 

from flask import render_template,redirect,request
from music import music
import os
import logging
from utils.is_login import is_login
from utils.voice import Voice
from utils.page import Page
from utils.encrypt import Encrypt
import collections


root=u'e:/psftp/voice'

folder_dict=Voice.read_folder_txt()
folder_list=Voice.get_folder_list()

@music.route('/')
@is_login
def category():


    return render_template('music/category.html',folders=folder_list,folder_dict=folder_dict) 


@music.route('/<folder>/<int:page>')
@is_login
def folder(folder,page):


    src_list=Voice.get_src(folder=folder)
    title=folder_dict.get(folder,folder)

    length=len(src_list)

    page_list=Page.get_list(pages=length,page=page,echo=5)

    page=max(1,page)
    page=min(length,page)

    last_page=max(1,page-1)
    next_page=min(length,page+1)

    src=src_list[page-1]
 


    return render_template('music/folder.html',page=page,src_list=src_list,folder=folder,title=title,src=src,\
                                                page_list=page_list,last_page=last_page,next_page=next_page,current_page=page,pages=length) 


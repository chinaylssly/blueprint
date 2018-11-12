# _*_ coding:utf-8 _*_ 

from flask import render_template,redirect,request
from mm import mm
import os
import logging
from utils.is_login import is_login
from utils.path import Path
from utils.page import Page
from utils.encrypt import Encrypt
import collections


#######设置static_folder，便于直接访问

# root_dict=Path.get_img_folder_by_category()
category_dict=Path.get_category()
folder_dict=Path.read_json_to_dict(name=u'folder')
item_dict=Path.read_json_to_dict(name=u'item')
img_b64_dict=collections.OrderedDict()
##用于存放最近访问过的img的base64


@mm.route('/')
@is_login
def category():

    
    return render_template('/mm/category.html',category_dict=category_dict)


@mm.route('/<category>/<int:page>')
@is_login
def folders(category,page):

    

    info=folder_dict.get(category)


    if not info:
        ##路径不存在，拒绝访问
        return redirect('/')

    else:

        folders=info.get('folders')

        length=len(folders)

        begin,end,pages=Page.get_index(total=length,per=30,page=page)

        inner_folders=folders[begin:end]

        page_list=Page.get_list(page=page,pages=pages,echo=5)


        last_page=max(1,page-1)
        next_page=min(pages,page+1)

        category_echo=category_dict.get(category)


        return render_template('mm/folder.html',category=category,page_list=page_list,category_echo=category_echo,\
                                                    folders=inner_folders,current_page=page,last_page=last_page,next_page=next_page,pages=pages)




@mm.route('/<category>/<folder>/<int:page>')
@is_login
def item(category,folder,page):

    ##利用img base64 读取不在static下的文件

    folder_dict_value=folder_dict.get(category)
    if folder_dict_value:

        root=folder_dict_value.get('root')
        folders=folder_dict_value.get('folders') 
        
        item_key=u'%s-%s'%(category,folder)
        filenames=item_dict.get(item_key)

        if filenames:

            category_dict=Path.get_category()

            category_echo=category_dict.get(category)

            item_length=len(filenames)
            folder_length=len(folders)

            folder_index=folders.index(folder)

            last_folder_index=max(1,folder_index-1)
            next_folder_index=min(folder_length-1,folder_index+1)

            last_folder=folders[last_folder_index]
            next_folder=folders[next_folder_index]
            ##上一篇以及下一篇


            page=min(page,item_length)
            page=max(page,1)
            ##page最小取值为1，最大取值为item_length
            filename=filenames[page-1]
            extend=filename.rsplit('.',1)[-1]
            img_path=u'%s/%s/%s'%(root,folder,filename)
            
            src=img_path.split(':',1)[-1]
            # print img_path

            


            last_page=max(1,page-1)
            next_page=min(item_length,page+1)
            #上一页以及下一页


            headers=request.headers
            agent=headers['User-Agent']
            width='70%'
            echo=5
            if 'linux' in agent.lower():
                width='100%'
                echo=1

            item_page_list=Page.get_list(page=page,pages=item_length,echo=echo)



            return render_template('/mm/item.html',category=category,category_echo=category_echo,folder=folder,last_folder=last_folder,\
                                                        next_folder=next_folder,last_page=last_page,next_page=next_page,src=src,\
                                                        folder_length=folder_length,item_length=item_length,width=width,page=page,\
                                                        item_page_list=item_page_list,current_page=page)




    ##category不存在以及item_key不存在的情况下，均重定向到首页
    return redirect('/')
    






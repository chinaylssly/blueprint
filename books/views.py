# _*_ coding:utf-8 _*_ 

from flask import render_template

from books import books
##默认命名空间在上级目录
import os

from utils.page import Page
from utils.is_login import is_login 
from utils.book import Book

BOOK=Book()


@books.route('/')
@is_login
def path():

    path=BOOK.path_dict.keys()

    return render_template('books/path.html',path=path)

@books.route('/<path>')
@is_login
def category(path):

    categorys=BOOK.category_dict.get(path)

    return render_template('books/category.html',categorys=categorys,path=path)


@books.route('/<path>/<category>/<int:page>')
@is_login
def book(path,category,page):


    filenames=BOOK.book_dict.get(path).get(category)

    length=len(filenames)

    begin,end,pages=Page.get_index(page=page,total=length,per=30)

    current_filenames=filenames[begin:end]

    page_list=Page.get_list(pages=pages,page=page,echo=5)

    next_page=min(pages,page+1)
    last_page=max(1,page-1)

    books=[filename.rsplit('.',1)[0] for filename in current_filenames]



    return render_template('/books/book.html',category=category,last_page=last_page,books=books,pages=pages,\
                                            current_page=page,next_page=next_page,path=path,page_list=page_list)




@books.route('/<path>/<category>/<book>')
@is_login
def read(path,category,book):

    root=BOOK.path_dict.get(path)
    filename=u'%s.txt'%book
    filepath=u'%s/%s/%s'%(root,category,filename)
    lines=Book.read_book_to_lines(filepath=filepath)

    filenames=BOOK.book_dict.get(path).get(category)

    index=filenames.index(filename)

    last_index=max(0,index-1)
    next_index=min(len(filenames)-1,index+1)

    last_exp=filenames[last_index].rsplit(',.',1)[0]
    next_exp=filenames[next_index].rsplit('.',1)[0]

    return render_template('books/read.html',path=path,lines=lines,category=category,book=book,last_exp=last_exp,\
                                                next_exp=next_exp)
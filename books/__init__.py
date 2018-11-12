# _*_ coding:utf-8 _*_ 

from flask import Blueprint

books=Blueprint('books',
                __name__,
                # template_folder='templates/local',
                # static_folder='f:/data/story',
                )


import views
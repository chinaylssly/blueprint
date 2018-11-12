# _*_ coding:utf-8 _*_ 

from flask import Blueprint


read=Blueprint('read',
                __name__,
                # template_folder='templates/read',
                static_folder='static/book',
                )

import views
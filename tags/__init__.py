# _*_ coding:utf-8 _*_ 

from flask import Blueprint


tags=Blueprint('tags',
                __name__,
                # template_folder='templates/read',
                # static_folder=u'json',
                )

import views
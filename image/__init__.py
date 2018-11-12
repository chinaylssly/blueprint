# _*_ coding:utf-8 _*_ 

from flask import Blueprint


image=Blueprint('image',
                __name__,
                # template_folder='templates/read',
                # static_folder='static',
                )

import views
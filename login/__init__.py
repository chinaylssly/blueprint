# _*_ coding:utf-8 _*_ 

from flask import Blueprint

login=Blueprint('login',
                __name__,
                # template_folder='../templates/login',
                # static_folder='../templates/read',
                )


import views
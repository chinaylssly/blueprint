# _*_ coding:utf-8 _*_ 

from flask import Blueprint


mm=Blueprint('mm',
                __name__,
                # template_folder='templates/read',
                static_folder=u'd:',
                )

import views
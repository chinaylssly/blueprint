# _*_ coding:utf-8 _*_ 

from flask import Blueprint


music=Blueprint('music',
                __name__,
                # template_folder='templates/read',
                static_folder=u'e:/psftp/voice',
                )

import views
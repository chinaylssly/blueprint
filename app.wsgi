# _*_ coding:utf-8 _*_

import sys
import logging
from traceback import format_exc

#Expand Python classes path with your app's path
#将项目根目录加入环境变量
sys.path.insert(0, "C:\Users\sunzhiming\Desktop\\blueprint")
 
import os

try:
    import test

    from run import app

except:
    s=test.__file__
    log=format_exc()
    logging.error(log)
    logging.error(s)
    logging.error(sys.path)

 
#Put logging code (and imports) here ...
 
#Initialize WSGI app object

application = app

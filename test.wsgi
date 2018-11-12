import sys
import logging
from traceback import format_exc

#Expand Python classes path with your app's path

sys.path.append( "C:\Users\sunzhiming\Desktop\\blueprint")
 
import os

try:
    import test

    from tests import app

except:
    s=test.__file__
    log=format_exc()
    logging.error(log)
    logging.error(s)
    logging.error(sys.path)

 
#Put logging code (and imports) here ...
 
#Initialize WSGI app object
application = app

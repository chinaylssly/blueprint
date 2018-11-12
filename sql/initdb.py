#_*_ coding:utf-8 _*_

from mysql import MySQL
import logging

def create_db(db=u'blueprint'):

    query=u'create database if not exists %s'%(db)

    MySQL(db='').execute(query)



if __name__=='__main__':

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        ) 

    create_db()

#_*_ coding:utf-8 _*_

import os,sys


from mysql import MySQL
import logging




if __name__=='__main__':

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        ) 

# os._exit(0)



class USER(MySQL):

    def __init__(self,db='blueprint'):

        MySQL.__init__(self,db=db)

    def create_user(self,):

        query='''create table if not exists user(
                id int not null primary key auto_increment,
                username varchar(100) not null ,
                password varchar(100) not null,
                status int not null default '0',
                create_time timestamp not null default current_timestamp)
                default charset=utf8'''

        self.execute(query)

       


    def check_user(self,username='admin'):
        ##用于注册以及用户登录
       
        sql='select password from user where username like "%s"'%(username)
        result = self.execute(sql)
        count=result.get('count')
        assert count<2
        if count:
            return result.get('data')[0].get('password')
        else:
            return None
     

    def insert_user(self,username='admin',password='password'):
        
        sql='insert into user (username,password) values ("%s","%s")'%(username,password)
        result = self.execute(sql)
        return result.get('count')

        

    def delete_user(self,username):
      
        sql='delete from user where username like "%s"'%(username)
        result = self.execute(sql)
        return result.get('count')
        


def INIT():

    user=USER()
    user.create_user()
    


if __name__ =='__main__':

    INIT()
    
    pass
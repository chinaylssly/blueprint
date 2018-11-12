# _*_ coding:utf-8 _*_ 

from flask import render_template,session,redirect,request
from functools import wraps
from sql import USER

'''
本module用来判断用户

'''
def is_login(func,):
    ##登录检测

    @wraps(func)
    def inner(*args,**kw):

        username=request.cookies.get('username')
        password=request.cookies.get('password')

        user=USER()
        password_from_sql=user.check_user(username=username)

        if password==password_from_sql:

            session['username']=username


        username=session.get('username')
        # print u'装饰器中的username:%s'%username

        if username:

            return func(*args,**kw)

        else:

            session['user_flash']=u'你尚未登录，登陆后可查看精彩内容'
            if request.method.lower()=='get':

                session['memory']=request.url

            else:
                session['memory']='/'
                
            ##要想有记忆功能，只能在func内部判断username，否则，无法记忆登陆之前请求的url，此出功能暂作保留
            return redirect('/user/login')

    return inner








        

    


# _*_ coding:utf-8 _*_ 

from flask import Flask,render_template,url_for,request,session,flash,redirect\
     ,make_response

from login import login
from config import ROOT
import os,sys
from traceback import format_exc
from sql import USER
from utils import Encrypt

from datetime import datetime
from datetime import timedelta

user=USER()



@login.route('/')
def index():
    ##登录首页

    return render_template('login/index.html')



@login.route('/sign',methods=['GET'])
def sign():
    ##注册页面
    return render_template('login/sign.html')



@login.route('/signin',methods=['POST'])
def signin():
    ##注册状态页面
    status=None
    form=request.form
    username=form['username']
    password=form['password']
    submit=form['submit']
    invention=form['invention']
    ##需要邀请码的话，可以在此处加扩展
    # invention_from_sql=user.check_invention(invention)
    invention_from_sql='8888'
    

    if (not username) and (not password) :#判断用户名或密码是否为空

        status='empty'
        sign_error_message=u'用户名或密码不能为空'
        code=0

    elif (r'%' in username) or (r'"' in username):#判断username中是否含有非法字符%,"

        status='illegal'
        sign_error_message=u'用户名中不能含有特殊字符%与"'
        code=0

    elif len(username)<4:

        sign_error_message=u'用户名需不少于4位'

    elif len(password)<6:

        sign_error_message=u'密码需不少于6位'


            
    elif password!=submit:#判断密码与确认密码是否相同
                
        status='different'
        sign_error_message=u'两次输入的密码不一致'
        code=0

    elif invention != invention_from_sql:

        status='bad invention'
        sign_error_message=u'邀请码无效'
        code=0

    else:

        chk=user.check_user(username)
        
        if  chk:#判断username是否已经注册过
            
            status='exists'
            sign_error_message=u'用户名：%s 已注册'%(username)
            code=0
        
        else:#注册成功，将注册信息写入数据库
                
            status='success'
            message=u''
            code=1

            password_b64=Encrypt.b64encode(password)

            count=user.insert_user(username=username,password=password_b64)



            if count==0:
                ##注册信息插入数据库失败
                status='sql error'
                message=u''
                code=0

            else:
                return render_template('login/signin.html',username=username,password=password,status=status)

    return render_template('login/sign.html',sign_error_message=sign_error_message)


    





@login.route('/login',methods=['GET'])
def logins():
    ##登录
    
    username=session.get('username')
        
    if username:
                
        return redirect('/')
        #登陆状态下再次尝试登陆会自动跳转到指定页面，如首页
    
    return render_template('login/login.html')





@login.route('/loginin',methods=['POST'])
def loginin():

    ##登录状态，（登录失败的情况可以重定向到login模块）


    ##form接受的字符串为unicode编码
    status=None 
    form=request.form
    username=form['username']
    password=form['password']

    
    
    if (r'%' in username) or (r'"' in username):#判断username中是否含有非法字符%,"

        status='illegal'
        login_fail_message=u'用户名中不能含有特殊字符%与"'
    else:

        password_sql=user.check_user(username)
        #数据库为utf-8编码，故参数需要转换为utf-8编码
        
        
        if password_sql:#查询数据库，发现username可以用以登录
            
            password_b64=Encrypt.b64encode(password)
            #数据库查询结果返回unicode编码字符


            
            if password_sql==password_b64:#用户输入密码与数据库中信息匹配，登陆成功
                
                status='success'

                session['username']=username

                hostory=session.get('memory')


    
                if hostory:
                    #登录成功以后跳转页面memory
                    # return redirect(hostory)
                    response=make_response(redirect(hostory))

                else:
                    # return redirect('/')
                    response=make_response(redirect('/'))

                expires = datetime.now() + timedelta(days=13,hours=16)#这里一定要减8个小时
                response.set_cookie('username',username,expires=expires)
                response.set_cookie('password',password_b64,expires=expires)

                return response
                
            else:#用户密码输入不正确，登录失败
                
                status='wrong_password'
                login_fail_message=u'密码错误'

                
        else:#用户输入username尚未注册，不能用以登录
            status='wrong_username'
            login_fail_message=u'用户名：%s 尚未注册'%(username)

    return render_template('/login/login.html',login_fail_message=login_fail_message)



    # return render_template('login/loginin.html',username=username,status=status)






@login.route('/logout')
def logout():
    ##登出
    session['user_flash']=u'You were logged out'
    session['username']=None
    session['memory']=None
    response=make_response(redirect('/user/login'))
    response.delete_cookie('username')
    response.delete_cookie('password')
    return response



@login.route('/delete')
def delete_user():

  
    username=session.get('login_in')

    
    if username:
        
        # user.delete_user(username=username)

        session['user_flash']=u'成功删除用户%s'%(username.decode('utf-8','ignore'))
        session['username']=None
    else:

        session['user_flash']=u'你还尚未登录，不能注销账号'

    return redirect('/user/login')

# _*_ coding:utf-8 _*_ 

from flask import Flask,render_template,session,redirect,request
from sql import USER
from login import login
from read import read
from local import local
from image import image
from music import music
from mm import mm
from tags import tags
from search import search
from books import books

app=Flask(__name__,template_folder='templates',static_folder='static')
app.secret_key = 'some_secret'

app.register_blueprint(login,url_prefix='/user')
app.register_blueprint(read,url_prefix='/books')
app.register_blueprint(local,url_prefix='/local')
app.register_blueprint(image,url_prefix='/image')
app.register_blueprint(music,url_prefix='/music')
app.register_blueprint(mm,url_prefix='/mm')
app.register_blueprint(tags,url_prefix='/tags')
app.register_blueprint(search,url_prefix='/search')
app.register_blueprint(books,url_prefix='/path')




@app.route('/')

def index():

    username=request.cookies.get('username')
    password=request.cookies.get('password')

    user=USER()
    password_from_sql=user.check_user(username=username)

    if password==password_from_sql:

        session['username']=username

    username=session.get('username')
    return render_template('index.html',username=username)





if __name__ =='__main__':

    app.run(host='0.0.0.0',port=80,debug=True)
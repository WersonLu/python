#!/usr/bin/env python

# encoding: utf-8

'''

@author: wersonliu

@contact: wersonliugmail.com

@time: 2018/1/12 8:49

'''

from flask import Flask, request, abort, make_response, redirect

# from flask.ext.script import Manager
from flask import Flask, render_template

app = Flask(__name__)
# manage = Manager(app)


# @app.route('/')
# def index():
#     # user_agent = request.headers.get('User-Agent')
#     # return '<h1>你正浏览%s</h1>' % user_agent
#     return '<h1>bad request</h1>',400
@app.route('/')
def index():
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response
    # 重定向
    # return redirect('http://www.baidu.com')
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '</h1>hello,%s</h1>' % user.name


if __name__ == '__main__':
    app.run(debug=True)

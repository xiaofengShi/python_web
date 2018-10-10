'''
File: app.py
Project: FLASK
File Created: Saturday, 6th October 2018 10:29:58 pm
Author: icey (sxf1052566766@163.com)
-----
Last Modified: Saturday, 6th October 2018 10:30:43 pm
Modified By: icey (sxf1052566766@163.com>)
-----
Copyright 2018.06 - 2018 onion Math, onion Math
'''

from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    log = 'hello world  sxf'
    return log


@app.route('/article/<id>')
def article(id):
    log = '请求的参数为：{}'.format(id)
    return log


if __name__ == '__main__':
    app.run()

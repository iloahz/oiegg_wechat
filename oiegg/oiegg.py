from func import *
from model import app
from flask import Flask, request, redirect
import topten

@app.route('/', methods = ['POST'])
def MainHandler():
    x = request.data
    ToUserName, FromUserName, CreateTime, MsgType, Content = parseTextXml(x)
    ToUserName, FromUserName = FromUserName, ToUserName
    res = ''
    if topten.validate(Content):
        res = topten.answer(ToUserName, FromUserName, CreateTime, MsgType, Content)
    return res

@app.route('/topten/<cmd>')
def TopTenHandler(cmd):
    if cmd == 'update':
        topten.update()
        return 'update successfully'

if __name__ == '__main__':
    app.run(debug = True)

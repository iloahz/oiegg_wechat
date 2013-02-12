from func import *
from model import app
from flask import Flask, request, redirect
import topten

@app.route('/', methods = ['GET', 'POST'])
def MainHandler():
    if request.method == 'GET':
        try:
            s = request.args.get('signature')
            t = request.args.get('timestamp')
            n = request.args.get('nonce')
            e = request.args.get('echostr')
            if validateSource(t, n, s):
                return e
            else:
                return 'Bad!'
        except:
            return 'Wechat for OIEGG!'
    else:
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

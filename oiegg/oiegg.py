from func import *
from model import app
from flask import Flask, request, redirect, render_template
import topten
import pattern

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
        if pattern.validate(Content):
            res = pattern.answer(ToUserName, FromUserName, CreateTime, MsgType, Content)
        elif topten.validate(Content):
            res = topten.answer(ToUserName, FromUserName, CreateTime, MsgType, Content)
        return res

@app.route('/topten/<cmd>')
def TopTenHandler(cmd):
    if cmd == 'update':
        topten.update()
        return 'update successfully'

@app.route('/pattern', methods = ['GET', 'POST'])
def PatternHandler():
    if request.method == 'GET':
        return render_template('pattern.html')
    else:
        i = request.form['input']
        o = request.form['output']
        pattern.updatePattern(i, o)
        return ''

@app.route('/pattern/<input>')
def PatternLookup(input):
    return pattern.getOutputByInput(input)

if __name__ == '__main__':
    app.run(host = SERVER_HOST, port = SERVER_PORT, debug = True)

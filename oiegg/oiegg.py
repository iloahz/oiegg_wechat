from func import *
from model import app
from flask import Flask, request, redirect, render_template
import topten
import pattern
import activity

@app.route('/', methods = ['GET', 'POST'])
def MainHandler():
    s = request.args.get('signature')
    t = request.args.get('timestamp')
    n = request.args.get('nonce')
    if not validateSource(t, n, s):
        return 'Invalid Request!'
    if request.method == 'GET':
        try:
            e = request.args.get('echostr')
            return e
        except:
            return 'Invalid Request!'
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
    # try:
    #     s = request.args.get('signature')
    #     t = request.args.get('timestamp')
    #     n = request.args.get('nonce')
    #     if not validateSource(t, n, s):
    #         return 'Invalid Request!'
    #     if request.method == 'GET':
    #         try:
    #             e = request.args.get('echostr')
    #             return e
    #         except:
    #             return 'Invalid Request!'
    #     else:
    #         x = request.data
    #         ToUserName, FromUserName, CreateTime, MsgType, Content = parseTextXml(x)
    #         ToUserName, FromUserName = FromUserName, ToUserName
    #         res = ''
    #         if pattern.validate(Content):
    #             res = pattern.answer(ToUserName, FromUserName, CreateTime, MsgType, Content)
    #         elif topten.validate(Content):
    #             res = topten.answer(ToUserName, FromUserName, CreateTime, MsgType, Content)
    #         return res
    # except:
    #     return render_template('index.html')

@app.route('/topten/<cmd>')
def TopTenHandler(cmd):
    if cmd == 'update':
        topten.update()
        return 'top 10 updated successfully'

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

@app.route('/activity/<cmd>')
def ActivityHandler(cmd):
    if cmd == 'update':
        activity.update()
        return 'activity updated successfully'

if __name__ == '__main__':
    app.run(host = SERVER_HOST, port = SERVER_PORT, debug = True)

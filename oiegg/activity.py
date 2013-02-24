from func import *

def validate(c):
    if c.startsWith('hd'):
        return True
    return False

def answer(ToUserName, FromUserName, CreateTime, MsgType, Content):
    Content = 'act'
    return genTextXml(ToUserName, FromUserName, CreateTime, MsgType, Content)

def update():
    pass
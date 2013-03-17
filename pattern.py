from func import *

def updatePattern(input, output):
    p = Pattern.query.filter_by(input = input).first()
    if p:
        p.output = output
    else:
        p = Pattern(input, output)
        db.session.add(p)
    db.session.commit()

def getOutputByInput(input):
    try:
        p = Pattern.query.filter_by(input = input).first()
        return p.output
    except:
        return 'Pattern doesn\'t exist!'

def validate(c):
    p = Pattern.query.filter_by(input = c).first()
    return p is not None

def answer(ToUserName, FromUserName, CreateTime, MsgType, Content):
    p = Pattern.query.filter_by(input = Content).first()
    Content = p.output
    return genTextXml(ToUserName, FromUserName, CreateTime, MsgType, Content)
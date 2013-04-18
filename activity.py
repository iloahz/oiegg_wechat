# -*- coding: utf-8 -*-
from func import *


def validate(c):
    if c.startswith('hd') or c.startswith('活动'):
        return True
    return False


def answer(ToUserName, FromUserName, CreateTime, MsgType, Content):
    # a = Activity.query.filter(Activity.end >= datetime.datetime.now()).order_by(Activity.start)
    a = Activity.query.order_by(Activity.start)
    Content = []
    cur = datetime.date.today()
    for i in a:
        if i.end < cur:
            db.session.delete(i)
        l = Link(title=i.title, url=i.url, desc=i.title, picUrl=i.avatar)
        if len(Content) < 10:
            Content.append(l)
    db.session.commit()
    return genLinkXml(ToUserName, FromUserName, CreateTime, MsgType, Content)


def parseDate(title):
    title = title.encode('utf-8')
    l = title.find("【")
    r = title.find("】", l)
    s = title[l:r]
    c = 0
    l = []
    # print s
    for i in s:
        if i.isdigit():
            c *= 10
            c += ord(i) - ord('0')
        else:
            if c > 0:
                l.append(c)
            c = 0
    if c > 0:
        l.append(c)
    if len(l) == 4:
        pass
    elif len(l) == 3:
        l.insert(2, l[0])
    elif len(l) == 2:
        l.append(l[0])
        l.append(l[1])
    else:
        l = None
    return l

def updateActivityByDate(ssM, ssD, stM, stD, title, url, avatar):
    print ssM, ssD, stM, stD, title, url, avatar
    a = Activity.query.filter_by(url = url).first()
    if a:
        # a = Activity(ssM, ssD, stM, stD, title, url, avatar)
        pass
    else:
        a = Activity(ssM, ssD, stM, stD, title, url, avatar)
        db.session.add(a)
    db.session.commit()

def update():
    res = getContentByUrl("http://www.oiegg.com/forumdisplay.php?fid=172")
    soup = BeautifulSoup(res)
    soup = soup.find("table", attrs={"id" : "forum_172"})
    soup = soup.findAll('tbody')
    for i in soup:
        try:
            title = i.find('span').getText()
            ssM, ssD, stM, stD = parseDate(title)
            url = 'http://www.oiegg.com/' + i.find('span').find('a')['href']
            updateActivityByDate(ssM, ssD, stM, stD, title, url, getAvatarByUrl(url))
        except:
            pass
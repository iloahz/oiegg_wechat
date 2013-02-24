from model import *
import urllib
import hashlib
from xml.dom import minidom
from BeautifulSoup import BeautifulSoup
import time


def validateSource(timestamp, nonce, signature):
    token = WECHAT_TOKEN
    l = [token, timestamp, nonce]
    l.sort()
    s = ''.join(l)
    s = hashlib.sha1(s).hexdigest()
    return s == signature


def getContentByUrl(url):
    print 'fetching ', url
    t1 = time.time()
    while True:
        try:
            c = urllib.urlopen(url).read()
            t2 = time.time()
            print (t2 - t1) * 1000, 'ms'
            return c
        except:
            pass


def parseTextXml(x):
    d = minidom.parseString(x)
    ToUserName = d.getElementsByTagName('ToUserName')[0].childNodes[0].data
    FromUserName = d.getElementsByTagName('FromUserName')[0].childNodes[0].data
    CreateTime = d.getElementsByTagName('CreateTime')[0].childNodes[0].data
    MsgType = d.getElementsByTagName('MsgType')[0].childNodes[0].data
    Content = d.getElementsByTagName('Content')[0].childNodes[0].data
    return ToUserName, FromUserName, CreateTime, MsgType, Content


def genTextXml(ToUserName, FromUserName, CreateTime, MsgType, Content, FuncFlag = '0'):
    CreateTime = str(int(time.time()))
    r = minidom.getDOMImplementation()
    d = r.createDocument(None, 'xml', None)
    x = d.createElement('xml')
    s = d.createElement('ToUserName')
    t = d.createCDATASection(ToUserName)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('FromUserName')
    t = d.createCDATASection(FromUserName)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('CreateTime')
    t = d.createCDATASection(CreateTime)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('MsgType')
    t = d.createCDATASection(MsgType)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('Content')
    t = d.createCDATASection(Content)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('FuncFlag')
    t = d.createTextNode(FuncFlag)
    s.appendChild(t)
    x.appendChild(s)
    return x.toxml()


def genLinkXml(ToUserName, FromUserName, CreateTime, MsgType, Content, FuncFlag = '0'):
    CreateTime = str(int(time.time()))
    r = minidom.getDOMImplementation()
    d = r.createDocument(None, 'xml', None)
    x = d.createElement('xml')
    s = d.createElement('ToUserName')
    t = d.createCDATASection(ToUserName)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('FromUserName')
    t = d.createCDATASection(FromUserName)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('CreateTime')
    t = d.createTextNode(CreateTime)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('MsgType')
    t = d.createCDATASection('news')
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('Content')
    t = d.createCDATASection('')
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('ArticleCount')
    t = d.createTextNode(str(len(Content)))
    s.appendChild(t)
    x.appendChild(s)
    #a is the 'Articles' node
    a = d.createElement('Articles')
    for link in Content:
        i = d.createElement('item')
        s = d.createElement('Title')
        t = d.createCDATASection(link.title)
        s.appendChild(t)
        i.appendChild(s)
        s = d.createElement('Description')
        t = d.createCDATASection(link.desc)
        s.appendChild(t)
        i.appendChild(s)
        s = d.createElement('PicUrl')
        t = d.createCDATASection(link.picUrl)
        s.appendChild(t)
        i.appendChild(s)
        s = d.createElement('Url')
        t = d.createCDATASection(link.url)
        s.appendChild(t)
        i.appendChild(s)
        a.appendChild(i)
    x.appendChild(a)
    s = d.createElement('FuncFlag')
    t = d.createTextNode(FuncFlag)
    s.appendChild(t)
    x.appendChild(s)
    dat = x.toxml()
    return dat
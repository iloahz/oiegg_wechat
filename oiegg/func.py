from model import *
import urllib
from xml.dom import minidom
from BeautifulSoup import BeautifulSoup
import time

def getContentByUrl(url):
    print 'fetching ', url
    while True:
        try:
            c = urllib.urlopen(url).read()
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
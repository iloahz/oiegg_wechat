from func import *


def validate(c):
    if c.startswith('hd'):
        return True
    return False


def answer(ToUserName, FromUserName, CreateTime, MsgType, Content):
    Content = 'act'
    return genTextXml(ToUserName, FromUserName, CreateTime, MsgType, Content)


def update():
    res = getContentByUrl("http://www.oiegg.com/forumdisplay.php?fid=172")
    soup = BeautifulSoup(res)
    soup = soup.find("table", attrs={"id" : "forum_172"})
    soup = soup.findAll('tbody')
    for i in soup:
        title = i.find('span').getText()
        print title
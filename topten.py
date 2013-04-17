from func import *


def updateTopicByRank(rank, url, title, avatar):
    # print rank, url, title, avatar
    t = TopTenTopic.query.filter_by(rank=rank).first()
    if t:
        t.url = url
        t.title = title
        t.avatar = avatar
    else:
        t = TopTenTopic(rank, url, title, avatar)
        db.session.add(t)
    db.session.commit()


def validate(c):
    if c == '10':
        return True
    return False


def answer(ToUserName, FromUserName, CreateTime, MsgType, Content):
    topics = TopTenTopic.query.order_by(TopTenTopic.rank)
    Content = list()
    for i in range(0, 10):
        topic = topics[i]
        link = Link(title=topic.title, desc="", picUrl=topic.avatar, url=topic.url)
        Content.append(link)
    return genLinkXml(ToUserName, FromUserName, CreateTime, MsgType, Content)


def getAvatarByUrl(url):
    try:
        res = getContentByUrl(url)
        soup = BeautifulSoup(res)
        soup = soup.find('div', attrs={'class': 'avatar'}).find('img')
        url = 'http://www.oiegg.com/' + soup.get('src')
        return url
    except:
        return 'http://www.oiegg.com/images/avatars/noavatar.gif'


def update():
    res = getContentByUrl('http://www.oiegg.com/index.php')
    soup = BeautifulSoup(res)
    soup = soup.find('div', attrs={'class': 'mainbox forumlist box on-left'})
    soup = soup.findAll('li')
    for i in range(0, len(soup)):
        j = soup[i].findAll('a')[1]
        title = j.getText()
        url = 'http://www.oiegg.com/' + j.get('href')
        avatar = getAvatarByUrl(url)
        updateTopicByRank(rank = i, title = title, url = url, avatar = avatar)
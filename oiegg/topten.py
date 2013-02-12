from func import *

def updateTopicByRank(rank, url, title, avatar):
    t = TopTenTopic.query.filter_by(rank = rank).first()
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
    CreateTime = str(int(time.time()))
    r = minidom.getDOMImplementation()
    d = r.createDocument(None, 'xml', None)
    #x is the root node
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
#    logging.info(Content)
    s.appendChild(t)
    x.appendChild(s)
    s = d.createElement('ArticleCount')
    t = d.createTextNode('10')
    s.appendChild(t)
    x.appendChild(s)
    #a is the 'Articles' node
    a = d.createElement('Articles')
    topics = TopTenTopic.query.order_by(TopTenTopic.rank)
    for i in range(0, 10):
#        topic = db.GqlQuery('SELECT * FROM TopTenTopic WHERE rank = :1', i).get()
        topic = topics[i]
        i = d.createElement('item')
        s = d.createElement('Title')
        t = d.createCDATASection(topic.title)
        s.appendChild(t)
        i.appendChild(s)
        s = d.createElement('Description')
        t = d.createCDATASection('')
        s.appendChild(t)
        i.appendChild(s)
        s = d.createElement('PicUrl')
        t = d.createCDATASection(topic.avatar)
        s.appendChild(t)
        i.appendChild(s)
        s = d.createElement('Url')
        t = d.createCDATASection(topic.url)
        s.appendChild(t)
        i.appendChild(s)
        a.appendChild(i)
    x.appendChild(a)
    s = d.createElement('FuncFlag')
    t = d.createTextNode('0')
    s.appendChild(t)
    x.appendChild(s)
    dat = x.toxml()
    return dat

def getAvatarByUrl(url):
    try:
        res = getContentByUrl(url)
        soup = BeautifulSoup(res)
        soup = soup.find('div', attrs = {'class' : 'avatar'}).find('img')
        url = 'http://www.oiegg.com/' + soup.get('src')
        return url
    except:
        return 'http://www.oiegg.com/images/avatars/noavatar.gif'

def update():
    res = getContentByUrl('http://www.oiegg.com/index.php')
    soup = BeautifulSoup(res)
    soup = soup.find('div', attrs = {'class' : 'mainbox forumlist box on-left'})
    soup = soup.findAll('li')
    for i in range(0, len(soup)):
        j = soup[i].findAll('a')[1]
        title = j.getText()
        url = 'http://www.oiegg.com/' + j.get('href')
        avatar = getAvatarByUrl(url)
        updateTopicByRank(i, title, url, avatar)
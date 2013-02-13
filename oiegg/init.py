from model import *
import pattern
import topten

def initDatabase():
    db.create_all()

def initPattern():
    pattern.updatePattern('213', '55555~~~~')

def initTopTen():
    topten.update()

if __name__ == '__main__':
    initDatabase()
    initPattern()
    initTopTen()
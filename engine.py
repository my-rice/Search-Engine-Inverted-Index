def Element:
    pass

def WebSite:

    def __init__(self, host):
        pass

    def __isDir(self, elem):
        pass

    def __isPage(self, elem):

    def __hasDir(self, ndir, cdir):
        pass

    def __newDir(self, ndir, cdir):
        pass

    def __hasPage(self, npag, cdir):
        pass

    def __newPage(self, npag, cdir):
        pass

    def getHomePage(self):
        pass

    def getSiteString(self):
        pass

    def insertPage(self, url, content):
        pass

    def getSiteFromPage(self, page):
        pass

def InvertedIndes:

    def __init__(self):
        pass

    def addWord(self, keyword):
        pass

    def addPage(self, page):
        pass

    def getList(self, keyword):
        pass

def SearchEngine:

    def __init__(self, namedir):
        pass

    def search(self, keyword, k):
        pass

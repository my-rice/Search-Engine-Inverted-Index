from Element import Element

class WebSite:

    def __init__(self, host):
        """È il costruttore della classe WebSite. Crea un nuovo oggetto WebSite per salvare il WebSite dell'host."""
        self._homeDirectory = Element(self,dir=True,name=host)    

    def __isDir(self, elem):
        return elem.isDir()

    def __isPage(self, elem):
        return elem.isWebPage()

    def __hasDir(self, ndir, cdir):
        """
            Se in cdir (un Element) c'è una directory chiamata ndir (una stringa) allora restituisco questa cartella.
            Altrimenti lancio un eccezione.
            Se cdir non è una cartella va lanciata un'altra eccezione.  
        """
        return cdir.searchInChildren(ndir,True)
            
    def __newDir(self, ndir, cdir):
        if(not self.__isDir(cdir)):
            raise Exception(cdir,"is not a directory")
        return cdir.addElement(self,dir=True,name=ndir)
        

    def __hasPage(self, npag, cdir):
        """
            Se in cdir (un Element) c'è una webpage chiamata npag (una stringa), allora restituisco l'Element di questa webPage.
            Altrimenti lancio un'eccezione. 
            Se cdir non è una directory va comunque lanciata un'eccezione.
        """
        return cdir.searchInChildren(npag,False)

    def __newPage(self, npag, cdir):
        if(not self.__isDir(cdir)):
            raise Exception(cdir,"is not a directory")
        return cdir.addElement(self,dir=False,name=npag,content="")

    def getHomePage(self):
        """ 
            Restituisce l'home page del website al quale l'oggetto corrente si riferisce. 
            Oppure lancia un eccezione se l'homepage non esiste.
            L'homepage è una webpage speciale chiamata index.html contenuta nella home directory.
        """
        return self.__hasPage("index.html",self._homeDirectory)
        

    def getSiteString(self):
        """Restituisce una stringa che mostra la struttura del website. (La stringa è formattata in un certo modo)."""
        pass

    def insertPage(self, url, content):
        """ Salva e restituisce la nuova pagina del website. 
        URL: è una stringa che rappresenta l'URL della pagina.
        content: è una stringa che rappresenta il testo contenuto nella pagina.
        """
        x = url.split("/")
        if x[0] != self._homeDirectory.getName():
            raise Exception("This WebPage doesn't belong to this website")
        e = self._homeDirectory
        for i in range(1,len(x)-1): #Da 1 a n-1 www.unisa.it/diem/profs/vinci.html -> n = 4 -> da 1 a 2. 1)diem 2)profs
            e = self.__hasDir(ndir=x[i],cdir=e)
        #Fuori dal for avrò l'Element che rappresenta la directory dove devo inserire la Page
        p = self.__newPage(npag = x[-1], cdir=e)
        p.setContent(content)

        return p
        #TODO: Manca l'aggiornare la seconda struttura dati da mettere
         

    def getSiteFromPage(self, page):
        """Data una webpage, restituisce l'oggetto website al quale la pagina appartiene."""
        if(not self.__isPage(page)):
            raise Exception("The parameter is not a WebPage")
        return page.getWebSite()
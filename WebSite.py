from element import Element,NonExistentElementError,WrongElementError,NotADirectoryError

class PageDoesNotBelongToThisWebSiteError(Exception):
    pass
class PageNotFoundError(Exception):
    pass
class DirectoryNotFoundError(Exception):
    pass
class HomePageDoesNotExistError(Exception):
    pass
class NotAnElementError(Exception):
    pass

class WebSite:
    __slots__ = '_homeDirectory','_homePage'
    def __init__(self, host):
        """È il costruttore della classe WebSite. Crea un nuovo oggetto WebSite per salvare il WebSite dell'host."""
        self._homeDirectory = Element(self,dir=True,name=host)  
        self._homePage = None
    def __isDir(self, elem):#Worst Case: O(1)
        """
            Il metodo __isDir prende in input elem, un'istanza della classe Element.
            Se elem è una directory restituisce True altrimenti False.
            Se elem non è un'istanza della classe Element, il metodo lancia l'eccezione NotAnElementError.
        """
        if not isinstance(elem,Element):
            raise NotAnElementError("elem is not an Element")
        return elem.isDir()

    def __isPage(self, elem): #Worst Case: O(1)
        """
            Il metodo __isPage prende in input elem, un'istanza della classe Element.
            Se elem è una WebPage restituisce True altrimenti False.
            Se elem non è un'istanza della classe Element, il metodo lancia l'eccezione NotAnElementError.
        """
        if not isinstance(elem,Element):
            raise NotAnElementError("elem is not an Element")
        return elem.isWebPage()

    def __hasDir(self, ndir, cdir): #Worst Case: O(log(k))
        """
            Il metodo __hasDir prende in input due parametri: una stringa chiamata ndir e un oggetto Element, che deve essere una directory, chiamato cdir.
            Se all'interno di cdir è presente una directory il cui nome è ndir allora il metodo restituisce la directory trovata in cdir.
            Se la directory il cui nome è ndir non esiste viene lanciata l'eccezione DirectoryNotFoundError.
            Se cdir non è una directory il metodo lancia l'eccezione NotADirectoryError.  
        """
        
        if(not self.__isDir(cdir)):
            raise NotADirectoryError(cdir,"is not a directory")

        try:
            return cdir.searchInOrderedChildren(ndir,True)
        except (NonExistentElementError,WrongElementError):
            raise DirectoryNotFoundError("The directory ",ndir," is not found")
        except:
            raise Exception("An error occurred in __hasDir method")

    def __hasPage(self, npag, cdir): #Worst Case: O(log(k))
        """
            Il metodo __hasPage prende in input due parametri: una stringa chiamata npag e un oggetto Element, che deve essere una directory, chiamato cdir.
            Se all'interno di cdir è presente una WebPage il cui nome è npag allora il metodo restituisce un riferimento ad essa.
            Se la WebPage chiamata npag non esiste viene lanciata l'eccezione PageNotFoundError.
            Se cdir non è una directory il metodo lancia l'eccezione NotADirectoryError.  
        """
        
        if(not self.__isDir(cdir)):
            raise NotADirectoryError(cdir,"is not a directory")

        try:
            return cdir.searchInOrderedChildren(npag,False)
        except (NonExistentElementError,WrongElementError):
            raise PageNotFoundError("The page ",npag," is not found")
        except:
            raise Exception("An error occurred in __hasPage method")
   
            
    def __newDir(self, ndir, cdir):
        """
            Il metodo __newDir prende in input due parametri: una stringa chiamata ndir e un oggetto Element, che deve essere una directory, chiamato cdir.
            Se all'interno di cdir è presente una directory il cui nome è ndir allora il metodo restituisce un riferimento alla directory trovata in cdir.
            Altrimenti crea la directory all'interno della current directory cdir e lo restituisce.
            Se cdir non è una directory il metodo lancia l'eccezione NotADirectoryError.
        """
        if(not self.__isDir(cdir)):
            raise NotADirectoryError(cdir,"is not a directory")
        e = cdir.addElement(self,dir=True,name=ndir) #O(k) nel worst case
        return e        


    def __newPage(self, npag, cdir):
        """
            Il metodo __newPage prende in input due parametri: una stringa chiamata npag e un oggetto Element, che deve essere una directory, chiamato cdir.
            Se all'interno di cdir è presente una WebPage il cui nome è npag allora il metodo restituisce un riferimento alla WebPage trovata in cdir.
            Altrimenti crea la WebPage all'interno della current directory cdir e restituisce un riferimento ad essa.
            Se cdir non è una directory il metodo lancia l'eccezione NotADirectoryError.
        """
        if(not self.__isDir(cdir)):
            raise NotADirectoryError(cdir,"is not a directory")
        e = cdir.addElement(self,dir=False,name=npag,content="") #O(log(k))
        return e

    def getHomePage(self): ###O(1)
        """ 
            Il metodo getHomePage restituisce l'home page del WebSite al quale l'oggetto corrente si riferisce oppure lancia un'eccezione se l'Homepage non esiste.
            L'homepage è una webpage speciale chiamata index.html contenuta nella home directory.
        """

        if(self.homePage == None):
            raise HomePageDoesNotExistError("The HomePage of ",self.getWebSiteName," does not exist")
        else:
            return self._homePage

        

    def getSiteString(self): #O(n)
        """Il metodo getSiteString restituisce una stringa che rappresenta la struttura del website."""
        return self._homeDirectory.getWebSiteStructure("")


    def insertPage(self, url, content): #Worst Case: O(l*k)
        """ 
            Il metodo insertPage salva e restituisce una nuova pagina del WebSite.
            Il parametro URL è una stringa che rappresenta l'URL della WebPage; il parametro content, invece, è una stringa che rappresenta il testo della WebPage.
            Se l'url non ho ha lo stesso hostname dell'oggetto WebSite su cui si sta chiamando il metodo viene lanciata l'eccezione PageDoesNotBelongToThisWebSiteError.
        """
        x = url.split("/")
        length = len(x)

        if x[0] != self._homeDirectory.getName():
            raise PageDoesNotBelongToThisWebSiteError("This WebPage does not belong to the website ",self._homeDirectory.getName())
        e = self._homeDirectory
        
        for i in range(1,length-1): #Da 1 a n-1 www.unisa.it/diem/profs/vinci.html -> n = 4 -> da 1 a 2. 1)diem 2)profs
            e = self.__newDir(ndir=x[i],cdir=e)
        #Fuori dal for avrò l'Element che rappresenta la directory dove devo inserire la Page
        p = self.__newPage(npag = x[-1], cdir=e)
        p.setContent(content)
        if x[1] == "index.html":
            self._homePage = e
        return p
         
    @staticmethod
    def getSiteFromPage(page): #O(1)
        """Il metodo getSiteFromPage è statico. Data una webpage, restituisce l'oggetto website al quale la pagina appartiene."""
        
        if not isinstance(page,Element):
            raise NotAnElementError("page is not an Element")
        
        if(not page.isWebPage(page)):
            raise Exception("The parameter is not a WebPage")
        return page.getWebSite()

    
    def getWebSiteName(self):
        """
            Metodo di utility. Il metodo getWebSiteName restituisce il nome della home directory del WebSite, cioè l'hostname del WebSite.
        """
        return self._homeDirectory.getName()
    
from HashTable.chain_hash_map import ChainHashMap 
class Element:
    """Questa classe gestisce sia le directory che le webpage"""

    def __init__(self,webSite,dir,name,content=None):
        self._webSite = webSite 
        self._name = name
        self._dir = dir
        if(dir): #è una directory
            self._HTchildren = ChainHashMap() #Questa hashtable mi permette di riferirmi al contenuto della directory
        else: #è una webpage
            self._HTchildren = None
            self._content = content   
              
    def isDir(self):
        return self._dir
    def isWebPage(self):
        return not self._dir

    def getName(self):
        return self._name
    def getContent(self):
        return self._content
    def getWebSite(self):
        return self._webSite
    def setContent(self,content):
        self._content = content
    
    
    def addElement(self,webSite,dir,name,content=None):
        """Se l'elemento è già presente il metodo lo restituisce altrimenti prima lo aggiunge all'HashTable e poi lo restituisce"""
        e = self._HTchildren.get(name)
        if(e == None):
            e = Element(webSite,dir,name,content)
            self._HTchildren[name] = e
        return e 


    def searchInChildren(self,elemName,dir):
        """Se sono una cartella controllo che elem sia uno dei miei figli. Poi controllo se è una WebPage o una directory"""
        #print(elemName," ",dir)
        if(self.isDir()):
            e = self._HTchildren[elemName] #Lancia già un eccezione se l'elemento non esiste
            if(e.isDir() == dir): #Controllo che se gli ho chiesto una Webpage l'elemento e sia una Webpage
                                  #Se invece ho chiesto un directory l'elemento sia una directory
                return e
            else:
                raise Exception("The element exists but it is not a WebPage/Directory")
        else:
            raise Exception("The element is not a directory")

    

    #SOLO PER TEST PERSONALI. DA CANCELLARE!!
    def __str__(self):
        if(self.isDir()):
            return self.getName()
        else:
            return self.getName() + ": " + self.getContent()

    



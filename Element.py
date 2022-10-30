from HashTable import chain_hash_map
from HashTable.chain_hash_map import ChainHashMap 
class Element:
    """Questa classe gestisce sia le directory che le webpage"""

    def __init__(self,name,content=None):
        self._name = name
        if(content is None): #è una directory
            #TODO: Cambiare questo if. Controllando il name devo capire se è un directory o una page
            self._dir = True
            self._HTchildren = ChainHashMap() #Questa hashtable mi permette di riferirmi al contenuto della directory
        else: #è una webpage
            self._HTchildren = None    
            self._dir = False
            self._content = content   
              
    def isDir(self):
        return self._dir
    
    def isWebPage(self):
        return not self._dir
    
    #Non serve?
    #def hasDir(self,elem):
    #    if(self.isDir()):
    #        return self._HTChildren[elem]

    def getName(self):
        return self._name
    def getContent(self):
        return self._content
    
    def addDir(self,elemName):
        e = self._HTchildren.get(elemName)
        if(e == None):
            e = Element(elemName)
            self._HTchildren[elemName] = e
        return e 

    def addPage(self,elemName,content):
        e = self._HTchildren.get(elemName)
        if(e == None):
            e = Element(elemName,content)
            self._HTchildren[elemName] = e
        return e 


    def searchInChildren(self,elemName,dir):
        """Se sono una cartella controllo che elem sia uno dei miei figli. Poi controllo se è una WebPage o una directory"""
        if(self.isDir()):
            e = self._HTchildren[elemName] #Lancia già un eccezione se l'elemento non esiste
            if(e.isDir() == dir): #Controllo che se gli ho chiesto una Webpage l'elemento e sia una Webpage
                                  #Se invece ho chiesto un directory l'elemento sia una directory
                return e
            else:
                raise Exception("The element exists but it is not a WebPage/Directory")
        else:
            raise Exception("The element is not a directory")

    

    def __str__(self):
        if(self.isDir()):
            return self.getName()
        else:
            return self.getName() + ": " + self.getContent()

    



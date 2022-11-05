#from dataStructure.hash_table.chain_hash_map import ChainHashMap
from dataStructure.hash_table.probe_hash_map import ProbeHashMap 
from dataStructure.tree.red_black_tree import RedBlackTreeMap
#from dataStructure.sorted_table_map import SortedTableMap

class DirectoryNotFoundError(Exception):
    pass
class NonExistenceElementError(Exception):
    pass
class WrongElementError(Exception):
    pass
class NotADirectoryError(Exception):
    pass

class Element:
    """La classe Element gestisce sia le directory che le webpage"""
    __slots__ = '_webSite','_name','_dir','_content','_HTchildren','_orderedChildren'
    def __init__(self,webSite,dir,name,content=None):
        self._webSite = webSite 
        self._name = name
        self._dir = dir
        if(self._dir): #è una directory
            
            ### v1
            #self._HTchildren = ChainHashMap() #Questa hashtable mi permette di riferirmi al contenuto della directory
            ### v2
            self._HTchildren = ProbeHashMap()
            ### vBest
            #self._HTchildren = {}

            self._orderedChildren = RedBlackTreeMap() #Questa struttura dati permette di conservare l'ordine dei riferimenti dei figli delle directory
            #self._orderedChildren = SortedTableMap()

            self._content = None
        else: #è una webpage
            self._HTchildren = None
            self._orderedChildren = None
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
    def getOrderedChildren(self):
        return self._orderedChildren
    def setContent(self,content):
        self._content = content
    
    
    def addElement(self,webSite,dir,name,content=None):
        """Se l'elemento è già presente il metodo lo restituisce altrimenti prima lo aggiunge all'HashTable e poi lo restituisce"""
        e = self._HTchildren.get(name)
        if(e == None):
            e = Element(webSite,dir,name,content)
            self._HTchildren[name] = e
            self.updateOrder(e)
        return e 


    def searchInChildren(self,elemName,dir):
        """Se sono una cartella controllo che elem sia uno dei miei figli. Poi controllo se è una WebPage o una directory"""
        
        if(self.isDir()):
            try:
                e = self._HTchildren[elemName] #Lancia già un'eccezione se l'elemento non esiste
            except:
                raise NonExistenceElementError("The element does not exist")
            if(e.isDir() == dir): #Si verifica che l'elemento richiesto sia una Webpage, se si sta cercando una WebPage, oppure che sia una directory, se si sta cercando una directory.
                return e
            else:
                raise WrongElementError("The element exists but it is not a WebPage (if I requested a WebPage) or it is not a directory (if I requested a directory)")
        else:
            raise NotADirectoryError("The element is not a directory")

    def updateOrder(self,elem):
        """
            Aggiunde elem alla struttura dati ordinata della directory parent di elem. 
            elem può essere sia un WebPage che una Directory.
        """
        if(not self.isDir):
            raise NotADirectoryError("I am not a directory")
        self._orderedChildren[elem.getName()] = elem
    

    def getWebSiteStructure(self,l) -> str:
        if(self == None):
            return ""
        if(self.isDir() and l == ""):
            s = self.getName()
            for i in self.getOrderedChildren():
                s+= self._HTchildren[i].getWebSiteStructure("---")
            return s    
        if(self.isDir() and l != ""):
            s = "\n" + l + " "+self.getName()
            l += "---"
            for i in self.getOrderedChildren():
                s+= self._HTchildren[i].getWebSiteStructure(l)
            return s
        if(self.isWebPage()):
            return "\n" + l + " "+self.getName()


    def __str__(self):
        return self.getName()
        


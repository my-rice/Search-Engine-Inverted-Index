#from dataStructure.tree.red_black_tree import RedBlackTreeMap
#from dataStructure.hash_table.chain_hash_map import ChainHashMap
from dataStructure.hash_table.probe_hash_map import ProbeHashMap

class KeywordNotInInvertedIndexError(Exception):
    pass

class OLItem:
    """"""
    __slots__ = '_page','_num'
    def __init__(self,page,num):
        self._page=page
        self._num=num
    def __str__(self):
        return self._page.getName() + " " + str(self._num)
    def getPage(self):
        return self._page
    def getNum(self):
        return self._num


class OccurenceList:
    """ 
        Questa versione di OccurenceList è basata su una mappa ed è implementata tramite un albero.
        La chiave è il riferimento (convertito in stringa) alla WebPage mentre il valore è il numero di occorrenze della keyword all'interno 
        della WebPage (il cui riferimento è utilizzato come chiave)
    """

    __slots__ = '_data'
    
    def __init__(self):
        ### v1
        #self._data = RedBlackTreeMap()
        ### v2
        self._data = ProbeHashMap()
        ### vBest
        #self._data = {}
    def add(self,page):
        """
            Provo ad aggiornare il numero di occorrenze se non esiste
        """

        ###DEBUG
        #print("[OccurenceList]: type di page:",type(page))
        #print("[OccurenceList]: id page:",id(page))
        
        key = str(id(page))
        try:
            ###DEBUG
            #print("[OccurenceList] Sono:", id(self)," provo il try di",page.getName(),"con id:",id(page))
            
            x = self._data[key]

            ###DEBUG
            #print("[OccurenceList]:",page.getName(),"sono nel try con",str(x))

            self._data[key]._num = x._num+1
        except:
            ###DEBUG
            #print("[OccurenceList]: try fallito.",page.getName()," è in except")

            item = OLItem(page,1)
            self._data[key] = item
        
        """
        if str(id(page)) in self._data.keys():
            #print("[OccurenceList] page:",page," è entrato nell'if")
            self._data[str(id(page))] += 1
            #print("sono nell'if -> ",self._data[page])
        else:
            self._data[str(id(page))] = 1
            #print("sono nell'else -> ",self._data[page])
        """
    def getData(self):
        return self._data
        
    
    def __str__(self):
        """FUNZIONE USATA PER IL ###DEBUG"""
        s = "keys: "
        for i in self._data.keys():
            s += str(i) + " "
        s += "\nValue: "
        for i in self._data.values():
            s += i
        return s

        


class InvertedIndex:
    """ 
        La classe InvertedIndex implementa un dizionario che memorizza coppie di chiave-valore (w,L). 
        Le chiavi del dizionario sono chiamate index terms. Sono un set di entry di un vocabulary e nomi propri lunghi il più possibile.
        I valori del dizionario sono chiamati occurence lists. Essi contengono quante pagine Web possono contenere.
        In realtà le vere occurence list sono oggetti separati. In questa classe verranno memeorizzati SOLO i riferimenti a questi oggetti occurence list.
        Nota: L'occurrence list memorizza anche il numero di occorrenze della parola nella pagina.
    """

    __slots__ = '_InvertedIndex'

    def __init__(self):
        """Instanzia un nuovo oggetto della classe InvertedIndex"""
        ### v1
        #self._InvertedIndex = ChainHashMap()
        ### v2
        self._InvertedIndex = ProbeHashMap()
        ### vBest
        #self._InvertedIndex = {}

    def addWord(self, keyword):
        """Aggiunge la stringa keyword nell'InvertedIndex"""
        self._InvertedIndex[keyword] = OccurenceList()

    def addPage(self, page):
        """ 
            Processa la webpage passata per parametro. Per ogni parola della webpage, 
            Se la parola non è presente essa viene inserita nell'InvertedIndex e la pagina viene inserita nell'OccurrenceList.
            Inoltre, viene aggiornato numero di occorrenze della parola nella pagina nell'occurrence list.
        """
        words = page.getContent().split() #Complessità è O(n = lunghezza testo pagina) ????? Forse è ottimizzata?
        for w in words:

            ### v1
            #if w not in self._InvertedIndex.keys():
            #    self.addWord(w)
            #self._InvertedIndex[w].add(page)

            #Si aggiunge la pagina della parola w alle Occurence List. Se w non è mai stati inserito in _InvertedIndex, deve essere inserito.
            try:
                self._InvertedIndex[w].add(page)
            except:
                self.addWord(w)
                self._InvertedIndex[w].add(page)

            ###DEBUG
            #print("[InvertedIndex: addPage] word:",w," page:",page.getName())
        

    def getList(self, keyword):
        """
            Il metodo getList prende in input una stringa, la keyword, e restituisce la corrispondente occurence list. 
            Viene lanciata l'eccezione KeywordNotInInvertedIndexError se non esiste una occurence list associata alla stringa keyword.
        """
        try:
            return self._InvertedIndex[keyword]
        except KeyError:
            raise KeywordNotInInvertedIndexError("The keyword "+keyword+" does not exist in the InvertedIndex")
        

    
from dataStructure.hash_table.probe_hash_map import ProbeHashMap

class KeywordNotInInvertedIndexError(Exception):
    pass

class OLItem:
    """La classe OLItem rappresenta ciò che viene memorizzato nell'Occurence List."""
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
        La classe OccurenceList è basata su una mappa ed è implementata tramite un HashTable.
        La chiave è il riferimento (convertito in stringa) alla WebPage mentre il valore è il numero di occorrenze della keyword all'interno 
        della WebPage (il cui riferimento è utilizzato come chiave)
    """
    __slots__ = '_data'
    
    def __init__(self):
        self._data = ProbeHashMap()
        ### vBest
        #self._data = {}
    def add(self,page):
        """
            Il metodo add aggiunge la WebPage nell'Occurence List ed aggiorna il numero di occorrenze.
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
        """Restituisce la stuttura dati che memorizza i dati dell'Occurence List"""
        return self._data
    
    def __str__(self):
        """Metodo di utility. Restituisce la struttura dati dell'Occurence List"""
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
        """È il costruttore della classe InvertedIndex. Instanzia un nuovo oggetto InvertedIndex"""

        self._InvertedIndex = ProbeHashMap(cap=127937) #Mi aspetto che ci siano molte parole
        ### vBest
        #self._InvertedIndex = {}

    def addWord(self, keyword):
        """Il metodo addWord aggiunge la stringa keyword all'interno della struttura dati InvertedIndex"""
        self._InvertedIndex[keyword] = OccurenceList()

    def addPage(self, page):
        """ 
            Il metodo addPage prende come parametro di input un oggetto della classe Element che sia una WebPage.
            Per ogni parola del contenuto della WebPage, se la parola non è presente nell'InvertedIndex essa viene aggiunta e la WebPage viene inserita nell'OccurrenceList.
            Il metodo addPage si occupa anche di aggiornare il numero di occorrenze della parola trovate nella pagina.
        """

        words = page.getContent().split() #Complessità è O(n = lunghezza testo pagina)
        for w in words:

            ### v1
            #if w not in self._InvertedIndex.keys():
            #    self.addWord(w)
            #self._InvertedIndex[w].add(page)

            #Si aggiunge la pagina che contiene la parola w all'Occurence List.
            #Se w è una keyword che non è mai stata inserita prima in _InvertedIndex, deve essere prima inserita e poi va aggiunta la pagina.
            try:
                self._InvertedIndex[w].add(page)
            except:
                self.addWord(w)
                self._InvertedIndex[w].add(page)

            ###DEBUG
            #print("[InvertedIndex: addPage] word:",w," page:",page.getName())
        

    def getList(self, keyword):
        """
            Il metodo getList prende in input una stringa, keyword, e restituisce la corrispondente Occurence List. 
            Il metodo getList lancia l'eccezione KeywordNotInInvertedIndexError se non esiste una Occurence List associata alla keyword.
        """
        try:
            return self._InvertedIndex[keyword]
        except KeyError:
            raise KeywordNotInInvertedIndexError("The keyword "+keyword+" does not exist in the InvertedIndex")
        

    
from dataStructure.tree.red_black_tree import RedBlackTreeMap
from dataStructure.hash_table.chain_hash_map import ChainHashMap
class OLItem:
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
        La chiave è il la stringa del riferimento alla WebPage mentre il valore è il numero di occorrenze della keyword all'interno 
        della WebPage (il cui riferimento è utilizzato come chiave)
    """
    
    def __init__(self):
        self._data = RedBlackTreeMap()
    def add(self,page):
        """
            Provo ad aggiornare il numero di occorrenze se non esiste
        """

        ###DEBUG
        #print("[OccurenceList]: type di page:",type(page))
        #print("[OccurenceList]: id page:",id(page))
        
        try:
            ###DEBUG
            #print("[OccurenceList] Sono:", id(self)," provo il try di",page.getName(),"con id:",id(page))

            x = self._data[str(id(page))]

            ###DEBUG
            #print("[OccurenceList]:",page.getName(),"sono nel try con",str(x))

            self._data[str(id(page))]._num = x._num+1
        except:
            ###DEBUG
            #print("[OccurenceList]: try fallito.",page.getName()," è in except")

            item = OLItem(page,1)
            self._data[str(id(page))] = item
        
        """
        if str(id(page)) in self._data.keys():
            #print("[OccurenceList] page:",page," è entrato nell'if")
            self._data[str(id(page))] += 1
            #print("sono nell'if -> ",self._data[page])
        else:
            self._data[str(id(page))] = 1
            #print("sono nell'else -> ",self._data[page])
        """
        
    
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
    """ Questa classe implementa un dizionario che memorizza coppie di chiave-valore (w,L). 
        Le chiavi del dizionario sono chiamate index terms. Sono un set di entry di un vocabulary e nomi propri lunghi il più possibile.
        I valori del dizionario sono chiamati occurence lists. Essi contengono quante pagine Web possono contenere.
        In realtà le vere occurence list sono oggetti separati. In questa classe verranno memeorizzati SOLO i riferimenti a questi oggetti occurence list.
        Nota: L'occurrence list memorizza anche il numero di occorrenze della parola nella pagina.
    """
    def __init__(self):
        """Crea un nuovo oggetto InvertedIndex"""
        self._InvertedIndex = ChainHashMap()

    def addWord(self, keyword):
        """Aggiunge la stringa keyword nell'InvertedIndex"""
        self._InvertedIndex[keyword] = OccurenceList()

    def addPage(self, page):
        """ 
            Processa la webpage passata per parametro. Per ogni parola della webpage, 
            Se la parola non è presente essa viene inserita nell'InvertedIndex e la pagina viene inserita nell'OccurrenceList.
            Inoltre, viene aggiornato numero di occorrenze della parola nella pagina nell'occurrence list.
        """
        words = page.getContent().split(" ") #Complessità è O(n = lunghezza testo pagina) ????? Forse è ottimizzata?
        for w in words:
            if w not in self._InvertedIndex.keys():
                self.addWord(w)
            
            ###DEBUG
            #print("[InvertedIndex: addPage] word:",w," page:",page.getName())
            
            self._InvertedIndex[w].add(page)
        

    def getList(self, keyword):
        """Prende in input la stringa keyword e restituisce la corrispondente occurence list. 
           Lancia un'eccezione se non c'è una occurence list associata alla stringa keyword
        """
        return self._InvertedIndex[keyword]

    
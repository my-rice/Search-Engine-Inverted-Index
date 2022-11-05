import os
from invertedIndex import InvertedIndex, OccurenceList
from dataStructure.hash_table.probe_hash_map import ProbeHashMap
from webSite import WebSite

from dataStructure.heap.heap_priority_queue import HeapPriorityQueue, Empty

class NotEnoughOccurencesError(Exception):
    pass

class SearchEngine:
    """"""

    __slots__ = '_websites','_invIndex'
    def __init__(self, namedir):
        """ 
            Inizializza il motore di ricerca. Prende in input un istanza della classe Element che sia una directory (namedir) nel quale ci sono molti file ognuno dei quali rappresenta una differente webpage. 
            Ogni file contiene: nella prima riga l'URL (incluso l'hostname); in tutte le altre righe il contenuto della webpage. 
            Questa funzione popola il database del motore di ricerca, inizializzando e inserendo i valori nelle strutture dati necessarie.
        """
        self._websites = ProbeHashMap() # _websites memorizza tutti i website creati affinchè NON vengano istanziati più di una volta  
        self._invIndex = InvertedIndex()
        for file in os.scandir(namedir):
            
            if not file.is_file() or file.name.startswith('.'):
                continue
            fp = open(file,'r')
            url = fp.readline().rstrip()
            content = fp.read()
            fp.close()
            
            websiteHost = url.partition("/")[0]
            
            try:
                ws = self._websites[websiteHost]
            except KeyError:
                ws = WebSite(websiteHost)
                self._websites[websiteHost] = ws
            except:
                raise Exception()
            
            page = ws.insertPage(url,content)
            
            #if websiteHost not in self._websites.keys():
            #    self._websites[websiteHost] = WebSite(websiteHost)
            #page = self._websites[websiteHost].insertPage(url,content)
            
            self._invIndex.addPage(page)


            ###DEBUG
            #for k,v in self._invIndex._InvertedIndex["triturando"].getData().items():
            #    print(k," ",v)
            
    def search(self, keyword, k):
        """Cerca le k (un intero) pagine web con il massimo numero di occorrenze della keyword cercata. 
           Restituisce una stringa s costruita come segue: 
           per ognuna di queste k pagine, sono ordinate in ordine decrescente di occorrenze, 
           la stringa del website del sito che hosta la pagina è aggiunta a s, a meno che il website non sia stato già inserito.  
        """
        matchedWords = self._invIndex.getList(keyword) #Restituisce un HT

        ### v1
        #array = []
        ### v2 heap
        array = HeapPriorityQueue()

        ###DEBUG:
        #print("Keyword: ", keyword, "k: ",k)

        for item in matchedWords._data.items(): #Per ogni coppia chiave-valore del RBTree
            ### v1
            #array.append((item[1].getNum(),item[1].getPage().getWebSite()))

            ### v2
            array.add(-item[1].getNum(),item[1].getPage().getWebSite())

            ###DEBUG:
            #print("nodo RBTree. Chiave.",item[0],"Valore. NomeWebPage:",item[1].getPage().getName(),"numero occorrenze:",item[1].getNum(),"nomeWebSite:",item[1].getPage().getWebSite().getWebSiteName())
        
        ### v1  #TODO: Provare un ordinamento migliore di quello dell'array
        # def sort_key(l):
        #    return l[0]
        # array.sort(key=sort_key,reverse=True)

        ###DEBUG:
        #print("ARRAY:")
        #for e in array:
        #    print(e[0]," ",e[1].getWebSiteName())

        websites = []
        s = ""
        

        ### v1 con lista semplice.
        # for i in range(0,k):
        #     try:
        #         wb = array[i][1]
        #     except IndexError:
        #         raise NotEnoughOccurencesError("There are not",k,"WebPages containing the keyword:",keyword)
        #     if i == 0:
        #         websites.append(wb)
        #         s += wb.getSiteString()
        #     elif wb not in websites:
        #         websites.append(wb)
        #         s += "\n" + wb.getSiteString()


        ### v2 con heap
        for i in range(0,k):
            try:
                wb = array.remove_min()[1]
            except Empty:
                raise NotEnoughOccurencesError("There are not",k,"WebPages containing the keyword:",keyword)
            if i == 0:
                websites.append(wb)
                s += wb.getSiteString()
            elif wb not in websites:
                websites.append(wb)
                s += "\n" + wb.getSiteString()
                
        
        ###DEBUG
        #print("out")
        #print(s)

        return s
        





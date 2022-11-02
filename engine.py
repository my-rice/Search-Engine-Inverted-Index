import os
from invertedIndex import InvertedIndex, OccurenceList
from webSite import WebSite


class SearchEngine:
    def __init__(self, namedir):
        """ 
            Inizializza il motore di ricerca. Prende in input una directory (namedir) 
            nel quale ci sono molti file ognuno dei quali rappresenta una differente webpage. 
            Ogni file contiene: nella prima riga l'URL (incluso l'hostname); 
            in tutte le altre righe il contenuto della webpage. 
            Questa funzione popola il database del motore di ricerca, 
            inizializzando e inserendo i valori nelle strutture dati necessarie.
        """
        """Nel nostro caso prende in input la cartella "dataset" e popola tutte le necessarie strutture dati."""
        
        """ ES: prende www.uniba.it/1zz.html crea il website www.uniba.it ed aggiunge la pagina 1zz.html con il suo contenuto
            
        """ 
        self._websites = {}
        self._invIndex = InvertedIndex()
        for file in os.scandir(namedir):
            
            if not file.is_file() or file.name.startswith('.'):
                continue
            fp = open(file,'r')
            url = fp.readline().rstrip()
            content = fp.read()
            fp.close()
            
            wb = url.partition("/")[0]
            if wb not in self._websites.keys():
                self._websites[wb] = WebSite(wb)
            page = self._websites[wb].insertPage(url,content)
            
            self._invIndex.addPage(page)
            
    def search(self, keyword, k):
        """Cerca le k (un intero) pagine web con il massimo numero di occorrenze della keyword cercata. 
           Restituisce una stringa s costruita come segue: 
           per ognuna di queste k pagine, sono ordinate in ordine decrescente di occorrenze, 
           la stringa del website del sito che hosta la pagina è aggiunta a s, a meno che il website non sia stato già inserito.  
        """
        matchedWords = self._invIndex.getList(keyword) #Restituisce un RBTree

        array = []
        
        ###DEBUG:
        #print("Keyword: ", keyword, "k: ",k)

        for item in matchedWords._data.items(): #Per ogni coppia chiave-valore del RBTree
            
            array.append((item[1].getNum(),item[1].getPage().getWebSite()))

            ###DEBUG:
            #print("nodo RBTree. Chiave.",item[0],"Valore. NomeWebPage:",item[1].getPage().getName(),"numero occorrenze:",item[1].getNum(),"nomeWebSite:",item[1].getPage().getWebSite().getWebSiteName())
        
        def sort_key(l):
            return l[0]
        array.sort(key=sort_key,reverse=True)

        ###DEBUG:
        #print("ARRAY:")
        #for e in array:
        #    print(e[0]," ",e[1].getWebSiteName())

        websites = []
        s = ""
        for i in range(0,k):
            wb = array[i][1]
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
        





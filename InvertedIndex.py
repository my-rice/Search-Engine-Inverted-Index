class InvertedIndex:
    """ Questa classe implementa un dizionario che memorizza coppie di chiave-valore (w,L). 
        Le chiavi del dizionario sono chiamate index terms. Sono un set di entry di un vocabulary e nomi propri lunghi il più possibile.
        I valori del dizionario sono chiamati occurence lists. Essi contengono quante pagine Web possono contenere.
        In realtà le vere occurence list sono oggetti separati. In questa classe verranno memeorizzati SOLO i riferimenti a questi oggetti occurence list.
        Nota: L'occurrence list memorizza anche il numero di occorrenze della parola nella pagina.
    """
    def __init__(self):
        """Crea un nuovo oggetto InvertedIndex"""
        pass

    def addWord(self, keyword):
        """Aggiunge la stringa keyworld nell'indice"""
        pass

    def addPage(self, page):
        """Processa la webpage passata per parametro. Per ogni parola della webpage, essa viene inserita nell'inverted index se non è presente e la pagina viene inserita nell'occurrence list.
           Inoltre, viene aggiornato numero di occorrenze della parola nella pagina nell'occurrence list.
        """
        pass

    def getList(self, keyword):
        """Prende in input la stringa keyword e restituisce la corrispondente occurence list. 
           Lancia un'eccezione se non c'è una occurence list associata alla stringa keyword
        """
        pass
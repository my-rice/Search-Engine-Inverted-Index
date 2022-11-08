from ..hash_table.probe_hash_map import ProbeHashMap


class Node:
    __slots__ = 'pointedWord','children','value','startIndex','endIndex'
    def __init__(self,word):
        self.pointedWord = word
        self.children = ProbeHashMap(59) #Le lettere dell'alfabeto sono 26. Il load factor è 0.5. Posso partire con un bucket array di questa dimensione. 
        self.startIndex = None
        self.endIndex = None
        self.value = None


class CompressedTrie:
    __slots__ = '_root'
    def __init__(self):
        #Siccome le tuple sono immutabili creo la struttura dati Node 
        self._root = Node(' ')

    def __getitem__(self,word) -> str:
        word +='\0'
        n = self._root
        for letter in word:
            p = ""
            try: ####!!!!!!
                n = n
            except:
                continue
        return n.getValue()
        

    def __setitem__(self,word,value):
        word += '\0'
        n = self._root
        for letter in word:
            try:
                n = n.children[letter]
            except KeyError:
                x = Node(letter)
                n.children[letter] = x
                n = x
        n.setValue(value)

        
        
         

        


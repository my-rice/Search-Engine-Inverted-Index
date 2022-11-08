from ..hash_table.probe_hash_map import ProbeHashMap


class Node:
    __slots__ = 'char','children','value'
    def __init__(self,char):
        self.char = char
        self.children = ProbeHashMap(59) #Le lettere dell'alfabeto sono 26. Il load factor è 0.5. Posso partire con un bucket array di questa dimensione. 
        self.value = None


class StandardTrie:
    __slots__ = '_root'
    def __init__(self):
        #Siccome le tuple sono immutabili creo la struttura dati Node 
        self._root = Node(' ')

    def __getitem__(self,word) -> str:
        word +='\0'
        n = self._root
        for letter in word:
            n = n.children[letter]
        #return n.getValue()
        return n.value
        

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
        n.value = value
        #n.setValue(value)
    
    def myGetSetNone(self,word):
        word +='\0'
        n = self._root
        for letter in word:
            res = n.children.myGetSetNone(letter)
            if not res[0]: #if found -> valore = item
                o = Node(letter)
                n.children.mySet(res[1],o) 
                n = o
            else:
                n = res[1]
        return res

    def mySet(self,n,value):
        """Da completare"""
        
         

        


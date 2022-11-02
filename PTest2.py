import os
from invertedIndex import InvertedIndex
from webSite import WebSite

invIndex = InvertedIndex()
wb = WebSite("www.unisa.it")

fp = open("./TestDataSet/unisa1.txt",'r')
url = fp.readline().rstrip()
content = fp.read()
fp.close()
page = wb.insertPage(url,content)           
invIndex.addPage(page)

fp = open("./TestDataSet/unisa2.txt",'r')
url = fp.readline().rstrip()
content = fp.read()
fp.close()
page = wb.insertPage(url,content)           
invIndex.addPage(page)


for i in invIndex._InvertedIndex: #Per ogni chiave dell'InvertedIndex
    print("key di InvertedIndex:",i)
    #print(invIndex._InvertedIndex[i])
    
    for k in invIndex._InvertedIndex[i]._data.items(): #Prendo ogni chiave RedBlackTree
        #print(type(k)) 
        #print(invIndex._InvertedIndex[i]._data)
        for j in k:
            print("\t",j)
        #print("\t TKey: ",k[0]," Tvalue: ",k[1])
        #print("\t TKey: ",k," Tvalue: ",invIndex._InvertedIndex[i]._data[k])
    
from element import Element
from webSite import WebSite


print("Testing Element methods")
ws = WebSite("www.unisa.it")
ws.insertPage(url="www.unisa.it/index.html",content="Questa è l'home page di www.unisa.it")
page = ws.getHomePage()
#print(page)
#print(ws.getSiteFromPage(page))
ws.insertPage(url="www.unisa.it/1zz.html",content="Questa è la page del diem")
ws.insertPage(url="www.unisa.it/aaa.html",content="Questa è la page del diem")
ws.insertPage(url="www.unisa.it/diem/daa.html",content="Questa è la page del diem")
ws.insertPage(url="www.unisa.it/diem/profs/auletta.html",content="Questa è la page del diem")
ws.insertPage(url="www.unisa.it/diem/profs/ferraioli.html",content="Questa è la page del diem")
ws.insertPage(url="www.unisa.it/diem/profs/vinci.html",content="Questa è la page del diem")
ws.insertPage(url="www.unisa.it/AAAA.html",content="Questa è la page del diem")

print("\n\nSTAMPA")
print(ws.getSiteString())
print("FINE STAMPA")
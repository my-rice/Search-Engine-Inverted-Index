from engine import SearchEngine
from time import time

DIR="dataset"
OUT_1="www.unisa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unisal.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unina.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unipa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html"

OUT_2="www.unica.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.uniba.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unito.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unimi.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unisa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unisal.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unina.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unipa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html"

start = time()
se=SearchEngine(DIR)

out1=se.search("algorithm", 5)
out2=se.search("design", 10)
end=time()-start
if out1 != OUT_1:
    print("FAIL")
elif out2 != OUT_2:
    print("FAIL")
else:
    print("True")
    print(end) 

###DEBUG
# print(se.search("preservo",3))
# print(se.search("mela",3))
# s = "www.unica.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html"
# print("\n****FINE\n****")
# print("out_1 risultato: ")
# print(out1)
# print("OUT_1 risultato corretto: ")
# print(OUT_1)
# print("out_2 risultato: ")
# print(out2)
# print("OUT_2 risultato corretto: ")
# print(OUT_2)
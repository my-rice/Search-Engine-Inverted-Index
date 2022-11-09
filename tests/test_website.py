import logging
import unittest
from webSite import WebSite,PageNotFoundError
from element import Element

class TestWebSite(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestWebSite, self).__init__(*args, **kwargs)
        self._log = logging.getLogger("TestWebSite")
        
    def test_root_is_dir(self):
        w = WebSite("www.unisa.it")
        self.assertTrue(w._WebSite__isDir(w._homeDirectory))
        self.assertFalse(w._WebSite__isDir(Element(w,False,"index.html","blabla")))
        self.assertRaises(Exception,lambda: w._WebSite__isDir("www.unipa.it"))
    def test_root_is_page(self):
        w = WebSite("www.unisa.it")
        self.assertTrue(w._WebSite__isPage(Element(w,False,"index.html","blabla")))
        self.assertFalse(w._WebSite__isPage(Element(w,True,"profs")))
        self.assertRaises(Exception,lambda: w._WebSite__isPage("www.unipa.it"))
    
    def test_root_has_page(self):
        w = WebSite("www.unisa.it")
        w.insertPage("www.unisa.it/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/3_anno/bbb.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/2_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/2_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/1_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/1_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/meccanica/3_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/chimica/3_anno/aaa.html","")
        page = w._homeDirectory.searchInChildren(elemName="aaa.html",dir=False)
        
        self.assertEquals(page,w._WebSite__hasPage("aaa.html",w._homeDirectory))
        self.assertRaises(Exception,lambda: w._WebSite__hasPage("NonExistence.html",w._homeDirectory))
        self.assertRaises(Exception,lambda: w._WebSite__hasPage("aaa.html","String"))
        self.assertRaises(Exception,lambda: w._WebSite__hasPage(npag=w,cdir=w._homeDirectory))
        
    def test_root_has_dir(self):
        w = WebSite("www.unisa.it")
        w.insertPage("www.unisa.it/aaa.html","")
        w.insertPage("www.unisa.it/informatica/bbb.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/2_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/2_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/1_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/informatica/1_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/meccanica/3_anno/aaa.html","")
        w.insertPage("www.unisa.it/ingegneria/chimica/3_anno/aaa.html","")
        dir = w._homeDirectory.searchInChildren(elemName="informatica",dir=True)
        
        self.assertEquals(dir,w._WebSite__hasDir("informatica",w._homeDirectory))
        self.assertRaises(Exception,lambda: w._WebSite__hasDir("NonExistence",w._homeDirectory))
        self.assertRaises(Exception,lambda: w._WebSite__hasDir("informatica","String"))
        self.assertRaises(Exception,lambda: w._WebSite__hasDir(ndir=w,cdir=w._homeDirectory))

    def test_root_newDir(self):
        w = WebSite("www.unisa.it")
        w.insertPage("www.unisa.it/aaa.html","")
        w.insertPage("www.unisa.it/informatica/bbb.html","")
        dir = w._homeDirectory.searchInChildren(elemName="informatica",dir=True)

        self.assertEquals(dir,w._WebSite__newDir("informatica",w._homeDirectory))
        new = w._WebSite__newDir("chimica",dir)
        x = w._homeDirectory.searchInChildren(elemName="informatica",dir=True)
        dirChimica = x.searchInChildren(elemName="chimica",dir=True)
        self.assertEquals(dirChimica,new)
        self.assertRaises(Exception,lambda: w._WebSite__newDir(ndir="informatica",cdir="String"))
        self.assertRaises(Exception,lambda: w._WebSite__newDir(ndir=w,cdir=w._homeDirectory))

    def test_root_newPage(self):
        w = WebSite("www.unisa.it")
        w.insertPage("www.unisa.it/aaa.html","")
        w.insertPage("www.unisa.it/informatica/bbb.html","")
        dir = w._homeDirectory.searchInChildren(elemName="informatica",dir=True)
        page = w._homeDirectory.searchInChildren(elemName="aaa.html",dir=False)
        
        self.assertEquals(page,w._WebSite__newPage("aaa.html",w._homeDirectory))
        new = w._WebSite__newPage("chimica.html",dir)
        x = w._homeDirectory.searchInChildren(elemName="informatica",dir=True)
        pageChimica = x.searchInChildren(elemName="chimica.html",dir=False)
        self.assertEquals(pageChimica,new)
        self.assertRaises(Exception,lambda: w._WebSite__newPage(npage="informatica.html",cdir="String"))
        self.assertRaises(Exception,lambda: w._WebSite__newPage(npage=w,cdir=w._homeDirectory))


    def test_get_site_string(self):
        w = WebSite("www.unisa.it")
        print("\n")
        page1 = w._WebSite__newPage("AAAA.html",w._homeDirectory)
        page2 = w._WebSite__newPage("aaa.html",w._homeDirectory)
        page3 = w._WebSite__newPage("1zz.html",w._homeDirectory)
        page4 = w._WebSite__newPage("index.html",w._homeDirectory)
        dir1 = w._WebSite__newDir("diem",w._homeDirectory)
        dir2 = w._WebSite__newDir("profs",dir1)
        page5 = w._WebSite__newPage("daa.html",dir1)
        page6 = w._WebSite__newPage("vinci.html",dir2)
        page7 = w._WebSite__newPage("ferraioli.html",dir2)
        page7 = w._WebSite__newPage("auletta.html",dir2)
        expectedResult = """www.unisa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html"""
        #print(expectedResult)
        #print(w.getSiteString())
        self.assertEqual(w.getSiteString(),expectedResult)
    
    def test_insert_page(self):
        w = WebSite("www.unisa.it")
        self.assertRaises(Exception,lambda: w.insertPage("www.unibo.it/test/index.html","ciao"))
        self.assertRaises(Exception,lambda: w.insertPage("www.unica.it/test/index.html","ciao"))
        w.insertPage("www.unisa.it/test/index.html","ciao")
        w.insertPage("www.unisa.it/1zz.html","ciao")
        w.insertPage("www.unisa.it/diem/profs/auletta.html","ciao")
        w.insertPage("www.unisa.it/diem/profs/vinci.html","ciao")
        w.insertPage("www.unisa.it/index.html","ciao")
        w.insertPage("www.unisa.it/diem/profs/ferraioli.html","ciao")
        w.insertPage("www.unisa.it/diem/daa.html","ciao")
        w.insertPage("www.unisa.it/AAAA.html","ciao")
        w.insertPage("www.unisa.it/aaa.html","ciao")
        #print(w.getSiteString())
        expectedResult = """www.unisa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- test\n------ index.html\n--- AAAA.html"""
        self.assertEqual(w.getSiteString(),expectedResult)
        
    def test_get_homepage(self):
        w = WebSite("www.unisa.it")
        self.assertRaises(Exception, lambda: w.getHomePage())
        print(w.insertPage("www.unisa.it/index.html","qwerty").getName())
        print(w.getHomePage().getName())
        self.assertEqual(w.getHomePage().getContent(), "qwerty")

    def test_getSiteFromPage(self):
        w1 = WebSite("www.unisa.it")
        w2 = WebSite("www.unipa.it")
        
        e1 = Element(w1,False,"aaa.html","blavllba")
        e2 = Element(w2,False,"aaa.html","blavllba")
        self.assertEqual(w1, WebSite.getSiteFromPage(e1))
        self.assertEqual(w2, WebSite.getSiteFromPage(e2))
        self.assertRaises(Exception,lambda: WebSite.getSiteFromPage(Element(w1,True,"diem")))

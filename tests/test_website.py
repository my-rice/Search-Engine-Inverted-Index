import logging
import unittest
from webSite import WebSite

class TestWebSite(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestWebSite, self).__init__(*args, **kwargs)
        self._log = logging.getLogger("TestWebSite")
        
    def test_root_is_dir(self):
        w = WebSite("www.unisa.it")
        self.assertTrue(w._WebSite__isDir(w._homeDirectory))
        self.assertFalse(w._WebSite__isPage(w._homeDirectory))
    
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
import unittest
from exceptions import NotAPageError, NotADirectoryError

from website import Element

class TestElement(unittest.TestCase):
        
    def test_constructor(self):
        root = Element("www.unisa.it", True, None, None)
        dir1 = Element("dir1", True, None, root)
        dir2 = Element("dir2", True, None, root)
        dir3 = Element("dir3", True, None, dir2)
        page1 = Element("index.html", False, None, dir2)
        page2 = Element("auletta.html", False, None, dir3)
        
        self.assertRaises(TypeError, lambda: Element("dir4", True, None, object()))
        self.assertRaises(TypeError, lambda: Element("dir4", True, object(), None))
        
        self.assertRaises(TypeError, lambda: Element("dir4", True, None, "ciao"))
        self.assertRaises(TypeError, lambda: Element("dir4", True, None, page1))
        self.assertRaises(TypeError, lambda: Element("page3", False, None, page1))
        
    def test_content_getter_setter(self):
        root = Element("www.unisa.it", True, None, None)
        dir1 = Element("dir1", True, None, root)
        dir2 = Element("dir2", True, None, root)
        dir3 = Element("dir3", True, None, dir2)
        page1 = Element("index.html", False, None, dir2)
        page2 = Element("auletta.html", False, None, dir3)
        
        self.assertRaises(NotAPageError, lambda: root.setContent("ciao"))
        self.assertRaises(NotAPageError, lambda: dir2.setContent("ciao"))
        self.assertRaises(NotAPageError, lambda: dir3.getContent())
        
        page1.setContent("42")
        page2.setContent("24")
        
        self.assertEqual(page1.getContent(),"42")
        self.assertEqual(page2.getContent(),"24")
    
    def test_url_building(self):
        root = Element("www.unisa.it", True, None, None)
        dir1 = Element("dir1", True, None, root)
        dir2 = Element("dir2", True, None, root)
        dir3 = Element("dir3", True, None, dir2)
        
        page1 = Element("index.html", False, None, dir2)
        page2 = Element("auletta.html", False, None, dir3)

        self.assertEqual(root.getUrl(),"www.unisa.it")
        self.assertEqual(dir1.getUrl(),"www.unisa.it/dir1")
        self.assertEqual(dir2.getUrl(),"www.unisa.it/dir2")
        self.assertEqual(dir3.getUrl(),"www.unisa.it/dir2/dir3")
        self.assertEqual(page1.getUrl(),"www.unisa.it/dir2/index.html")
        self.assertEqual(page2.getUrl(),"www.unisa.it/dir2/dir3/auletta.html")
    
    def test_child_methods(self):
        root = Element("www.unisa.it", True, None, None)
        dir1 = Element("dir1", True, None, root)
        dir2 = Element("dir2", True, None, root)
        dir3 = Element("dir3", True, None, dir2)
        page1 = Element("index.html", False, None, dir3)
        page2 = Element("auletta.html", False, None, dir3)
        
        root.addChild(dir1)
        root.addChild(dir2)
        dir2.addChild(dir3)
        dir3.addChild(page1)
        dir3.addChild(page2)
        self.assertRaises(NotADirectoryError, lambda: page2.addChild(page1))
        self.assertRaises(TypeError, lambda: root.addChild(object()))
        
        self.assertFalse(dir1.hasChild("dir2"))
        self.assertTrue(dir2.hasChild("dir3"))
        self.assertTrue(dir3.hasChild("auletta.html"))
        self.assertFalse(dir3.hasChild("dir42"))
        self.assertRaises(NotADirectoryError, lambda: page1.hasChild("wewe"))
        
        self.assertRaises(NotADirectoryError, lambda: page1.getChild("wewe"))
        self.assertEqual(dir2.getChild("dir3"),dir3)
        self.assertEqual(dir3.getChild("auletta.html"),page2)
        self.assertRaises(KeyError, lambda: dir3.getChild("aulettaaaa.html"))
        self.assertRaises(StopIteration, lambda: next(page1.children()))
        iter = dir3.children()
        self.assertEqual(next(iter),page2)
        self.assertEqual(next(iter),page1)
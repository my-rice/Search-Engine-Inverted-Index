import unittest
from timeit import timeit,repeat
import random

class TestPython(unittest.TestCase):
    
    def test_default_object_equality(self):
        a = object()
        b = object()
        self.assertEqual(a,a)
        self.assertEqual(b,b)
        self.assertNotEqual(a,b)
        
    def test_default_object_order(self):
        class my_obj(object):
            def __lt__(self, other):
                if not isinstance(other,my_obj):
                    raise TypeError('')
                return id(self) < id(other)
            def __ge__(self, other):
                if not isinstance(other,my_obj):
                    raise TypeError('')
                return id(self) >= id(other)
        a = my_obj()
        b = my_obj()
        self.assertTrue(a<b)
        self.assertFalse(a>=b)
        
    def test_string_split(self):
        string = """abbatti sifoni restie
lambivamo spiegando"""
        tokens = string.split()
        print(tokens[2])
        self.assertEqual(len(tokens),5)
        
    def test_dict_iterator(self):
        d = {'a':3,'b':6}
        for x in iter(d):
            print(x)
            
    def test_modulo_pow_2(self):
        for m in [2**x for x in range(100)]:
            for x in range(100000):
                self.assertEqual(x % m , x & (m-1))
                
    def test_modulo_pow_2(self):
        for m in [2**x for x in range(100)]:
            for x in range(100000):
                self.assertEqual(x % m , x & (m-1))
        
    def test_modulo_performance(self):
        print('\n')
        time = repeat(lambda: random.randint(0,1000000) % 42, number=100000, repeat = 10)
        print("Elapsed time: {}".format(min(time)))
        time = repeat(lambda: random.randint(0,1000000) % 128, number=100000, repeat = 10)
        print("Elapsed time: {}".format(min(time)))
        time = repeat(lambda: random.randint(0,1000000) & 127, number=100000, repeat = 10)
        print("Elapsed time: {}".format(min(time)))
from engine import SearchEngine
from time import time

start = time()
se=SearchEngine("TestDataSet")

print(se.search("ciao",2))
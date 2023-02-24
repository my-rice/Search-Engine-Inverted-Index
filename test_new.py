from time import time
import engine

DIR = "dataset_new/dataset"

f1 = open("dataset_new/output1.txt", "r")
OUT_1 = f1.read()
f2 = open("dataset_new/output2.txt", "r")
OUT_2 = f2.read()
f3 = open("dataset_new/output3.txt", "r")
OUT_3 = f3.read()
start = time()
se = engine.SearchEngine(DIR)
out1 = se.search("heapify", 600)
out2 = se.search("priorityqueues", 30)
out3 = se.search("downheap", 1500)
end = time() - start

if out1 != OUT_1 or out2 != OUT_2 or out3 != OUT_3:
    print("FAIL")
else:
    print("True")
print(end)

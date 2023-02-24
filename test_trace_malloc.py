from engine import SearchEngine
from time import time
import linecache
import os
import tracemalloc

def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

DIR="dataset"
OUT_1="www.unisa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unisal.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unina.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unipa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html"

OUT_2="www.unica.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.uniba.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unito.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unimi.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unisa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unisal.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unina.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html\nwww.unipa.it\n--- 1zz.html\n--- aaa.html\n--- diem\n------ daa.html\n------ profs\n--------- auletta.html\n--------- ferraioli.html\n--------- vinci.html\n--- index.html\n--- AAAA.html"

#start = time()
tracemalloc.start()
se=SearchEngine(DIR)
snapshot = tracemalloc.take_snapshot()
display_top(snapshot,limit=10)



nucleobase = 'ATGC'
from random import randint
from sys import argv
split = len(argv) == 3
splitInterval = 0
if split:
    splitInterval = int(argv[2])
outf = open('randomseq.fasta', 'w')
outf.write('>random\n')
seqlength = int(argv[1])
for i in range(0, seqlength):
    a = randint(0,3)
    res = nucleobase[a]
    outf.write(res)
    if split and (i + 1) % splitInterval == 0:
        outf.write("\n")
outf.close()
indata.close()

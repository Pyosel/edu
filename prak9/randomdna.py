nucleobase = 'ATGC'
from random import randint
from sys import argv
outf = open('randomseq.fasta', 'w')
outf.write('>random\n')
seqlength = int(argv[1])
for i in range(0, seqlength):
    a = randint(0,3)
    res = nucleobase[a]
    outf.write(res)
outf.close()

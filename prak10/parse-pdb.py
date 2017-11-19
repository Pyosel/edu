from sys import argv
import urllib2
outFile = open(argv[2], 'w')
urlName =  'https://files.rcsb.org/download/' + argv[1] + '.pdb'
try:
    urlFile = urllib2.urlopen(urlName)
    res = []
    for line in urlFile:
        if line[0:4] == 'ATOM' and line[12:16] == ' CA ':
            res.append(line[:-1])
    outFile.write('Residue Chain\t'+ 'Number\t' + 'X\t' + 'Y\t' + 'Z\n')
    for atom in res:
        outFile.write(atom[17:20] + '\t' + atom[22:26] + '\t' + atom[30:38] + '\t' + atom[38:46] + '\t' + atom[46:54] + '\n')
    urlFile.close()
    outFile.close()
except Exception:
    print 'Code does not exist'

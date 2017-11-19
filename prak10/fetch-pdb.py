from sys import argv
import urllib2
outFile = open(argv[2], 'w')
urlName =  'https://files.rcsb.org/download/' + argv[1] + '.pdb'
try:
    urlFile = urllib2.urlopen(urlName)
    for line in urlFile:
        outFile.write(line)
    urlFile.close()
    outFile.close()
except Exception:
    print 'Code does not exist'

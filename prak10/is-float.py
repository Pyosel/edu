from sys import argv
try:
    float(argv[1])
    print 'Is float'
except Exception:
    print 'Is not float'

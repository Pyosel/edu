from sys import argv
inputFile = open(argv[1])
k = argv[2]
indata = inputFile.read().splitlines()
dict = {}
for line in indata:
    x = 0
    sequence = True
    if '>' in line:
        sequence = False
    if sequence:
        nucl = line [ x:(x+k)]
        kMer = dict.get(nucl)
        if kMer == None:
            dict[nucl] = 1
        else:
            dict[nucl] = kMer+1
    x = x +1
inputFile.close()

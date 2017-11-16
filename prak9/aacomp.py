from sys import argv
length = len(argv)
inputFile = None
outputFile = None
if length > 2:
    inputFile = open(argv[1])
    outputFile = open(argv[2], 'w')
if length == 2:
    inputFile = open(argv[1])
if length < 2:
    print 'Enter file name:'
    inputFile = open(raw_input())
indata = inputFile.read().splitlines()
dict = {}
for x in range(1, len(indata)):
    for i in indata[x]:
        i = i.upper()
        res = dict.get(i)
        if res == None:
            dict[i] = 1
        else:
            dict[i] = res+1
for key in sorted(dict):
    res = dict.get(key)
    if length > 2:
        key = str(key)
        res = str(res)
        outputFile.write(key + '\t' + res + '\n' )
    if length <= 2:
        print key, '\t', res
inputFile.close()
if outputFile != None:
    outputFile.close()

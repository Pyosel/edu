from sys import argv
if len(argv) == 3:
    indata = open(argv[1])
    outf = open(argv[2], 'w')
if len(argv) == 2:
    indata = open(argv[1])
if len(argv) == 1:
    print 'Enter file name:'
    indata = open(raw_input())
indata = indata.read().splitlines()
dict = {}
for x in range(1,len(indata)):
    for i in indata[x]:
        i = i.upper()
        res = dict.get(i)
        if res == None:
            dict[i] = 1
        else:
            dict[i] = res+1
for key in sorted(dict):
    res = dict.get(key)
    if len(argv) == 3:
        key = str(key)
        res = str(res)
        outf.write(key + '\t' + res + '\n' )
    if len(argv) == 2 or len(argv) == 1:
        print key, '\t', res

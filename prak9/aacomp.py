from sys import argv
indata = open(argv[1])
indata = indata.read().splitlines()
outf = open(argv[2], 'w')
d = {}
x = 1
for str in indata:
    for i in str[x]:
        res = dict.get(i)
        if res == None:
            dict[i] = 1
        else:
            dict[i] = res+1
print dict

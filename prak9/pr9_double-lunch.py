from sys import argv
indata = open(argv[1], "r")
dict = {}
while True:
    i = indata.readline()[:-1]
    if i == "STOP":
        break
    res = dict.get(i)
    if res == None:
        dict[i] = 1
    else:
        dict[i] = res + 1
for key in dict:
    res = dict.get(key)
    if res > 1:
        print key
indata.close()

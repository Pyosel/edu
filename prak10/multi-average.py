from sys import argv
fileNames = argv[1:]
for file in fileNames:
    try:
        inputFile = open(file)
        indata = inputFile.readline()[:-1].split()
        inputFile.close()
        try:
            theSum = 0
            for number in indata:
                number = float(number)
                theSum = theSum + number
            print theSum/len(indata)
        except Exception:
            print 'File ' + file + ' has wrong format'
    except Exception:
        print 'Error reading file ' + file 

from sys import argv
size = int(argv[1])
if (size == 0):
    print 0
else:
    list = [None] * (size + 1)
    list[0] = 0
    list[1] = 1
    def fibonacci(x):
        first = list[x-1]
        if first == None:
            first = fibonacci(x-1)
        second = list[x-2]
        if second == None:
            second = fibonacci(x-2)
        result = first + second
        list[x] = result
        return result
    fibonacci(size)
    s = ''
    for i in list:
        s = s + str(i) + ' '
    print s

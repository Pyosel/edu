from sys import argv
number = int(argv [1])
def Factorial(x):
    if x <= 1:
        return 1
    else:
        return x * Factorial(x-1)
print Factorial(number)

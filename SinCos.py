import math
from sys import argv
degreeInput = float(argv[1])
radiansInput = math.radians(degreeInput)

print round(math.sin(radiansInput), 4)
print round(math.cos(radiansInput), 4)

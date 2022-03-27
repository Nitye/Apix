import os
import numpy as np
from functools import reduce
import operator

string = input()

numbers = {int(word) for word in string.split() if word.isdigit()}
print(numbers)
ab = sum(numbers)
print(ab)
bc = reduce((lambda x, y: x*y), numbers)
print(bc)
cd = abs(reduce((lambda x, y: x-y), numbers))
print(cd)
de = reduce((lambda x, y: x/y), numbers)
print(de)
df = reduce((lambda x, y: x/y), numbers)
print(df)

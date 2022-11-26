import pandas as pd
import binascii

st = "h"
s = ' '.join(format(ord(x), 'b') for x in st)
#print(s)
a = "1110111"
print(chr(int(a)))
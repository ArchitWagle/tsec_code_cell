from math import *

def ln2(x):
    return(pow(2,floor(log(x,2)))%1000000007)


print(ln2(10)+ln2(100)+ln2(1000000)+ln2(1000000000)+ln2(12345654321)+ln2(9999999999999999 ))

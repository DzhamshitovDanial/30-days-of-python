from random import *
def unique_array():
    s=[]
    while len(s)!=7:
        n=randint(0,9)
        if not n in s:
            s.append(n)
    return s
print(unique_array())
import math

def v(r,pai=math.pi):

    return [4*pai*int(r)**2 for r in r]
m=v([1,2,4,9,10,13])
for i in m:
    print(round(i,2))

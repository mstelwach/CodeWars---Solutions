import math

def isPP(x):
    for n in range(2, 1+round(math.log2(x)) ):
        root   = pow( 10, math.log10(x)/n )
        result = round(root)
        if result**n == x:
            return [result,n]


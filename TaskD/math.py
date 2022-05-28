import math

def C (x, y, a):
    return (x - (math.exp(2 * y)/(4 * math.fabs(1-math.pow(x,3)))) + 3.34 * math.pow(math.sin(2 * x), 2) + a * math.log(27, 3))


def B(x, k, y):
    return (math.pow((8 * y),1/3) - math.pi * math.log( math.asin(1/k*x),math.exp(1)))

print(C(2,3,5))
print(B(2,5,4))
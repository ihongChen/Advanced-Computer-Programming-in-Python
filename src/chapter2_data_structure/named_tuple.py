## namedtuple 

from collections import namedtuple

namedtuple('Register','ID name age') 

def compute_geometry(a, b):
    Features = namedtuple('Geometrical','area perimeter mpa mpb')
    area = (a,b)
    perimeter = (2*a) + (2*b)
    mpa = a/2
    mpb = b/2
    return Features(area, perimeter, mpa, mpb)

data = compute_geometry(20, 10)
print(data)


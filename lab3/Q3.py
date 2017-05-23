from math import sqrt

def find_root(a, b, c):
    """Returns one of two roots of a quadratic function.
    
    Since there are two roots to quadratics, return the the larger
    root. In other words, the + or - part of the quadratic equation
    should just be replaced with a +
    
    >>> find_root(1, 2, 1)
    -1.0
    >>> find_root(1, -7, 12)
    4.0
    """
    def discriminant(a, b, c):
        delta=pow(b,2)-4*a*c
        return delta
    roots=(-b+sqrt(discriminant(a,b,c)))/2*a
    return roots

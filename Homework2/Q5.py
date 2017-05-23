from operator import add
def Successor(n):
    return lambda f:lambda x :f(n(f)(x))

def f(x):
    return add(x,1)

def one(f):
    return lambda x: f(x)

def two(f):
    return lambda x:f(f(x))

def church_to_int(n):
    return lambda f: lambda x: f(n(f)(x))

def add_chruch(m,n):
    return lambda add:  add(church_to_int(m),church_to_int(n))


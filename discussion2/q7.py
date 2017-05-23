"""Q7"""
def and_add_one(f):
    def g(n):
        result=f(n)+1
        print(result)
    return g


def num(n):
    return n

def and_add(f,n):
    def g(x):
        result=f(x)+n
        print(result)
    return g


"""Accumulate"""
from operator import add
def lazy_accumulate(f, start, n, term):
    r_n=logic(start=start,n=n,term=term,i=1)
    def g(m,r_n=r_n):
        r_m=logic(start=start,n=m+n,term=term,i=n+1)
        acc=f(r_n,r_m)
        return acc
    return g
        


def logic(start,n,term,i):
    result=start
    while i<=n:
        result=term(result,i)
        i+=1
    return result

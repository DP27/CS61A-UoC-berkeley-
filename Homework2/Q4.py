def repeated(f,n):
    def g(x):
        k=0
        while k<n:
            x,k=f(x),k+1
        return x
    return g



def f(x):
    return x*x

    

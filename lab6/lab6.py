"""
Write a function make_fib that returns a function that returns the next Fibonnaci number each time it is called. Examples:
>>> fib = make_fib()
>>> fib()
1
>>> fib()
1
>>> fib()
2
>>>fib()
3
"""
def make_fib():
    fib_s=1;curr=0;prev=0
    def fib():
        nonlocal prev,curr,fib_s
        curr,prev=fib_s+prev,curr
        fib_s=curr
        return fib_s
    return fib
        
    
    
    

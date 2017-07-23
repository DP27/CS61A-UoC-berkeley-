def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    for i in range(n+1):
        yield n-i
    

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    "*** YOUR CODE HERE ***"
    t=iter(s)
    while k:
        yield next(t)
        k-=1
    raise ValueError
        
            
        

def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(s, 2)
    4
    >>> repeated(s, 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    n=0
    count=1
    for elem in t:
        s=t[n+1:]
        j=0
        while elem == s[j]:
            count+=1
            if k==count:
                return elem
            if j<=len(t)-1:
                j+=1
        count=1
        n+=1



def repeated_with_trap(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    first = True
    for v in t:
        if first:
            first, previous = False, v
        elif v != previous:
            previous, count = v, 1
        else:
            count += 1
            if count == k:
                return v
           

def hailstone(n):
    """
    Here's a quick reminder of how the hailstone sequence is defined:
    Pick a positive integer n as the start.
    If n is even, divide it by 2.
    If n is odd, multiply it by 3 and add 1.
    Continue this process until n is 1.
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    if n<0:
        assert n>0,'n should be positive'
    else:
        while n!=1:
            yield n
            if n%2==0:
                n=n//2
            else:
                n=((3*n)+1)
        yield n
            
            
            
    

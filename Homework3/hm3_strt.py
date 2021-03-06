"""61A Homework 3
Name:
Login:
TA:
Section:
"""


def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


# Q1.

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    tuple=(a,b)
   # assert (a!=b),"The interval should have different start and end values"
    return tuple

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    if x[0]<x[1]:
        return x[0]
    else:
        return x[1]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    if x[0]>x[1]:
        return x[0]
    else:
        return x[1]

# Q2.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert (y[0]!=y[1]),"Interval span is Zero"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    y_new=(-lower_bound(y),-upper_bound(y))
    lower = lower_bound(x) + lower_bound(y_new)
    upper = upper_bound(x) + upper_bound(y_new)
    return interval(lower, upper)


# Q4.

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(interval(-2, -1), interval(4, 8)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(interval(-1, 3), interval(-4, 8)))
    '-12 to 24'
    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(-8, 4)))
    '-16 to 8'
    >>> str_interval(mul_interval_fast(interval(-1,-2), interval(-8,-4)))
    '4 to 16'
    >>> str_interval(mul_interval_fast(interval(-1,2), interval(-8,-4)))
    '-16 to 8'
    """
    "*** YOUR CODE HERE ***"
    if lower_bound(x)<0 and upper_bound(x)>0 and lower_bound(y)>0 and upper_bound(y)>0:
        return interval(lower_bound(x)*upper_bound(y),upper_bound(x)*upper_bound(y))
    elif lower_bound(x)<0 and upper_bound(x)<0 and lower_bound(y)>0 and upper_bound(y)>0:
        return interval(lower_bound(x)*upper_bound(y),upper_bound(x)*lower_bound(y))
    elif lower_bound(x)<0 and upper_bound(x)>0 and lower_bound(y)<0 and upper_bound(y)>0:
        if lower_bound(x)<lower_bound(y):
            return interval(lower_bound(x)*upper_bound(y),upper_bound(x)*upper_bound(y))
        else:
            return interval(lower_bound(y)*upper_bound(x),upper_bound(x)*upper_bound(y))
    elif lower_bound(x)<0 and upper_bound(x)<0 and lower_bound(y)<0 and upper_bound(y)<0:
        return interval(lower_bound(x)*lower_bound(y),upper_bound(x)*upper_bound(y))
    elif lower_bound(x)<0 and upper_bound(x)>0 and lower_bound(y)<0 and upper_bound(y)<0:
        return interval(upper_bound(x)*lower_bound(y),lower_bound(x)*lower_bound(y))
    # 3 more cases follows 
    
    
        
    
            
        


# Q5.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    "*** YOUR CODE HERE ***"
    return interval(c-(c*p/100),c+(c*p/100))

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    "*** YOUR CODE HERE ***"
    c=center(x)
    p=(100*abs(lower_bound(x)-c))/c
    return p
    

# Q6.

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
a=interval(6,2)
b=interval(16,4)
parallel1=par1(a,b)
parallel2=par2(a,b)

# Q7.

def multiple_references_explanation():
  return """The mulitple reference problem..."""

# Q8.


def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b, and
    c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    f=lambda t: a*t*t+b*t+c
    extr=(-b)/(2*a)
    l,u,extr=map(f,(lower_bound(x),upper_bound(x),extr))
    print(l,u,extr)
    if extr>=l and extr<=u:
        return (min(l,u,extr),max(l,u,extr))
    else:
        return (min(l,u),max(l,u))
    

# Q9.

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.

    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    zero_interval=0
    result=zero
    for i in range (0,len(seq)):
        if non_zero(seq[i])==True:
            result=add_interval(result,square_interval(seq[i]))
        else:
            zero_interval+=1
    print("Number of zero intervals in the given seq are:",zero_interval)
    return result

    
from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.

    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    result=zero
    map_list=map(square_interval,(filter(non_zero,seq)))
    result=reduce(add_interval,map_list,zero)

    return result
                

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.

    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    gen=(square_interval(x) for x in seq if non_zero(x))
    result=reduce(add_interval,gen,zero)
    return result


# Q10.

def polynomial(x, c):
    """Return the interval that is the range the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> r = polynomial(interval(0.5, 2.25), (10, 24, -6, -8, 3))
    >>> round(lower_bound(r), 5)
    18.0
    >>> round(upper_bound(r), 5)
    23.0
    """
    "*** YOUR CODE HERE ***"
    k=len(c)-1
    print(k)
    for i in range (0,len(c)):
        f=lambda t:c[k-i]*pow(t,k-i)
    result=(f(lower_bound(x)),f(upper_bound(x)))
    return result
    
            



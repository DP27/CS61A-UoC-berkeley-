"""1. Write a function sum that uses a while loop to calculate the sum of the elements of a
tuple. Note: sum is actually already built into Python!"""
""" Sums up the tuple.
>>> sum((1, 2, 3, 4, 5))
15"""
def sum(tup):
    i=0;sum=0
    while i!=len(tup):
        sum+=tup[i]
        i+=1
    return sum
    
"""2. Write a function min element that returns the minimum element in a tuple."""
""" Returns the minimum element in tup.
>>> a = (1, 2, 3, 2, 1)
>>> min_element(a)
1
"""
def min_element(tup):
    return min(tup)

"""3. Fill in the definition of map tuple. map tuple takes in a function and a tuple as arguments
and applies the function to each element of the tuple."""
"""Applies func to each element of tup and returns a new tuple.
>>> a = (1, 2, 3, 4)
>>> func = lambda x: x * x
>>> map_tuple(func, a)
(1, 4, 9, 16)
"""
def map_tuple(func, tup):
    return list(map(func,tup))

"""4. Fill in the definition of cartesian product. cartesian product takes in two tuples and
returns a tuple that is the Cartesian product of those tuples. To find the Cartesian
product of tuple X and tuple Y, you take the first element in X and pair it up with all
the elements in Y. Then, you take the second element in X and pair it up with all the
elements in Y, and so on."""

"""Returns a tuple that is the cartesian product of tup_1 and tup_2.
>>> X = (1, 2)
>>> Y = (4, 5)
>>> cartesian_product(X, Y)
((1, 4), (4, 1) (1, 5), (5, 1), (2, 4), (4, 2) (2, 5), (5, 2))
"""
    
def tup(a,cycle):
    if cycle==1:
        global tup_var
        tup_var=a
    else:
        tup_var=(a,tup_var)
    return tup_var

def cartesian_product(tup_1, tup_2):
    n=0;cycle=0;
    for i in range (0,len(tup_2)):
        cart_p=(tup_1[n],tup_2[i])
        result=tup(cart_p,cycle)
        cycle+=1
        cart_p=(tup_1[n+1],tup_2[i])
        result=tup(cart_p,cycle)
    for i in range (0,len(tup_1)):
        cart_p=(tup_2[n],tup_1[i])
        result=tup(cart_p,cycle)
        cycle+=1
        cart_p=(tup_2[n+1],tup_1[i])
        result=tup(cart_p,cycle)    
    return result

def cartesian_product_1(tup1, tup2):
    i, j = 0, 0
    len_1, len_2 = len(tup1), len(tup2)
    product = ()
    while i < len_1:
        while j < len_2:
            product += ((tup1[i], tup2[j]), )
            product += ((tup2[j], tup1[i]), )
            j += 1
            i += 1
    return product

"""1. Implement sum one more time, this time using a for-loop."""
def sum(sequence):
    sum=0
    for i in range (0,len(sequence)):
        sum+=sequence[i]
    return sum
        
        

"""2. Now use a for-loop to write a function filter that takes a predicate of one argument
and a sequence and returns a tuple. (A predicate is a function that returns True or
False.)
This tuple should contain the same elements as the original sequence, but without the
elements that do not match the predicate, i.e. the predicate returns False when you
call it on that element.
>>> filter(lambda x: x % 2 == 0, (1, 4, 2, 3, 6))
(4, 2, 6)  """
def filter(pred, sequence):
    tup=()
    for i in range (0,len(sequence)):
        if pred(sequence[i])==True:
            tup+=(sequence[i],)
        else:
           next
    return tup
        
            
            
"""1. Write a function cube root that computes the cube root of the input number x.
(Hint: Use newtons method with a function that is zero at the cube root of the input.)"""

"""Errors in code need to be resolved"""

def cube_root(x):
    def cube_guess(y):
        return y*y*y-x
    return cube_guess
    

def derivative(f,dx=0.0001):
    def derive(x):
        return f(x+dx)-f(dx)/dx
    return derive

def newton(fn,guess=1,iterate=100):
    def newton_update(guess):
        f_der=derivative(fn(guess))
        guess=guess-(fn(guess)/f_der)
        return guess
    def newton_isdone(guess):
        error_margin=0.0001
        return abs(fn(guess))<=error_margin
    return max_iterate(newton_update,newton_isdone,iterate)

def max_iterate(update,isdone,guess=1,iterate=100):
    i=0
    while not isdone(guess) and i<iterate:
        guess=update(guess)
        i+=1
    return guess


        


"""61A Homework 4
Name:
Login:
TA:
Section:
"""

# Q1.

def reverse_list(s):
    """Reverse the contents of list s and return None.

    >>> digits = [6, 2, 9, 5, 1, 4, 1, 3]
    >>> reverse_list(digits)
    >>> digits
    [3, 1, 4, 1, 5, 9, 2, 6]
    >>> d = digits
    >>> reverse_list(d)
    >>> digits
    [6, 2, 9, 5, 1, 4, 1, 3]
    """
    "*** YOUR CODE HERE ***"
    x=s
    new_list=[]
    counter=len(x)-1
    while counter>=0:
        new_list+=[x[counter],]
        counter-=1

    s[:]=new_list
    print(s,x)
    return 
        


# Q2.

def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    sum=0
    def acc_logic(value):
        nonlocal sum
        sum+=value
        return sum
    return acc_logic
        
        


# Q4.

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a', 3)
    3
    >>> c('a', 5)
    8
    >>> c('b', 7)
    7
    >>> c('a', 9)
    17
    >>> c2 = make_counter()
    >>> c2(1, 2)
    2
    >>> c2(3, 4)
    4
    >>> c2(3, c('b', 6))
    17
    """
    "*** YOUR CODE HERE ***"
    value=0
    dir={}
    def count_imp(str,value_passed):
        nonlocal value
        bool=str not in dir
        if bool==True:
            dir[str]=value_passed
            value=value_passed
        else:
            value=dir[str]
            value+=value_passed
            dir[str]=value
        print(dir)
        return value
    return count_imp
        


# Q5.

def square(x):
    return x*x

def compose1(f, g):
    """Return a function of x that computes f(g(x))."""
    return lambda x: f(g(x))

from functools import reduce

def repeated(f, n):
    """Return the function that computes the nth application of f, for n>=1.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    if n==1:
        return f
    assert type(n) == int and n > 0, "Bad n"
  #  return reduce(compose1,[f for _ in range(0,n)])
    return reduce(compose1,(repeated(f,n-1),f))


# Q6.

def card(n):
    """Return the playing card type for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))


def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> suits = ['♡', '♢', '♤', '♧']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['Aâ™¡', 'Aâ™¢', 'Aâ™¤', 'Aâ™§', '2â™¡', '2â™¢', '2â™¤', '2â™§', '3â™¡', '3â™¢', '3â™¤', '3â™§']
    >>> cards[26:30]
    ['7â™¤', '7â™§', '8â™¡', '8â™¢']
    >>> shuffle(cards)[:12]
    ['Aâ™¡', '7â™¤', 'Aâ™¢', '7â™§', 'Aâ™¤', '8â™¡', 'Aâ™§', '8â™¢', '2â™¡', '8â™¤', '2â™¢', '8â™§']
    >>> shuffle(shuffle(cards))[:12]
    ['Aâ™¡', '4â™¢', '7â™¤', '10â™§', 'Aâ™¢', '4â™¤', '7â™§', 'Jâ™¡', 'Aâ™¤', '4â™§', '8â™¡', 'Jâ™¢']
    >>> cards[:12]  # Should not be changed
    ['Aâ™¡', 'Aâ™¢', 'Aâ™¤', 'Aâ™§', '2â™¡', '2â™¢', '2â™¤', '2â™§', '3â™¡', '3â™¢', '3â™¤', '3â™§']
    >>> repeated(shuffle, 8)(cards) == cards
    True
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    "*** YOUR CODE HERE ***"
    cards_inst=list(cards)
    nofcards=52
    n=1
    halves=nofcards//pow(2,n)
    shuff_cards=[]

   
    cards_firsthalf=[cards[n] for n in range(0,halves)]
    cards_secondhalf=[cards_inst[m] for m in range(halves,nofcards)]

   
    
   
    for n in range(0,halves):
        shuff_cards.append(cards_firsthalf[n])
        shuff_cards.append(cards_secondhalf[n])
    

    return shuff_cards

    
  

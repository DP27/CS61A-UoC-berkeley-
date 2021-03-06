"""1) Now let’s wrap up by seeing how nonlocal programs and environment programs come together.Write a procedure make_counter that returns a dispatch procedure that behaves in the following way.
Then also draw the environment diagram for this interaction. Do you see the connection? Try and see if you can fit the two together at the same time.
>>> counter1 = make_counter(0)
>>> counter1('inc')
>>> counter1('count')
1
>>> counter1(‘inc’)
>>> counter1(‘inc’)
>>> counter1(‘count’)
3
>>> counter2 = make_counter(42)
>>> counter1('inc')
>>> counter2('inc')
>>> counter2('count')
43
>>> counter1('reset')
>>> counter1('inc')
>>> counter2(‘count’)
43
>>> counter1(‘count’)
1
"""
def make_counter(n):
    inc=0
    def counter(string):
        nonlocal n,inc
        if string=='inc':
            inc+=1
            n+=1
        elif string=='count':
            return n
        elif string=='reset':
            n=n-inc
    return counter
            
            
        

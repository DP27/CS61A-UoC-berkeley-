def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function 
    >>> add1 = lambda x: x+1 
    >>> times2 = lambda x: 2*x 
    >>> add3 = lambda x: x+3 
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1) # semanitcally the same as times2(add1(1))
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2) # semantically the same as add3(times2(add1(2)))
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2) # semantically the same as add1(add3(times2(add1(2))))
    10
    >>> do_two_cycles = my_cycle(6) # semantically the same as add3(times2(add1(add3(times2(add1(1))))))
    >>> do_two_cycles(1)
    19
    """

    " *** YOUR CODE HERE *** "
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return ret
    return ret_fn





    
        

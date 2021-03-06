def make_derivative(f, h=1e-5):
    """Returns a function that is the derivative of f.
    
    >>> square = lambda x: x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3)
    6.0
    """
    "*** YOUR CODE HERE ***"
    def g(a):
        der= (f(a+h)-f(a))/h
        return der
    return g


    




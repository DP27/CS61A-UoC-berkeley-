"""Square"""
def square_every_number(n):
    sqaure=1
    for square in range (1,n+1):
        square=pow(square,2)
        print(square)
        square+=1
    return 
    
        
        
"""Double"""
def double_every_number(n):
    double=1
    for double in range (1,n+1):
        double*=2
        print (double)
        double+=1
    return


def Square(n):square_every_number(n)
def Double(n):double_every_number(n)

"""Generalized"""
def every(f,n):
    if f is Square:
        return Square(n)
    elif f is Double:
        return Double(n)
    else:
        print("Invalid Operator")
    return
    

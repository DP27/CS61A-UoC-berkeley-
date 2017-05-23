def make_rat(num,den):
    return (num,den)

def num(x):
    return x[0]

def den(x):
    return x[1]

from fractions import gcd
def div_rat(a,b):
    new_num=(num(a)*den(b))//gcd(num(a),den(b))
    new_den=(den(a)*num(b))//gcd(den(a),num(b))
    return make_rat(new_num,new_den)

def str_rat(x):
    return '{0}/{1}'.format(num(x),den(x))
    
    

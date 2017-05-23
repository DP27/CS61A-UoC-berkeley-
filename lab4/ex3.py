def make_rat(num, den):
    return (num, den)

def num(rat):
    return rat[0]

def den(rat):
    return rat[1]

def mul_rat(a, b):
    new_num = num(a) * num(b)
    new_den = den(a) * den(b)
    return make_rat(new_num, new_den)

def str_rat(x):  #from lecture notes
       """Return a string 'n/d' for numerator n and denominator d."""
       return '{0}/{1}'.format(num(x), den(x))

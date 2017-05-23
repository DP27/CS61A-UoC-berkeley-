def isnumber(thing):
   try:
       int(thing)
   except:
       return False
   return True

def type_check(func,isnumber,dat):
    if isnumber(dat)==True:
        return func(dat)
    else:
        return False
    return

def make_safe(f,isnumber):
    def g(a):
        if isnumber(a)==True:
            return f(a)
        else:
            return False
    return g

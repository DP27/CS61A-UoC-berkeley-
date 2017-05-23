
def make_pair(x, y):
       """Return a function that behaves like a pair."""
       
       def dispatch(m):
           if m == 0:
               return x
           elif m == 1:
               return y
           elif m=='pair':
               return (x,y)
           assert (m<=1 or m=='pair'),"Message Not Recognized"
       return dispatch

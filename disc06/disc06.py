"""
1. Write a function remove duplicates that takes as input a sorted linked list of integers, lnk, and mutates lnk so that all duplicates are removed.
"""
def remove_duplicates(lnk):
    """
>>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
>>> unique = remove_duplicates(lnk)
>>> len(unique)
2
"""
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    else:
        for val in lnk.rest:
            if lnk.first==val:
                lnk=lnk.rest
                remove_duplicates(lnk)

        lnk='Link({0},{1})'.format(lnk.first,remove_duplicates(lnk.rest))
    
    return eval(lnk)

"""Alternative with Mutation"""

"""
>>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
>>> unique = remove_duplicates(lnk)
>>> len(unique)
2
>>> len(lnk)
2
"""

def remove_duplicates_2(lnk):
    if lnk is not Link.empty and lnk.rest is not Link.empty:
        remove_duplicates_2(lnk.rest)
        if lnk.rest.first == lnk.first:
            lnk.rest = lnk.rest.rest
    return lnk



"""
3. Write multiply lnks, which takes in a Python list of Link objects and multiplies them element-wise. It should return a new linked list. If not all of the Link objects
are of equal length, return a linked list whose length is that of the shortest linked list given. You may assume the Link objects are shallow linked lists, and that lst of lnks contains at least one linked list.
"""
def multiply_lnks(lst_of_lnks):
    """
>>> a = Link(2, Link(3, Link(5)))
>>> b = Link(6, Link(4, Link(2)))
>>> c = Link(4, Link(1, Link(0, Link(2))))
>>> p = multiply_lnks([a, b, c])
>>> p.first
48
>>> p.rest.first
12
>>> p.rest.rest.rest
()
    """
    product=1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return lnk
        product*=lnk.first
    lst_of_lnk_rest=[lnk.rest for lnk in lst_of_lnks]
    print(lst_of_lnk_rest)
    return Link(product,multiply_lnks(lst_of_lnk_rest))
        
    
            
            
                

"""
2. Define reverse, which takes in a linked list and reverses the order of the links. The function may not return a new list; it must mutate the original list. Return a pointer
to the head of the reversed list.
"""
def reverse(lnk):
    """
>>> a = Link(1, Link(2, Link(3)))
>>> r = reverse(a)
>>> r.first
3
>>> r.rest.first
2
    """
 
    if lnk==Link.empty or lnk.rest==Link.empty:
       return lnk
  
    rest_rev=reverse(lnk.rest)
  
    
    lnk.rest.rest=lnk
    
    lnk.rest=Link.empty
  
    return rest_rev












class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first,repr(self.rest))

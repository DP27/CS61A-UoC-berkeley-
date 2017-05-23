"""1. Implement the function map mut, which applies a function fn onto every element of a list called lst."""
"""Maps fn onto lst by mutation.
>>> lst = [1, 2, 3, 4]
>>> map_mut(lambda x: x**2, lst)
>>> lst
[1, 4, 9, 16]"""
def map_mut(fn, lst):
    i=0
    while i <= len(lst)-1:
        temp=fn(lst[i])
        lst[i]=temp
        i+=1
    return 

"""2. Define shift left, a function that takes a list and shifts each element in the list to
the left by n indices. If elements start ”falling off” on the left, they are placed back on
the right. NOTE: you may assume that n is a non-negative integer."""
"""Shifts the elements of lst over by n indices.
>>> lst = [1, 2, 3, 4, 5]
>>> shift_left(lst, 2)
>>> lst
[3, 4, 5, 1, 2]
"""
def shift_left(lst, n):
    if n==0 and n==len(lst):
        lst=lst
        return
    if n < len(lst):
        temp=list(lst)
        for i in range (0,len(lst)):
            lst[-n+i]=temp[i]
        del temp
        return
    if n > len(lst):
        assert n<= len(lst),"n out of range"
        return


"""3. Define filter mut, which takes a list and filters out elements that don’t satifsy a given predicate."""
"""Filters lst by mutating it.
>>> lst = [1, 2, 3, 4]
>>> is_even = lambda x: x % 2 == 0
>>> filter_mut(is_even, lst)
>>> lst
[2, 4]
"""
def filter_mut(pred, lst):
    temp=[pred(i) for i in lst]
    lst_new=[]
    for i in range (0,len(temp)):
        if temp[i]==True:
            lst_new.append(lst[i])
    del temp
    i=0;j=0
    while i <=len(lst_new)-1:
        while j <=len(lst)-1:
            if lst_new[i]!=lst[j]:
                lst.pop(j)
                j+=1
            else:
                j+=1
        i+=1
    return



"""1. Write make inverse dict(d) that returns a new dictionary with the ‘inverse’ mapping.
The ‘inverse’ mapping of a dictionary d is a new dictionary that maps each of
d’s values to all keys in d that mapped to it. For instance,
>>> d1 = {‘call’: 3, ‘me’: 2, ‘maybe’: 3}
>>> d2 = make_inverse_dict(d1)
>>> d2 #note that we know nothing about the order of dictionaries
{3: (‘maybe’, ‘call’), 2: (‘me’,)}
The ordering of the tuple of keys doesn’t matter, i.e., d2 could have instead been 3:
(‘call’, ’maybe’), 2: (‘me’,)."""
def make_inverse_dict(d):
    new_dir={}
    i=0
    d_list=list(d.keys())
    d_values=list(d.values())
    while i <= len(d.keys())-1:    
        if d_values[i] in list(new_dir.keys()):
            print('in if')
            new_dir[d_values[i]]+=(d_list[i],)
        else:
            new_dir[d_values[i]]=(d_list[i],)
        
        i+=1
    return new_dir

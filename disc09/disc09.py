"""
   1. Define an generator function that combines two input iterators using a given combiner function. 
   The resulting iterator should have a size equal to the size of the shorter
   of its two input iterators.
   Test Cases:
   >>> from operator import add
   >>> evens = combiner(gen_naturals(), gen_naturals(), add)
   >>> next(evens)
   0
   >>> next(evens)
   2
   >>> next(evens)
   4"""
from operator import add
def combiner(iterator1, iterator2, combiner):
    return map(lambda x,y: combiner(x,y),list(iterator1),list(iterator2))
    
"""    
3. Write a generator function that returns all subsets of the positive integers from 1 to
n. Each call to this generator’s next method will return a list of subsets of the set
[1, 2, ..., n], where n is the number of times next was previously called.
"""
def generate_subsets(lst):
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ... print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    n=0
    lst_of_subsets=[[],]
    yield lst_of_subsets
    temp_lst=list(lst_of_subsets)
    while n < len(lst):
        for elem in temp_lst:
            lst_of_subsets+=[sum([elem],[lst[n]]),]
        yield lst_of_subsets
        temp_lst=list(lst_of_subsets)
        n+=1
    


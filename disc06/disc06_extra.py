"""
2. Implement the functions max product, which takes in a list and returns the maximum product that can be formed using nonconsecutive elements of the list. The
input list will contain only numbers greater than or equal to 1.
"""
def max_product(lst):

    """Return the maximum product that can be formed using lst
without using any consecutive numbers
>>> max_product([10,3,1,9,2]) # 10 * 9
90
>>> max_product([5,10,5,10,5]) # 5 * 5 * 5
125
>>> max_product([])
1 
"""
    index=0
    computed_product=[]
    result=[]
    while index <= len(lst)-1:
        if index<2:
            s=[lst[index]*lst[index+n] for n in range(2,len(lst)) if index+n <= len(lst)-1]
        if index>=2:
            s=[lst[index]*lst[index-n]*lst[index+n] for n in range(2,len(lst)) if index-n >= 0 and index+n <= len(lst)-1]
        if index>=len(lst)-2:
            s=[lst[index]*lst[index-n] for n in range(2,len(lst)) if index-n >= 0]
        computed_product.append(s)
        index+=1
    s=0
    while s <= len(computed_product)-1:
        temp=max(computed_product[s])
        result.append(temp)
        s+=1
    return max(result)


"""
3. An expression tree is a tree that contains a function for each non-leaf root, which can be either ’+’ or ’*’. All leaves are numbers. Implement eval tree, which
evaluates an expression tree to its value. You may want to use the functions sum and prod, which take a list of numbers and compute the sum and product respectively.
"""
def eval_tree(tree):

    """Evaluates an expression tree with functions as root
>>> eval_tree(tree(1))
1
>>> expr = tree('*', [tree(2), tree(3)])
>>> eval_tree(expr)
6
>>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
15
    """
    from numpy import prod
    if tree.branches==[]:
        return tree.root
    else:
        for b in tree.branches:
            if type(b.root)!=int:
                d=eval_tree(b)
                tree.branches.remove(b)
                tree.branches.append(Tree(d))    
            else:
                if tree.root=='+':
                    lst_sum=[lst_sum.root for lst_sum in tree.branches]
                    return sum(lst_sum)
                elif tree.root=='*':
                    lst_prod=[lst_prod.root for lst_prod in tree.branches]
                    return prod(lst_prod)
        if tree.root=='*':
            lst_branches=[lst_branches.root for lst_branches in tree.branches]
            return Tree(prod(lst_branches))
        elif tree.root=='+':
            lst_branches=[lst_branches.root for lst_branches in tree.branches]
            return Tree(sum(lst_branches))

        
class Tree(object):
    empty=()
    def __init__(self,root,branches=[]):
        for b in branches:
            assert isinstance(b,Tree)
        self.root=root
        self.branches=branches

    def __repr__(self):
        str=''
        if self.branches!=[]:
            str='Tree({0},{1})'.format(self.root,self.branches)
            return str
        else:
            if self.root:
                return 'Tree({0})'.format(self.root)
    def isleaf(self):
        return not self.branches



"""
4. The quicksort sorting algorithm is an efficient and commonly used algorithm to order the elements of a list. We choose one element of the list to be the pivot element and
partition the remaining elements into two lists: one of elements less than the pivot and one of elements greater than the pivot. We recursively sort the two lists, which
gives us a sorted list of all the elements less than the pivot and all the elements greater than the pivot, which we can then combine with the pivot for a completely sorted list.
First, implement the quicksort list function. Choose the first element of the list as the pivot. You may assume that all elements are distinct.
"""

def quicksort_list(lst):
    """
>>> quicksort_list([3, 1, 4])
[1, 3, 4]
    """
    if len(lst)<=1:
        return lst
    else:
        pivot=lst[0]
        less=[n for n in lst if n < pivot]
        greater=[n for n in lst[1:] if n >= pivot]
        lst=quicksort_list(less)+[pivot]+quicksort_list(greater)
        return lst



            
            
"""
5. We can also use quicksort to sort linked lists! Implement the quicksort link function, without constructing additional Link instances.You can assume that the extend links function 
is already defined. It takes two linked lists and mutates the first so that the ending node points to the second. extend link returns the head of the first linked list.
>>> l1, l2 = Link(1, Link(2)), Link(3, Link(4))
>>> l3 = extend_links(l1, l2)
>>> l3
Link(1, Link(2, Link(3, Link(4))))
>>> l1 is l3
True
"""

def quicksort_link(link):
    """
>>> s = Link(3, Link(1, Link(4)))
>>> quicksort_link(s)
Link(1, Link(3, Link(4)))
    """
    Less=Link.empty
    greater=Link.empty
    if link is Link.empty:
        return Link.empty
    if len(link)==1:
        return link
    else:
        pivot=link.first
        while link.rest is not Link.empty:
            if link.rest.first < pivot:
                Less=Link(link.rest.first,Less)
            elif link.rest.first > pivot:
                greater=Link(link.rest.first,greater)
            link=link.rest
        p=Link(pivot)
        Less=p.extend_list(Less)
        return quicksort_link(greater).extend_list(quicksort_link(Less))
        

"""
6. Implement widest level, which takes a Tree instance and returns the elements at the depth with the most elements.
"""
def widest_level(t):
    """
>>> sum([[1], [2]], [])
[1, 2]
>>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
... Tree(4, [Tree(9, [Tree(2)])])])
>>> widest_level(t)
[1, 5, 9]
"""
    levels=[]
    x=[t]
    while x:
        levels.append([t.root for t in x])
        x = sum ([t.branches for t in x], [])
    return max (levels, key= len )
        
        
"""
7. Complete redundant map, which takes a tree t and a function f, and applies f to the node (2^d) times, where d is the depth of the node. The root has a depth of 0.
"""
def redundant_map(t, f):
    """
>>> double = lambda x: x*2
>>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
>>> print_levels(redundant_map(tree, double))
[2] # 1 * 2 ˆ (1) ; Apply double one time
[4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
[16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
[256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
"""
    t.root=f(t.root)
    new_f=lambda x: f(f(x))
    t.branches=[redundant_map(n,new_f) for n in t.branches]
    return t
            

class Link:

    empty=()
    
    def __init__(self,first,rest=empty):
        assert rest==Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest

    def first(self):
        return self.first

    def rest(self):
        return self.rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({0})'.format(self.first)
        else:
            return 'Link({0},{1})'.format(self.first,self.rest)

    def __len__(self):
        return 1+len(self.rest)

    def reverse_list(lst):
        if lst.rest is Link.empty:
            return lst
        else:
            reverse=Link.reverse_list(lst.rest)
            lst.rest.rest=lst
            lst.rest=Link.empty
            return reverse
            

    def extend_list(self,lst):
        f=Link.empty
        while self is not Link.empty:
            if lst is not Link.empty:
                f=Link(lst.first,f)
               
                lst=lst.rest
                
            else:
                lst=Link(self.first)
                
                self=self.rest
        f=Link(lst.first,f)
        ret_f=Link.reverse_list(f)
        return ret_f

   

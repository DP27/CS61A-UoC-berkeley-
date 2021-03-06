"""
Exercise 7: Abstracting Rectangles

Implement a representation for rectangles in a plane. (Hint: You may want to make use of your procedures from exercise 5). Then, in terms of your constructors and selectors, create procedures that compute the perimeter and the area of a given rectangle.

"""
from operator import sub
def rect_const(x1,x2):
    if sub(x1[0],x2[0])==0 or sub(x1[1],x2[1])==0:
        return True
    else :
        return False
    assert (x1==0 or x2 == 0),"Error not a rect"
    return

def rect_s(a,b):
    return a

def rect_e(a,b):
    return b

from operator import abs
def proc(l,m,n,o):
    bol=rect_const(l,m)
    bol_n=rect_const(n,o)
    if bol==True and bol_n==True:
        x1=l;x2=m;x3=n;x4=o
    elif bol==False:
        check=rect_const(l,n)
        if check==True:
            x1=l;x2=n;x3=m;x4=o
    
    x_1=rect_s(x1,x2)
    x_2=rect_e(x1,x2)
    len_x=pow(abs(x_1[0]-x_2[0]),2)
    len_y=pow(abs(x_1[1]-x_2[1]),2)
    len=pow(len_x+len_y,0.5)
    x_2=rect_s(x2,x3)
    x_3=rect_e(x2,x3)
    wid_x=pow(abs(x_2[0]-x_3[0]),2)
    wid_y=pow(abs(x_2[1]-x_3[1]),2)
    width=pow(wid_x+wid_y,0.5)
    peri=2*(len+width)
    area=len*width
    print("Perimeter of rect is",peri)
    print("Area of rect is",area)
    return
    

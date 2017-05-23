def accumulate(combiner,start,n,term):
    if combiner=='+':
        n=n+start
        result=summation_using_accumulate(n,term)
    if combiner=='*':
        n=n*start
        result=product_using_accumulate(n,term)
    print("The result is :",result)
    return

def summation_using_accumulate(n,term):
    sum=pow(n,term)
    for i in range(1,n):
        sum=sum+pow((n-i),term)
    return sum
        

def product_using_accumulate(n,term):
    p=n
    for i in range(1,n-1):
        p=p*(n-i)
    result_p=pow(p,term)
    return result_p

def product(n,term):
    p=n
    if n==0:
        return 1
    else:
        for i in range (1,n-1):
            p=p*(n-i)
        print ("The factorial is :",p)
        print("The power of the product is:",pow(p,term))
        return
            

def hailstone(n):
    a=1
    print(n)
    while(n>1):
        if n%2==0:
            n=n/2
            print(n)
            a+=1
        elif n%2!=0:
            n=n*3+1
            print(n)
            a+=1
    print("Length of Sequence",a)
    

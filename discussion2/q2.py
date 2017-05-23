"""Returns Prime Numbers"""
def n_prime(n):
    k=2
    if n<=k:
        print("Number needs to be greater than 2")
    else:
        while n>k:
            if k%2==0:
                k=k+1
                print(k)
            else:
                k+=1
        return 
            
            

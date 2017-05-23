def is_asc(n):
    if n<10:
        print("True")
        return
    elif n>10:
        a=0
        ori=n
        while(n):
            n=n//10
            a+=1
            continue
        temp=0
        print(a)
        for i in range(1,a+1):
            r2=ori%10
            ori=ori//10
            if temp<=r2 and ori!=0:
                i=i+1
                temp=r2
                
            elif ori==0 and temp<=r2:
                print("True")
                return
            if  r2<temp:
                print("False")
                return
               
                   
                    
                

            
            
        
        
    
        
        
    
        

def cycle(f1, f2, f3):
    def ret_fn(n):
        def ret(x):
            i=1
            if n==0:
                return x
            while(i<=n):
                if i%3==1:
                    x=f1(x)
                    i+=1
                elif i%3==2:
                    x=f2(x)
                    i+=1
                elif i%3==0:
                    x=f3(x)
                    i+=1
            return x
        return ret
    return ret_fn


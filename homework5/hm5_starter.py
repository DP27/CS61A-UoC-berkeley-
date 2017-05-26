"""61A Homework 5
Name:
Login:
TA:
Section:
"""

# Q1.

def count_calls(f):
    """A function that returns a version of f that counts calls to f and can
    report that count to how_many_calls.


    >>> from operator import add
    >>> counted_add, add_count = count_calls(add)
    >>> add_count()
    0
    >>> counted_add(1, 2)
    3
    >>> add_count()
    1
    >>> add(3, 4)  # Doesn't count
    7
    >>> add_count()
    1
    >>> counted_add(5, 6)
    11
    >>> add_count()
    2
    """
    "*** YOUR CODE HERE ***"
    func_count=0
    def g(*args):
        nonlocal func_count
        func_count=func_count+1
        return f(*args)
    return g,lambda: func_count
        

# Q2.

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    balance=balance
    password=password
    attempts=0
    list_of_attempts=[]
    def withdraw(amount,pass_code):
        nonlocal balance,attempts,list_of_attempts
        
        if balance!=0 and pass_code==password and balance>=amount and attempts<3:
            balance-=amount
            return balance
        if balance==0 or amount>balance and pass_code==password and attempts<3:
            print('Insufficient funds')
            return
        if pass_code!= password and attempts<=3:
            attempts+=1
            print('Incorrect password')
            list_of_attempts+=[str(pass_code),]
            if attempts>3:
                print('Your account is locked.Attempts:',list_of_attempts)
                return
        if attempts>=3 and pass_code==password:
            print("Your account is locked.Attempts:",list_of_attempts)
            return
    return withdraw

# Q3.

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15 """
    "*** YOUR CODE HERE ***"
    list_of_attempts=[]
    old_password_list=[]
    attempts=0
    if type(withdraw(0,old_password))!= int:
        list_of_attempts=[str(old_password),]
        attempts+=1
        return
    else:
        balance=withdraw(0,old_password)
        old_password_list+=[str(old_password),]
        print(old_password_list)
        if new_password:
            account=make_withdraw(balance,old_password)
            def joint_acc(amount,password):
                nonlocal balance,attempts,list_of_attempts,account
                    
                if password == old_password:
                    balance=account(amount,password)
                    if type(balance)!=int:
                        return
                    else:
                        return balance
                if password == new_password:
                    balance=account(amount,old_password)
                    if type(balance)!=int:
                        return
                    else:
                        return balance
                else:
                    return account(amount, password)
                        
                    
    return joint_acc

#Alternative solution:
def make_joint_alt(withdraw, old_password, new_password):
 """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    error = withdraw(0, old_password)
    if type(error) == str:
        return error
    def joint(amount, password_attempt):
        if password_attempt == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, password_attempt)
    return joint
    

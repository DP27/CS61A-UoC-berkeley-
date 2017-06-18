class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self):
        self.value = 0
    

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value==0 or self.invoked==1:
            self.prev=0
            self.curr=0
            self.value=1
        else:
            self.prev,self.curr=self.curr,self.value
            self.value=self.curr+self.prev
        self.invoked=0
        return self

    def __repr__(self):
        self.invoked=1
        return str(self.value)
    

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    balance=0
    quantity=0
    def __init__(self,product,price):
        self.product=product
        self.price=price

    def vend(self):
        if self.balance < self.price and self.quantity!=0:
            print('You must deposit','$',self.price-self.balance,'more')
            return
        if self.balance==self.price and self.quantity!=0:
            self.quantity=self.quantity-1
            print('Here is your',self.product)
            self.balance=0
            return
        if self.quantity==0 and self.balance==0:
            print("'Machine is out of stock.'")
            return
        if self.balance!=0 and self.quantity==0:
            print('Machine is out of stock.Here is your $',self.balance)
            self.balance=0
            return
        if self.quantity!=0 and self.balance>self.price:
            print('Here is your',self.product,'and',self.balance-self.price,'change')
            self.balance=0
            self.quantity=self.quantity-1
            return
            
    def restock(self,quantity):
        self.quantity=self.quantity+quantity
        print('Current',self.product,'stock:',self.quantity)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Current balance:',self.balance)
        if self.balance!=0 and self.quantity==0:
            print('Machine is out of stock.Here is your $',self.balance)
            self.balance=0
        
    
        

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        else:
            self.operation_str=message.split()
            self.operation=self.operation_str[1]
            if self.operation in MissManners.__dict__.keys():
                op='self.{0}'.format(self.operation)
                temp=[b for b in args if type(b)==str]
                temp_split=temp[0].split()
                temp_op=temp_split[1]
                if temp_op in VendingMachine.__dict__.keys():
                    self.obj=self.obj.obj
                rest_arg=[amount for amount in args if type(amount)==int]
                return eval(op)(temp[0],rest_arg[0])
            if self.operation in VendingMachine.__dict__.keys() and isinstance(self.obj,VendingMachine):
                if args:
                    op='self.obj.{0}'.format(self.operation)
                    return eval(op)(args[0])
                else:
                    op='self.obj.{0}'.format(self.operation)
                    return eval(op)()
            if self.operation in VendingMachine.__dict__.keys() and not isinstance(self.obj,VendingMachine):
                print('Thanks for asking,but I know not how to',message[6:])
            else:
                print('Thanks for asking,but I know not how to',message[6:])

        

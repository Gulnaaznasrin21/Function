def factorial(n):
    return n
def my_function(s):
    i=s
    fact=1
    while i>=1:
        a=factorial(i)
        fact=fact*a
        i-=1
    print(fact)
user=int(input("enter any number"))
my_function(user)
    

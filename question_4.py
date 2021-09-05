def my_function(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(n1,"is greater then all")
    elif n2>n1 and n2>n3:
        print(n2,"is greater")
    else:
        print(n3,"is greater")
a=int(input("enter any number"))
b=int(input("enetr another number"))
c=int(input("enter any number"))
my_function(a,b,c)

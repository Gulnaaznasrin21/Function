def my_function(a,b):
    i=0
    c=[]
    while i<len(a):
        if a[i] in b:
            c.append(a[i])
            c.sort()
        i+=1
    print(c)
list1=[1,342,75,23,98]
list2=[75,23,98,12,78,10,1]
my_function(list1,list2)

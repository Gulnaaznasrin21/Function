def my_function(a,b):
    i=0
    d=[]
    while i<len(a):
        d.append(a[i])
        i+=1
        j=0
        while j<len(b):
            if b[j] not in a and b[j] not in d:
                d.append(b[j])
            j+=1
        d.sort()
        print(d)
l1=[1,5,10,12,16,20]
l2=[1,2,10,13,16]
my_function(l1,l2)
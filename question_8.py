def isharshad(j,k):
    if j%k==0:
        return "it is a harshad number"
    else:
        return "it is not a harshad number"
def my_function(s):
    m=list(str(s))
    i=0
    sum=0
    while i<len(m):
        k=int(m[i])
        i+=1
        sum+=k
        b=isharshad(s,sum)
    print(b)
n=int(input("enterany any number"))
my_function(n)
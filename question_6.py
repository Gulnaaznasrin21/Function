def my_function(str_list):
    return str_list
def names(s):
    i=0
    b=[]
    while i<len(s):
        a=my_function(i)
        if s[i] not in b:
            b.append(s[i])
        i+=1
    print(b)
user=["naaz","sukanya","naaz","sukanya","naaz","saai","saai"]
names(user)
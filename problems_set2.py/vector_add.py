def vector_add(a,b):
    if len(a)!=len(b):
        print("length of vector should be same")
        sum=[]
        for i in range(len(a)):
            sum.append(a[i]+b[i])
        return sum

a=[10,20,30]
b=[12,34,56]
result=vector_add(a,b)
print(result)
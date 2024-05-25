ar = [23,1,61,2,43,2]
for i in range(len(ar)):
    for j in range(0,len(ar)-i-1):
        if ar[j]>ar[j+1]:
            ar[j],ar[j+1]=ar[j+1],ar[j]
print(ar)
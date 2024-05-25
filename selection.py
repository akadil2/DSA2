ar=[2,1,21,3,8]
for i in range(len(ar)):
    min_i = i
    for j in range(i+1,len(ar)):
        if ar[j]<ar[min_i]:
            min_i=j
    ar[i],ar[min_i]=ar[min_i],ar[i]
print(ar)


ar = [-3,21,-9,21,8,9]
for i in range(1,len(ar)):
    key = ar[i]
    j=i-1
    while j>=0 and ar[j]>key:
        ar[j+1]=ar[j]
        j=j-1
    ar[j+1]=key
print(ar)


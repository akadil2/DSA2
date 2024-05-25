def partition(ar,low,high):
    pivot = ar[high]
    i= low-1
    for j in range(low,high):
        if ar[j]<=pivot:
            i=i+1
            ar[j],ar[i]=ar[i],ar[j]
    ar[i+1],ar[high]=ar[high],ar[i+1]
    return i+1
def quicksort(ar,low,high):
    if low<high:
        pindex = partition(ar,low,high)
        quicksort(ar,low,pindex-1)
        quicksort(ar,pindex+1,high)

ar=[2,1,4,3,6,5]
quicksort(ar,0,len(ar)-1)
print(ar)
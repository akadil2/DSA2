def mergesort(ar):
    if len(ar)>1:
        mid = len(ar)//2
        lefthalf = ar[:mid]
        righthalf = ar[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)

        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                ar[k]=lefthalf[i]
                i+=1
            else:
                ar[k]=righthalf[j]
                j+=1
            k+=1
        while i<len(lefthalf):
            ar[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            ar[k]=righthalf[j]
            j+=1
            k+=1
ar=[2,-2,5,-5,10,8]
mergesort(ar)
print(ar)
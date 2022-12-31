def QuickSort(arr,s,e)->None:
     if(s>=e):
        return
     PartitionIndex=Partitions(arr,s,e)
     QuickSort(arr,s,PartitionIndex)
     QuickSort(arr,PartitionIndex+1,e)

def Partitions(arr,l,h)->int:
    pivot=arr[l]
    i=l+1
    mi=0
    while(i<h):
        if(pivot>=arr[i]):
            mi+=1
        i+=1
    pivotIndex=mi+l
    arr[l]=arr[pivotIndex]
    arr[pivotIndex]=pivot
    i=l
    j=h

    while(i<=pivotIndex and j> pivotIndex):

        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i<=pivotIndex and j>pivotIndex):
            t=arr[i]
            arr[j]=arr[i]
            arr[i]=t
            i+=1
            j-=1
    return pivotIndex

l=[2,3,7,13,12,435,76,889,8]

QuickSort(l,0,len(l)-1)
print(l)
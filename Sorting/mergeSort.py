def MergeSort(arr,lowerboundery,maxboundery)->None:
    
    if(lowerboundery>=maxboundery):
        return
    middle=lowerboundery+int((maxboundery-lowerboundery)/2)
    # left sort
    MergeSort(arr,lowerboundery,middle)
    # right sort
    MergeSort(arr,middle+1,maxboundery)
    # merge
    Merge(arr,lowerboundery,middle,maxboundery)

def Merge(arr,lowerboundery,middle,maxboundery)->None:
    temparr=[None]*len(arr)
    firstArrayindex=lowerboundery
    secondArrayindex=middle+1
    current=lowerboundery
    while(firstArrayindex<=middle and secondArrayindex<= maxboundery):
        if(arr[firstArrayindex]< arr[secondArrayindex]):
           temparr[current]=arr[firstArrayindex]
           firstArrayindex+=1
        else:
           temparr[current]=arr[secondArrayindex]
           secondArrayindex+=1
        current+=1
    while(firstArrayindex<=middle):
           temparr[current]=arr[firstArrayindex]
           firstArrayindex+=1
           current+=1
    while(secondArrayindex<= maxboundery):
           temparr[current]=arr[secondArrayindex]
           secondArrayindex+=1
           current+=1
    current=lowerboundery
    while(current<= maxboundery):
           arr[current]=temparr[current]
           current+=1
    
l=[1,5,10,45,2,89,7,6]
MergeSort(l,0,len(l)-1)
print(l)    

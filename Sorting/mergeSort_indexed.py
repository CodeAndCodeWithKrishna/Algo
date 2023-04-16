#merge sort
def merge_sort(items,start,end):
    if (end-start)<2:
        return
    middle=int((end+start)/2)
    merge_sort(items,start,middle)
    merge_sort(items,middle,end)
    merge(items,start,middle,end)

def merge(items,start,middle,end):
    if(items[middle-1]<items[middle]):
        return
    i=start
    j=middle
    tindex=0
    temp=[-1]*(end-start)
    # copy small items from both left and right array
    while(i< middle and j < end):
        if(items[i]<=items[j]):
           temp[tindex]=items[i]
           i+=1 
        else:
           temp[tindex]=items[j]
           j+=1
        tindex+=1

    # copy remaining items from left array to correct position from start+tindex till middle-i
    moveindex=start+tindex
    copyi=0
    templen=middle-i
    while(copyi<templen):
        items[moveindex]=items[i]
        i+=1
        moveindex+=1
        copyi+=1
    # copy all small array from temp to items
    copyi=0
    while copyi <tindex:
        items[start]=temp[copyi]
        start+=1
        copyi+=1    

l=[11,5,2,10,7,3,2]
merge_sort(l,0,len(l))
print(l)


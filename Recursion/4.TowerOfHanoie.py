# swap items from A tower to B using C
def SwapItems(item,S,T,U):
    if item==0:
        return
    SwapItems(item-1,S,U,T)
    print(item,S,"->",T)
    SwapItems(item-1,U,T,S)
SwapItems(3,'A','B','C')        
 
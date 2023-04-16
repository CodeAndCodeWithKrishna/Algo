
def ZigZag(n):
    if(n==0):
        print("--BASECASE--")
        return
    print(n,"PRE")
    ZigZag(n-1)
    print(n,"IN")
    ZigZag(n-1)
    print(n,"OUT")
ZigZag(3)    
 

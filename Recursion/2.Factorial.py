class Basics:
 # HL 4=4*3!
 # LL 3,2,1,<-0
  def Factorial(self,n):
    if(n==1):
        return 1
    return n*self.Factorial(n-1)
  # if i got power of 2^2 then I will also get 2^3
  # 2^3=2*2^2
  def Power(self,n,m):
     if(m==1):
        return n
     return n*self.Power(n,m-1)  
  def PowerArth(self,n,m):
     if(m==1):
        return n
     values= self.PowerArth(n,int(m/2))
     if(m%2==0):
        return values*values
     else:
        return values*values*n

     
obj=Basics()
print(obj.PowerArth(4,3)) 
class Solution:
    def mySqrt(self, x):
        if(0<=x<1):
            return 0
        elif(1<=x<4):
            return 1
        
        for t in range(x//2+1):
           if(t*t==x):
               return t
           if (t*t<x) and ((t+1)*(t+1)>x):
               return t


k=Solution()
t=[x*2 for x in range(2,23,3)]
v=[k.mySqrt(i) for i in t]

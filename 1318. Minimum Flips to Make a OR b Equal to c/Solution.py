% error in test case with values [5,2,8] --> solution points at a result of 4 bit flips but upon manual calculation it is noted that 1 bit flip is enough 
from math import *

class Solution:
    def minFlips(self, a, b, c):
        l=[a,b,c]
        l.sort()
        if(l[0]+l[1]==l[2]) and l[0]!=a:
            return l[0]
        if(a!=b and b!=c and a!=c):
            s=c-(b+a)
            return abs(s)
        else:
            if(a==b==c):
                return 0
            if(a==b or b==c or c==a):
                return 1
    pass




k=Solution()
t=[[1,2,3],[4,5,9],[2,4,7],[7,7,7],[1,1,2],[1,2,1],[2,6,5],[5,3,8]]
v=[k.minFlips(i[0],i[1],i[2]) for i in t]

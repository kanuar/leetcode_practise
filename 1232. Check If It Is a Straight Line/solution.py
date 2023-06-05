from math import *
class Solution:
    def checkStraightLine(self, coordinates):
        global flag;
        flag=0;
        def slope_intercept(x1,x2):
            try:
                m=(x1[1]-x2[1])/(x1[0]-x2[0])
                c=ceil(x1[1]-m*x1[0])
            except ZeroDivisionError:
                m=0
                c=x1[0]
                global flag
                flag=1
                
            return [m,c]
        
        def linecheck(line,point):
            m,c=line
            if(flag):
                return c==point[0]
            else:
                x,y=point
                return y==ceil(m*x+c)
            
        line=slope_intercept(coordinates[0],coordinates[1])
        for i in coordinates[2:]:
            k=linecheck(line,i)
            if not(k):
                return False
        return True

        

l1=[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
l2=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
l3=[[0,0],[0,1],[0,-1]]
k=Solution()
val1=k.checkStraightLine(l1)
val2=k.checkStraightLine(l2)
val3=k.checkStraightLine(l3)


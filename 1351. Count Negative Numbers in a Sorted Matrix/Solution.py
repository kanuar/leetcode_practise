class Solution:
    def countNegatives(self, grid) :
        k=[[x for x in i if x<0] for i in grid]
        k=sum([len(i) for i in k])
        return k

k=Solution()
t=  [[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    [[3,2],[1,0]]]
v=[k.countNegatives(i) for i in t]
print(v)

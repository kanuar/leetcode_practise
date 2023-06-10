class Solution:
    def plusOne(self, digits) :
        def inc(l):
            if l:
                if l[-1]==9:
                    return inc(l[:-1])+[0]
                else:
                    return l[:-1]+[l[-1]+1]
            else:
                return [1]
            
        return inc(digits)

k=Solution()
t=[[4,2,6],[6,1,1],[5,2,9],[3,2,8],[9,3,6],[0],[9,9,9]]
v=[k.plusOne(i) for i in t]

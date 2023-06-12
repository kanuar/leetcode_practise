class Solution:
    def summaryRanges(self, nums):
        r=[]
        if not nums:
            return nums
        a=nums[0]
        b=nums[0]
        for i in nums[1:]:
            if i==b+1:
                b=i
            else:
                if a==b:
                    s=str(a)
                    r.append(s)
                else:
                    s=str(a)+'->'+str(b)
                    r.append(s)
                a=i
                b=i
        if a==b:
            s=str(a)
            r.append(s)
        else:
            s=str(a)+'->'+str(b)
            r.append(s)
        return r

k=Solution()
s=k.summaryRanges
t=[[0,1,2,4,5,7],
   [0,2,3,4,6,8,9],
   [0,5,9]]
t1=[[j for j in i] for i in t]
v=[s(i) for i in t]

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

class Solution:
    def removeElement(self, nums, val) :
        k=len(nums)
        t=[]
        for i in nums:
            if i==val:
                pass
            else:
                t.append(i)
        for j in range(len(t)):
            nums[j]=t[j]
        return len(t)

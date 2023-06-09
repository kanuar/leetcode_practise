class Solution:
    def searchInsert(self, nums, target):
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        if len(nums)==1:
            
            if target>nums[0]:
                return 1
            return 0
        l=0
        u=len(nums)-1
        r=u+l
        r//=2
        while u>l:
            if nums[r]==target:
                return r
            elif nums[r]<target:
                l=r+1
            else:
                u=r-1     
            r=(u+l)//2
        if(nums[r]>=target):
            return r
        else:
            return r+1
        return r
    

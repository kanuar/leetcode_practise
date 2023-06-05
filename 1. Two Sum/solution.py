class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            k=nums[i]
            n=target-k
            if (n in nums) and (n!=k):
                j=nums.index(n)
                return [i,j] 
                
            elif(n==k):
                try:
                    j=nums.index(n,i+1)
                    return [i,j] 
                except ValueError:
                    continue
            pass
        pass
    pass


l1=[2,7,11,15]
t1=9
l2=[3,2,4]
t2=6
l3=[3,3]
t3=6
l4=[2,5,5,11]
t4=10
k=Solution()
val1=k.twoSum(l1,t1)
val2=k.twoSum(l2,t2)
val3=k.twoSum(l3,t3)
val4=k.twoSum(l4,t4)

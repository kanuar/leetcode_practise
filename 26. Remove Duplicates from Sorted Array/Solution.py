class Solution:
    def removeDuplicates(self, nums):
        k=[]
        for i in nums:
            if i not in k:
                k.append(i)
                pass
            pass
        n=len(k)
        for i in range(n):
            nums[i]=k[i]
        
        return n

k=Solution()
t=[[0,1,1,1,2,3,4,4,5,6,7],[1,1,2,3,4,5,6,8,8,8,9],[1,2,3,4,5]]
v=[k.removeDuplicates(i) for i in t]

for i in range(len(v)):
    print(t[i][:v[i]])

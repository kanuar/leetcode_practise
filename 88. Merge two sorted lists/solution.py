class Solution:
    def merge(self, nums1, m, nums2, n ):
        k=[]
        l1=nums1[:m]
        l2=list(nums2)
        while l1 and l2:
            if l1[0]<l2[0]:
                k.append(l1.pop(0))
            elif l1[0]>l2[0]:
                k.append(l2.pop(0))
            else:
                k.append(l1.pop(0))
                k.append(l2.pop(0))
        if l1:
            k.extend(l1)
        else:
            k.extend(l2)
        for i in range(len(nums1)):
            nums1[i]=k.pop(0)

t=[[[1,2,4,0,0,0],[3,5,6]],
   [[1,2,3,0,0,0],[2,5,6]],
   [[0],[1]]]
k=Solution()
for i in t:
    print(i[0],i[1])
    k.merge(i[0],i[0].index(0),i[1],len(i[1]))
    print(i[0])
    print()

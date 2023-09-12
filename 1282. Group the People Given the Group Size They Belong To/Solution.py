class Solution:
    def groupThePeople(self,l):
        group=[]
        temp=[]
        d={}
        for i in range(len(l)):
            if(l[i]not in d):
                d[l[i]]=[i]
            else:
                d[l[i]].append(i)
        for i in d:
            temp=d[i]
            k=len(d[i])
            if i==k:
                group.append(temp)
            else:
                temp1=[temp[x:x+i] for x in range(k//i)]
                group.extend(temp1)
        return group
    pass

k=Solution()
test=[[2,1,3,3,3,2],[3,3,3,3,3,1,3]]
v=[k.groupThePeople(i) for i in test]
print(v)

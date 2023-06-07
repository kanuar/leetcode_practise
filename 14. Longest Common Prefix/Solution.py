class Solution:
    def longestCommonPrefix(self, strs):
        def smallest(s):
            k=[len(x) for x in s]
            k.sort()
            return [x for x in sorted(s) if(len(x)==k[0])][0]
            
        sub=smallest(strs)
        w=''
        c=0
        flag=1
        for i in range(len(sub)):
            k=sub[i]
            for j in strs:
                if(flag==0):
                    break
                else:
                    if(k==j[c]):
                        pass
                    else:
                        flag=0
                        break
                    pass
                pass
            if(flag==0):
                return sub[:c]
            else:
                c+=1
        return sub[:c]

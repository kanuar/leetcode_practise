class Solution:
    def romanToInt(self, s):
        s=s.upper()
        n=0
        flag=0
        d={'I' : 1,'V' : 5,'X' : 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000}
        if(len(s)>1):
            for i in range(len(s)-1):
                if(flag==1):
                    flag=0
                    continue
                if(d[s[i+1]]>d[s[i]]) :
                    n+=d[s[i+1]]-d[s[i]]
                    flag=1
                    continue
                
                    if(i==len(s)):
                        return n
                    pass
                else:
                    n+=d[s[i]]
                    pass
                pass
            if(d[s[-1]]>d[s[-2]]):
                return n
            else:
                return n+d[s[-1]]
        else:
            return d[s[-1]]

        
        
k=Solution()
v1='II'
v2='XXVII'
val1=k.romanToInt(v1)
val2=k.romanToInt(v2)

v3="MCMXCIV"
val3=k.romanToInt(v3)

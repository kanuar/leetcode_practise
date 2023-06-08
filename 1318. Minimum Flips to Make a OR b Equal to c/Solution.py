class Solution:
    def minFlips(self, a,b,c):
        k=len(bin(max(a,b,c)))-2

        a=bin(a)[2:]
        b=bin(b)[2:]
        c=bin(c)[2:]
        ka=k-len(a)
        kb=k-len(b)
        kc=k-len(c)
        a='0'*ka+a
        b='0'*kb+b
        c='0'*kc+c
        count=0
        for i in range(k):
            x=int(a[i])
            y=int(b[i])
            z=int(c[i])
            if(x|y!=z):
                count+=1
                if(x==y==1):
                    count+=1
                    pass
                pass
            pass
        return count
    pass


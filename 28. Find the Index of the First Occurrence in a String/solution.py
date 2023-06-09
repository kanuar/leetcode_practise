class Solution:
    def strStr(self, haystack, needle):
        k=0
        z=haystack.split(needle)
        if len(z)==1:
            return -1
        for i in haystack.split(needle):
            if i=='':
                return k
            else:
                k+=len(i)
        for i in range(len(haystack)-len(needle)):
            sub=haystack[i:i+len(needle)]
            if sub==needle:
                return i
k=Solution()
t=[['hello','ll'],
   ['abcdd','abd'],
   ['xbfsie','sie']]

v=[k.strStr(i[0],i[1]) for i in t]

class Solution:
    def longestPalindrome(self, s):
        for i in range(len(s),-1,-1):
            for j in range(len(s)-i+1):
                sub=s[j:i+j]
                if sub[::-1]==sub:
                    return sub
        return ''
    pass

k=Solution()
t=['abba','abcd','aba','babad','badab']
v=[k.longestPalindrome(i) for i in t]

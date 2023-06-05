class Solution:
    def isPalindrome(self, x):
        return str(x)[::-1]==str(x)
    pass

k=Solution()
t1=121
t2=-121
val1=k.isPalindrome(t1)
val2=k.isPalindrome(t2)

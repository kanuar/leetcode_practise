class Solution:
    def lengthOfLastWord(self, s) :
        return len(s.split()[-1])
    pass
pass
k=Soltion()
t=['hello world', 'good morning']
v=[k.lengthOfLastWord(i) for i in t]

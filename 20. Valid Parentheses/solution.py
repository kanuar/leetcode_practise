class Solution:
    def isValid(self, s) :
        if(len(s)%2==1):
            return False

        d={'{':'}',
           '(':')',
           '[':']'}
        stk=''
        if(s[0] not in d.keys()) or (s[-1] not in d.values()):
            return False
        for i in s:
            try:
                if i in d:
                    stk+=i
                    pass
                else:
                    if i!=d[stk[-1]]:
                        return False
                    else:
                        stk=stk[:-1]
                        pass
                    pass
                pass
            except IndexError:
                return False
            except KeyError:
                return False
        return len(stk)==0

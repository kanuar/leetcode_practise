class Solution:
    def isIsomorphic(self, s, t) :
        da={}
        db={}
        if(len(s)!=len(t)):
            return False
        
        for i in s:
            if i in da:
                da[i]+=1
            else:
                da[i]=1
        
        for i in t:
            if i in db:
                db[i]+=1
            else:
                db[i]=1

        if(len(da)!=len(db)) or (sorted(list(da.values()))!=sorted(list(db.values()))):
            return False
        else:
            for i in range(len(s)):
                ls=s.split(s[i])
                lt=t.split(t[i])
                ks=len(ls)
                kt=len(lt)
                if ks!=kt:
                    return False
                else:
                    t1=[len(x) for x in ls]
                    t2=[len(x) for x in lt]
                    if t1!=t2:
                        return False
                pass
            return True

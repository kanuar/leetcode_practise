class Solution:
    def canMakeArithmeticProgression(self, arr):
        def gen(arr):
            a,b,c=arr
            d1=b-a
            d2=c-b
            if(d1==d2):
                d=d1
            else:
                d=0
            return a,d
        
        arr.sort()
        if(len(set(arr))==1):
            return True
        if(len(arr)>=3):
            test=arr[:3]
            arr=arr[3:]
            a,d=gen(test)
            if(d==0):
                return False
            else :
                a+=2*d
                for i in arr:
                    if(a+d==i):
                        a+=d
                    else:
                        return False
                    pass
                pass
            return True
        else:
            return True
    pass

t0=[0,0,0,0]
t1=[1,2,4]
t2=[1,2,3]
t3=[1,3,5]
t4=[x for x in range(2,15,3)]
t5=[3*x for x in range(2,15,3)]
t6=[3**x for x in range(2,15,3)]
t7=[1]
t8=[1,100]
k=Solution()
t=[t0,t1,t2,t3,t4,t5,t6,t7,t8]
v=[k.canMakeArithmeticProgression(i) for i in t]

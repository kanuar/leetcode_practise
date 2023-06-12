# Definition for singly-linked list.
class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        def lister(head):
            if head.next:
                return [head.val]+lister(head.next)
            else:
                return [head.val]
        def noder(l):
            if l:
                t=ListNode()
                t.val=l.pop(0)
                t.next=noder(l)
                return t
        k1=lister(l1)
        k2=lister(l2)
        n1=len(k1)
        n2=len(k2)
        if n1>n2:
            k2+=[0]*(n1-n2)
        else:
            k1+=[0]*(n2-n1)
        
        k=[]
        for i in range(len(k2)):
            s=k1[i]+k2[i]
            k.append(s)
        for i in range(len(k)-1):
            if k[i]>9:
                k[i]=k[i]%10
                k[i+1]+=1
        if k[-1]>=10:
            k[-1]-=10
            k.append(1)
        return noder(k)

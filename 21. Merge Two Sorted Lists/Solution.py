# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    k=ListNode()
    def mergeTwoLists(self, list1, list2):
        if not(list1):
            return list2
        elif not(list2):
            return list1
        elif not(list1) and not(list2):
            return None
        
        global k
        k=ListNode()
        c=ListNode()
        k.next=c
        while list1 and list2:
            if list1.val<list2.val:
                c.val=list1.val
                c.next=ListNode()
                c=c.next
                list1=list1.next
            elif list2.val<list1.val:
                c.val=list2.val
                c.next=ListNode()
                c=c.next
                list2=list2.next
            elif list1.val==list2.val:
                c.val=list1.val
                c.next=ListNode()
                c=c.next
                c.val=list2.val
                c.next=ListNode()
                c=c.next
                list1=list1.next
                list2=list2.next

        if list1:
            c.val=list1.val
            c.next=list1.next
            return k.next
        
        elif list2:
            c.val=list2.val
            c.next=list2.next
            return k.next
        
        k=k.next
        d=k
        while k.next.next:
            k=k.next
        k.next=None
        return d

def disp(s):
    try:
        if(s.next):
            print(s.val,end='-->')
            disp(s.next)
        elif s:
            print(s.val)
    except AttributeError:
        print()
        

test=Solution()

l1=ListNode()
l1.val=1
l1.next=ListNode()
l1.next.val=2

l2=ListNode()
l2.val=1
l2.next=ListNode()
l2.next.val=2

k1=ListNode()
k1.val=2

k2=ListNode()
k2.val=1
t=[[l1,l2],
   [None,ListNode()],
   [None,None],
   [k1,k2]]

v=[test.mergeTwoLists(i[0],i[1]) for i in t]
for i in v:
    disp(i)

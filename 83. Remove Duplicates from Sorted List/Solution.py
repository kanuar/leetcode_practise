## Definition for singly-linked list.
#  class ListNode:
#      def __init__(self, val=0, next=None):
#          self.val = val
        #  self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        def lister(head):
            if head.next:
                print(head.val,end='-->')
                return [head.val] + lister(head.next)
            else:
                print(head.val)
                return [head.val]
        l=lister(head)
        print(l)
        k=[]
        for i in l:
            if i not in k:
                k.append(i)
        c=ListNode()
        head=c
        for i in k:
            c.val=i
            c.next=ListNode()
            c=c.next
        c=head
        while c.next.next:
            c=c.next
        c.next=None
        return head
    pass

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        preH = ListNode()
        
        p = preH
        
        while l1 or l2:
            if not l1:
                p.next = l2
                l2 = l2.next
            elif not l2:
                p.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
            
        return preH.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        currH = head
        
        while head.next:
            p = head.next
            head.next = p.next
            p.next = currH
            currH = p
            
        return currH
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        p = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return p
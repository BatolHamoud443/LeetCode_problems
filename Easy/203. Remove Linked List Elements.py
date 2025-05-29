# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        s = head
        p  = []
        while s:
            if s.val != val:
                p.append(s.val)
            s = s.next

        if not p:  
            return None
        
        head = ListNode(p[0])
        current = head
        
        for value in p[1:]:  
            current.next = ListNode(value)  
            current = current.next  
            
        return head
        

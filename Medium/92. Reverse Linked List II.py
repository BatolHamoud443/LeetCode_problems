# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        s = head
        p  = []
        while s:
            p.append(s.val)
            s = s.next
        a = p[:left-1] + p[left-1:right][::-1] + p[right:]
        if not a:  
            return None
        
        head = ListNode(a[0])
        current = head
        
        for value in a[1:]:  
            current.next = ListNode(value)  
            current = current.next  
            
        return head

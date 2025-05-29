# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = e = head
        while e and e.next:
            s = s.next
            e = e.next.next
            if s == e:
                return True
        return False
        

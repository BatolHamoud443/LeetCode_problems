# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            new_node = cur.next.next
            second = cur.next
            second.next = cur
            cur.next = new_node
            prev.next = second
            prev = cur
            cur = new_node
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, greater = ListNode(), ListNode()
        p_1, p_2 = less, greater 

        while head:
            if head.val < x:
                p_1.next = head
                p_1 = p_1.next
            else:
                p_2.next = head
                p_2 = p_2.next

            head = head.next

        p_1.next = greater.next
        p_2.next = None 

        return less.next

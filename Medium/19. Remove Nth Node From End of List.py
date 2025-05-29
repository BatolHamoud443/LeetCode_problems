# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        def remove_nth_from_end(head, n):
            if n <= 0:
                return head
            
            if n == 1:
                return head.next
            
            current = head
            for _ in range(n - 2):
                if current is None:
                    return head 
                current = current.next

            if current is None or current.next is None:
                return head 
    
            current.next = current.next.next
            return head

        def reverse_and_remove(head, n):
        
            head = reverse_list(head)
            print(head)
           
            head = remove_nth_from_end(head, n)
            
            head = reverse_list(head)
            
            return head

    
        new_head = reverse_and_remove(head, n)

    
        return new_head

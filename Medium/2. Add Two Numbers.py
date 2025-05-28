# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        i = 0
        j = 0
        out = ListNode(0)
        output = out
        while l1:
            n1 += l1.val*(10**i)
            l1 = l1.next
            i +=1
        while l2:
            n2 += l2.val*(10**j)
            l2 = l2.next
            j +=1
        n = n1+n2
        output.next = ListNode(n%10)
        output = output.next
        while n >= 10:
           n = n//10
           output.next = ListNode(n%10)
           output = output.next
        return out.next
        


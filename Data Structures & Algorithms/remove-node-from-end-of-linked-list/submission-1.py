# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        length = 0
        temp = head

        while temp:
            length+=1
            temp = temp.next
        
        ix = length-n
        if ix == 0:
            return head.next
        prev = None
        curr = head
        i = 0
        while i<ix:
            i+=1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        
        return head
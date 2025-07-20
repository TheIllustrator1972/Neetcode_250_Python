# Iterative Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# Recursive Approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        nextHead = head
        if head.next:
            nextHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        return nextHead

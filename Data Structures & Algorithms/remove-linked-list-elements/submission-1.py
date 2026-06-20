# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        """
            create a dummy value and dummy.next is head 

            loop and see if the next value is the target 

            curr.next = curr.next.next
        """
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy

        while curr.next:
            print(curr.val)
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        # loop through the array and get the length 
        counter = 0 
        curr = head
        while curr:
            counter = counter + 1
            curr = curr.next

        # get the middle element
        middle = counter//2
        new_counter = 0
            
        curr2 = head

        while curr2:
            if new_counter == middle:
                return curr2
            curr2 = curr2.next
            new_counter = new_counter + 1
            
        
        
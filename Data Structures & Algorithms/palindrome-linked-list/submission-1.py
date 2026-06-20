# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        """
            find the fast and slow pointer and find the middle 
        """

        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # now slow is pointing to the middle of the linkedlist
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
            

        # now prev contains the mid element 

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


        
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        """ 

            create a list - push the elements to the list

            do two pointer techique on the list
        """
        

        res = list()
        curr = head
        if not curr:
            return res
        while curr:
            res.append(curr.val)
            curr = curr.next
        

        # palindrme check 
        start = 0
        end = len(res)-1
        while start < end:
            if res[start] == res[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

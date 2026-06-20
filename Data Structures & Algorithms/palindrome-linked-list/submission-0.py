# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {


        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        ListNode pointer = head;
        int counter = 0;
        while(pointer != null) {
            counter++;
            pointer = pointer.next;
        }

        // get the difference
        int elementCounter = counter - n;
        pointer = dummy;


        for(int i=0;i<elementCounter;i++) {
            pointer = pointer.next;
        }

        pointer.next = pointer.next.next;
        // loop through the list again 


        return dummy.next;
    }
}

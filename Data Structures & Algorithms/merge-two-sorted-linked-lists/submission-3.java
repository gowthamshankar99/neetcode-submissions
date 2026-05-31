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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // result list 
        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;

        while(list1 != null && list2 != null) {
            if(list1.val > list2.val) {
                tail.next = list2;
                tail = tail.next;

                // increment list2
                list2 = list2.next;
            } else {
                tail.next = list1;
                tail = tail.next;

                // increment list2
                list1 = list1.next;                
            }
        }

        // if values are present after iteration 
        if(list1 != null) {
            tail.next = list1;
        }

        if(list2 != null) {
            tail.next = list2;
        }

        return dummy.next;
        
    }
}


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

class Solution3 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;

        while(list1 != null && list2 != null) {

            if(list1.val > list2.val) {
                tail.next = list2;
                list2 = list2.next;
            } else {
                tail.next = list1;
                list1 = list1.next;
            }

            tail = tail.next;
        }

        if(list2 != null) { 
            tail.next = list2;
        }

        if(list1 != null) {
            tail.next = list1;
        }


        return dummy.next;
    }
}
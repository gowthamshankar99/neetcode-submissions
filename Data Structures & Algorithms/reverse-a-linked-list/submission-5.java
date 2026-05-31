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

    public ListNode reverseList(ListNode head) {

        ListNode prev = null;
        ListNode curr = head;

        while(curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            
        }

        return prev;
    }

    public ListNode reverseList2(ListNode head) {



        Stack<Integer> stack = new Stack<Integer>();

        while(head != null) {
            ListNode node = head;
            stack.add(node.val);
            head = head.next;
        }

        ListNode dummy = new ListNode(-1);
        head = dummy;        

        // pop from the stack and add to dummy node 

        while(!stack.isEmpty()) {
            int val = stack.pop();
            ListNode node = new ListNode(val);
            head.next = node;
            head = head.next;
        }

        return dummy.next;
    }
}

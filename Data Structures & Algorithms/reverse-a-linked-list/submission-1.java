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


        Stack<ListNode> stack = new Stack<ListNode>();
        // create a stack and push the element to the stack 
        while(head != null) {
            stack.push(head);
            head = head.next;
        }


        ListNode dummy = new ListNode(-1);
        head = dummy;

        // pop it up from the stack and form the linkedlist
        while(!stack.isEmpty()) {
            ListNode node = stack.pop();
            ListNode newnode = new ListNode(node.val);

            head.next = newnode;
            head = head.next;
        }


        return dummy.next;
    }
}

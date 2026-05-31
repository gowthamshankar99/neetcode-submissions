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

        // Create Stack 
        Stack<ListNode> stack = new Stack<ListNode>();

        while(head!=null) {
            stack.push(head);
            head  = head.next;
        }

        ListNode dummy = new ListNode(-1);
        head = dummy;
        while(!stack.isEmpty()) {
            ListNode node = stack.pop();
            head.next = new ListNode(node.val);
            head = head.next;
        }

        return dummy.next;
    }
}

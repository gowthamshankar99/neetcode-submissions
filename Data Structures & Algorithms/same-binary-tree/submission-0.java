/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) {
            System.out.println("loop 1");
            return true;
        }

        if(p == null || q == null) {
            System.out.println("loop 2");
            return false;
        }
        if(p.val != q.val) {
            System.out.println("loop 3");
            return false;
        }
           
        
        boolean val1 = isSameTree(p.left, q.left);
        boolean val2 = isSameTree(p.right, q.right);

        if(val1 == true && val2 == true) {
            return true;
        } 
        return false;

    }
}

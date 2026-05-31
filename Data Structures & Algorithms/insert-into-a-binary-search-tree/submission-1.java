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
    public TreeNode insertIntoBST(TreeNode root, int val) {

        if(root == null) {
            TreeNode node = new TreeNode(val);
            return node;
        }

        // if(root.left == null && val < root.val) {
        //     TreeNode leftNode = new TreeNode(val);
        //     root.left = leftNode;
        // }

        // if(root.right == null && val > root.val) {
        //     TreeNode rightNode = new TreeNode(val);
        //     root.right = rightNode;
        // }

         if(val > root.val) {
            root.right = insertIntoBST(root.right, val);
         } else if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
         }

         return root;
        
    }
}
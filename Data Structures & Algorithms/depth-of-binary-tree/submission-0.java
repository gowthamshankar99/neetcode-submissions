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
    public int maxDepth(TreeNode root) {
        List<List<TreeNode>> depth = new ArrayList<>();
        if(root == null) {
            return depth.size();
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            int size = queue.size();
            List<TreeNode> list = new ArrayList<>();
            for(int i=0;i<size;i++) {
                TreeNode node = queue.poll();
                if(node.left != null) {
                    list.add(node.left);
                    queue.add(node.left);
                }
                if(node.right != null) {
                    list.add(node.right);
                    queue.add(node.right);
                }
            }
            depth.add(list);
            
        }

        return depth.size();
    }
}

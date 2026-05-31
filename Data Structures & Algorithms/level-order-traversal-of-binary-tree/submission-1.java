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
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        // we have the root - get the root 

        // push the root to list 

        // push the left and right of the root to the queue ...

        // if there is a value in the queue - get the value -> if thee is left and right push that to the queue 


        List<List<Integer>> result = new ArrayList<>();
        if(root == null)
            return result;

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        result.add(new ArrayList<>(List.of(root.val)));
        while(!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> list = new ArrayList<>();

            for(int i=0;i<size;i++) {
                TreeNode node = queue.poll();
                if(node.left != null) {
                    queue.add(node.left);
                    list.add(node.left.val);
                }

                if(node.right != null) {
                    queue.add(node.right);
                    list.add(node.right.val);
                }
            }
            if(list.size() != 0)        
                result.add(list);   
        }
        return result;
    }
}

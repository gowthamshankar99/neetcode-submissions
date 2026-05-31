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
        
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(root == null)
            return result;

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        

        // add the first element 
        result.add(new ArrayList<Integer>(List.of(root.val)));
        
        List<Integer> list = null;

        while(!queue.isEmpty()) {

            // get the size of the queue
            int size = queue.size();
            list = new ArrayList<>();
            for(int i=0;i<size;i++) {
                TreeNode node = queue.poll();

                if(node.left != null) {
                    list.add(node.left.val);
                    queue.offer(node.left);
                } 
                if(node.right != null) {
                    list.add(node.right.val);
                    queue.offer(node.right);
                }
            }
            if(list.size() != 0)
                result.add(list);
        }



        return result;
    }
}

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        
        # Define a normal helper function for the min() key
        def get_distance(val):
            # Returns a tuple: (absolute distance, value itself for tie-breaking)
            return (abs(target - val), val)
        
        while root:
            # Update the closest value using the named function
            closest = min(root.val, closest, key=get_distance)
            
            # Move left or right based on the target value
            if target < root.val:
                root = root.left
            else:
                root = root.right
                
        return closest

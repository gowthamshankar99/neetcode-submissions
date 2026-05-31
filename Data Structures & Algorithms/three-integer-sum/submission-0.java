class Solution {
public static List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    Arrays.sort(nums);
    
    for (int i = 0; i < nums.length - 2; i++) {
        // Skip duplicates for i
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        
        // Early termination
        if (nums[i] > 0) break;
        
        int start = i + 1;
        int end = nums.length - 1;
        
        while (start < end) {
            int sum = nums[i] + nums[start] + nums[end];
            
            if (sum == 0) {
                result.add(Arrays.asList(nums[i], nums[start], nums[end]));
                
                // Skip duplicates for start and end
                while (start < end && nums[start] == nums[start + 1]) start++;
                while (start < end && nums[end] == nums[end - 1]) end--;
                
                start++;
                end--;
            } else if (sum < 0) {
                start++;
            } else {
                end--;
            }
        }
    }
    
    return result;
}
}

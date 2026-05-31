class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i=0;i<nums.length;i++) {
            map.put(nums[i], i);
        }
        
        for(int j=0;j<nums.length;j++) {
            int num = nums[j];  // 4
            int diff = target - num; // 2
        	if (map.containsKey(diff) && j != map.get(diff)) {
        		return new int[]{j, map.get(diff)};
        	}
        }
        return new int[] {};
    }
}




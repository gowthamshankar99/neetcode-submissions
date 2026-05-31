class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new TreeSet<Integer>();

        for(int num : nums) {
            set.add(num);
        }
        int temp = 0;
        for(int s: set) {
            nums[temp] = s;
            temp++;
        }

        // set.size = 3 nums.length = 5 

        // int difference = 2 

        for(int i=set.size();i<nums.length;i++) {
            nums[i] = 0;
        }

        return set.size();
    }
}
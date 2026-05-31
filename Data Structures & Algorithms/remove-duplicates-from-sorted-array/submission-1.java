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

        for(int i=set.size();i<nums.length;i++) {
            nums[i] = 0;
        }

        return set.size();
    }
}
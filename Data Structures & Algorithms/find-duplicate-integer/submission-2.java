class Solution {
    public int findDuplicate(int[] nums) {

        // create a set 

        Set<Integer> set = new HashSet<Integer>();

        for(int num : nums) {
            if(set.contains(num))
                return num;
            else {
                set.add(num);
            }
        }
        return -1;
    }

    public int findDuplicate3(int[] nums) {

        // sort the array

        Arrays.sort(nums);

        int currentNumber = nums[0];
        for(int i=1;i<nums.length;i++) {
            if(currentNumber == nums[i])
                return currentNumber;
            else {
                currentNumber = nums[i];
            }
        }

        return -1; // will never return this
    }    
}

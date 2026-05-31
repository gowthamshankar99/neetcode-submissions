class Solution {
    public static int longestConsecutive(int[] nums) {


        if(nums.length == 0) {
            return 0;
        }


        // sort the array
        Arrays.sort(nums);

        int counter = 0;
        int maxCounter = 0;
        // loop through the array
        for(int i=1;i<nums.length;i++) {
            //System.out.println(nums[i]);
            // check if the next element is +1 of the previous element
            if((nums[i-1] == nums[i]-1)) {
                // increment the counter
                counter++;
                // check if its more than the max value - if it is - then replace the max value
                if(maxCounter < counter) {
                    maxCounter = counter;
                }
            } else if(nums[i-1] == nums[i]) {
                continue;
            }
            else {
                counter = 0;
            }
        }
        return maxCounter+1;
    }
}

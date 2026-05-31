class Solution {
    public void moveZeroes(int[] nums) {
        
        int currentpointer = 0;

        // loop through the array 
        /**
            if you find a non zero value 

            put it at the current pointer

            inceement the point 

            do another loop and start zeros from 1 after the pointer
        **/


        for(int i=0;i<nums.length;i++) {
            if(nums[i] != 0) {
                nums[currentpointer] = nums[i];
                currentpointer++;
            }
        }

        for(int i=currentpointer;i<nums.length;i++) {
            nums[i] = 0;
        }
     }
}
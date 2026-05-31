class Solution {
    public int[] productExceptSelf(int[] nums) {

        // result 
        int[] result = new int[nums.length];
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];

        int counter = 0;
        for(int i=0;i<nums.length;i++) {
            counter = i-1;
            int value = 1;
            while(counter >= 0) {
                value = value * nums[counter];
                counter--;
            }
            left[i] = value; 
        }

        // right 

        for(int i=0;i<nums.length;i++) { // 1
            counter = i+1;
            int value = 1;
            while(counter <= nums.length-1) { // 
                value = value * nums[counter];
                counter++; 
            }
            right[i] = value; 
        }
        
        // combine both left and right 

        for(int i=0;i<nums.length;i++) {
            result[i] = left[i] * right[i];
        }

        return result;
    }
}  


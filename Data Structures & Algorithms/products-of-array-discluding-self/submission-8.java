class Solution {


    public int[] productExceptSelf(int[] nums) {

        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] result = new int[nums.length];


        left[0]  = 1;
        right[nums.length-1] = 1;

         // left 

         for(int i=1;i<nums.length;i++) {
            left[i] = left[i-1] * nums[i-1];
         }       

         // right

         for(int i=nums.length-2;i>=0;i--) {
            right[i] = right[i+1] * nums[i+1];
         }                

        for(int i=0;i<nums.length;i++) {
            result[i] = left[i] * right[i];
        }

        return result;


    }

    public int[] productExceptSelf2(int[] nums) {

        /**
            [1,2,4,6]

            [1,1,2,8]

            [48,24,6,1]

            [48,24,12,8]

        **/

        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] result = new int[nums.length];


        int counter = 0;
        for(int i=0;i<nums.length;i++) {
            counter = i-1;
            int value = 1;
            while(counter>=0) {
                value = nums[counter] * value;
                counter--;
            }
            left[i] = value;
        }


        for(int i=0;i<nums.length;i++) {
            counter = i+1;
            int value = 1;
            while(counter<nums.length) {
                value = value * nums[counter];
                counter++;
            }

            right[i] = value;
        }

        for(int i=0;i<nums.length;i++) {
            result[i] = left[i] * right[i];
        }

        return result;
    }
}  


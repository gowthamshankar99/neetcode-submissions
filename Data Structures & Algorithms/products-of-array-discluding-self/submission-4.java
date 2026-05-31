class Solution {
    public int[] productExceptSelf(int[] nums) {

        /**
            [1,2,4,6]

            [1,1,2,8]

            [48,24,6,1]

            [48,24,12,8]

        **/

        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] result = new int[nums.length];


        for(int i=0;i<nums.length;i++) {
            int temp = i;
            int value = 1;
            while(temp>0) {
                temp--;
                value = value * nums[temp];
            }
            
            left[i] = value;
        }

        for(int n : left) {
            System.out.println(n);
        }

        for(int i=0;i<nums.length;i++) {
            int temp = i+1;
            int value = 1;
            while(temp<nums.length) {
                value = value * nums[temp];
                temp++;
            }

            right[i] = value;
        }

        for(int n : right) {
            System.out.println(n);
        }

        for(int i=0;i<nums.length;i++) {
            result[i] = left[i] * right[i];
        }

        return result;
    }
}  


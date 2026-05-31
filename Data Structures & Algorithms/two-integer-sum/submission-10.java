class Solution {
    public int[] twoSum(int[] nums, int target) {
        

        // use a hashmap

        /**

            loop through array 

            for each value get the difference and see if the difference is there in the map - if not 

            push the value. 

            if the difference exist - return the indices

            
        **/


        Map<Integer, Integer> map = new HashMap<>();

        for(int i=0;i<nums.length;i++) {
            // get the difference 
            int difference = target - nums[i];  // 4
            if(map.containsKey(difference)) {   
                // get the target 
                return new int[]{map.get(difference), i}; // 
                //return new int[]{i, map.get(difference)}; // 
            } else {
                map.put(nums[i], i);
            }
        }


        // for(int i=0;i<nums.length;i++) {
        //     for(int j=i+1;j<nums.length;j++) {
        //         if(nums[i]+nums[j] == target) {
        //             return new int[]{i,j};
        //         }
        //     }
        // }

        return new int[]{-1,-1};

}
}

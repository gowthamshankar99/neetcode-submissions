class Solution {
public static List<List<Integer>> threeSum(int[] nums) {

        // sort the array 

        // for a loop 

        // start = i+1

        // end = end 

        /***

        [-1,0,1,2,-1,-4]

        [-4,-1,-1,0,1,2]

        i = -4
        start = -1
        end = 2

        end--

        start++
        **/

        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);

        for(int i=0;i<nums.length;i++) {
            if (i>0 && nums[i] == nums[i-1]) continue;
            int start = i+1;
            int end = nums.length-1;
            while(start < end) {
                if(nums[i] + nums[start] + nums[end] == 0) {
                    list.add(new ArrayList<>(List.of(nums[i], nums[start], nums[end])));
                    while(start < end && nums[start] == nums[start+1]) start++;
                    while(start < end && nums[end] == nums[end-1]) end--;
                    start++;
                    end--;
                } else if(nums[i] + nums[start] + nums[end] > 0) {
                    end--;
                }
                else {
                    start++;
                }                    
            }
        }

        return list;
    }
}

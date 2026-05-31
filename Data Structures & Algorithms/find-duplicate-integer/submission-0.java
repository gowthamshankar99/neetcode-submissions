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
}

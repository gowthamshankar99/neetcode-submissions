class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        
        return recur(nums, target, start, end);
}
 
    public int recur(int[] nums, int target, int left, int right) {
        if(left > right)
            return -1;

        int mid = left + (right - left)/2;

        if(nums[mid] == target)
            return mid;
        else if(nums[mid] > target) {
            right = mid-1;
            return recur(nums, target, left, right);
        }else {
            left = mid+1;
            return recur(nums, target, left, right);
        }
    }

}


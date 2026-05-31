class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int i=0;i<matrix.length;i++) {
                boolean single = binarySearch(matrix[i], target, 0, matrix[i].length-1);
                if(single) {
                    return true;
                }
            }
            return false;
    }

    public boolean binarySearch(int[] nums, int target, int start, int end) {

        if(start>end) {
            return false;
        }
        int mid = start + (end - start) / 2; 
        if(target > nums[mid]) {
            start = mid+1;
            return binarySearch(nums, target, start,end);
        } else if(target < nums[mid]) {
            end=mid-1;
            return binarySearch(nums, target, start,end);
        } else  {
            return true;
        }
    }
 }

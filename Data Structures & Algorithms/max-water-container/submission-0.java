class Solution {
    public int maxArea(int[] heights) {
        int maxAreavar = 0;
        for(int i=0;i<heights.length;i++) {
            for(int j=i+1;j<heights.length;j++) {
                int bigger = Math.min(heights[i], heights[j]);
                int length = j-i;
                maxAreavar = Math.max(maxAreavar, bigger*length);
            }
        }

        return maxAreavar;
    }
}

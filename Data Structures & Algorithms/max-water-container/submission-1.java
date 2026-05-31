class Solution {
    // public int maxArea(int[] heights) {
    //     int maxAreavar = 0;
    //     for(int i=0;i<heights.length;i++) {
    //         for(int j=i+1;j<heights.length;j++) {
    //             int bigger = Math.min(heights[i], heights[j]);
    //             int length = j-i;
    //             maxAreavar = Math.max(maxAreavar, bigger*length);
    //         }
    //     }

    //     return maxAreavar;
    // }

    public int maxArea(int[] heights) {
        int maxAreavar = 0;
        int start = 0;
        int end = heights.length-1;
        while(start<end) {
            int currentArea = (Math.min(heights[start],heights[end])*(end-start));
            maxAreavar = Math.max(maxAreavar,currentArea);
            if(heights[start]<heights[end])
                start++;
            else
                end--;
            
        }
        return maxAreavar;
    }    
}

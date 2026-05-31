class Solution {
    public int[][] merge(int[][] intervals) {

        List<int[]> list = new ArrayList<>();
        // Sort the Array based on the first value 
        
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        int currentStart = intervals[0][0]; 
        int currentEnd = intervals[0][1];

        for(int i=1;i<intervals.length;i++) {
            if(currentEnd >= intervals[i][0]) { //overlap
                currentEnd = Math.max(intervals[i][1], currentEnd);
            } else {
                list.add(new int[]{currentStart, currentEnd});
                currentStart = intervals[i][0];
                currentEnd = intervals[i][1];
            }
        }

        list.add(new int[]{currentStart, currentEnd});
        return list.toArray(new int[list.size()][]);
        
    }
}


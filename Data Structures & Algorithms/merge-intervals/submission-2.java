class Solution {
    public int[][] merge(int[][] intervals) {

        /**

            [1,5] [1,10] -> [1,10]
            [1,3][2,5] = > [1,3]
            Sort the array 

            currentEnd > nextStart 
                nextEnd = Math.max(currentend, nextEnd);
            else {
                list.add(new int[]{})
            }

        **/

        Arrays.sort(intervals, (a,b) -> a[0] -b[0]);

        List<int[]> result = new ArrayList<>();
        int currentStart = intervals[0][0];
        int currentEnd = intervals[0][1];

        
        for(int i=1;i<intervals.length;i++) {
            int nextStart = intervals[i][0];
            int nextEnd = intervals[i][1];
            if(currentEnd >= nextStart) {  // overlap
                currentEnd = Math.max(currentEnd, nextEnd);
            } else {
                result.add(new int[]{currentStart, currentEnd});
                currentStart = nextStart;
                currentEnd = nextEnd;
            }

            }
            result.add(new int[]{currentStart, currentEnd});

            return result.toArray(new int[result.size()][]);
        }
        
    }



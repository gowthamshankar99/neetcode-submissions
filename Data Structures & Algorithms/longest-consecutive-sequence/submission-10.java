class Solution {
    public static int longestConsecutive(int[] nums) {
        // loop through the array and convert to set
        Set<Integer> set = new HashSet<>();
        for(int num: nums) {
            set.add(num);
        }

        int counter = 0;
        int maxCounter = 0;

        // loop through the elements
        for(int num: nums) {
            counter = 0;
            // see if the element is the start of the set
            if(!set.contains(num-1)) {// if its the start of the set
                // its the start of the set
                while(set.contains(num)) {
                    counter++;
                    if (counter > maxCounter) {
                        maxCounter = counter;
                    }
                    num++;
                }
            }
        }
        return maxCounter;
    }
}

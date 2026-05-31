class Solution {
    // public int[] dailyTemperatures(int[] temperatures) {
    //     // result array 
    //     int[] result = new int[temperatures.length];
    //     for(int i=0;i<temperatures.length;i++) {
    //         for(int j=i+1;j<temperatures.length;j++) {
    //             if(temperatures[j] > temperatures[i]) {
    //                 result[i] = j-i;
    //                 break;
    //             } 
    //         }
    //     }

    //     return result;
    // }

    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        Stack<int[]> stack = new Stack<>();
        // loop through the tempreture -
        for(int i=0;i<temperatures.length;i++) {
            if(stack.isEmpty()) {
                stack.push(new int[]{temperatures[i], i});
            } else {
                while(!stack.isEmpty() && stack.peek()[0] < temperatures[i]) {
                        int[] poppedValue = stack.pop();
                        int value = poppedValue[0];
                        int index = poppedValue[1];

                        // cal index value
                        int actualIndex = i - index;
                        result[index] = actualIndex;

                }
                stack.push(new int[]{temperatures[i], i});

            }
        }
        return result;
    }    
}

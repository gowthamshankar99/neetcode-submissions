class Solution {
    public int notOptimalmaxProfit(int[] prices) {
        int max = 0;
        for(int i=0;i<prices.length;i++) {
            for(int j=i+1;j<prices.length;j++) {
                if(prices[j] > prices[i])
                    max = Math.max(max, prices[j]-prices[i]);
            }
        }
        return max;
    }


    public int maxProfit(int[] prices) {

        int max = 0;
        if(prices.length < 2) {
            return max;
        }
        int start = 0;
        int end = 1;
        while(start<end) {
            if(prices[start] < prices[end]) {
                max = Math.max(max,prices[end]-prices[start]);
                end = end + 1;
            } else {
                start = end;
                end = end + 1;
            }

            if(end == prices.length){
                break;
            }
        }
        return max;

    }    
}

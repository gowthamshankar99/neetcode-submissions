class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int start = 0;
        int end = 1;

        while(end < prices.length) {
            if(prices[end] > prices[start]) {
                System.out.println(prices[start] + " " + prices[end]);
                int difference = prices[end] - prices[start];
                // calc max 
                max = Math.max(difference, max);
                end++;
            } else  {
                start = end;
                end++;
            }
        }

        return max;
    }
}

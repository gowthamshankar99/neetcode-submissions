class Solution {
    public int maxProfit(int[] prices) {
        int start = 0;
        int end = 1;
        int max = 0;
        while(end < prices.length) {
            if(prices[start] < prices[end]) {
                int difference = prices[end]-prices[start];
                max = Math.max(difference, max);
                end++;
            } else {
                start = end;
                end++;
            }
        }
        return max;
    }
}

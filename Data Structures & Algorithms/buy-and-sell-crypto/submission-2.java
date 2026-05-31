class Solution {
    public int maxProfit(int[] prices) {
        int start = 0;
        int end = 1;
        int maxPrice = 0;
        while(end < prices.length) {
            if(prices[start] > prices[end]) {
                start = end;
                end++;
            } else
            {
                maxPrice = Math.max(maxPrice, (prices[end]-prices[start]));
                end++;
            }
        }
        return maxPrice;
    }
}

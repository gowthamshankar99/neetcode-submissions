class Solution {
    public int lengthOfLongestSubstring(String s) {

        Set<Character> set = new HashSet<Character>();
        int max = 0;
        int temp = 0;

        for(int i=0;i<s.length();i++) {
            while(set.contains(s.charAt(i))) {
                set.remove(s.charAt(temp));
                temp++;
            }
            set.add(s.charAt(i));
            max = Math.max(max, set.size());
        }
        return max;
    }
}

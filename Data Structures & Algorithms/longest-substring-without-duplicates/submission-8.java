class Solution {
    public int lengthOfLongestSubstring(String s) {

        // set 

        
        int max = 0;

        for(int i=0;i<s.length();i++) {
            Set<Character> set = new HashSet<Character>();
            for(int j=i;j<s.length();j++) {
                if(set.contains(s.charAt(j))) {
                    break;
                } else {
                    set.add(s.charAt(j));
                }
                max = Math.max(max, set.size());
            }
        }
        return max;
    }
}

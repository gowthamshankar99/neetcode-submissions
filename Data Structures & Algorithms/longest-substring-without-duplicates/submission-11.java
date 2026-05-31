class Solution {

    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();

        int result = 0;
        int temp = 0;

        for(int i=0;i<s.length();i++) {
            while(set.contains(s.charAt(i))) {
                set.remove(s.charAt(temp));
                temp++;
            }

            set.add(s.charAt(i));
            result = Math.max(result, set.size());
        }

        return result;
        
    }


    public int lengthOfLongestSubstring2(String s) {

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

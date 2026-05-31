class Solution {
    public boolean isAnagram(String s, String t) {

        int[] alphabets = new int[26];

        for(int i=0;i<s.length();i++) {
            alphabets[s.charAt(i) - 'a'] = alphabets[s.charAt(i) - 'a'] + 1;
        }

        for(int i=0;i<t.length();i++) {
            alphabets[t.charAt(i) - 'a'] = alphabets[t.charAt(i) - 'a'] - 1;
        }
        
        for(int alp : alphabets) {
            if(alp != 0)
                return false;
        }

        return true;
    }

    public boolean test(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        
        //loop through String s
        for(int i=0;i<s.length();i++) {
            if(map.containsKey(s.charAt(i))) {
            	map.put(s.charAt(i), map.get(s.charAt(i)) + 1);
            } else {
            	map.put(s.charAt(i), 1);
            }
        }

        // loop through string t
        for(int j=0;j<t.length();j++) {
            if(map.containsKey(t.charAt(j))) {
            	map.put(t.charAt(j), map.get(t.charAt(j)) - 1);
            } else {
            	map.put(t.charAt(j), 1);
            }
        }
        
        
        
        for(Integer value : map.values()) {
        	if(value > 0)
        		return false;
        }
        
        return true;
    }

    
}
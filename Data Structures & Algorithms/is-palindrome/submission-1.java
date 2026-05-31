class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll(" ", "").toLowerCase();

        int len = s.length();
        int start = 0;
        int end = len-1;

        if(s.length() == 0)
            return true;

        

        while(start < end) {
            if(!alphaNum(s.charAt(start))) {
                start++;
            } 
            if(!alphaNum(s.charAt(end))) {
                end--;
            }

            if(start >= end)
                return true;
                
            if(s.charAt(start) == s.charAt(end)) {                
                start++;
                end--;
            } else {
                return false;
            }
        }
        return true;
    }

    public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' || 
                c >= 'a' && c <= 'z' || 
                c >= '0' && c <= '9');
    }    
}

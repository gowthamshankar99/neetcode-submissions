class Solution {
    public boolean isAnagram(String s, String t) {

        int[] alpha = new int[26];

        for(int i=0;i<s.length();i++) {
            System.out.println((int)s.charAt(i) - 96);
            alpha[(int)s.charAt(i) - 97] =  alpha[(int)s.charAt(i) - 97] + 1;
        }



        for(int i=0;i<t.length();i++) {
            alpha[(int)t.charAt(i) - 97] =  alpha[(int)t.charAt(i) - 97] - 1;
        }
        

        for(int i=0;i<alpha.length;i++) {
            if(alpha[i] != 0) {
                return false;
            }
        }

        return true;
    }
}

class Solution {
    public boolean isAnagram(String s, String t) {
        
        return isValid(s).equals(isValid(t));

    }

    public String isValid(String s) {

        int[] arr  = new int[26];
        for(int i=0;i<s.length();i++) {
            arr[s.charAt(i) -'a']++;
        }

        return Arrays.toString(arr);
    }
}

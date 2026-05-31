public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) {
            return strs[0];
        }

        StringBuilder sb = new StringBuilder();
        Arrays.sort(strs);
        int N = Math.min(strs[0].length(), strs[strs.length - 1].length());
        for (int i = 0; i < N; i++) {
            if (strs[0].charAt(i) == strs[strs.length - 1].charAt(i)) {
                sb.append(strs[0].charAt(i));
            } else {
                break;
            }
        }
        return sb.toString();
    }
}
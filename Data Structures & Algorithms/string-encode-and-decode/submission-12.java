class Solution {

    public String encode(List<String> strs) {
        // take the 257th string character

        if(strs.isEmpty()) {
            return null;
        }

        String weirdCharacter = Character.toString((char)257);
        StringBuilder encodedString = new StringBuilder("");
        int temp = 1;
        for(String s : strs) {
            // for each string add a #
            if(strs.size() > temp){
                encodedString.append(s + weirdCharacter);
            } else {
                encodedString.append(s);
            }
            temp++;
        }

        return encodedString.toString();
    }

    public List<String> decode(String str) {
        List<String> resultString = new ArrayList<>();
        System.out.println(str);
        if(str == null) 
            return resultString;
        String weirdCharacter = Character.toString((char)257);
        
        for(String s : str.split(weirdCharacter)) {
            resultString.add(s);
        }
        return resultString;
    }
}

class WordDictionary {

    List<String> list;

    public WordDictionary() {
        list = new ArrayList<String>();
    }

    public void addWord(String word) {
        list.add(word);
    }

    public boolean search(String word) {

        for(String s: list) {

            if(s.length() != word.length())
                continue;

            int temp = 0;
            while(temp < s.length()) {
                if(s.charAt(temp) == word.charAt(temp) || word.charAt(temp) == '.') {
                    temp++;
                } else {
                    break;
                }
            }

            if(temp == word.length()) {
                return true;
            }
        }

        return false;
    }

    
}

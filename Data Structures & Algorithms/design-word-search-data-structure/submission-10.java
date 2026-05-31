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
            if(word.length() != s.length())
                continue;


            int i = 0;
            while(i<s.length()) {
                if(s.charAt(i) == word.charAt(i) || word.charAt(i) == '.') {
                    i++;
                } else {
                    break;
                }
            }

            if(i == s.length()) return true;
        }
    return false;
    }

    
}

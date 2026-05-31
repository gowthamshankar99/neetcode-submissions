class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        /**
            Create a hashmap <String> <List>

            create a array alphase function - loop through and increment/decrement them 

            <List> 

        **/

        HashMap<String, List<String>> map = new HashMap<>();
        ArrayList<List<String>> list = new ArrayList<>();

        for(int i=0;i<strs.length;i++) {
            System.out.println();
            if(map.containsKey(alphacalc(strs[i]))) {
                List<String> contains = map.get(alphacalc(strs[i]));
                contains.add(strs[i]);
                map.put(alphacalc(strs[i]), contains);
            }
            else {
                List<String> innerlist = new ArrayList<>();
                innerlist.add(strs[i]);
                map.put(alphacalc(strs[i]), innerlist);
            }
        }


        for(List<String> l :  map.values()) {
            list.add(l);
        }

        return list;

    }


    public String alphacalc(String str) {
        int[] arr = new int[26];
        for(int i=0;i<str.length();i++) {
            arr[str.charAt(i) - 'a']++;
        }

        return Arrays.toString(arr);
    }
}

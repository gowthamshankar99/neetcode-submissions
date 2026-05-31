class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        /**
            Create a hashmap <String> <List>

            create a array alphase function - loop through and increment/decrement them 

            <List> 

        **/
        List<List<String>> resultList = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();

        for(int i=0;i<strs.length;i++) {
            //calc = alphas 
            String result = alphacalc(strs[i]);
            if(map.containsKey(result)) {
                List<String> list = map.get(result);
                list.add(strs[i]);
                map.put(result, list);
            } else {
                // doesnt exist in the map
                map.put(result, new ArrayList<String>(List.of(strs[i])));
            }
        }

        for(List<String> list : map.values()) {
            resultList.add(list);
        }

        return resultList;

    }

    public String alphacalc(String str) {
            int[] result = new int[26];
            // convert string to char
            for(int i=0;i<str.toCharArray().length;i++) {
                result[str.charAt(i) - 'a']++;
            }
        // convert array to string
            return Arrays.toString(result);
    }

}

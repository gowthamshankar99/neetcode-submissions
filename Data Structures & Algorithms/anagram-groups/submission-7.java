class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // create HashMap 
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();

        for(String str: strs) {
            String result = calcValues(str);
            List<String> currentList = null;
            if(map.containsKey(result)) {
                currentList = map.get(result);
                currentList.add(str);
                map.put(result, currentList);
            } else {
                currentList = new ArrayList<String>();
                currentList.add(str);
                map.put(result, currentList);
            }
        }


        // count the alphabet numericals and put that in index - create this as a function 

        // if the hashmap contains the value - add to array 

        // else - create a new value in the hashmap
        List<List<String>> finalResult = new ArrayList<List<String>>();

        // loop through the hashmap 
        map.forEach((key, value) -> {
            System.out.println("Key: " + key + ", Value: " + value);
            finalResult.add(value);
        });

        return finalResult;
    }


    public static String calcValues(String s) {
        int[] result = new int[26];
        for(int i=0;i<s.length();i++) {
            result[s.charAt(i) - 'a']++; 
        }

        return Arrays.toString(result);
    }
}

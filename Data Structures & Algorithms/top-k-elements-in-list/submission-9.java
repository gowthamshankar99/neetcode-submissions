class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // Create HashMap

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i=0;i<nums.length;i++) {
            if(map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i])+1);
            } else { 
                map.put(nums[i], 1);
            }
        }

        List<int[]> list = new ArrayList<>();

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            list.add(new int[]{entry.getKey(), entry.getValue()});
        }

        list.sort((a,b) -> b[1] - a[1]);

        // result array 

        int[] result = new int[k];


        for(int i=0;i<k;i++) {
            result[i] = list.get(i)[0];
        }

        return result;
    }
}

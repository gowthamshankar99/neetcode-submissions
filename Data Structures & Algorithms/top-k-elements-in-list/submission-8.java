class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        int[] result = new int[k];

        // push to hashmap 

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        

        for(int i=0;i<nums.length;i++) {
            if(map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i])+1);
            } else {
                map.put(nums[i], 1);
            }
        }

        // create pq 

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>((a,b) -> map.get(a) - map.get(b));
        for(int key: map.keySet()) {
            pq.add(key);
            if(pq.size() > k) {
                pq.poll();
            }
        }

        System.out.println(pq.size());

        int counter = 0;
        // loop through the queue and add to result 
        for(int p: pq) {
            result[counter] = p;
            counter++;
        }

        return result;
    }
}

class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        int[] results = new int[k];

    
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i])+1);
            } else {
                map.put(nums[i], 1);
            }
        }


        // pq 

        PriorityQueue<Integer> queue = new PriorityQueue<Integer>((a,b) -> map.get(a) - map.get(b));
        for(int key: map.keySet()) {
            queue.add(key);
            if(queue.size() > k) {
                queue.poll();
            }
        }

        int counter = 0;
        for(int pq : queue) {
            results[counter] = pq;
            counter++;
        }
        
        return results;
    }
}

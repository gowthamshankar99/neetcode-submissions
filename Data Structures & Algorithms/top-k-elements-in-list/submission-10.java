class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // result array 
        int[] result = new int[k];

        // hash map 

        /**
            [1, 1]
            [2, 2]
            [3 ,3]
        **/

        /**
             heap -> sort based on the value of the map 
             if the capacity is more than a k - remove from the queue. 
        **/

        // min heaps - 


        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++) {
            if(map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i])+1);
            } else {
                map.put(nums[i], 1);
            }
        }

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>((a,b) -> map.get(a) - map.get(b));

        for(int key: map.keySet()) {
            pq.add(key);
            if(pq.size() > k) {
                pq.poll();
             } 
        }

        int temp = 0;
        for(int res : pq) {
            result[temp] = res;
            temp++;
        }

        return result;

    }
}

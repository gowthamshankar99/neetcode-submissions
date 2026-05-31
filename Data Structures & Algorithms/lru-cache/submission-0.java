class LinkedListNode {
    int key;
    int value;

    public LinkedListNode(int key, int value) {
        this.value = value;
        this.key = key;
    }
}


class LRUCache {

    HashMap<Integer, LinkedListNode> map;
    LinkedList<LinkedListNode> list;
    int capacity;

    public LRUCache(int capacity) {
        this.list = new LinkedList<LinkedListNode>();
        this.map = new HashMap<Integer, LinkedListNode>();
        this.capacity = capacity;
    }
    
    public int get(int key) {
        // check if the key exist - if not return -1
        if(map.containsKey(key))  {
            // return key
            LinkedListNode node = map.get(key);
            list.remove(node);
            list.addFirst(node);
            return node.value;
        } 
        return -1;
    }
    
    public void put(int key, int value) {
        // if the key already exist
        if(map.containsKey(key)) {
            // get the node 
            LinkedListNode node = map.get(key);
            list.remove(node);
            node.value = value;
            list.addFirst(node);
        } else {

            if(map.size() >= capacity) {
                LinkedListNode node =  list.removeLast();
                map.remove(node.key);
            }
            // if the value doesnt exist
            LinkedListNode node = new LinkedListNode(key, value);
            map.put(key, node);
            //make the node first node 
            list.addFirst(node);

        }
    }
}





/**
 
  [1,1] -> [2,2]
  


**/
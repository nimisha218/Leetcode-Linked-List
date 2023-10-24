class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Make it a doubly Linked List
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Remove the node from the Linked List
            self.remove(self.cache[key])
            # Re-insert the node in the Linked List
            self.insert(self.cache[key])
             # Return the value at the node 
            return self.cache[key].val
         # Return -1 if node is not present
        return -1

    def put(self, key: int, value: int) -> None:
        # Check is key is already present in cache
        if key in self.cache:
            # If yes, remove it first.
            self.remove(self.cache[key])
        # Insert the key, value pair as Node
        self.cache[key] = Node(key, value)
        # Add it to the Linked List 
        self.insert(self.cache[key])

        # Check if the length of the cache is more than capacity
        if len(self.cache) > self.capacity:
            # Remove the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
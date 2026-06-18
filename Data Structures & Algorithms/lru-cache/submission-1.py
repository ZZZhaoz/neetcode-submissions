class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currcapacity = 0
        self.mp = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        pre, nex = node.prev, node.next
        pre.next = nex
        nex.prev = pre



    def insert(self, node):
        pre, nex = self.right.prev, self.right
        node.prev, node.next = pre, nex
        pre.next = node
        nex.prev = node 
      


    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        Node(key, value)
        self.mp[key] = Node(key, value)
        self.insert(self.mp[key])
        if len(self.mp) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]

        

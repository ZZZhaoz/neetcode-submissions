class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None
      
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.m = {}
        self.left.next, self.right.prev = self.right, self.left
        
    def get(self, key: int) -> int:
        if key in self.m:
            self.remove(self.m[key])
            self.insert(self.m[key])
            return self.m[key].val
        return -1
       
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
      
    def insert(self, node):
        temp = self.right.prev
        self.right.prev, node.next = node, self.right
        node.prev, temp.next = temp, node
       
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.remove(self.m[key])
        self.m[key] = Node(key, value)
        self.insert(self.m[key])

        if len(self.m) > self.capacity:
            l = self.left.next
            self.remove(l)
            del self.m[l.key]

        
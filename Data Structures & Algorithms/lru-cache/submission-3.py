class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.pre = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.pre = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        node = self.m[key]
        self.remove(node)
        self.insert(node)
        return node.val


    def remove(self, node):
       pre, nxt = node.pre, node.next
       pre.next, nxt.pre = nxt, pre

    def insert(self, node):
        pre, nxt = self.right.pre, self.right
        pre.next = nxt.pre = node
        node.next, node.pre = nxt, pre
        


    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.remove(self.m[key])
        self.m[key] = Node(key, value)
        self.insert(self.m[key])

        if len(self.m) > self.capacity:
            d = self.left.next
            self.remove(d)
            del self.m[d.key]        

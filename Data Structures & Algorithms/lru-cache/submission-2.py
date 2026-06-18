class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.previous = None
        self.next = None
       
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.previous, self.left.next = self.left, self.right
       
    def remove(self, node):
        pre, nxt = node.previous, node.next
        pre.next, nxt.previous = node.next, node.previous
      

    def insert(self, node):
        pre, nxt = self.right.previous, self.right
        pre.next, nxt.previous = node, node
        node.previous, node.next = pre, nxt

     
    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1

      

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
           
        self.mp[key] = Node(key, value)
        self.insert(self.mp[key])
       
        if len(self.mp) > self.cap:
            #记住存储lru, 不然del时找不到
            lru = self.left.next
            self.remove(lru)
            #记住del 字典
            del self.mp[lru.key]
            
      
        

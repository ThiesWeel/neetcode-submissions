class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Dummy nodes simplify edge cases (empty list, single element)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Add node right after dummy head -> O(1)
    def add_to_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # Remove any existing node directly via its reference -> O(1)
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capa = capacity 
        self.map = {} # key: Node
        self.ru = {}
        self.LRU = DoublyLinkedList()

    def get(self, key: int) -> int:
        node = self.map.get(key, None)
        # if not -1, update how recently used
        if node:    
            self.LRU.remove(node)
            self.LRU.add_to_front(node)
            return node.val
        # return -1 as node was not present in LRU
        return -1

    def put(self, key: int, value: int) -> None:
        old_node = self.map.get(key,False)
        if old_node:
            # address in use, remove first
            # only from LRU, redefining in mapping is okay
            self.LRU.remove(old_node)
    
        node = Node(key, value)
        self.map[key] = node        # possibly overwriting old_node
        self.LRU.add_to_front(node)

        # check if cache full
        if len(self.map) > self.capa:
            # remove LRU, use DLL to find its key
            lru_node = self.LRU.tail.prev # find LRU Node
            # now we HAVE TO remove from map
            self.map.pop(lru_node.key)
            self.LRU.remove(lru_node)




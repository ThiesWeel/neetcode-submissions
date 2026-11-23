class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        # Dummy sentinels: head <-> [MRU ... LRU] <-> tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

    def insert(self, node: Node) -> None:
        # Insert right after dummy head (Most Recently Used position)
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}  # key -> Node
        self.ru = DLL()

    def get(self, key: int) -> int:
        node = self.hashmap.get(key)
        if not node:
            return -1

        # Move accessed node to MRU position
        self.ru.remove(node)
        self.ru.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # 1. If key already exists, remove its old node first
        if key in self.hashmap:
            self.ru.remove(self.hashmap[key])

        # 2. Insert new node at MRU position and update hashmap
        node = Node(key=key, val=value)
        self.hashmap[key] = node
        self.ru.insert(node)

        # 3. If over capacity, evict the LRU node (right before dummy tail)
        if len(self.hashmap) > self.capacity:
            lru = self.ru.tail.prev
            self.ru.remove(lru)
            del self.hashmap[lru.key]

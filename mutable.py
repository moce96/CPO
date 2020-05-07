class List(object):
    def __init__(self, root=None):
        self.root = root
    def __str__(self):
        """for str() implementation for printing"""
        return " : ".join(map(str, self.to_list()))

    def size(self):
        res = 0
        cur = self.root
        while cur is not None:
            res += 1
            cur = cur.next
        return res

    def to_list(self):
        res = []
        cur = self.root
        while cur is not None:
            res.append(cur.value)
            cur = cur.next
        return res

    def from_list(self, lst):
        if len(lst) == 0:
            self.root = None
            return
        root = None
        for e in reversed(lst):
            root = Node(e, root)
        self.root = root

    def add_to_head(self, value):
        self.root = Node(value, self.root)

    def _last_node(self):
        """helper function for find last node, should be private"""
        assert self.root is not None, "list should be not empty"
        cur = self.root
        while cur.next is not None:
            cur = cur.next
        return cur

    def add_to_tail(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._last_node().next = Node(value)

    def map(self, f):
        cur = self.root
        while cur is not None:
            cur.value = f(cur.value)
            cur = cur.next

    def reduce(self, f, initial_state):
        state = initial_state
        cur = self.root
        while cur is not None:
            state = f(state, cur.value)
            cur = cur.next
        return state

    def __iter__(self):
        return List(self.root)

    def __next__(self):
        if self.root is None:
            raise StopIteration
        tmp = self.root.value
        self.root = self.root.next
        return tmp


class Node(object):
    def __init__(self, value, next=None):
        """node constructor"""
        self.value = value
        self.next = next
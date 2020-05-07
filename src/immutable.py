def size(n):
    if n is None:
        return 0
    else:
        return 1 + size(n.next)

def cons(head, tail):
    """add new element to head of the list"""
    return Node(head, tail)

def remove(n, element):
    assert n is not None, "element should be in list"
    if n.value == element:
        return n.next
    else:
        return cons(n.value, remove(n.next, element))

def head(n):
    assert type(n) is Node
    return n.value

def tail(n):
    assert type(n) is Node
    return n.next

def reverse(n, acc=None):
    if n is None:
        return acc
    return reverse(tail(n), Node(head(n), acc))

def mempty():
    return None

def mconcat(a, b):
    if a is None:
        return b
    tmp = reverse(a)
    res = b
    while tmp is not None:
        res = cons(tmp.value, res)
        tmp = tmp.next
    return res

def to_list(n):
    res = []
    cur = n
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    return res

def from_list(lst):
    res = None
    for e in reversed(lst):
        res = cons(e, res)
    return res

def iterator(lst):
    cur = lst
    def foo():
        nonlocal cur
        if cur is None: raise StopIteration
        tmp = cur.value
        cur = cur.next
        return tmp
    return foo

class Node(object):
    def __init__(self, value, next):
        """node constructor"""
        self.value = value
        self.next = next

    def __str__(self):
        """for str() implementation"""
        if type(self.next) is Node:
            return "{} : {}".format(self.value, self.next)
        return str(self.value)

    def __eq__(self, other):
        """for write assertion, we should be abel for check list equality (list are equal, if all elements are equal)."""
        if other is None:
            return False
        if self.value != other.value:
            return False
        return self.next == other.next
import unittest

from hypothesis import given

import hypothesis.strategies as st

from mutable import *


class TestMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(List().size(), 0)
        self.assertEqual(List(Node('a')).size(), 1)
        self.assertEqual(List(Node('a', Node('b'))).size(), 2)

    def test_to_list(self):
        self.assertEqual(List().to_list(), [])
        self.assertEqual(List(Node('a')).to_list(), ['a'])
        self.assertEqual(List(Node('a', Node('b'))).to_list(), ['a', 'b'])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = List()
        lst.from_list(e)
        self.assertEqual(lst.to_list(), e)

    def test_add_to_head(self):
        lst = List()
        self.assertEqual(lst.to_list(), [])
        lst.add_to_head('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.add_to_head('b')
        self.assertEqual(lst.to_list(), ['b', 'a'])

    def test_add_to_tail(self):
        lst = List()
        self.assertEqual(lst.to_list(), [])
        lst.add_to_tail('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.add_to_tail('b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_map(self):
        lst = List()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])

        lst = List()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

    def test_reduce(self):
        # sum of empty list
        lst = List()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = List()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = List()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.size())

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = List()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = List()
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))

    def test_iter(self):
        x = [1, 2, 3]
        lst = List()
        lst.from_list(x)
        tmp = []
        for e in lst:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)

        i = iter(List())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()